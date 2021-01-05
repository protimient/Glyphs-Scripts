# MenuTitle: Add Anchors for Each Smart Axis
# -*- coding: utf-8 -*-
__doc__ = """
Adds anchors to the current layer for each smart axis if the current glyph is a smart glyph.
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

l = Glyphs.font.selectedLayers[0]
g = Glyphs.font.selectedLayers[0].parent

for ax in g.smartComponentAxes:
    # aname = re.sub('[^\w]', '', ax.name)
    aname = ax.name
    a = GSAnchor(aname, NSPoint(0, 0))
    l.anchors.append(a)
