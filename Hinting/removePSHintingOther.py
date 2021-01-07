# MenuTitle: Remove Other Layer's PS Hinting for Selected

__doc__ = """
Removes Postscript hinting from all layers except for the currently selected layer.
"""

Glyphs.clearLog()

for l1 in Glyphs.font.selectedLayers:
    g = l1.parent
    for l2 in g.layers:
        if l1.layerId == l2.layerId:
            continue
        keep_hints = []
        for h in l2.hints:
            if h.type not in [TOPGHOST, STEM, BOTTOMGHOST]:
                keep_hints.append(h)

        l2.hints = keep_hints
