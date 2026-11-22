package org.jdownloader.gui.laf.amoled;

import javax.swing.JPanel;

import org.jdownloader.updatev2.gui.DefaultFlatLAFExtension;

/**
 * LAFOptions color extension tailored for pure-black AMOLED Dark mode.
 */
public class AmoledDarkLookAndFeelExtension extends DefaultFlatLAFExtension {
    public AmoledDarkLookAndFeelExtension(final String laf) {
        super(laf);
    }

    @Override
    public String getColorForConfigHeaderTextColor() {
        return "FFF0F6FC";
    }

    @Override
    public String getColorForConfigPanelDescriptionText() {
        return "FF8B949E";
    }

    @Override
    public String getColorForErrorForeground() {
        return "FFFF5555";
    }

    @Override
    public String getColorForLinkgrabberDupeHighlighter() {
        return "33FF453A";
    }

    @Override
    public String getColorForPanelBackground() {
        return "FF000000";
    }

    @Override
    public String getColorForPanelBorders() {
        return "FF1E1E1E";
    }

    @Override
    public String getColorForPanelHeaderBackground() {
        return "FF0A0A0A";
    }

    @Override
    public String getColorForPanelHeaderForeground() {
        return "FFE8EAED";
    }

    @Override
    public String getColorForProgressbarForeground1() {
        return "801F6FEB";
    }

    @Override
    public String getColorForProgressbarForeground2() {
        return "99388BFD";
    }

    @Override
    public String getColorForProgressbarForeground3() {
        return "CC388BFD";
    }

    @Override
    public String getColorForProgressbarForeground4() {
        return "99388BFD";
    }

    @Override
    public String getColorForProgressbarForeground5() {
        return "801F6FEB";
    }

    @Override
    public String getColorForScrollbarsMouseOverState() {
        return "FF3A3A3A";
    }

    @Override
    public String getColorForScrollbarsNormalState() {
        return "FF242424";
    }

    @Override
    public String getColorForSpeedMeterAverage() {
        return "FF3FB950";
    }

    @Override
    public String getColorForSpeedMeterAverageText() {
        return "FF9AA0A6";
    }

    @Override
    public String getColorForSpeedMeterText() {
        return "FFE8EAED";
    }

    @Override
    public String getColorForSpeedmeterCurrentBottom() {
        return "CC238636";
    }

    @Override
    public String getColorForSpeedmeterCurrentTop() {
        return "333FB950";
    }

    @Override
    public String getColorForTableAccountErrorRowBackground() {
        return "FF3B0D11";
    }

    @Override
    public String getColorForTableAccountErrorRowForeground() {
        return "FFFFD2D6";
    }

    @Override
    public String getColorForTableAccountTempErrorRowBackground() {
        return "FF332600";
    }

    @Override
    public String getColorForTableAccountTempErrorRowForeground() {
        return "FFFFE69C";
    }

    @Override
    public String getColorForTableAlternateRowBackground() {
        return "FF060606";
    }

    @Override
    public String getColorForTableMouseOverRowBackground() {
        return "FF121822";
    }

    @Override
    public String getColorForTablePackageRowBackground() {
        return "FF0B0D12";
    }

    @Override
    public String getColorForTablePackageRowForeground() {
        return "FFF0F6FC";
    }

    @Override
    public String getColorForTableSelectedRowsBackground() {
        return "FF163B6B";
    }

    @Override
    public String getColorForTableSelectedRowsForeground() {
        return "FFFFFFFF";
    }

    @Override
    public String getColorForTooltipForeground() {
        return "FFE8EAED";
    }

    @Override
    public String getConfigLabelDisabledTextColor() {
        return "FF6E7681";
    }

    @Override
    public String getConfigLabelEnabledTextColor() {
        return "FFE8EAED";
    }

    @Override
    public void customizeLinkPropertiesPanel(JPanel downloadPropertiesBasePanel) {
        if (downloadPropertiesBasePanel != null) {
            downloadPropertiesBasePanel.setBackground(java.awt.Color.BLACK);
        }
    }
}
