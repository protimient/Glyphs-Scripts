# MenuTitle: Center Glyphs for All Layers
# -*- coding: utf-8 -*-
__doc__ = """
Center all selected glyphs inside their respective widths.
"""

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers
selectedGlyphs = [g.parent for g in selectedLayers]

thisFont.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
    for thisLayer in thisGlyph.layers:
        thisGlyph.beginUndo()
        oldWidth = thisLayer.width
        thisLayer.LSB = (thisLayer.LSB + thisLayer.RSB) // 2
        thisLayer.width = oldWidth
        thisGlyph.endUndo()

thisFont.enableUpdateInterface()
print("Centered: {}".format(", ".join([l.parent.name for l in selectedLayers])))
