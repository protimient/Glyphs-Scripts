# MenuTitle: Make Lowercase
# -*- coding: utf-8 -*-
__doc__ = """
Makes the glyph names lowercase for the selected glyphs.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()

for sl in Glyphs.font.selectedLayers:
    g = sl.parent
    g.name = g.name.lower()

Glyphs.font.enableUpdateInterface()
