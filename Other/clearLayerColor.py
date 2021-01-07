# MenuTitle: Clear Layer Colors
# -*- coding: utf-8 -*-
__doc__ = """
Clears all coloring from the selected glyphs.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

glyph_selection = [l.parent for l in Glyphs.font.selectedLayers]

for g in glyph_selection:
    g.color = 9223372036854775807
    for l in g.layers:
        l.color = 9223372036854775807
