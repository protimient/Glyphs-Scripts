# MenuTitle: Make numr/dnom from sups/sinf
# -*- coding: utf-8 -*-
__doc__ = """
Adds numerator and denominator glyphs as components of superior and inferior numerals.
"""
Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()

nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for base_gn in nums:
    source_gn = base_gn + 'superior'
    source_g = Glyphs.font.glyphs[source_gn]
    gn = base_gn + '.numr'

    if Glyphs.font.glyphs[gn] is None:
        new_g = GSGlyph(gn)
        Glyphs.font.glyphs.append(new_g)
        new_g = Glyphs.font.glyphs[gn]
        new_g.updateGlyphInfo()
        for l in new_g.layers:
            new_c = GSComponent(source_gn)
            new_c.automaticAlignment = True
            l.components = [new_c]

    source_gn = base_gn + 'inferior'
    source_g = Glyphs.font.glyphs[gn]
    gn = base_gn + '.dnom'

    if Glyphs.font.glyphs[gn] is None:
        new_g = GSGlyph(gn)
        Glyphs.font.glyphs.append(new_g)
        new_g = Glyphs.font.glyphs[gn]
        new_g.updateGlyphInfo()
        for l in new_g.layers:
            new_c = GSComponent(source_gn)
            new_c.automaticAlignment = True
            l.components = [new_c]

Glyphs.font.enableUpdateInterface()
