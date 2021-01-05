# MenuTitle: Display Glyph With All Others
# -*- coding: utf-8 -*-
__doc__ = """
Makes a AXA AXB AXC AXD... display with the selected glyph against all glyphs in the font. Mainly to check for collisions.
"""

Glyphs.clearLog()

all_glyph_names = [g.name for g in Glyphs.font.glyphs if g.export]

for sl in Glyphs.font.selectedLayers:
    g = sl.parent

    gn = g.name
    glyph_strings = ['/{0}/{1}/{0}'.format(x, gn) for x in all_glyph_names]
    string = '  '.join(glyph_strings)
    Glyphs.font.newTab(string)

# Glyphs.showMacroWindow()
