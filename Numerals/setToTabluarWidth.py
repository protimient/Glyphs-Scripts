# MenuTitle: Set Selected To Tabluar Width
# -*- coding: utf-8 -*-
__doc__ = """
Sets the width of the selected glyphs to the same as the other tabular numerals.
"""
# Glyphs.clearLog()
# Glyphs.showMacroWindow()


thisFont = Glyphs.font  # frontmost font
thisFontMaster = thisFont.selectedFontMaster  # active master
listOfSelectedLayers = thisFont.selectedLayers  # active layers of selected glyphs
selectedGlyphs = [g.parent for g in listOfSelectedLayers]

nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def _tabularWidths():
    widths = {}
    for m in thisFont.masters:
        numberWidths = set([thisFont.glyphs[gn].layers[m.id].width for gn in nums])
        if thisFont.glyphs['zero.tf']:
            widths[m.id] = thisFont.glyphs['zero.tf'].layers[m.id].width

        elif len(numberWidths) == 1:
            widths[m.id] = thisFont.glyphs['zero'].layers[m.id].width

    return widths


tabularWidths = _tabularWidths()
thisFont.disableUpdateInterface()  # suppresses UI updates in Font View

for g in selectedGlyphs:
    g.leftMetricsKey = None
    g.rightMetricsKey = None
    g.widthMetricsKey = None
    for l in g.layers:
        l.leftMetricsKey = None
        l.rightMetricsKey = None
        l.widthMetricsKey = None
        for thisComp in l.components:
            thisComp.automaticAlignment = False
            addToSides = (tabularWidths[l.associatedMasterId] - l.width) / 2

            l.LSB += addToSides
            l.width = tabularWidths[l.associatedMasterId]


thisFont.enableUpdateInterface()  # re-enables UI updates in Font View
