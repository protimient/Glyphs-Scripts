# MenuTitle: Disable alignment for selected Component in All layers
# -*- coding: utf-8 -*-
__doc__ = """
Disables automatic alignment for the selected component in all layers in the current glyph.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()


Glyphs.font.disableUpdateInterface()  # suppresses UI updates in Font View

c_is = [ci for ci, c in enumerate(Glyphs.font.selectedLayers[0].components) if c.selected]
print(c_is)

for l in Glyphs.font.selectedLayers[0].parent.layers:
    for ci in c_is:
        l.components[ci].automaticAlignment = False

Glyphs.font.enableUpdateInterface()  # re-enables UI updates in Font View
