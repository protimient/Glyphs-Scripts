# MenuTitle: Display Permutations With Red Marked
# -*- coding: utf-8 -*-
__doc__ = """
When one or more glyphs in a selection is marked Red, a new tab will open showing all glyph permutations around/with the red marked glyph(s).
Only shows classes.
"""


try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest


# Glyphs.clearLog()
# Glyphs.showMacroWindow()


groups_dict = dict()
groups_dict['left'] = {}
groups_dict['right'] = {}
target_glyphs = []
leftside_glyphs = []
rightside_glyphs = []
for g in [x.parent for x in Glyphs.font.selectedLayers if x.parent.export]:
    if g.color == 0:
        target_glyphs.append('/' + g.name)
        continue

    if not g.leftKerningGroup:
        rightside_glyphs.append('/' + g.name)
    elif g.leftKerningGroup == g.name:
        groups_dict['left'][g.leftKerningGroup] = '/' + g.name
    elif not groups_dict['left'].get(g.leftKerningGroup):
        groups_dict['left'][g.leftKerningGroup] = '/' + g.name

    if not g.rightKerningGroup:
        leftside_glyphs.append('/' + g.name)
    elif g.rightKerningGroup == g.name:
        groups_dict['right'][g.rightKerningGroup] = '/' + g.name
    elif not groups_dict['right'].get(g.rightKerningGroup):
        groups_dict['right'][g.rightKerningGroup] = '/' + g.name

leftside_glyphs += groups_dict['right'].values()
rightside_glyphs += groups_dict['left'].values()

leftside_glyphs.sort()
rightside_glyphs.sort()

filler = leftside_glyphs[-1] if len(leftside_glyphs) < len(rightside_glyphs) else rightside_glyphs[-1]
strings = []
for gn in target_glyphs:
    permutation_strings = [gn.join(x) for x in zip_longest(leftside_glyphs, rightside_glyphs, fillvalue=filler)]
    line = '  '.join(permutation_strings)
    strings.append(line)

if strings:
    string = '\n\n'.join(strings)
    Glyphs.font.newTab(string)
