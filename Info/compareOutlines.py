# MenuTitle: Compare Outlines
# -*- coding: utf-8 -*-
__doc__ = """
Compares the outlines in all glyphs in the front font with the other opened font.
Any glyphs with differences are coloured accordingly.
"""
# Glyphs.clearLog()

if len(Glyphs.fonts) == 2:
    f1, f2 = Glyphs.fonts

    for g1 in f1.glyphs:
        try:
            g2 = f2.glyphs[g1.name]
            if g2 is None:
                g1.color = 7
            try:
                l1_id = f1.selectedFontMaster.id
                l2_id = f2.selectedFontMaster.id

                g1_nodes = [(n.x, n.y, n.type) for p in g1.layers[l1_id].paths for n in p.nodes]
                g2_nodes = [(n.x, n.y, n.type) for p in g2.layers[l2_id].paths for n in p.nodes]

                if len(g1.layers[l1_id].components) != len(g2.layers[l2_id].components):
                    # Dark Gray - different number of components
                    g1.setColorIndex_(11)
                    g2.setColorIndex_(11)

                elif g1_nodes != g2_nodes:
                    if set(g1_nodes) - set(g2_nodes) or set(g2_nodes) - set(g1_nodes):
                        # Red - Different position or number of nodes
                        print(g1.name)
                        print(set(g1_nodes) - set(g2_nodes))
                        print()
                        g1.setColorIndex_(0)
                        g2.setColorIndex_(0)
                    else:
                        # Purple - identically positioned nodes, different start point
                        g1.setColorIndex_(8)
                        g2.setColorIndex_(8)

                elif g1.layers[l1_id].width != g2.layers[l2_id].width:
                    # Yellow - different metrics
                    g1.setColorIndex_(3)
                    g2.setColorIndex_(3)
                else:
                    if g1.color != 9223372036854775807:
                        g1.setColorIndex_(9223372036854775807)
                    if g2.color != 9223372036854775807:
                        g2.setColorIndex_(9223372036854775807)
            except Exception as err2:
                print(err2)
        except Exception as err1:
            print(err1)

    print('Red - Different position or number of nodes')
    print('Purple - identically positioned nodes, different start point')
    print('Yellow - different metrics')
    print('Dark Gray - different number of components')
    Glyphs.showMacroWindow()

else:
    print('Two, and only two, fonts can be open.')
