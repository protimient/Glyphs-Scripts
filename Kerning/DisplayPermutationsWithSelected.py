# MenuTitle: Display Permutations With Selected
# -*- coding: utf-8 -*-
__doc__ = """
Displays all glyph permutations around/with the selected glyphs.
"""
from itertools import product


# Glyphs.clearLog()
# Glyphs.showMacroWindow()


groups_dict = dict()
groups_dict['left'] = {}
groups_dict['right'] = {}
target_glyphs = []
leftside_glyphs = []
rightside_glyphs = []

glyphnames = ['/' + x.parent.name for x in Glyphs.font.selectedLayers if x.parent.export]
gn_combos = product(glyphnames, repeat=2)
character_pairs = [''.join(x) for x in gn_combos]
string = '  '.join(character_pairs)

if string:
    Glyphs.font.newTab(string)
