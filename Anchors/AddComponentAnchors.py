# MenuTitle: Add Component Anchors
# -*- coding: utf-8 -*-
__doc__ = """
Adds the anchors from all the components to all the layers in the current glyph.
"""

from AppKit import NSEvent

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

# --- From mekkablue ---
keysPressed = NSEvent.modifierFlags()
shiftKey = 131072
shiftKeyPressed = keysPressed & shiftKey == shiftKey
# ---
keep_existing = shiftKeyPressed


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
            if keep_existing and l.anchors[aname] is not None:
                continue
            newA = GSAnchor(aname, position)
            l.anchors[aname] = newA
