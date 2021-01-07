# MenuTitle: Make .notdef
# -*- coding: utf-8 -*-
__doc__ = """
Makes a basic rectangular .notdef.
"""

import math

# Glyphs.clearLog()


def notdefGlyph(font):
    for n in ['endash', 'emdash', 'minus', 'hyphen', 'uni002D', 'I', 'period']:
        minus = font.glyphs[n]
        if minus:
            break

    thickness = 90

    new_glyph = GSGlyph('.notdef')
    for m in font.masters:
        if minus:
            minus_thickness = minus.layers[m.id].bounds.size.height
        else:
            minus_thickness = thickness

        if not minus_thickness:
            minus_thickness = thickness

        vertical_thickness = math.ceil(minus_thickness * 1.02)
        horizontal_thickness = minus_thickness
        total_height = m.ascender
        total_width = None
        for x in ['e', 'N']:
            try:
                total_width = font.glyphs[x].layers[m.id].bounds.size.width
                break
            except AttributeError:
                pass

        if not total_width:
            total_width = 400

        lsb = 0
        rsb = 0

        contours = []

        glyph_nodes = [((0, 0), GSLINE, 0)]
        glyph_nodes.append(((total_width, 0), GSLINE, 0))
        glyph_nodes.append(((total_width, total_height), GSLINE, 0))
        glyph_nodes.append(((0, total_height), GSLINE, 0))
        contours.append(glyph_nodes)

        glyph_nodes = [((vertical_thickness, horizontal_thickness), GSLINE, 0)]
        glyph_nodes.append(((total_width - vertical_thickness, horizontal_thickness), GSLINE, 0))
        glyph_nodes.append(((total_width - vertical_thickness, total_height - horizontal_thickness), GSLINE, 0))
        glyph_nodes.append(((vertical_thickness, total_height - horizontal_thickness), GSLINE, 0))
        contours.append(reversed(glyph_nodes))

        l = GSLayer()
        l.width = total_width
        l.associatedMasterId = m.id

        for contour in contours:
            p = GSPath()
            p.closed = True

            for node in contour:
                coords, type, connection = node
                x = int(coords[0])
                y = int(coords[1])
                n = GSNode(NSPoint(x, y))
                n.type = type
                # n.connection = connection

                p.nodes.append(n)

            l.paths.append(p)

        l.setLSB_(lsb)
        l.setRSB_(rsb)

        new_glyph.layers[m.id] = l

    return new_glyph


def makeGlyph(font):
    if font.glyphs['.notdef']:
        del font.glyphs['.notdef']

    notdef = notdefGlyph(font)

    font.glyphs.append(notdef)
    notdef.updateGlyphInfo()

    print('Made .notdef')
    return font


font = Glyphs.font
makeGlyph(font)
