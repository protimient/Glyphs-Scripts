# MenuTitle: Compare Glyphs Names and Unicodes Font to Font
# -*- coding: utf-8 -*-
__doc__ = """
Colours in Green any glyphs contained in one font and not the other. Glyphs that are contained in both are coloured white.
"""

ignore_colours = []

if len(Glyphs.fonts) == 2:
    for fi, f in enumerate(Glyphs.fonts):
        if f == Glyphs.font:
            thisFont = f
            otherFont = Glyphs.fonts[abs(fi - 1)]
            break

    for g in [x for x in thisFont.glyphs if x.color not in ignore_colours]:
        if g.color < 12:
            g.color = 666
        g1 = g
        g2 = otherFont.glyphs[g.name]

        if not g2 and g.unicode:
            g2 = otherFont.glyphs[g.unicode]

        if not g2:
            g.color = 5

        elif not g1.export == g2.export:
            g.color = 4

    for g in [x for x in otherFont.glyphs if x.color not in ignore_colours]:
        if g.color < 12:
            g.color = 666
        g1 = g
        g2 = thisFont.glyphs[g.name]

        if not g2 and g.unicode:
            g2 = thisFont.glyphs[g.unicode]

        if not g2:
            g.color = 5

        elif not g1.export == g2.export:
            g.color = 4

else:
    Glyphs.clearLog()
    Glyphs.showMacroWindow()
    print('2, and only 2, fonts can be open!')
