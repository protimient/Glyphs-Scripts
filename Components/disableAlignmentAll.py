# MenuTitle: Disable alignment for selected glyphs in All layers
# -*- coding: utf-8 -*-
__doc__ = """
Disables automatic alignment for all components in all selected glyphs.
"""


Glyphs.font.disableUpdateInterface()  # suppresses UI updates in Font View

for sl in Glyphs.font.selectedLayers:
    for l in sl.parent.layers:
        for c in l.components:
            c.automaticAlignment = False

Glyphs.font.enableUpdateInterface()  # re-enables UI updates in Font View
