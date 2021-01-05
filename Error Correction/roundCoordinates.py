# MenuTitle: Round All Coordinates for Everything

# Glyphs.clearLog()
# Glyphs.showMacroWindow()


for g in Glyphs.font.glyphs:
    for l in g.layers:
        for p in l.paths:
            for n in p.nodes:
                n.position = NSPoint(float(int(n.x)), float(int(n.y)))

        for c in l.components:
            c.position = NSPoint(float(int(c.x)), float(int(c.y)))

        for a in l.anchors:
            a.position = NSPoint(float(int(a.x)), float(int(a.y)))


for mid, ks in Glyphs.font.kerning.items():
    for left, rights in ks.items():
        for right, val in rights.items():
            Glyphs.font.kerning[mid][left][right] = int(val)
