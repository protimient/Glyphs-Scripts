# MenuTitle: Copy selected layer to all others
# -*- coding: utf-8 -*-
__doc__ = """
Copies the outlines, components and anchors of the current layer to all other layers.
"""
import copy


def doit():
    for selected_l in Glyphs.font.selectedLayers:
        g = selected_l.parent
        for l in g.layers:
            if l != selected_l:
                l.paths = copy.copy(selected_l.paths)
                l.anchors = copy.copy(selected_l.anchors)
                l.components = copy.copy(selected_l.components)
                l.width = copy.copy(selected_l.width)
                l.hints = copy.copy(selected_l.hints)


Glyphs.font.disableUpdateInterface()

doit()

Glyphs.font.enableUpdateInterface()
