# MenuTitle: Interpolate Anchors to Brace Layers
# -*- coding: utf-8 -*-
__doc__ = """
Interpolates the Anchors from the main masters to any Brace Layers.
"""

import re
import copy

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

temp_font = copy.copy(Glyphs.font)

for g in [l.parent for l in Glyphs.font.selectedLayers]:
    for this_layer in g.layers:
        lname_parse = re.search(r'{(\d+(\.\d+)?),? ?(\d+?(\.?\d+)?)?}', this_layer.name)
        if lname_parse is not None:
            source_glyph = temp_font.glyphs[g.name]
            for l in source_glyph.layers:
                l.paths = []
                l.components = []
            source_layer = source_glyph.layers[this_layer.name]
            source_master = source_layer.master
            other_source_layers = [copy.copy(l) for l in source_glyph.layers if l.associatedMasterId == source_master.id and l.layerId != source_master.id and l.layerId != source_layer.layerId]
            for l in other_source_layers:
                del(source_glyph.layers[l.layerId])

            source_layer.reinterpolate()
            # this_layer.anchors = []
            # original_l = copy.copy(this_layer)

            this_layer.anchors = copy.copy(source_layer.anchors)
            # g.layers[this_layer.layerId] = original_l

            for l in other_source_layers:
                source_glyph.layers.append(l)
