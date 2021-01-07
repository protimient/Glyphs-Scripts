# MenuTitle: Compare Kerning Groups Font to Font
# -*- coding: utf-8 -*-
__doc__ = """
Colours glyphs in font view according to their differences.
"""

import os
Glyphs.clearLog()

if len(Glyphs.fonts) == 2:
    f1 = Glyphs.font
    f2 = Glyphs.fonts[abs(Glyphs.fonts.index(f1) - 1)]

    for g in f1.glyphs:
        if g.color < 12:
            g.color = 666
        g1 = g
        g2 = f2.glyphs[g.name]

        if not g2:
            g.color = 0
            break

        if g1.rightKerningGroup != g2.rightKerningGroup:
            g.color = 3

        if g1.leftKerningGroup != g2.leftKerningGroup:
            if g.color == 3:
                g.color = 4
            else:
                g.color = 6

    message = [
        'Comparing {0} vs. {1}'.format(os.path.basename(f1.filepath), os.path.basename(f2.filepath)),
        'Red = The glyph is missing in the other font.',
        'Blue = The left Kerning Group is different.',
        'Yellow = The right Kerning Group is different.',
        'Green = Both left and right Kerning Groups are different.',
    ]

    print('\n'.join(message))

Glyphs.showMacroWindow()
