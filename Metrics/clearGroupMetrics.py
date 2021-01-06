# MenuTitle: Clear Group Metrics
Glyphs.font.disableUpdateInterface()

for g in [x.parent for x in Glyphs.font.selectedLayers]:
    g.leftMetricsKey = None
    g.rightMetricsKey = None
    g.widthMetricsKey = None
    for l in g.layers:
        l.leftMetricsKey = None
        l.rightMetricsKey = None
        l.widthMetricsKey = None

Glyphs.font.enableUpdateInterface()
