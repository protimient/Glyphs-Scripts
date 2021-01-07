# MenuTitle: Make Dotted Circle
# -*- coding: utf-8 -*-
__doc__ = """
Makes or replaces the dottedcircle with a default version.
"""


def make_glyph(font):
    glyph_nodes = [
        [
            ((588.0, 602.0), OFFCURVE, 0),
            ((606.0, 620.0), OFFCURVE, 0),
            ((606.0, 641.0), CURVE, 100),
            ((606.0, 664.0), OFFCURVE, 0),
            ((588.0, 682.0), OFFCURVE, 0),
            ((567.0, 682.0), CURVE, 100),
            ((545.0, 682.0), OFFCURVE, 0),
            ((527.0, 664.0), OFFCURVE, 0),
            ((527.0, 641.0), CURVE, 100),
            ((527.0, 620.0), OFFCURVE, 0),
            ((545.0, 602.0), OFFCURVE, 0),
            ((567.0, 602.0), CURVE, 100)
        ],
        [
            ((705.0, 483.0), OFFCURVE, 0),
            ((723.0, 500.0), OFFCURVE, 0),
            ((723.0, 523.0), CURVE, 100),
            ((723.0, 544.0), OFFCURVE, 0),
            ((705.0, 562.0), OFFCURVE, 0),
            ((682.0, 562.0), CURVE, 100),
            ((661.0, 562.0), OFFCURVE, 0),
            ((643.0, 544.0), OFFCURVE, 0),
            ((643.0, 523.0), CURVE, 100),
            ((643.0, 500.0), OFFCURVE, 0),
            ((661.0, 483.0), OFFCURVE, 0),
            ((682.0, 483.0), CURVE, 100)
        ],
        [
            ((754.0, 318.0), OFFCURVE, 0),
            ((773.0, 336.0), OFFCURVE, 0),
            ((773.0, 358.0), CURVE, 100),
            ((773.0, 380.0), OFFCURVE, 0),
            ((754.0, 397.0), OFFCURVE, 0),
            ((733.0, 397.0), CURVE, 100),
            ((711.0, 397.0), OFFCURVE, 0),
            ((692.0, 380.0), OFFCURVE, 0),
            ((692.0, 358.0), CURVE, 100),
            ((692.0, 336.0), OFFCURVE, 0),
            ((711.0, 318.0), OFFCURVE, 0),
            ((733.0, 318.0), CURVE, 100)
        ],
        [
            ((708.0, 161.0), OFFCURVE, 0),
            ((726.0, 180.0), OFFCURVE, 0),
            ((726.0, 202.0), CURVE, 100),
            ((726.0, 223.0), OFFCURVE, 0),
            ((708.0, 242.0), OFFCURVE, 0),
            ((686.0, 242.0), CURVE, 100),
            ((664.0, 242.0), OFFCURVE, 0),
            ((647.0, 223.0), OFFCURVE, 0),
            ((647.0, 202.0), CURVE, 100),
            ((647.0, 180.0), OFFCURVE, 0),
            ((664.0, 161.0), OFFCURVE, 0),
            ((686.0, 161.0), CURVE, 100)
        ],
        [
            ((589.0, 43.0), OFFCURVE, 0),
            ((608.0, 61.0), OFFCURVE, 0),
            ((608.0, 82.0), CURVE, 100),
            ((608.0, 103.0), OFFCURVE, 0),
            ((589.0, 122.0), OFFCURVE, 0),
            ((568.0, 122.0), CURVE, 100),
            ((547.0, 122.0), OFFCURVE, 0),
            ((528.0, 103.0), OFFCURVE, 0),
            ((528.0, 82.0), CURVE, 100),
            ((528.0, 61.0), OFFCURVE, 0),
            ((547.0, 43.0), OFFCURVE, 0),
            ((568.0, 43.0), CURVE, 100)
        ],
        [
            ((427.0, -4.0), OFFCURVE, 0),
            ((445.0, 14.0), OFFCURVE, 0),
            ((445.0, 36.0), CURVE, 100),
            ((445.0, 57.0), OFFCURVE, 0),
            ((427.0, 75.0), OFFCURVE, 0),
            ((406.0, 75.0), CURVE, 100),
            ((384.0, 75.0), OFFCURVE, 0),
            ((366.0, 57.0), OFFCURVE, 0),
            ((366.0, 36.0), CURVE, 100),
            ((366.0, 14.0), OFFCURVE, 0),
            ((384.0, -4.0), OFFCURVE, 0),
            ((406.0, -4.0), CURVE, 100)
        ],

        [
            ((266.0, 40.0), OFFCURVE, 0),
            ((284.0, 58.0), OFFCURVE, 0),
            ((284.0, 81.0), CURVE, 100),
            ((284.0, 102.0), OFFCURVE, 0),
            ((266.0, 120.0), OFFCURVE, 0),
            ((245.0, 120.0), CURVE, 100),
            ((222.0, 120.0), OFFCURVE, 0),
            ((205.0, 102.0), OFFCURVE, 0),
            ((205.0, 81.0), CURVE, 100),
            ((205.0, 58.0), OFFCURVE, 0),
            ((222.0, 40.0), OFFCURVE, 0),
            ((245.0, 40.0), CURVE, 100)
        ],
        [
            ((145.0, 160.0), OFFCURVE, 0),
            ((163.0, 178.0), OFFCURVE, 0),
            ((163.0, 201.0), CURVE, 100),
            ((163.0, 222.0), OFFCURVE, 0),
            ((145.0, 240.0), OFFCURVE, 0),
            ((123.0, 240.0), CURVE, 100),
            ((102.0, 240.0), OFFCURVE, 0),
            ((84.0, 222.0), OFFCURVE, 0),
            ((84.0, 201.0), CURVE, 100),
            ((84.0, 178.0), OFFCURVE, 0),
            ((102.0, 160.0), OFFCURVE, 0),
            ((123.0, 160.0), CURVE, 100)
        ],
        [
            ((105.0, 318.0), OFFCURVE, 0),
            ((123.0, 336.0), OFFCURVE, 0),
            ((123.0, 358.0), CURVE, 100),
            ((123.0, 380.0), OFFCURVE, 0),
            ((105.0, 397.0), OFFCURVE, 0),
            ((84.0, 397.0), CURVE, 100),
            ((61.0, 397.0), OFFCURVE, 0),
            ((43.0, 380.0), OFFCURVE, 0),
            ((43.0, 358.0), CURVE, 100),
            ((43.0, 336.0), OFFCURVE, 0),
            ((61.0, 318.0), OFFCURVE, 0),
            ((84.0, 318.0), CURVE, 100)
        ],
        [
            ((149.0, 486.0), OFFCURVE, 0),
            ((166.0, 504.0), OFFCURVE, 0),
            ((166.0, 526.0), CURVE, 100),
            ((166.0, 547.0), OFFCURVE, 0),
            ((149.0, 565.0), OFFCURVE, 0),
            ((126.0, 565.0), CURVE, 100),
            ((105.0, 565.0), OFFCURVE, 0),
            ((87.0, 547.0), OFFCURVE, 0),
            ((87.0, 526.0), CURVE, 100),
            ((87.0, 504.0), OFFCURVE, 0),
            ((105.0, 486.0), OFFCURVE, 0),
            ((126.0, 486.0), CURVE, 100)
        ],
        [
            ((266.0, 602.0), OFFCURVE, 0),
            ((284.0, 620.0), OFFCURVE, 0),
            ((284.0, 641.0), CURVE, 100),
            ((284.0, 664.0), OFFCURVE, 0),
            ((266.0, 682.0), OFFCURVE, 0),
            ((245.0, 682.0), CURVE, 100),
            ((222.0, 682.0), OFFCURVE, 0),
            ((205.0, 664.0), OFFCURVE, 0),
            ((205.0, 641.0), CURVE, 100),
            ((205.0, 620.0), OFFCURVE, 0),
            ((222.0, 602.0), OFFCURVE, 0),
            ((245.0, 602.0), CURVE, 100)
        ],
        [
            ((427.0, 641.0), OFFCURVE, 0),
            ((445.0, 660.0), OFFCURVE, 0),
            ((445.0, 682.0), CURVE, 100),
            ((445.0, 703.0), OFFCURVE, 0),
            ((427.0, 722.0), OFFCURVE, 0),
            ((406.0, 722.0), CURVE, 100),
            ((384.0, 722.0), OFFCURVE, 0),
            ((366.0, 703.0), OFFCURVE, 0),
            ((366.0, 682.0), CURVE, 100),
            ((366.0, 660.0), OFFCURVE, 0),
            ((384.0, 641.0), OFFCURVE, 0),
            ((406.0, 641.0), CURVE, 100)
        ]
    ]
    new_glyph = GSGlyph('dottedCircle')

    for m in font.masters:
        try:
            scale = float(font.glyphs['eight'].layers[m.id].bounds.size.height + font.glyphs['eight'].layers[m.id].bounds.origin.y) / 723
        except AttributeError:
            scale = font.upm / 1000

        if not scale:
            scale = font.upm / 1000

        l = GSLayer()
        l.width = int(772 * scale)
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
        new_glyph.layers[m.id] = l

    new_glyph.updateGlyphInfo()
    return new_glyph


def make_it():
    extant_glyph = Glyphs.font.glyphs['25CC']

    if extant_glyph:
        del(Glyphs.font.glyphs[extant_glyph.name])

    created_glyph = make_glyph(Glyphs.font)

    Glyphs.font.glyphs.append(created_glyph)

    print('Made dottedCircle')


Glyphs.font.disableUpdateInterface()
make_it()
Glyphs.font.enableUpdateInterface()
