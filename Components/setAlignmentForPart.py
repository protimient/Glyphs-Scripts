# MenuTitle: Set Alignment For _part
# -*- coding: utf-8 -*-
__doc__ = """
Aligns _part glyphs and un-aligns other components to allow for metrics keys.
"""

Glyphs.font.disableUpdateInterface()  # suppresses UI updates in Font View

g = Glyphs.font.selectedLayers[0].parent

for g in [x.parent for x in Glyphs.font.selectedLayers]:
    for l in g.layers:
        for ci, c in enumerate(l.components):
            if ci > 0:
                c.setIsAligned_(2)
            else:
                c.setIsAligned_(-1)

Glyphs.font.enableUpdateInterface()  # re-enables UI updates in Font View
