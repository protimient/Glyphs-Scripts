# MenuTitle: Display All Kern Pairs
# -*- coding: utf-8 -*-
__doc__ = """
Opens a tab containing all the kern pairs in the font for the currently selected master.
"""
from collections import defaultdict

Glyphs.clearLog()
# Glyphs.showMacroWindow()

selected_master_id = Glyphs.font.selectedFontMaster.id

lefts = defaultdict(list)
rights = defaultdict(list)

for g in Glyphs.font.glyphs:
    if g.leftKerningGroup:
        lefts[g.leftKerningGroup].append(g.name)
    if g.rightKerningGroup:
        rights[g.rightKerningGroup].append(g.name)


def glyph_for_id(some_name):
    try:
        return Glyphs.font.glyphForId_(some_name).name
    except AttributeError:
        return some_name


def get_key_glyph(g_name):
    if not g_name.startswith('@'):
        return glyph_for_id(g_name)

    kerning_group_dict = rights if g_name[5] == 'L' else lefts

    base_group_name = g_name[7:]
    kerning_group = kerning_group_dict.get(base_group_name)

    try:
        if base_group_name in kerning_group:
            return base_group_name
    except TypeError:
        print(g_name, 'has no members')

    return sorted(kerning_group)[0]


def name_to_layer(gn, m_id=None):
    if m_id is None:
        m_id = selected_master_id

    g = Glyphs.font.glyphs[gn]
    if g is None:
        return

    l = g.layers[m_id]
    return l


display_pairs_names = []
space_l = Glyphs.font.glyphs['space'].layers[selected_master_id]
for left_gs, rights_gs in Glyphs.font.kerning[selected_master_id].items():
    left_display_name = get_key_glyph(left_gs)

    for right_gs, val in rights_gs.items():
        right_display_name = get_key_glyph(right_gs)
        display_pairs_names.append((left_display_name, right_display_name))

display_layers = []
for names in display_pairs_names:
    display_layers.append(name_to_layer(names[0]))
    display_layers.append(name_to_layer(names[1]))
    display_layers.append(space_l)

Glyphs.font.newTab(display_layers)
Glyphs.font.tabs[-1].previewHeight = Glyphs.font.tabs[0].previewHeight
