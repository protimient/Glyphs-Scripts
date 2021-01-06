# MenuTitle: Compare With Background
# -*- coding: utf-8 -*-
__doc__ = """
Compares the outline with the background/mask in the selected glyphs and opens a tab with any discrepancies.
"""

from collections import defaultdict

Glyphs.clearLog()
Glyphs.showMacroWindow()


def make_node_to_tuple(n):
    return (n.x, n.y, n.type)


strings = defaultdict(list)
for g in [x.parent for x in Glyphs.font.selectedLayers]:
    for l in g.layers:
        if not l.paths:
            continue

        fg_nodes = set([make_node_to_tuple(n) for p in l.paths for n in p.nodes])

        if l.background.paths:
            bg_nodes = set([make_node_to_tuple(n) for p in l.background.paths for n in p.nodes])
        else:
            bg_nodes = set()

        if bg_nodes ^ fg_nodes:
            strings[l.name].append(l)

layers = []
for x in strings.values():
    layers += [GSControlLayer(10)]
    layers += x

if layers:
    Glyphs.font.newTab()
    Glyphs.font.tabs[-1].layers = layers
