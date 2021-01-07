# MenuTitle: Show Glyphs with MetricsKeys
# -*- coding: utf-8 -*-
__doc__ = """
Opens a tab listing glyphs in the selection with MetricsKeys.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

strings = []

for g in [x.parent for x in Glyphs.font.selectedLayers]:
    if g.leftMetricsKey or g.rightMetricsKey:
        strings.append('/{0}  '.format(g.name))
    else:
        for l in g.layers:
            if l.leftMetricsKey() or l.rightMetricsKey():
                strings.append('/{0}  '.format(g.name))


string = ''.join(sorted(strings))
Glyphs.font.newTab(string)
