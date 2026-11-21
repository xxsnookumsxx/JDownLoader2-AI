package org.jdownloader.crosssystem.macos;

import java.awt.Image;

/**
 * macOS application adapter stub.
 * Original code used com.apple.eawt.* classes which are only available on macOS.
 * This stub provides compilation compatibility without macOS-specific functionality.
 */
public class MacOSApplicationAdapter {

    /**
     * Set the dock icon. Stub implementation does nothing on non-macOS platforms.
     *
     * @param icon the icon image to set
     */
    public static void setDockIcon(final Image icon) {
        // No-op on non-macOS platforms
    }
}
