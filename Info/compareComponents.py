# MenuTitle: Compare Components
# -*- coding: utf-8 -*-
__doc__ = """
Compares the components in all glyphs in the front font with the other opened fonts.
Any glyphs with differences are coloured accordingly.
"""

Glyphs.clearLog()

if len(Glyphs.fonts) == 2:
    f1, f2 = Glyphs.fonts
    l1_id = f1.selectedFontMaster.id
    l2_id = f2.selectedFontMaster.id

    for g1 in f1.glyphs:
        try:
            g2 = f2.glyphs[g1.name]
            if not g2:
                g1.color = 11
                continue

            l1 = g1.layers[l1_id]
            l2 = g2.layers[l2_id]

            try:

                if not l1.components and not l2.components:
                    continue

                if (l1.components and not l2.components) or (not l1.components and l2.components):
                    # Red - Not components
                    g1.setColorIndex_(0)
                    g2.setColorIndex_(0)
                    continue

                g1_component_names = [c.componentName for c in l1.components]
                g2_component_names = [c.componentName for c in l2.components]
                if g1_component_names != g2_component_names:
                    # Orange - Different components
                    g1.setColorIndex_(1)
                    g2.setColorIndex_(1)
                    continue

                g1_component_positions = [(c.position.x, c.position.y) for c in l1.components]
                g2_component_positions = [(c.position.x, c.position.y) for c in l2.components]

                if g1_component_positions != g2_component_positions:
                    # Yellow - Different component positions
                    g1.setColorIndex_(3)
                    g2.setColorIndex_(3)
                    continue

                if g1.color != 9223372036854775807:
                    g1.setColorIndex_(9223372036854775807)
                if g2.color != 9223372036854775807:
                    g2.setColorIndex_(9223372036854775807)
            except Exception as err2:
                raise
                print(err2)
        except Exception as err1:
            raise
            print(err1)

    print('Red - Not both components')
    print('Orange - different component names')
    print('Yellow - different position')
    print('Grey - Glyph is missing from the other font')
    Glyphs.showMacroWindow()

else:
    Glyphs.showNotification('Compare Components', 'Two, and only two, fonts can be open.')
