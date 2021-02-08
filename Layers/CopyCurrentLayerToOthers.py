# MenuTitle: Copy Current Layer to Others
# -*- coding: utf-8 -*-
__doc__ = """
Replaces the contents of all other layers in the selected glyphs with the contents of the currently selected layer.
"""

import copy

Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()

for sl in Glyphs.font.selectedLayers:
    g = sl.parent
    for li, l in enumerate(g.layers):
        if l == sl:
            continue
        new_l = copy.copy(sl)
        new_l.name = l.name
        new_l.associatedMasterId = l.associatedMasterId
        g.layers[li] = new_l

Glyphs.font.enableUpdateInterface()
