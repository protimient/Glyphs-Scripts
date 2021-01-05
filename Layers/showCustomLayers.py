# MenuTitle: Show glyphs with custom layers (ignores special layers)

string = ' '.join(['/' + g.name for g in Glyphs.font.glyphs if len(g.layers) > len(Glyphs.font.masters)])
if string:
    Glyphs.font.newTab(string)
