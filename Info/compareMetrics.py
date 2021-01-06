# MenuTitle: Compare Metrics
# -*- coding: utf-8 -*-
__doc__ = """
Compares the metrics values in all glyphs in the front font with the other opened font.
Any glyphs with differences are coloured accordingly.
"""
Glyphs.clearLog()

COLOR_1 = 3
COLOR_1_Name = 'Yellow'
COLOR_2 = 7
COLOR_2_Name = 'Blue'
COLOR_3 = 0
COLOR_3_Name = 'Red'

tolerence = 0

if len(Glyphs.fonts) == 2:
    f1, f2 = Glyphs.fonts

    for g1 in [g for g in f1.glyphs if g.export]:
        m1 = f1.selectedFontMaster.id
        m2 = f2.selectedFontMaster.id

        g2 = f2.glyphs[g1.name]
        l1 = g1.layers[m1]

        try:
            l2 = g2.layers[m2]
        except KeyError:
            print('"{0}" is not in {1}'.format(g1.name, f2))
            continue

        if not l1.width + tolerence >= l2.width >= l1.width - tolerence:
            # 'Different Width'
            g1.setColorIndex_(COLOR_3)
            g2.setColorIndex_(COLOR_3)

        elif not l1.LSB + tolerence >= l2.LSB >= l1.LSB - tolerence:
            # 'Different Left sidebearing'
            g1.setColorIndex_(COLOR_1)
            g2.setColorIndex_(COLOR_1)

        elif not l1.RSB + tolerence >= l2.RSB >= l1.RSB - tolerence:
            # 'Different Right sidebearing'
            g1.setColorIndex_(COLOR_2)
            g2.setColorIndex_(COLOR_2)

        else:
            if g1.color < 12:
                g1.setColorIndex_(9223372036854775807)
            if g2.color < 12:
                g2.setColorIndex_(9223372036854775807)

    print('{} - Different Width'.format(COLOR_3_Name))
    print('{} - Different Left sidebearing'.format(COLOR_1_Name))
    print('{} - Different Right sidebearing'.format(COLOR_2_Name))
    Glyphs.showMacroWindow()

else:
    print('Two, and only two, fonts can be open.')
