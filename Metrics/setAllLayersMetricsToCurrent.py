# MenuTitle: Set LSB and Width of all Layers to the Current layer
# -*- coding: utf-8 -*-
__doc__ = """
Sets the left sidebearing and width of all other layers in the selected glyphs to that of the currently selected layer.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()

for sl in Glyphs.font.selectedLayers:
    g = sl.parent
    for li, l in enumerate(g.layers):
        if l == sl:
            continue

        l.LSB = sl.LSB
        l.width = sl.width

Glyphs.font.enableUpdateInterface()
