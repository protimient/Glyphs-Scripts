# MenuTitle: Remove PS Hinting for Selected
Glyphs.clearLog()

for g in [x.parent for x in Glyphs.font.selectedLayers]:
    for l in g.layers:
        keep_hints = []
        for h in l.hints:
            if h.type not in [TOPGHOST, STEM, BOTTOMGHOST]:
                keep_hints.append(h)

        l.hints = keep_hints
