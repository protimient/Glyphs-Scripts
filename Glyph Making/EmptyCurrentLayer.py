# MenuTitle: Empty Current layer for Selected
# -*- coding: utf-8 -*-
__doc__ = """
Deletes all anchors, outlines and components for the selected layers.
"""


def doit():
    for l in Glyphs.font.selectedLayers:
        l.paths = []
        l.anchors = []
        l.components = []


Glyphs.font.disableUpdateInterface()

doit()

Glyphs.font.enableUpdateInterface()
