# MenuTitle: Make Selected into .case varients
# -*- coding: utf-8 -*-
__doc__ = """
Makes a .case variant of the selected glyphs if not already present using components and vertically positions them.
"""

import copy

Glyphs.clearLog()
# Glyphs.showMacroWindow()


def build_glyph_name(basename, i):
    return basename + '.' + str(i).rjust(3, '0')


def duplicateAsComponents(g, glyph_name=None, replace_extant=False, copy_anchors=False):
    all_glyph_names = [x.name for x in Glyphs.font.glyphs]
    if glyph_name is None:
        glyph_name = g.name

    if Glyphs.font.glyphs[glyph_name] is None:
        new_g = GSGlyph(glyph_name)
        Glyphs.font.glyphs.append(new_g)
    else:
        if replace_extant:
            # del(Glyphs.font.glyphs[glyph_name])
            for l in Glyphs.font.glyphs[glyph_name].layers:
                l.paths = []
                l.anchors = []
                l.components = []
            new_g = Glyphs.font.glyphs[glyph_name]
        else:
            new_g_suffix = 1
            while build_glyph_name(g.name, new_g_suffix) in all_glyph_names:
                new_g_suffix += 1

            glyph_name = build_glyph_name(g.name, new_g_suffix)
            new_g = GSGlyph(glyph_name)
            Glyphs.font.glyphs.append(new_g)

    if g.leftKerningGroup:
        new_g.leftKerningGroup = g.leftKerningGroup
    if g.rightKerningGroup:
        new_g.rightKerningGroup = g.rightKerningGroup

    for m in Glyphs.font.masters:
        new_layer = GSLayer()
        new_layer.associatedMasterId = m.id
        new_g.layers[m.id] = new_layer

        new_component = GSComponent(g.name)
        new_component.automaticAlignment = True
        new_layer.components.append(new_component)
        new_layer.width = Glyphs.font.glyphs[g.name].layers[m.id].width

        if copy_anchors:
            new_layer.anchors = copy.copy(g.layers[m.id].anchors)

    return new_g


def centre_vertically_on_capheight(l):
    l_centre = l.bounds.origin.y + (l.bounds.size.height / 2)
    offset = (Glyphs.font.masters[l.associatedMasterId].capHeight / 2) - l_centre
    l.applyTransform((1, 0, 0, 1, 0, offset))
    print(offset)


def move_above_capheight(l):
    l_centre = l.bounds.origin.y + (l.bounds.size.height / 2)
    offset = Glyphs.font.masters[l.associatedMasterId].capHeight - l_centre
    l.applyTransform((1, 0, 0, 1, 0, offset))
    print(offset)


Glyphs.font.disableUpdateInterface()
for sl in Glyphs.font.selectedLayers:
    g = sl.parent
    new_g = duplicateAsComponents(g, glyph_name=g.name + '.case', replace_extant=True, copy_anchors=g.category == 'Mark')
    if g.category != 'Mark':
        for l in new_g.layers:
            centre_vertically_on_capheight(l)
Glyphs.font.enableUpdateInterface()
