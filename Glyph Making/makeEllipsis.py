# MenuTitle: Make Ellipsis
# -*- coding: utf-8 -*-
__doc__ = """
Makes or replaces the ellipsis with a default version.
"""

Glyphs.clearLog()


def period_positions(period_width, period_left, em_width):
    y = (em_width - (3 * period_width)) / 3

    a = round(y / 2) - period_left
    b = round(((y * 3) / 2) + period_width) - period_left
    c = round(((y * 5) / 2) + (period_width * 2)) - period_left

    return a, b, c


def makeEllipsis(font):
    if font.glyphs['ellipsis']:
        del font.glyphs['ellipsis']

    ellipsis = GSGlyph('ellipsis')
    period = font.glyphs['period']

    for i, l in enumerate(period.layers):
        em_width = font.glyphs['emdash'].layers[i].width

        new_layer = GSLayer()
        new_layer.width = em_width
        new_layer.associatedMasterId = l.associatedMasterId
        # new_layer.layerId = l.layerId

        for pos in period_positions(l.bounds.size.width, l.LSB, em_width):
            new_layer.components.append(GSComponent('period', NSPoint(pos, 0)))

        ellipsis.layers[l.layerId] = new_layer

    font.glyphs.append(ellipsis)

    print('Made ellipsis')
    return font


makeEllipsis(Glyphs.font)
