# MenuTitle: Delete ALL Anchors for Selected
# -*- coding: utf-8 -*-
__doc__ = """
Deletes all anchors on every layer. Can be run on a single glyph in edit view or a selection of glyphs in font view.
"""

for g in [x.parent for x in Glyphs.font.selectedLayers]:
    for l in g.layers:
        for i, aname in enumerate(l.anchors.keys()):
            l.removeAnchorWithName_(aname)
