# MenuTitle: Center and Zero-Width current Layer
# -*- coding: utf-8 -*-
__doc__ = """
Center and make Zero-Width all selected glyphs.
"""

from collections import defaultdict


class centerAndZeroWidth:
    def __init__(self):
        self.composites_dict = defaultdict(set)
        for g in Glyphs.font.glyphs:
            for l in g.layers:
                for c in l.components:
                    self.composites_dict[c.name].add(g)

    def __call__(self, this_layer):
        relocation = self.get_relocation(this_layer)
        self.make_zerowidth(this_layer, relocation)
        self.relocate_components(this_layer, -relocation)

    def relocate_components(self, component_l, relocation):
        affected_glyphs = self.composites_dict.get(component_l.parent.name)
        for g in affected_glyphs:
            affected_layer = self.get_corresponding_layer(g, component_l)
            for c in affected_layer.components:
                if c.name == component_l.parent.name:
                    c.applyTransform((1, 0, 0, 1, relocation, 0))

    def get_corresponding_layer(self, target_g, source_l):
        try:
            ml = [x for x in target_g.layers if x.name == source_l.name][0]
        except IndexError:
            ml = target_g.layers[source_l.associatedMasterId]

        return ml

    def make_zerowidth(self, l, relocation=None):
        print(relocation)
        if relocation is None:
            relocation = self.get_relocation(l)

        l.width = 0
        l.applyTransform((1, 0, 0, 1, relocation, 0))

    def get_relocation(self, l):
        if l.width == 0:
            return 0

        relocation = -l.LSB - (l.bounds.size.width / 2)

        return relocation

    def clear_metrics_keys(self, g):
        g.leftMetricsKey = None
        g.rightMetricsKey = None
        g.widthMetricsKey = None
        for l in g.layers:
            l.leftMetricsKey = None
            l.rightMetricsKey = None
            l.widthMetricsKey = None


Glyphs.font.disableUpdateInterface()
make_zero = centerAndZeroWidth()

for l in Glyphs.font.selectedLayers:
    make_zero(l)

Glyphs.font.enableUpdateInterface()
