# MenuTitle: Copy Components Metrics for All Layers
# -*- coding: utf-8 -*-
__doc__ = """
Sets each layer's metrics to match the first component.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

for sl in Glyphs.font.selectedLayers:
    for l in sl.parent.layers:
        try:
            c = l.components[0]
        except IndexError:
            continue

        if c.transform[0] < 0:
            l.LSB = c.componentLayer.RSB
        else:
            l.LSB = c.componentLayer.LSB
        l.width = c.componentLayer.width
