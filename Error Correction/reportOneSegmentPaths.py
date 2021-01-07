# MenuTitle: Report One-Segment paths
# -*- coding: utf-8 -*-
__doc__ = """
Opens a tab with glyphs containing degenerate paths (paths with only two (x, y) locations).
"""

Glyphs.clearLog()

effected_glyphs = []


def report():
    for g in [x for x in Glyphs.font.glyphs if x.export]:
        for l in g.layers:
            test_l = l.copyDecomposedLayer()
            for p in test_l.paths:
                if len(p.segments) == 1:
                    print(p.nodes)
                    effected_glyphs.append(l)

    print(effected_glyphs)
    if effected_glyphs:
        Glyphs.font.newTab()
        Glyphs.font.tabs[-1].layers = effected_glyphs


report()
print('Done')


# Glyphs.showMacroWindow()
