# MenuTitle: Mark Marks
# -*- coding: utf-8 -*-
__doc__ = """
Checks every glyph in the font and colours them if they contain an anchor starting with '_' (e.g. _top).
Otherwise, marks them clear.
"""

Glyphs.font.disableUpdateInterface()
for g in Glyphs.font.glyphs:
    if g.color < 12:
        g.color = 666

    for l in g.layers:
        for a in l.anchors:
            if a.name.startswith('_'):
                g.color = 4
Glyphs.font.enableUpdateInterface()
