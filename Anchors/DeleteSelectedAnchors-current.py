# MenuTitle: Delete Current Layer's Anchors
# -*- coding: utf-8 -*-
__doc__ = """
Deletes all anchors in the current layer. Can be run on a single glyph in edit view or a selection of glyphs in font view.
"""

for l in Glyphs.font.selectedLayers:
    for i, aname in enumerate(l.anchors.keys()):
        l.removeAnchorWithName_(aname)
