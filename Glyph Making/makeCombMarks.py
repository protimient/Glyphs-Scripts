# MenuTitle: Add missing combining marks
# -*- coding: utf-8 -*-
__doc__ = """
Makes combining versions of the legacy accent glyphs if they are missing.
"""

import math

Glyphs.clearLog()
# Glyphs.showMacroWindow()


def make_zerowidth(l, doit=True):
    if l.width == 0:
        return 0

    relocation = -l.LSB - (l.bounds.size.width / 2)
    if doit:
        l.width = 0
        l.applyTransform((1, 0, 0, 1, relocation, 0))

    return relocation


class glyphData():
    def __init__(self, glyph_name, **kwargs):
        self.glyph_name = glyph_name
        self.source_name = kwargs.get('source_name', '')
        self.source_names = kwargs.get('source_names', [self.source_name])
        self.position_y = kwargs.get('position_y')
        self.rotation = float(kwargs.get('rotation', 0))
        self.flip = kwargs.get('rotation')
        self.glyph = self._glyph()
        self.source = self._source()

    def italic_angle(self, layer):
        try:
            return Glyphs.font.masters[layer.associatedMasterId].italicAngle
        except AttributeError:
            return 0

    def report(self, message):
        print(message)
        return

    def _glyph(self):
        return Glyphs.font.glyphs[self.glyph_name]

    def _source(self):
        for gn in self.source_names:
            g = Glyphs.font.glyphs[gn]
            if g is not None:
                return g
        return None

    def compensate_italic_angle(self, pos_y, italic_angle):
        if not italic_angle:
            return 0
        return round(math.tan(math.radians(italic_angle)) * pos_y)

    def get_coords(self, position_key, layer):
        if position_key is None:
            return {}

        return getattr(self, position_key, lambda _: (0, 0))(layer)

    def above_ascender(self, layer):
        g = Glyphs.font.glyphs['0308']
        if g is None:
            for gn in ['dieresiscomb', 'dieresis']:
                g = Glyphs.font.glyphs[gn]
                if g is not None:
                    break

        if g is None:
            newy = Glyphs.font.masters[layer.associatedMasterId].ascender
        else:
            newy = g.layers[layer.associatedMasterId].bounds.origin.y - layer.bounds.origin.y

        new_coords = (self.compensate_italic_angle(newy, self.italic_angle(layer)), newy)
        return new_coords

    def below_baseline(self, layer):
        g = Glyphs.font.glyphs['0326']
        if g is None:
            for gn in ['commaaccentcomb', 'commaaccent', 'uni0326']:
                g = Glyphs.font.glyphs[gn]
                if g is not None:
                    break

        if g is None:
            newy = int(-69000.0 / Glyphs.font.upm)
        else:
            newy = (g.layers[layer.associatedMasterId].bounds.origin.y + g.layers[layer.associatedMasterId].bounds.size.height) - (layer.bounds.origin.y + layer.bounds.size.height)

        newx = self.compensate_italic_angle(newy, self.italic_angle(layer))
        new_coords = (newx, newy)
        return new_coords

    def make_glyph(self):
        if self.glyph is not None:
            self.report('{} already exists'.format(self.glyph_name))
            return

        if self.source is None:
            self.report('Could not find the source glyph! {}'.format(self.source_names[0]))
            return

        newG = GSGlyph()
        newG.name = self.glyph_name

        for m in font.masters:
            parent_layer = self.source.layers[m.id]
            newLayer = GSLayer()
            newLayer.associatedMasterId = m.id
            newC = GSComponent(self.source.name)
            newLayer.components.append(newC)
            newLayer.width = self.source.layers[m.id].width

            if self.flip or self.rotation:
                if self.flip == 'horizontal':
                    this_scale_x = -1
                    this_scale_y = 1
                elif self.flip == 'vertical':
                    this_scale_x = 1
                    this_scale_y = -1
                else:
                    this_scale_x = 1
                    this_scale_y = 1

                if abs(self.rotation) == 90:
                    this_scale_x, this_scale_y = (this_scale_y, this_scale_x)

                newC.setScaleX_scaleY_rotation_(this_scale_x, this_scale_y, self.rotation)

                offset_x = parent_layer.bounds.origin.x - newC.bounds.origin.x
                offset_y = parent_layer.bounds.origin.y - newC.bounds.origin.y
                newC.setPosition_(NSPoint(offset_x, offset_y))

            if self.position_y is not None:
                new_x, new_y = self.get_coords(self.position_y, parent_layer)
                newC.position = NSPoint(new_x, new_y)

            newG.layers[m.id] = newLayer

        Glyphs.font.glyphs.append(newG)

        newG.updateGlyphInfo()
        self.glyph = newG


glyphs = (
    glyphData('commaabovecomb', source_names=['commaaccent', 'commaaccentcomb'], position_y='above_ascender'),
    glyphData('commaaccentcomb', source_names=['commaaccent', 'commaaccentcomb'],),
    glyphData('commaturnedabovecomb', source_names=['commaaccent', 'commaaccentcomb'], rotation=180, position_y='above_ascender'),
    glyphData('acutecomb', source_name='acute',),
    glyphData('brevecomb', source_name='breve',),
    glyphData('caroncomb', source_name='caron',),
    glyphData('cedillacomb', source_name='cedilla',),
    glyphData('circumflexcomb', source_name='circumflex',),
    glyphData('dieresiscomb', source_name='dieresis',),
    glyphData('dotaccentcomb', source_name='dotaccent',),
    glyphData('gravecomb', source_name='grave',),
    glyphData('hungarumlautcomb', source_name='hungarumlaut',),
    glyphData('macroncomb', source_name='macron',),
    glyphData('ogonekcomb', source_name='ogonek',),
    glyphData('ringcomb', source_name='ring',),
    glyphData('tildecomb', source_name='tilde',),
    glyphData('macronbelowcomb', source_name='macron', position_y='below_baseline'),
    glyphData('brevebelowcomb', source_name='breve', position_y='below_baseline'),
    glyphData('dotbelowcomb', source_name='dotaccent', position_y='below_baseline'),
    glyphData('dieresisbelowcomb', source_name='dieresis', position_y='below_baseline'),
    glyphData('ringbelowcomb', source_name='ring', position_y='below_baseline'),
)


def go(font):
    for g in glyphs:
        g.make_glyph()


font = Glyphs.font
go(font)
