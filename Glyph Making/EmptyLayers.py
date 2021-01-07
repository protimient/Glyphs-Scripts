# MenuTitle: Empty All layers for Selected
# Author: Ben Jones
__doc__ = """
Deletes all anchors, outlines and components for the selected glyph
"""
Font = Glyphs.currentDocument.font


def doit():
    for g in [x.parent for x in Glyphs.font.selectedLayers]:
        for l in g.layers:
            l.paths = []
            l.anchors = []
            l.components = []


Glyphs.font.disableUpdateInterface()

doit()

Glyphs.font.enableUpdateInterface()
