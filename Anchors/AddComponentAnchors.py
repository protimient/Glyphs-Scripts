# MenuTitle: Add Component Anchors
# -*- coding: utf-8 -*-
__doc__ = """
Adds the anchors from all the components to all the layers in the current glyph.
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()


def get_component_anchors(layer, anchor_dict):
    for c in layer.components:
        l = c.componentLayer
        for a in l.anchors:
            if anchor_dict.get(a.name) is None:
                anchor_dict[a.name] = NSPoint(a.x + c.transform[-2], a.y + c.transform[-1])

        anchor_dict = get_component_anchors(l, anchor_dict)

    return anchor_dict


for g in [x.parent for x in Glyphs.font.selectedLayers]:
    for l in g.layers:
        anchors = get_component_anchors(l, {})
        for aname, position in anchors.items():
            newA = GSAnchor(aname, position)
            l.anchors[aname] = newA
