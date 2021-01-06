# MenuTitle: Make Inferior Numerals from Superiors
# -*- coding: utf-8 -*-
__doc__ = """
Adds the Inferiors to the font as composite glyphs using the Superiors as vertically shifted components.
"""

Glyphs.font.disableUpdateInterface()

suffixes = ('.sups', '.subs')

Glyphs.clearLog()
# Glyphs.showMacroWindow()


theseGlyphs = [g for g in Glyphs.font.glyphs if g.name.endswith(suffixes[0])]

for g in theseGlyphs:
    sinf_gn = g.name.replace(suffixes[0], suffixes[1])
    sinf_g = Glyphs.font.glyphs[sinf_gn]

    if sinf_g is None:
        sinf_g = GSGlyph(sinf_gn)
        Glyphs.font.glyphs.append(sinf_g)
    else:
        for l in sinf_g.layers:
            l.paths = []
            l.anchors = []
            l.components = []

    for li, l in enumerate(g.layers):
        outline_height = l.bounds.size.height
        outline_bottom = l.bounds.origin.y
        offset = -(outline_bottom + (outline_height / 2))
        comp = GSComponent(g.name)
        comp.setPosition_((0, offset))
        Glyphs.font.glyphs[sinf_gn].layers[li].components.append(comp)

        Glyphs.font.glyphs[sinf_gn].layers[li].LSB = l.LSB
        Glyphs.font.glyphs[sinf_gn].layers[li].RSB = l.RSB

    Glyphs.font.glyphs[sinf_gn].leftMetricsKey = g.name
    Glyphs.font.glyphs[sinf_gn].rightMetricsKey = g.name


Glyphs.font.enableUpdateInterface()
