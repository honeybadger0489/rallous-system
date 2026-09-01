package com.rallous.recruitsbridge;

import com.mojang.logging.LogUtils;
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
 *
 * Recruits types live only in {@link RecruitsBridgeEvents} / {@link HostFounder},
 * which are loaded after {@code ModList.isLoaded("recruits")}. The {@code @Mod}
 * class must not mention those types or a missing Recruits jar becomes
 * {@code NoClassDefFoundError} on dedicated-server boot.
 */
@Mod(RallousRecruitsBridge.MODID)
public class RallousRecruitsBridge {
    public static final String MODID = "rallous_recruits_bridge";
    static final Logger LOGGER = LogUtils.getLogger();

    public RallousRecruitsBridge() {
        if (!ModList.get().isLoaded("recruits")) {
            LOGGER.warn("Recruits is not loaded — skip founding banners");
            return;
        }
        RecruitsBridgeEvents.register();
        LOGGER.info("rallous-recruits-bridge: will found Recruits hosts after Warp-crash assign");
    }
}
