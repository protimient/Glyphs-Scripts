# MenuTitle: Add Missing Smallcaps
# -*- coding: utf-8 -*-
__doc__ = """
Adds an empty .sc glyph to match each uppercase glyph in the font.
"""

# Glyphs.showMacroWindow()


Glyphs.font.disableUpdateInterface()
for g in [g for g in Glyphs.font.glyphs if g.subCategory == "Uppercase"]:
    sc_name = g.name.lower() + '.sc'
    if not Glyphs.font.glyphs[sc_name]:
        newG = Glyphs.glyph()
        newG.name = sc_name
        newG.color = 0
        Glyphs.font.glyphs.append(newG)

Glyphs.font.enableUpdateInterface()
