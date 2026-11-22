package org.jdownloader.gui.laf.amoled;

import java.awt.Color;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;

import javax.swing.UIDefaults;

import com.formdev.flatlaf.FlatDarkLaf;

/**
 * Pure black AMOLED dark Look &amp; Feel built on top of FlatDarkLaf.
 */
public class AmoledDarkLookAndFeel extends FlatDarkLaf {
    private static final long                serialVersionUID = 1L;
    private static final Map<String, String> AMOLED_DEFAULTS;
    static {
        final Map<String, String> m = new LinkedHashMap<String, String>();
        m.put("@background", "#000000");
        m.put("@foreground", "#e8eaed");
        m.put("@disabledBackground", "#000000");
        m.put("@disabledForeground", "#6e7681");
        m.put("@buttonBackground", "#141414");
        m.put("@componentBackground", "#0a0a0a");
        m.put("@menuBackground", "#080808");
        m.put("@menuHoverBackground", "#181818");
        m.put("@menuSelectionBackground", "#163b6b");
        m.put("@selectionBackground", "#163b6b");
        m.put("@selectionForeground", "#ffffff");
        m.put("@selectionInactiveBackground", "#112238");
        m.put("@selectionInactiveForeground", "#e8eaed");
        m.put("@accentColor", "#2f81f7");
        m.put("@icon", "#d0d7de");
        AMOLED_DEFAULTS = Collections.unmodifiableMap(m);
    }

    public AmoledDarkLookAndFeel() {
        setExtraDefaults(AMOLED_DEFAULTS);
    }

    @Override
    public String getName() {
        return "AMOLED Dark";
    }

    @Override
    public String getDescription() {
        return "Pure black AMOLED Dark Look and Feel";
    }

    @Override
    public UIDefaults getDefaults() {
        final UIDefaults defaults = super.getDefaults();
        final Color pureBlack = new Color(0x00, 0x00, 0x00);
        final Color elevated = new Color(0x0A, 0x0A, 0x0A);
        final Color elevatedHover = new Color(0x16, 0x16, 0x16);
        final Color border = new Color(0x1E, 0x1E, 0x1E);
        final Color foreground = new Color(0xE8, 0xEA, 0xED);
        final Color selectionBg = new Color(0x16, 0x3B, 0x6B);

        defaults.put("Panel.background", pureBlack);
        defaults.put("RootPane.background", pureBlack);
        defaults.put("Viewport.background", pureBlack);
        defaults.put("ScrollPane.background", pureBlack);
        defaults.put("SplitPane.background", pureBlack);
        defaults.put("OptionPane.background", pureBlack);
        defaults.put("MenuBar.background", pureBlack);
        defaults.put("ToolBar.background", pureBlack);
        defaults.put("TabbedPane.background", pureBlack);
        defaults.put("TabbedPane.selectedBackground", new Color(0x0F, 0x0F, 0x0F));
        defaults.put("TabbedPane.hoverColor", elevatedHover);
        defaults.put("TabbedPane.underlineColor", new Color(0x2F, 0x81, 0xF7));
        defaults.put("TabbedPane.focusColor", new Color(0x0F, 0x0F, 0x0F));
        defaults.put("Table.background", pureBlack);
        defaults.put("Table.alternateRowColor", new Color(0x06, 0x06, 0x06));
        defaults.put("Table.gridColor", border);
        defaults.put("Table.selectionBackground", selectionBg);
        defaults.put("Table.selectionForeground", Color.WHITE);
        defaults.put("TableHeader.background", elevated);
        defaults.put("TableHeader.bottomSeparatorColor", border);
        defaults.put("TableHeader.separatorColor", border);
        defaults.put("Tree.background", pureBlack);
        defaults.put("Tree.selectionBackground", selectionBg);
        defaults.put("Tree.selectionForeground", Color.WHITE);
        defaults.put("List.background", pureBlack);
        defaults.put("List.selectionBackground", selectionBg);
        defaults.put("List.selectionForeground", Color.WHITE);
        defaults.put("TextField.background", elevated);
        defaults.put("PasswordField.background", elevated);
        defaults.put("FormattedTextField.background", elevated);
        defaults.put("TextArea.background", pureBlack);
        defaults.put("EditorPane.background", pureBlack);
        defaults.put("ComboBox.background", elevated);
        defaults.put("Spinner.background", elevated);
        defaults.put("PopupMenu.background", new Color(0x08, 0x08, 0x08));
        defaults.put("PopupMenu.borderColor", border);
        defaults.put("ToolTip.background", elevated);
        defaults.put("ToolTip.foreground", foreground);
        defaults.put("ToolTip.borderColor", border);
        defaults.put("Component.borderColor", new Color(0x24, 0x24, 0x24));
        defaults.put("Separator.foreground", border);
        defaults.put("ScrollBar.track", pureBlack);
        defaults.put("ScrollBar.thumb", new Color(0x24, 0x24, 0x24));
        defaults.put("ScrollBar.hoverThumbColor", new Color(0x38, 0x38, 0x38));
        defaults.put("ScrollBar.pressedThumbColor", new Color(0x4A, 0x4A, 0x4A));
        defaults.put("TitlePane.background", pureBlack);
        defaults.put("TitlePane.inactiveBackground", pureBlack);
        defaults.put("TitlePane.foreground", foreground);
        defaults.put("TitlePane.inactiveForeground", new Color(0x8B, 0x94, 0x9E));
        defaults.put("TitlePane.borderColor", border);
        return defaults;
    }
}
