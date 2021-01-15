# MenuTitle: Unlock Kerning For Selected
# -*- coding: utf-8 -*-
__doc__ = """
Unlocks the kerning for the current layer of the selected glyphs.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()


Glyphs.font.disableUpdateInterface()  # suppresses UI updates in Font View

these_layers = Glyphs.font.selectedLayers
if len(these_layers) < 2:
    try:
        these_layers = [
            Glyphs.font.currentTab.layers[Glyphs.font.currentTab.layersCursor - 1],
            Glyphs.font.currentTab.layers[Glyphs.font.currentTab.layersCursor],
        ]
    except IndexError:
        print('oppps')
        these_layers = None
print(these_layers)
if these_layers:
    for li, l in enumerate(these_layers):
        try:
            next_l = these_layers[li + 1]
        except IndexError:
            break

        kv = Glyphs.font.kerningForPair(l.associatedMasterId, l.parent.rightKerningKey or l.parent.name, next_l.parent.leftKerningKey or next_l.parent.name)

        if kv == 9.223372036854776e+18:
            kv = 0

        Glyphs.font.setKerningForPair(l.associatedMasterId, l.parent.name, next_l.parent.name, kv)

Glyphs.font.enableUpdateInterface()  # re-enables UI updates in Font View
