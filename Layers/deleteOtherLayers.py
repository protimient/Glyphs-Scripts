# MenuTitle: Delete layers other than the first

for g in Glyphs.font.glyphs:
    if len(g.layers) > 1:
        for lid in list(x.layerId for x in g.layers)[1:]:
            del(g.layers[lid])
