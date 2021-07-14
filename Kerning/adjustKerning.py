# MenuTitle: Increase Kerning
# -*- coding: utf-8 -*-
__doc__ = """
Uses modifier keys to adjust the kerning.
"""

from AppKit import NSEvent
from GlyphsApp import Glyphs

Glyphs.clearLog()
# Glyphs.showMacroWindow()

# --- From mekkablue ---
keysPressed = NSEvent.modifierFlags()
shiftKey = 131072
controlKey = 262144
optionKey = 524288
commandKey = 1048576
shiftKeyPressed = keysPressed & shiftKey == shiftKey
controlKeyPressed = keysPressed & controlKey == controlKey
optionKeyPressed = keysPressed & optionKey == optionKey
commandKeyPressed = keysPressed & commandKey == commandKey
# ---


def get_current_glyphs():
    g1 = Glyphs.font.currentTab.layers[Glyphs.font.currentTab.layersCursor - 1].parent
    g2 = Glyphs.font.currentTab.layers[Glyphs.font.currentTab.layersCursor].parent
    return g1, g2


def get_current_layers(names=False):
    g1, g2 = get_current_glyphs()
    l1 = g1.layers[Glyphs.font.selectedFontMaster.id]
    l2 = g2.layers[Glyphs.font.selectedFontMaster.id]
    if names:
        return l1.parent.name, l2.parent.name
    return l1, l2


def get_kerning_dict_entry(current_kerning_dict):
    l1, l2 = get_current_layers()

    left_name = l1.parent.name
    left_key = l1.parent.id
    left_class = l1.parent.rightKerningGroup
    if left_class:
        left_class = '@MMK_L_{}'.format(left_class)

    right_name = l2.parent.name
    right_key = l2.parent.id
    right_class = l2.parent.leftKerningGroup
    if right_class:
        right_class = '@MMK_R_{}'.format(right_class)

    if current_kerning_dict.get(left_key):
        if current_kerning_dict[left_key].get(right_key):
            val = current_kerning_dict[left_key][right_key]
            return left_name, right_name, val
        elif current_kerning_dict[left_key].get(right_class):
            val = current_kerning_dict[left_key].get(right_class, 0)
            return left_name, right_class, val
    elif current_kerning_dict.get(left_class):
        if current_kerning_dict.get(left_class).get(right_key):
            val = current_kerning_dict[left_class][right_key]
            return left_class, right_name, val
        elif current_kerning_dict[left_key].get(right_class):
            val = current_kerning_dict[left_class].get(right_class, 0)
            return left_class, right_class, val

    left_side = left_class or left_name
    right_side = right_class or right_name
    val = 0

    return left_side, right_side, val


def adjust_kerning(offset):
    current_kerning_dict = Glyphs.font.kerning[Glyphs.font.selectedFontMaster.id]
    left_side, right_side, val = get_kerning_dict_entry(current_kerning_dict)

    gn1, gn2 = get_current_layers(names=True)
    print(left_side, right_side, val)
    if not left_side.startswith('@'):
        left_side = gn1
    if not right_side.startswith('@'):
        right_side = gn2

    new_val = val + offset

    Glyphs.font.setKerningForPair(Glyphs.font.selectedFontMaster.id, left_side, right_side, new_val)
    # Glyphs.font.currentTab.redraw()
