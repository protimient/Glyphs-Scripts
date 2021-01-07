# MenuTitle: Delete Custom Layers (keeps bracket layers)
# -*- coding: utf-8 -*-
__doc__ = """
"""

import re

Glyphs.clearLog()
# Glyphs.showMacroWindow()

masterIds = [m.id for m in Glyphs.font.masters]

for g in Glyphs.font.glyphs:
    if g.name.startswith('_part.'):
        continue

    deletables = []
    for l in g.layers:
        isBracketLeyer = bool(re.search(r'\[|\]|\{|\}', l.name))

        if l.layerId not in masterIds and not isBracketLeyer:
            deletables.append(l.layerId)

    if deletables:
        print(g.name)
    for lid in deletables:
        print(g.layers[lid].name)
        del g.layers[lid]
