package com.rallous.recruitsbridge;

import com.mojang.logging.LogUtils;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.ModList;
import net.minecraftforge.fml.common.Mod;
import org.slf4j.Logger;

/**
 * After Warp-crash assign, found or rename the player's Recruits host to the
 * compiled camp (Reikland, Clan Mors, …) so they do not see Team 2.
 *
 * Recruits 1.15.x has no player command that founds a banner. This mod calls
 * {@code FactionEvents.createTeam} — the same server method as Found a Banner
 * ({@code MessageCreateTeam}) — with {@code menu=false} so the emerald / cloth
 * checks are skipped (same as Recruits' intercepted {@code /team add}).
 */
@Mod(RallousRecruitsBridge.MODID)
public class RallousRecruitsBridge {
    public static final String MODID = "rallous_recruits_bridge";
    static final Logger LOGGER = LogUtils.getLogger();

    public RallousRecruitsBridge() {
        if (!ModList.get().isLoaded("recruits")) {
            LOGGER.error("Recruits is not loaded — cannot found a banner");
            return;
        }
        MinecraftForge.EVENT_BUS.register(this);
        LOGGER.info("rallous-recruits-bridge: will found Recruits hosts after Warp-crash assign");
    }

    @SubscribeEvent
    public void onPlayerTick(TickEvent.PlayerTickEvent event) {
        if (event.phase != TickEvent.Phase.END) {
            return;
        }
        if (event.player.level().isClientSide()) {
            return;
        }
        if ((event.player.tickCount & 19) != 0) {
            return;
        }
        HostFounder.tryFound(event.player);
    }
}
