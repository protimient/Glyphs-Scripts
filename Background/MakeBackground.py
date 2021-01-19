# MenuTitle: Make Background
# -*- coding: utf-8 -*-
__doc__ = """
Copies the forground to the background in all selected glyphs.
"""

import copy

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()

for g in [x.parent for x in Glyphs.font.selectedLayers]:
    for l in g.layers:
        l.background = copy.copy(l)

Glyphs.font.enableUpdateInterface()
