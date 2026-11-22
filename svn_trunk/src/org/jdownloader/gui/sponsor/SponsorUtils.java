package org.jdownloader.gui.sponsor;

import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.event.MouseEvent;

public class SponsorUtils {
    private final static Sponsor SPONSOR = new Sponsor() {
        @Override
        public void onMouseOver(MouseEvent e) {
        }

        @Override
        public void onMouseOut(MouseEvent e) {
        }

        @Override
        public void onClicked(MouseEvent e) {
        }

        @Override
        public Rectangle paint(Graphics2D g) {
            return null;
        }

        @Override
        public boolean isVisible() {
            return false;
        }

        @Override
        public String getPreSelectedInAddAccountDialog() {
            return null;
        }
    };

    public static Sponsor getSponsor() {
        return SPONSOR;
    }
}
