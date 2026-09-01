package com.rallous.recruitsbridge;

import com.talhanation.recruits.FactionEvent;
import com.talhanation.recruits.world.RecruitsFaction;
import net.minecraft.server.level.ServerPlayer;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;

/**
 * Recruits-facing subscribers. Loaded only after Recruits is present.
 * Does not call {@code openTeamEditScreen} (its non-ServerPlayer path is
 * {@code SIMPLE_CHANNEL.sendToServer}).
 */
public final class RecruitsBridgeEvents {
    private RecruitsBridgeEvents() {}

    static void register() {
        MinecraftForge.EVENT_BUS.register(new RecruitsBridgeEvents());
    }

    @SubscribeEvent
    public void onPlayerTick(TickEvent.PlayerTickEvent event) {
        if (event.phase != TickEvent.Phase.END) {
            return;
        }
        if (event.player.level().isClientSide()) {
            return;
        }
        if ((event.player.tickCount % 10) != 0) {
            return;
        }
        HostFounder.tryFound(event.player);
    }

    /** Confirm / tag only — do not invent a second create path. Cancel would roll back via {@code removeTeam}. */
    @SubscribeEvent
    public void onFactionCreated(FactionEvent.Created event) {
        RecruitsFaction faction = event.getFaction();
        if (faction == null) {
            return;
        }
        ServerPlayer leader = event.getCreator();
        RallousRecruitsBridge.LOGGER.info("FactionEvent.Created stringID={} display={} unitColor={} creator={}",
                faction.getStringID(),
                faction.getTeamDisplayName(),
                faction.getUnitColor(),
                leader == null ? "none" : leader.getScoreboardName());
    }
}
