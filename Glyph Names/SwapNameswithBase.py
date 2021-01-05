# MenuTitle: Swap selected suffix'd Name with Base name
# -*- coding: utf-8 -*-
__doc__ = """
For the selected glyphs, the base name and the selected name will be swapped.
E.g. A.sc -> A (A -> A.sc)
"""

Glyphs.clearLog()
Glyphs.showMacroWindow()

for g in [x.parent for x in Glyphs.font.selectedLayers]:
    gn = str(g.name)
    base_name, x, suffix = gn.partition('.')
    base_g = Glyphs.font.glyphs[base_name]
    temp_name = 'kajhsksjdhbdsavbhakjsdhvb'
    if base_g:
        base_g.name = temp_name
        g.name = base_name
        base_g.name = gn
