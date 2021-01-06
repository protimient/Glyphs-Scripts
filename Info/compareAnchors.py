# MenuTitle: Compare Anchors
# -*- coding: utf-8 -*-
__doc__ = """
Compares the anchors in all the glyphs in the front font with the other opened font.
Any glyphs with differences are coloured accordingly.
"""
# Glyphs.clearLog()

if len(Glyphs.fonts) == 2:
    f1, f2 = Glyphs.fonts

    for g1 in f1.glyphs:
        g1.setColorIndex_(9223372036854775807)
        g2 = f2.glyphs[g1.name]

        if g2 is None:
            print('Could not find {} in the other font.'.format(g1.name))
            continue

        g2.setColorIndex_(9223372036854775807)

        l1 = f1.selectedFontMaster.id
        l2 = f2.selectedFontMaster.id

        a1 = [(a.name, a.x, a.y) for a in g1.layers[l1].anchors]
        a2 = [(a.name, a.x, a.y) for a in g2.layers[l2].anchors]
        if a1 != a2:
            g1.setColorIndex_(0)
            g2.setColorIndex_(0)

else:
    Glyphs.showNotification('Compare Anchors', 'Two, and only two, fonts can be open.')
