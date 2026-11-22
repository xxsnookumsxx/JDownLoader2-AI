package org.jdownloader.donate;

public class DonationManager {
    private static final DonationManager INSTANCE = new DonationManager();

    private DonationManager() {
    }

    public static DonationManager getInstance() {
        return INSTANCE;
    }

    public boolean isButtonVisible() {
        return false;
    }
}
