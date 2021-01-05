# MenuTitle: Report Non Extreme Nodes
# -*- coding: utf-8 -*-
__doc__ = """
Reports Glyphs that do not have nodes at extremes (y-direction only).
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

from collections import defaultdict
eff_layers = defaultdict(list)


def reporter(l, node, point, li):
    eff_layers[l.name].append(l)

    print('Non-Extreme node found in glyph {0}, layer {1}, nodes {2}, {3}'.format(g.name, li, node, point))


Glyphs.font.disableUpdateInterface()

for g in [x for x in Glyphs.font.glyphs]:
    for li, l in enumerate(g.layers):
        if l.paths:
            all_nodes = [n for p in l.paths for n in p.nodes if n.type != GSOFFCURVE]
            all_points = [n for p in l.paths for n in p.nodes if n.type == GSOFFCURVE]

            if all_nodes and all_points:
                xMax_node = max(all_nodes, key=lambda x: x.x)
                xMin_node = min(all_nodes, key=lambda x: x.x)
                yMax_node = max(all_nodes, key=lambda x: x.y)
                yMin_node = min(all_nodes, key=lambda x: x.y)

                xMax_point = max(all_points, key=lambda x: x.x)
                xMin_point = min(all_points, key=lambda x: x.x)
                yMax_point = max(all_points, key=lambda x: x.y)
                yMin_point = min(all_points, key=lambda x: x.y)

                # if xMax_node.x < xMax_point.x:
                # 	reporter(g, xMax_node, xMax_point, li)

                # if xMin_node.x > xMin_point.x:
                # 	reporter(g, xMin_node, xMin_point, li)

                if yMax_node.y < yMax_point.y:
                    reporter(l, yMax_node, yMax_point, li)

                if yMin_node.y > yMin_point.y:
                    reporter(l, yMin_node, yMin_point, li)


layers = []
for x in eff_layers.values():
    layers += [GSControlLayer(10)]
    layers += x

if layers:
    if not Glyphs.font.tabs:
        Glyphs.font.newTab()

    Glyphs.font.tabs[0].layers = layers
else:
    Glyphs.showNotification('Non-Extreme Nodes', 'All good. All glyphs have nodes at the extremes.')

Glyphs.font.enableUpdateInterface()
