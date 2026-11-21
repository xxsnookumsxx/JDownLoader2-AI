// Platform-specific macOS EAWT code - stub for non-Mac platforms
// Original EAWT code requires com.apple.eawt.* classes which are not available on non-Mac platforms.
// This stub provides compilation compatibility without macOS-specific functionality.

package org.jdownloader.crosssystem.macos;

/**
 * Stub implementation for macOS-specific EAWT integration.
 * On non-Mac platforms, this class does nothing.
 * On Mac platforms, the real EAWT code would need com.apple.eawt.* classes.
 */
public class EAWTMacOSApplicationAdapter {

    /**
     * Enable macOS special features. Stub implementation does nothing.
     *
     * @throws Exception never thrown in stub
     */
    public static void enableMacSpecial() throws Exception {
        // No-op on non-Mac platforms
    }

    private EAWTMacOSApplicationAdapter() {
    }

}
