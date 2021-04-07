# MenuTitle: Decompose selected components or all in All layers
# -*- coding: utf-8 -*-
from AppKit import NSEvent
__doc__ = """
Decomposes the selected component in all layers or all components if none are selected.
"""
Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()  # suppresses UI updates in Font View

# --- From mekkablue ---
keysPressed = NSEvent.modifierFlags()
capslockKey = 65536
capslockKeyPressed = keysPressed & capslockKey == capslockKey
# ---


def decompose_component(c, source_l, target_l):
    c_names = [x.name for x in target_l.components]
    if c_names.count(c.name) == 1:
        target_l.components[c_names.index(c.name)].decompose()

    elif c_names.count(c.name) > 1:
        print(source_l.components)
        ci = [x for x in source_l.components].index(c)
        if target_l.components[ci].name == c.name:
            target_l.components[ci].decompose()
        else:
            for ci, c2 in enumerate(target_l.components):
                if c.name == c2.name:
                    target_l.components[ci].decompose()


for selected_l in Glyphs.font.selectedLayers:
    g = selected_l.parent
    selected_components = [c for c in selected_l.components if c.selected]
    g.beginUndo()

    for l in g.layers:
        extant_anchors = list(l.anchors)
        if selected_components:
            for c in selected_components:
                decompose_component(c, selected_l, l)
        else:
            for c in list(l.components):
                c.decompose()

        if capslockKeyPressed:
            l.anchors = extant_anchors

    g.endUndo()

Glyphs.font.enableUpdateInterface()  # re-enables UI updates in Font View
