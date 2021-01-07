# MenuTitle: Fix Component Order
# -*- coding: utf-8 -*-
__doc__ = """
Searches all glyphs for any component of type 'Mark' at index 0 in the components list, and moves it to the end if found.
"""

Glyphs.clearLog()

Glyphs.font.disableUpdateInterface()


def reportCorrectedComponents(gylyphName, layerName, componentName):
    print('Reordered {2} on layer {1} in glyph {0}'.format(gylyphName, layerName, componentName))


if Glyphs.font.selectedLayers is None:
    these_glyphs = Glyphs.font.glyphs
else:
    these_glyphs = [x.parent for x in Glyphs.font.selectedLayers]

for g in these_glyphs:
    for l in g.layers:
        if any(x.component.category != 'Mark' for x in l.components):
            while l.components[0].component.category == 'Mark':
                c = l.components[0]
                del l.components[0]
                l.components.append(c)

                reportCorrectedComponents(g.name, l.name, c.componentName)

Glyphs.font.enableUpdateInterface()

# Glyphs.showMacroWindow()
