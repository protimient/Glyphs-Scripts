# MenuTitle: Display Kerning Permutations for Pair
# -*- coding: utf-8 -*-
__doc__ = """
When 2 glyphs are selected, this will open a new tab listing all the possible pairs in the glyph’s groups.
"""

from itertools import product

# Glyphs.clearLog()
# Glyphs.showMacroWindow()


def get_current_glyphs():
    g1 = Glyphs.font.currentTab.layers[Glyphs.font.currentTab.layersCursor - 1].parent
    g2 = Glyphs.font.currentTab.layers[Glyphs.font.currentTab.layersCursor].parent
    return g1, g2


try:
    g1, g2 = [g.parent for g in Glyphs.font.selectedLayers]
except ValueError:
    g1, g2 = get_current_glyphs()

if g1 and g2:
    leftGroup = g1.rightKerningGroup
    rightGroup = g2.leftKerningGroup

    lefts = []
    rights = []

    if not leftGroup:
        lefts = ['/' + g1.name]

    if not rightGroup:
        rights = ['/' + g2.name]

    for g in Glyphs.font.glyphs:
        if leftGroup and g.rightKerningGroup == leftGroup:
            lefts.append('/' + g.name)
        if rightGroup and g.leftKerningGroup == rightGroup:
            rights.append('/' + g.name)

    string = '  '.join(list(''.join(x) for x in product(lefts, rights)))

    if string:
        Glyphs.font.newTab(string)
