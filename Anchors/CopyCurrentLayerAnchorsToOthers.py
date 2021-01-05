# MenuTitle: Copy Selected Anchors to Other Layers
# -*- coding: utf-8 -*-
__doc__ = """
Copies the selected Anchors in the current layer to all other layers in the current glyph.
"""
import copy

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

sl = Glyphs.font.selectedLayers[0]
g = Glyphs.font.selectedLayers[0].parent

for l in g.layers:
    if l.layerId == sl.layerId:
        continue

    selected_anchors = [x for x in sl.selection if type(x) == GSAnchor] or sl.anchors
    for a in selected_anchors:
        new_a = copy.copy(a)
        l.anchors.append(new_a)
