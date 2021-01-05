# MenuTitle: Decompose selected components or all in All layers
# -*- coding: utf-8 -*-
__doc__ = """
Decomposes the selected component in all layers or all components if none are selected.
"""
# Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()  # suppresses UI updates in Font View

for selected_l in Glyphs.font.selectedLayers:
    g = selected_l.parent
    selected_component_names = [c.name for c in selected_l.components if c.selected]

    for l in g.layers:
        selected_components = []
        for c in l.components:
            if not selected_component_names:
                selected_components.append(c)
            elif c.name in selected_component_names:
                selected_components.append(c)

        for c in selected_components:
            c.decompose()


Glyphs.font.enableUpdateInterface()  # re-enables UI updates in Font View
