# MenuTitle: Add Horizontal PS Hint
# -*- coding: utf-8 -*-
__doc__ = """
Adds a horizontal hint to the selected 2 nodes, or a ghost hint to a single selected node.
"""
Glyphs.clearLog()

try:
    l = Glyphs.font.selectedLayers[0]
    selected_nodes = [n for p in l.paths for n in p.nodes if n.selected]
except IndexError:
    selected_nodes = None


def is_top(node):
    p = node.parent
    return node.y > (p.bounds.size.height / 2) + p.bounds.origin.y


if selected_nodes is not None:
    s_node_1 = selected_nodes[0]
    try:
        s_node_2 = selected_nodes[1]
        if s_node_2.y == s_node_1.y:
            s_node_2 = None
    except IndexError:
        s_node_2 = None

    newH = GSHint()
    newH.horizontal = True
    newH.originNode = s_node_1
    if s_node_2 is not None:
        newH.targetNode = s_node_2
        newH.type = STEM
    else:
        newH.type = TOPGHOST if is_top(s_node_1) else BOTTOMGHOST

    l.hints.append(newH)
