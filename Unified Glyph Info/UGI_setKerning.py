# MenuTitle: Set UGI Kerning Groups
# -*- coding: utf-8 -*-
__doc__ = """
Sets the kerning keys for the selected glyphs using the UGI.
"""

from UGI.unifiedglyphinfo import italic_angle
from AppKit import NSEvent

from UGI.UGI_importer import import_scripts
unified_infos = import_scripts(Glyphs.font)

Glyphs.clearLog()
# Glyphs.showMacroWindow()

# --- From mekkablue ---
keysPressed = NSEvent.modifierFlags()
capslockKey = 65536
capslockKeyPressed = keysPressed & capslockKey == capslockKey
# ---


def make_sc_2_uc_name(gn):
    return gn[0].upper() + gn[1:].replace('.sc', '')


def make_smallcap_name(gn):
    arbitrary_initial_letters_len = 3
    try:
        return gn[:arbitrary_initial_letters_len].lower() + gn[arbitrary_initial_letters_len:] + '.sc'
    except TypeError:
        return gn


for sl in Glyphs.font.selectedLayers:
    is_smallcapped = False
    g = sl.parent
    ugi = unified_infos.get(g.name)

    if ugi is None:
        uc_name = g.name
        ugi = unified_infos.get(make_sc_2_uc_name(g.name))
        if ugi is not None:
            is_smallcapped = True

    if ugi is not None:
        if not ugi.has_kerning and not is_smallcapped:
            ugi = unified_infos.get(make_sc_2_uc_name(g.name))
            is_smallcapped = True
            if ugi is None:
                continue

        if italic_angle(sl):
            kerning_left = ugi.kerning_italic_left or ugi.kerning_left
            kerning_right = ugi.kerning_italic_right or ugi.kerning_right
        else:
            kerning_left = ugi.kerning_left
            kerning_right = ugi.kerning_right

        g.leftKerningGroup = None
        g.rightKerningGroup = None

        if is_smallcapped:
            kerning_left = make_smallcap_name(kerning_left)
            kerning_right = make_smallcap_name(kerning_right)

        try:
            if Glyphs.font.glyphs[kerning_left] is None and not kerning_left.startswith('='):
                kerning_left = None
        except AttributeError:
            pass

        try:
            if Glyphs.font.glyphs[kerning_right] is None and not kerning_right.startswith('='):
                kerning_right = None
        except AttributeError:
            pass

        if kerning_left is not None:
            g.leftKerningGroup = kerning_left

        if kerning_right is not None:
            g.rightKerningGroup = kerning_right

    elif '_' in g.name:
        baseName1, _, styleSuffix = g.name.partition('.')

        if styleSuffix and styleSuffix not in ['liga', 'dlig', 'rlig']:
            styleSuffix = '.' + styleSuffix
        else:
            styleSuffix = ''

        baseName, x, suffix = baseName1.partition('-')
        if suffix:
            suffix = '-' + suffix

        nameParts = baseName.split('_')
        leftGN = nameParts[0] + suffix + styleSuffix
        rightGN = nameParts[-1] + suffix + styleSuffix

        if Glyphs.font.glyphs[leftGN]:
            g.leftKerningGroup = leftGN
        if Glyphs.font.glyphs[rightGN]:
            g.rightKerningGroup = rightGN
