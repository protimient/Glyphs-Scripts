# MenuTitle: Delete ALL Anchors for Selected
# -*- coding: utf-8 -*-
__doc__ = """
Deletes all anchors on the current layer, or with capslock on, every layer. Can be run on a single glyph in edit view or a selection of glyphs in font view.
"""
# --- From mekkablue ---
from AppKit import NSEvent
keysPressed = NSEvent.modifierFlags()
capslockKey = 65536
capslockKeyPressed = keysPressed & capslockKey == capslockKey
# ---

if capslockKeyPressed:
    for g in [x.parent for x in Glyphs.font.selectedLayers]:
        for l in g.layers:
            l.anchors = []
else:
    for l in Glyphs.font.selectedLayers:
        l.anchors = []
