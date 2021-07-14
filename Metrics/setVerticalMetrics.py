# MenuTitle: Set Vertical Metrics
# -*- coding: utf-8 -*-
__doc__ = """
Sets the vertical metrics based on the yMax/yMin and typographic values.
"""
from collections import defaultdict
Glyphs.clearLog()


class setVerticalMetrics:
    def __init__(self):
        self.makeitso()

    def get_extremes(self, master):
        extremes = defaultdict(list)
        for g in [x for x in Glyphs.font.glyphs if x.export and x.layers[master.id].width]:
            extremes['xMin'].append(g.layers[master.id].bounds.origin.x)
            extremes['xMax'].append(g.layers[master.id].bounds.origin.x + g.layers[master.id].bounds.size.width)
            extremes['yMin'].append(g.layers[master.id].bounds.origin.y)
            extremes['yMax'].append(g.layers[master.id].bounds.origin.y + g.layers[master.id].bounds.size.height)

        extremes['xMin'] = min(extremes['xMin'])
        extremes['xMax'] = max(extremes['xMax'])
        extremes['yMin'] = min(extremes['yMin'])
        extremes['yMax'] = max(extremes['yMax'])

        return extremes

    def makeitso(self):
        for m in Glyphs.font.masters:
            extremes = self.get_extremes(m)

            try:
                ascender_g = Glyphs.font.glyphs['d'].layers[m.id]
            except AttributeError:
                ascender_g = Glyphs.font.glyphs['H'].layers[m.id]
            ascender = ascender_g.bounds.size.height + ascender_g.bounds.origin.y
            m.setAscender_(ascender)

            cap_g = Glyphs.font.glyphs['H'].layers[m.id]
            cap = cap_g.bounds.size.height + cap_g.bounds.origin.y
            m.setCapHeight_(cap)

            try:
                x_g = Glyphs.font.glyphs['x'].layers[m.id]
                x = x_g.bounds.size.height + x_g.bounds.origin.y
                m.setXHeight_(x)
            except AttributeError:
                pass

            try:
                descender_g = Glyphs.font.glyphs['p'].layers[m.id]
            except AttributeError:
                descender_g = Glyphs.font.glyphs['J'].layers[m.id]
            descender = descender_g.bounds.origin.y
            m.setDescender_(descender)

            m.customParameters['typoAscender'] = ascender
            m.customParameters['typoDescender'] = descender
            m.customParameters['typoLineGap'] = 200

            m.customParameters['hheaAscender'] = extremes['yMax']
            m.customParameters['hheaDescender'] = extremes['yMin']
            m.customParameters['hheaLineGap'] = 0

            m.customParameters['winAscent'] = extremes['yMax']
            m.customParameters['winDescent'] = extremes['yMin']


setVerticalMetrics()
