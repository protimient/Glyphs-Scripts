# MenuTitle: Autohint (Postscript) Selected
# -*- coding: utf-8 -*-
__doc__ = """
Autohints all the selected glyphs in the current master.
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
    if len(Glyphs.font.masters) == len(Glyphs.font.instances):
        layers = sl.parent.layers
    else:
        layers = [sl]

    for l in layers:
        l.autohint()
        if Glyphs.font.masters[l.associatedMasterId].italicAngle:
            keep_hints = []
            for h in l.hints:
                if h.horizontal or h.type not in [TOPGHOST, STEM, BOTTOMGHOST]:
                    keep_hints.append(h)
            l.hints = keep_hints


#     l.hints[0].selected = True
