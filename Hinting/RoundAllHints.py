# MenuTitle: Round All Hint values
# -*- coding: utf-8 -*-
__doc__ = """
Rounds the hints to a whole number for all glyphs in the font.
"""

for g in Glyphs.font.glyphs:
    for l in g.layers:
        for h in l.hints:
            h.position = round(h.position)
            h.width = round(h.width)
            if h.originNode:
                h.originNode.position = NSPoint(round(h.originNode.position.x), round(h.originNode.position.y))
            if h.targetNode:
                h.targetNode.position = NSPoint(round(h.targetNode.position.x), round(h.targetNode.position.y))
            if h.otherNode1:
                h.otherNode1.position = NSPoint(round(h.otherNode1.position.x), round(h.otherNode1.position.y))
            if h.otherNode2:
                h.otherNode2.position = NSPoint(round(h.otherNode2.position.x), round(h.otherNode2.position.y))
