# MenuTitle: Copy Components Metrics for Current Layer
# -*- coding: utf-8 -*-
__doc__ = """
Sets the current layer's metrics to match the selected or first component.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

for l in Glyphs.font.selectedLayers:
    if not l.selection:
        try:
            c = l.components[0]
        except IndexError:
            continue
    else:
        try:
            c = [x for x in l.selection if type(x) == GSComponent][0]
        except IndexError:
            continue
    if not c:
        continue

    if c.transform[0] < 0:
        l.LSB = c.componentLayer.RSB
    else:
        l.LSB = c.componentLayer.LSB
    l.width = c.componentLayer.width
