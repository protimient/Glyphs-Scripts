# MenuTitle: Duplicate Selected Glyphs as Composite Glyphs
# -*- coding: utf-8 -*-
__doc__ = """
Duplicates the selected glyph(s) as composite glyphs of themselves.
"""

Glyphs.clearLog()


def glyph_name(basename, i):
    return basename + '.' + str(i).rjust(3, '0')


def duplicateAsComponents(g):
    all_glyph_names = [x.name for x in Glyphs.font.glyphs]
    new_g_suffix = 1
    while glyph_name(g.name, new_g_suffix) in all_glyph_names:
        new_g_suffix += 1

    new_g = GSGlyph(glyph_name(g.name, new_g_suffix))
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


Glyphs.font.disableUpdateInterface()

for sl in Glyphs.font.selectedLayers:
    g = sl.parent
    duplicateAsComponents(g)

Glyphs.font.enableUpdateInterface()
