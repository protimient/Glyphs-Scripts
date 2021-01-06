# MenuTitle: Report Top 20 Lowest Glyphs
Glyphs.clearLog()

display_number = 20

all_layers = []

for m in Glyphs.font.masters:
    these_layers = [g.layers[m.id] for g in Glyphs.font.glyphs if g.export]
    these_layers.sort(key=lambda l: l.bounds.origin.y)
    all_layers.append(these_layers[:display_number])

Glyphs.font.newTab()
for these_layers in all_layers:
    for l in these_layers:
        Glyphs.font.tabs[-1].layers.append(l)
    Glyphs.font.tabs[-1].layers.append(GSControlLayer(10))
