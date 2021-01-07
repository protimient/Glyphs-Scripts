# MenuTitle: Print Nodes As Python
# -*- coding: utf-8 -*-
__doc__ = """
Converts the outline in the current layer to a python list.
"""

Glyphs.clearLog()


def make_python(l):
    path_strings = []
    for p in l.paths:
        node_strings = ['(({nx}, {ny}), {ntype}, {nconnection})'.format(
            nx=n.x,
            ny=n.y,
            ntype=n.type.upper(),
            nconnection=n.connection,
        ) for n in p.nodes]

        nodes_string = '[{}]'.format(', '.join(node_strings))
        path_strings.append(nodes_string)
    print('[{}]'.format(', '.join(path_strings)))


l = Glyphs.font.selectedLayers[0]
make_python(l)

Glyphs.showMacroWindow()
