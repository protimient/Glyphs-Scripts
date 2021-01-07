# MenuTitle: Set First 4 glyphs
# -*- coding: utf-8 -*-
__doc__ = """
Sets the order and, if needed, builds the first 4 glyphs .notdef, NULL, CR, space
"""

import math


Glyphs.clearLog()
Glyphs.showMacroWindow()


def notdefGlyph(this_font):
    for n in ['endash', 'emdash', 'minus', 'hyphen', 'uni002D', 'I', 'period']:
        minus = this_font.glyphs[n]
        if minus:
            break

    thickness = 90

    new_glyph = GSGlyph('.notdef')
    for m in this_font.masters:
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
        for x in ['endash', 'e', 'N']:
            try:
                total_width = this_font.glyphs[x].layers[m.id].bounds.size.width
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

                p.nodes.append(n)

            l.paths.append(p)

        l.LSB = lsb
        l.RSB = rsb

        new_glyph.layers[m.id] = l
        new_glyph.updateGlyphInfo()

    return new_glyph


def makeEmptyGlyph(this_font, gname, gunicode, **kwargs):
    gwidthkey = kwargs.get('width_key')
    gwidth = kwargs.get('width', 0)

    g = this_font.glyphs[gunicode]
    if g is not None:
        del this_font.glyphs[g.name]

    newG = GSGlyph(gname)
    newG.unicode = gunicode
    newG.updateGlyphInfo()
    this_font.glyphs.append(newG)
    if gwidthkey is not None and this_font.glyphs[gwidthkey] is not None:
        newG.widthMetricsKey = gwidthkey
        for l in newG.layers:
            l.syncMetrics()
    else:
        for l in newG.layers:
            l.width = gwidth


this_font = Glyphs.font

# Check for the .notdef
g_notdef = this_font.glyphs['.notdef']
if g_notdef is None:
    g_notdef = notdefGlyph(this_font)
    this_font.glyphs.append(g_notdef)

elif not any([l.paths for l in g_notdef.layers] + [l.components for l in g_notdef.layers]):
    del this_font.glyphs['.notdef']
    g_notdef = notdefGlyph(this_font)
    this_font.glyphs.append(g_notdef)

elif not all([l.paths for l in g_notdef.layers] + [l.components for l in g_notdef.layers]):
    new_notdef = notdefGlyph(this_font)
    for l in g_notdef.layers:
        if not l.paths and not l.components:
            l.paths = new_notdef.layers[l.layerId].paths


# Remove any mis-named null glyphs
for gname in ['null', '.null']:
    if this_font.glyphs[gname]:
        del this_font.glyphs[gname]

# Make the NULL
if not this_font.glyphs['NULL'] and not this_font.glyphs['0000']:
    makeEmptyGlyph(this_font, 'NULL', '0000', width=0)

# Make the CR
if not this_font.glyphs['CR'] and not this_font.glyphs['000D']:
    makeEmptyGlyph(this_font, 'CR', '000D', width_key='space')


# Set the first 4 order
first_four_order = '.notdef NULL CR space'.split(' ')

if this_font.customParameters['glyphOrder'] is not None:
    new_order = [gn for gn in this_font.customParameters['glyphOrder'] if gn not in first_four_order]
    first_four_order += new_order

this_font.customParameters['glyphOrder'] = first_four_order
