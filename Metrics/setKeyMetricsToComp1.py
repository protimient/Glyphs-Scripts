# MenuTitle: Set KeyMetrics to BaseComponent
# -*- coding: utf-8 -*-
__doc__ = """
Sets the left and right KeyMetrics to the name of the first component.
"""

for g in [x.parent for x in Glyphs.font.selectedLayers]:
    g.leftMetricsKey = g.layers[0].components[0].componentName
    g.rightMetricsKey = g.layers[0].components[0].componentName
