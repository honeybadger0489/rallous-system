package com.rallous.recruitsbridge;

import com.talhanation.recruits.FactionEvents;
import com.talhanation.recruits.world.RecruitsFaction;
import com.talhanation.recruits.world.RecruitsFactionManager;
import net.minecraft.ChatFormatting;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.nbt.ListTag;
import net.minecraft.nbt.Tag;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.BannerItem;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraft.world.scores.Objective;
import net.minecraft.world.scores.PlayerTeam;
import net.minecraft.world.scores.Scoreboard;
import net.minecraft.world.scores.Team;

/**
 * Reads {@code rallous.rec.id} / {@code rallous.fac.id} and storage
 * {@code rallous_recruits_bind:contact}, then founds or renames the Recruits
 * host. This is not a datapack hint — it writes {@code RecruitsFaction} saved data.
 */
public final class HostFounder {
    public static final String TAG_BOUND = "rallous.rec.bound";
    public static final String TAG_FOUNDED = "rallous.rec.founded";
    public static final String TAG_FAILED = "rallous.rec.bridge_fail";
    /** {@code FactionEditScreen.unitColors} index 12 = red, not DyeColor 14. */
    public static final byte UNIT_COLOR_RED = 12;
    private static final ResourceLocation CONTACT =
            new ResourceLocation("rallous_recruits_bind", "contact");

    private HostFounder() {}

    public static void tryFound(Player raw) {
        if (!(raw instanceof ServerPlayer player)) {
            return;
        }
        if (player.getTags().contains(TAG_FOUNDED) || player.getTags().contains(TAG_FAILED)) {
            return;
        }
        if (FactionEvents.recruitsFactionManager == null) {
            return;
        }
        int recId = score(player, "rallous.rec.id");
        if (recId <= 0) {
            recId = score(player, "rallous.fac.id");
        }
        if (recId <= 0) {
            recId = score(player, "rallous.contact_id");
        }
        if (recId <= 0 && !player.getTags().contains(TAG_BOUND)) {
            return;
        }
        String name = resolveName(player, recId);
        if (name == null || name.isBlank()) {
            return;
        }
        name = cap(displayName(name), 32);
        if (name.isBlank()) {
            return;
        }
        ServerLevel level = player.serverLevel();
        RecruitsFactionManager manager = FactionEvents.recruitsFactionManager;
        try {
            if (apply(player, level, manager, name, recId)) {
                player.addTag(TAG_FOUNDED);
                player.sendSystemMessage(Component.literal("Crash-camp host founded: ")
                        .withStyle(ChatFormatting.GOLD)
                        .append(Component.literal(name).withStyle(ChatFormatting.WHITE, ChatFormatting.BOLD))
                        .append(Component.literal(" — not Team 2.").withStyle(ChatFormatting.DARK_GRAY)));
                RallousRecruitsBridge.LOGGER.info("Founded Recruits host '{}' for {}", name, player.getScoreboardName());
            }
        } catch (RuntimeException ex) {
            player.addTag(TAG_FAILED);
            RallousRecruitsBridge.LOGGER.error("Failed to found Recruits host '{}' for {}", name, player.getScoreboardName(), ex);
            player.sendSystemMessage(Component.literal("Recruits bridge failed to found " + name + ".")
                    .withStyle(ChatFormatting.RED));
        }
    }

    private static boolean apply(ServerPlayer player, ServerLevel level, RecruitsFactionManager manager, String name, int recId) {
        Team current = player.getTeam();
        if (current != null) {
            RecruitsFaction existing = manager.getFactionByStringID(current.getName());
            if (existing != null) {
                if (sameHost(existing, current, name)) {
                    return true;
                }
                if (isGeneric(current.getName()) || isGeneric(existing.getTeamDisplayName())) {
                    burnGeneric(player, level, current.getName());
                } else {
                    existing.setTeamDisplayName(name);
                    if (player.getTeam() instanceof PlayerTeam pt) {
                        pt.setDisplayName(Component.literal(name));
                    }
                    manager.save(overworld(player, level));
                    Team afterRename = player.getTeam();
                    return afterRename != null && manager.getFactionByStringID(afterRename.getName()) != null;
                }
            } else if (isGeneric(current.getName()) && current instanceof PlayerTeam pt) {
                level.getScoreboard().removePlayerFromTeam(player.getScoreboardName(), pt);
            }
        }

        String teamId = uniqueTeamId(manager, name, player);
        int race = score(player, "rallous.rec.race");
        ItemStack banner = hostBanner(race);
        // menu=false skips emerald cost + cloth-banner uniqueness (same as /team add intercept)
        FactionEvents.createTeam(
                false,
                player,
                level,
                teamId,
                name,
                player.getScoreboardName(),
                banner,
                ChatFormatting.RED,
                UNIT_COLOR_RED);

        Team after = player.getTeam();
        RecruitsFaction founded = after == null ? null : manager.getFactionByStringID(after.getName());
        if (founded == null) {
            player.addTag(TAG_FAILED);
            player.sendSystemMessage(Component.literal("Recruits did not accept host " + name + ".")
                    .withStyle(ChatFormatting.RED));
            RallousRecruitsBridge.LOGGER.error("createTeam did not persist '{}' for {}", name, player.getScoreboardName());
            return false;
        }
        return !isGeneric(founded.getTeamDisplayName()) && !isGeneric(after.getName());
    }

    private static boolean sameHost(RecruitsFaction faction, Team team, String name) {
        String id = stringId(name);
        return name.equalsIgnoreCase(faction.getTeamDisplayName())
                || id.equalsIgnoreCase(faction.getStringID())
                || id.equalsIgnoreCase(team.getName())
                || name.equalsIgnoreCase(team.getName());
    }

    /**
     * Recruits client: {@code getCorrectFormatStringID} — strip {@code [^\p{L}\p{N} ]},
     * then drop spaces so {@code Clan Mors} → {@code ClanMors}.
     */
    static String displayName(String text) {
        return text.replaceAll("[^\\p{L}\\p{N} ]", "");
    }

    static String stringId(String display) {
        return displayName(display).replace(" ", "");
    }

    private static String uniqueTeamId(RecruitsFactionManager manager, String name, ServerPlayer player) {
        String base = cap(stringId(name), 32);
        if (!nameTaken(manager, player, base)) {
            return base;
        }
        String suffix = player.getScoreboardName().replaceAll("[^\\p{L}\\p{N}]", "");
        String candidate = cap(base + suffix, 32);
        if (!nameTaken(manager, player, candidate)) {
            return candidate;
        }
        String shortId = player.getUUID().toString().substring(0, 8);
        return cap(base + shortId, 32);
    }

    /**
     * Recruits {@code isNameInUse} NPEs when a stored faction has a null stringID
     * ({@code getStringID().toLowerCase()}). Walk the map ourselves instead.
     */
    private static boolean nameTaken(RecruitsFactionManager manager, ServerPlayer player, String id) {
        if (id == null || id.isBlank()) {
            return true;
        }
        if (player.server.getScoreboard().getPlayerTeam(id) != null) {
            return true;
        }
        if (manager.getFactionByStringID(id) != null) {
            return true;
        }
        for (RecruitsFaction faction : manager.getFactions()) {
            if (faction == null) {
                continue;
            }
            String existing = faction.getStringID();
            if (existing != null && existing.equalsIgnoreCase(id)) {
                return true;
            }
        }
        return false;
    }

    /**
     * Recruits {@code removeTeam} walks claims and NPEs when
     * {@code getOwnerFaction()} is null. Still detach the player so Team 1/2
     * does not block {@code createTeam}.
     */
    private static void burnGeneric(ServerPlayer player, ServerLevel level, String teamName) {
        try {
            FactionEvents.removeTeam(level, teamName);
        } catch (RuntimeException ex) {
            RallousRecruitsBridge.LOGGER.warn("removeTeam({}) threw; detaching player", teamName, ex);
        }
        Team still = player.getTeam();
        if (still instanceof PlayerTeam pt && isGeneric(still.getName())) {
            try {
                player.server.getScoreboard().removePlayerFromTeam(player.getScoreboardName(), pt);
            } catch (IllegalStateException ignored) {
                // already off the team
            }
        }
    }

    private static ServerLevel overworld(ServerPlayer player, ServerLevel fallback) {
        ServerLevel ow = player.server.overworld();
        return ow != null ? ow : fallback;
    }

    static boolean isGeneric(String name) {
        if (name == null) {
            return true;
        }
        String n = name.strip();
        return n.isEmpty() || n.equalsIgnoreCase("team") || n.matches("(?i)team\\s*\\d+");
    }

    private static String resolveName(ServerPlayer player, int recId) {
        CompoundTag contact = player.server.getCommandStorage().get(CONTACT);
        if (contact != null && contact.contains("name", Tag.TAG_STRING)) {
            String stored = contact.getString("name");
            int storedId = contact.contains("id") ? contact.getInt("id") : 0;
            if (!stored.isBlank() && (storedId == 0 || recId <= 0 || storedId == recId)) {
                return stored;
            }
        }
        return FactionNames.name(recId);
    }

    private static int score(ServerPlayer player, String objectiveName) {
        Scoreboard board = player.getScoreboard();
        Objective objective = board.getObjective(objectiveName);
        if (objective == null) {
            return 0;
        }
        return board.getOrCreatePlayerScore(player.getScoreboardName(), objective).getScore();
    }

    private static String cap(String s, int max) {
        if (s.length() <= max) {
            return s;
        }
        return s.substring(0, max);
    }

    private static ItemStack hostBanner(int race) {
        Item item = switch (race) {
            case 2 -> Items.BLACK_BANNER;
            case 3 -> Items.GREEN_BANNER;
            case 4 -> Items.BROWN_BANNER;
            case 5 -> Items.LIME_BANNER;
            case 6 -> Items.YELLOW_BANNER;
            case 7 -> Items.GRAY_BANNER;
            case 8 -> Items.RED_BANNER;
            default -> Items.RED_BANNER;
        };
        ItemStack stack = new ItemStack(item);
        CompoundTag be = new CompoundTag();
        ListTag patterns = new ListTag();
        CompoundTag pattern = new CompoundTag();
        pattern.putString("Pattern", "gra");
        pattern.putInt("Color", dye(race));
        patterns.add(pattern);
        be.put("Patterns", patterns);
        BlockItem.setBlockEntityData(stack, BlockEntityType.BANNER, be);
        if (!(stack.getItem() instanceof BannerItem)) {
            return new ItemStack(Items.RED_BANNER);
        }
        return stack;
    }

    private static int dye(int race) {
        return switch (race) {
            case 2 -> 15; // black
            case 3 -> 2;  // green
            case 4 -> 12; // brown
            case 5 -> 5;  // lime
            case 6 -> 11; // yellow
            case 7 -> 7;  // gray
            case 8 -> 14; // red
            default -> 14;
        };
    }
}
