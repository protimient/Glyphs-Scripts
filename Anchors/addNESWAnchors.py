# MenuTitle: Add Top, Bottom, Left, Right anchors
# -*- coding: utf-8 -*-
__doc__ = """
Adds all compass point anchors TopLeft, Top, TopRight, Right, BottomRight, Bottom, BottomLeft, Left
"""

# anchor_name = '_#stem'
anchor_name = ''


def get_anchors(xMin, yMin, xMax, yMax, anchor_name=''):
    top = yMax
    bottom = yMin
    left = xMin
    right = xMax
    middle = int(sum((top, bottom)) / 2)
    center = int(sum((left, right)) / 2)

    top_left = NSPoint(left, top)
    top_center = NSPoint(center, top)
    top_right = NSPoint(right, top)
    middle_left = NSPoint(left, middle)
    # middle_center = NSPoint(center, middle)
    middle_right = NSPoint(right, middle)
    bottom_left = NSPoint(left, bottom)
    bottom_center = NSPoint(center, bottom)
    bottom_right = NSPoint(right, bottom)

    return [
        GSAnchor('{}topleft'.format(anchor_name or '#'), top_left),
        GSAnchor('{}top'.format(anchor_name), top_center),
        GSAnchor('{}topright'.format(anchor_name or '#'), top_right),
        GSAnchor('{}right'.format(anchor_name or '#'), middle_right),
        GSAnchor('{}bottomright'.format(anchor_name or '#'), bottom_right),
        GSAnchor('{}bottom'.format(anchor_name), bottom_center),
        GSAnchor('{}bottomleft'.format(anchor_name or '#'), bottom_left),
        GSAnchor('{}left'.format(anchor_name or '#'), middle_left),
    ]


for g in [x.parent for x in Glyphs.font.selectedLayers]:
    for l in g.layers:
        xMin = l.bounds.origin.x
        yMin = l.bounds.origin.y
        xMax = l.bounds.origin.x + l.bounds.size.width
        yMax = l.bounds.origin.y + l.bounds.size.height
        l.anchors = list(l.anchors) + get_anchors(xMin, yMin, xMax, yMax, anchor_name=anchor_name)
