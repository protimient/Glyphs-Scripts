# MenuTitle: Make Background Outline
# -*- coding: utf-8 -*-
__doc__ = """
Copies the forground to the background as outlines in all selected glyphs.
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()

for g in [x.parent for x in Glyphs.font.selectedLayers]:
    for l in g.layers:
        l.background = l.copyDecomposedLayer()

Glyphs.font.enableUpdateInterface()
