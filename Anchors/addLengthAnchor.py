# MenuTitle: Add Length Anchor
# -*- coding: utf-8 -*-
__doc__ = """
Adds an anchor named ‘length’ at the top right node on all layers.
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

g = Glyphs.font.selectedLayers[0].parent

for l in g.layers:
    pos_node = max([n for p in l.paths for n in p.nodes], key=lambda z: z.x)
    a = GSAnchor('length', NSPoint(pos_node.x, pos_node.y))
    l.anchors.append(a)
