# MenuTitle: Delete Background for Selected Glyphs
# -*- coding: utf-8 -*-
__doc__ = """
Clears the background layer for all selected glyphs.
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()

for g in [x.parent for x in Glyphs.font.selectedLayers]:
    for l in g.layers:
        l.background = GSLayer()

Glyphs.font.enableUpdateInterface()
