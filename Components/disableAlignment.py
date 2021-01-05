# MenuTitle: Disable alignment for selected layer
# -*- coding: utf-8 -*-

__doc__ = """
Disables automatic alignment for all components in the current layer.
"""

Glyphs.font.disableUpdateInterface()  # suppresses UI updates in Font View

for l in Glyphs.font.selectedLayers:
    for c in l.components:
        c.automaticAlignment = False

Glyphs.font.enableUpdateInterface()  # re-enables UI updates in Font View
