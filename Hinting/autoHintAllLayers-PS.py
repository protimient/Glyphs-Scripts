# MenuTitle: Autohint (Postscript) Selected - All Layers
# -*- coding: utf-8 -*-
__doc__ = """
Autohints all the selected glyphs in all layers.
If the font is italic, only autohints horizontally.
"""
Glyphs.clearLog()

for g in [x.parent for x in Glyphs.font.selectedLayers]:
    for l in g.layers:
        keep_hints = []
        for h in l.hints:
            if h.type not in [TOPGHOST, STEM, BOTTOMGHOST]:
                keep_hints.append(h)

        l.hints = keep_hints

for sl in Glyphs.font.selectedLayers:
    g = sl.parent
    for l in g.layers:
        l.autohint()
        if Glyphs.font.masters[l.associatedMasterId].italicAngle:
            keep_hints = []
            for h in l.hints:
                if h.horizontal or h.type not in [TOPGHOST, STEM, BOTTOMGHOST]:
                    keep_hints.append(h)
            l.hints = keep_hints

        try:
            l.hints[0].selected = True
        except AttributeError:
            pass
