# MenuTitle: Re-number iMatras and iiMatras
# -*- coding: utf-8 -*-
__doc__ = """
Sorts the i(i)Matras by length and assigns the corresponding number.
"""

import re
from collections import defaultdict

Glyphs.clearLog()
# Glyphs.showMacroWindow()

affected_glyphs = [g for g in Glyphs.font.glyphs if re.match(r'^iMatra-beng\.\d', g.name)]

affected_glyphs_groups = defaultdict(list)
for g in Glyphs.font.glyphs:
    try:
        affected_glyphs_groups[re.search(r'^(iMatra-beng\.)\d+(.*)', g.name).groups()].append(g)
    except AttributeError:
        pass


def sorterer(its):
    return (
        len(its[1]),
        -len(its[0]),
    )


def sortGlyph(g):
    l = g.layers[0]
    return l.bounds.size.width


test_group = max(affected_glyphs_groups.items(), key=sorterer)

number_mapping = {}
for i, g in enumerate(sorted(test_group[1], key=sortGlyph), 1):
    original_number = re.search(r'iMatra-beng\.(\d+).*', g.name).group(1)
    number_mapping[original_number] = i
    max_number = i

for g in affected_glyphs:
    g.name = 'X' + g.name

for g in affected_glyphs:
    original_number = re.search(r'^XiMatra-beng\.(\d+).*', g.name).group(1)
    new_number = number_mapping.get(original_number)
    if new_number is None:
        max_number += 1
        new_number = max_number
    new_gn = re.sub(r'^XiMatra-beng\.(\d)(.*)', r'iMatra-beng.{}\2'.format(new_number), g.name)
    g.name = new_gn
