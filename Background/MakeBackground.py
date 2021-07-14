# MenuTitle: Make Background
# -*- coding: utf-8 -*-
__doc__ = """
Copies the forground to the background in all selected glyphs.
"""

import copy

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()

for sl in Glyphs.font.selectedLayers:
    for l in sl.parent.layers:
        l.background = copy.copy(l)

Glyphs.font.enableUpdateInterface()
