# MenuTitle: Report Node Numbers
# -*- coding: utf-8 -*-
__doc__ = """
Reports the number of nodes in each layer for each selected glyph.
"""

Glyphs.clearLog()


for g in [x.parent for x in Glyphs.font.selectedLayers]:
    all_nodes = []
    for l in g.layers:
        nodes = [n for p in l.paths for n in p.nodes]
        len_nodes = len(nodes)
        all_nodes.append(len_nodes)
        print('{nodes_len}: {layer}'.format(
            layer=l,
            nodes_len=len_nodes
        ))
    if len(set(all_nodes)) == 1:
        print('*** All identical ***')

Glyphs.showMacroWindow()
