# MenuTitle: Align Anchor Between Selected Nodes - Centre
# -*- coding: utf-8 -*-
__doc__ = """
Aligns the selected anchor centrally between the selected Nodes.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

current_selection = Glyphs.font.selectedLayers[0].selection
try:
    anchor = [x for x in current_selection if isinstance(x, GSAnchor)][0]
except KeyError:
    anchor = None

nodes = [x for x in current_selection if isinstance(x, GSNode)]

if anchor is not None and len(nodes) > 1:
    leftmost_node = min(nodes, key=lambda n: n.x)
    rightmost_node = max(nodes, key=lambda n: n.x)
    middle_x = (leftmost_node.x + rightmost_node.x) / 2
    anchor.x = middle_x
