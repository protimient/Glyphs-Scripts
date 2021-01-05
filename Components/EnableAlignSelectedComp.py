# MenuTitle: Enable alignment for selected Component in All layers
# -*- coding: utf-8 -*-
__doc__ = """
Enables automatic alignment for the selected component in all layers in the current glyph.
"""

Glyphs.clearLog()


thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers
selectedGlyphs = [g.parent for g in selectedLayers]


def process(thisLayer):
    for thisComp in thisLayer.components:
        thisComp.automaticAlignment = True


thisFont.disableUpdateInterface()  # suppresses UI updates in Font View

sl = Glyphs.font.selectedLayers[0]
g = sl.parent

g.beginUndo()

for x in sl.selection:
    if type(x) == GSComponent:
        x.automaticAlignment = True

        for l in g.layers:
            if sl == l:
                continue
            for c in l.components:
                if c.name == x.name:
                    c.automaticAlignment = True

g.endUndo()

thisFont.enableUpdateInterface()  # re-enables UI updates in Font View
