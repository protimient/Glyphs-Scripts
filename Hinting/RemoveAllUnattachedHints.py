# MenuTitle: Remove All Unattached PS Hints
# -*- coding: utf-8 -*-
__doc__ = """
Removes all Postscript hints that are not attached to a node.
"""

Glyphs.clearLog()
Glyphs.showMacroWindow()

# for g in Glyphs.font.glyphs:
if 1:
    g = Glyphs.font.selectedLayers[0].parent
    for l in g.layers:
        deletable_hint_indexes = [hi for hi, h in enumerate(l.hints) if not h.originNode]
        for hi in deletable_hint_indexes:
            del(l.hints[hi])
