# MenuTitle: Report Nested Components

Glyphs.clearLog()


def sort_layers(l):
    return l.parent.name, [m.id for m in Glyphs.font.masters].index(l.associatedMasterId)


strings = set()
affected_layers = set()
for g in Glyphs.font.glyphs:
    for l in g.layers:
        for c in l.components:
            c_parent = c.component
            try:
                if c_parent.layers[l.layerId].components and not c_parent.layers[l.layerId].paths:
                    affected_layers.add(l)
                    break
            except AttributeError:
                pass


if affected_layers:
    affected_layers = sorted(affected_layers, key=sort_layers)
    Glyphs.font.newTab()
    Glyphs.font.tabs[-1].layers = affected_layers
