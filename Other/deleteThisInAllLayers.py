# MenuTitle: Delete This in All Layers
# -*- coding: utf-8 -*-
__doc__ = """
Deletes whatever is selected in all other layers.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

l = Glyphs.font.selectedLayers[0]
g = l.parent


def delete_component(c, target_l, c_index=None):
    c_names = [c.name for c in target_l.components]
    if c_names.count(c.name) == 1:
        del target_l.components[c_names.index(c.name)]
    elif c_names.count(c.name) > 1 and c_index is not None:
        if target_l.components[c_index].name == c.name:
            del target_l.components[c_index]
        else:
            for ci, c2 in enumerate(target_l.components):
                if c2.name == c.name:
                    del target_l.components[ci]


for o in l.selection:
    if type(o) == GSComponent:
        ci = [x for x in l.components].index(o)
    else:
        ci = None

    for l2 in g.layers:
        if type(o) == GSAnchor:
            del l2.anchors[o.name]

        if type(o) == GSComponent:
            delete_component(o, l2, c_index=ci)

        if type(o) == GSHint:
            for hi, h in enumerate(l2.hints):
                if h.name == o.name and h.originNode.index == o.originNode.index:
                    del l2.hints[hi]

for pi, p in enumerate(l.paths):
    if p.selected:
        for l2 in g.layers:
            del(l2.paths[pi])


deletable_node_indexes = [o.index for o in l.selection if type(o) == GSNode]
for l in g.layers:
    deletable_nodes = [n for p in l.paths for n in p.nodes if n.index in deletable_node_indexes]
    print(deletable_nodes)
    for n in sorted(deletable_nodes, key=lambda x: x.index, reverse=True):
        del(n.parent.nodes[n.index])

    for pi in reversed(range(len(l.paths))):
        p = l.paths[pi]
        if not p.nodes:
            del(l.paths[pi])
