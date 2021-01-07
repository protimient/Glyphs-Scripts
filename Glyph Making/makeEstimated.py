# MenuTitle: Make Estimated
# -*- coding: utf-8 -*-
__doc__ = """
Makes or replaces the estimated with the correct, EU approved shape.
"""


def estimatedGlyph(font):
    glyph_nodes = (
        (
            ((202.0, 723.0), OFFCURVE, 0),
            ((50.0, 562.0), OFFCURVE, 0),
            ((50.0, 354.0), CURVE, 100),
            ((50.0, 142.0), OFFCURVE, 0),
            ((209.0, -13.0), OFFCURVE, 0),
            ((453.0, -13.0), CURVE, 100),
            ((624.0, -13.0), OFFCURVE, 0),
            ((729.0, 63.0), OFFCURVE, 0),
            ((776.0, 129.0), CURVE, 0),
            ((704.0, 129.0), LINE, 0),
            ((649.0, 62.0), OFFCURVE, 0),
            ((556.0, 14.0), OFFCURVE, 0),
            ((453.0, 14.0), CURVE, 0),
            ((355.0, 14.0), OFFCURVE, 0),
            ((276.0, 50.0), OFFCURVE, 0),
            ((215.0, 110.0), CURVE, 100),
            ((202.0, 122.0), OFFCURVE, 0),
            ((199.0, 135.0), OFFCURVE, 0),
            ((199.0, 156.0), CURVE, 100),
            ((199.0, 331.0), LINE, 0),
            ((199.0, 338.0), OFFCURVE, 0),
            ((205.0, 344.0), OFFCURVE, 0),
            ((213.0, 344.0), CURVE, 0),
            ((855.0, 344.0), LINE, 0),
            ((855.0, 548.0), OFFCURVE, 0),
            ((708.0, 723.0), OFFCURVE, 0),
            ((453.0, 723.0), CURVE, 100)
        ),
        (
            ((534.0, 696.0), OFFCURVE, 0),
            ((617.0, 669.0), OFFCURVE, 0),
            ((689.0, 598.0), CURVE, 100),
            ((702.0, 586.0), OFFCURVE, 0),
            ((705.0, 575.0), OFFCURVE, 0),
            ((705.0, 555.0), CURVE, 100),
            ((705.0, 380.0), LINE, 100),
            ((705.0, 372.0), OFFCURVE, 0),
            ((699.0, 367.0), OFFCURVE, 0),
            ((691.0, 367.0), CURVE, 100),
            ((213.0, 367.0), LINE, 0),
            ((205.0, 367.0), OFFCURVE, 0),
            ((199.0, 372.0), OFFCURVE, 0),
            ((199.0, 380.0), CURVE, 0),
            ((199.0, 555.0), LINE, 100),
            ((199.0, 575.0), OFFCURVE, 0),
            ((202.0, 586.0), OFFCURVE, 0),
            ((215.0, 598.0), CURVE, 100),
            ((276.0, 659.0), OFFCURVE, 0),
            ((355.0, 696.0), OFFCURVE, 0),
            ((453.0, 696.0), CURVE, 100)
        )
    )

    estimated = GSGlyph('estimated')

    for m in font.masters:
        try:
            scale = float(font.glyphs['eight'].layers[m.id].bounds.size.height + font.glyphs['eight'].layers[m.id].bounds.origin.y) / 723
        except AttributeError:
            scale = font.upm / 1000

        if not scale:
            scale = font.upm / 1000

        l = GSLayer()
        l.width = int(905 * scale)
        l.associatedMasterId = m.id

        for path in glyph_nodes:
            p = GSPath()
            p.closed = True

            for node in path:
                coords, node_type, connection = node

                x = int(coords[0] * scale)
                y = int(coords[1] * scale)
                n = GSNode(NSPoint(x, y))
                n.type = node_type
                n.connection = connection

                p.nodes.append(n)

            l.paths.append(p)
        estimated.layers[m.id] = l

    estimated.updateGlyphInfo()
    return estimated


def makeEstimated(font):
    if font.glyphs['estimated']:
        del font.glyphs['estimated']

    estimated = estimatedGlyph(font)

    font.glyphs.append(estimated)

    print('Made estimated')
    return font


font = Glyphs.font
makeEstimated(font)
