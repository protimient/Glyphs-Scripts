# MenuTitle: Show Top 10 Largest Kerning Pairs
# -*- coding: utf-8 -*-
__doc__ = """
Show Top 10 Largest Kerning Pairs.
"""
from collections import defaultdict

script = ''


Glyphs.clearLog()
# Glyphs.showMacroWindow()

thisFont = Glyphs.font  # frontmost font

thisFont.disableUpdateInterface()

groupsDict = {'left': defaultdict(list), 'right': defaultdict(list)}

for g in thisFont.glyphs:
    groupsDict['left'][u'@MMK_R_{0}'.format(g.leftKerningGroup)] = g.name
    groupsDict['right'][u'@MMK_L_{0}'.format(g.rightKerningGroup)] = g.name

valuesDict = []
for master in thisFont.masters:
    kerningDict = thisFont.kerning[master.id]
    masterValuesDict = {}
    for left, rights in kerningDict.items():
        try:
            leftGlyphName = thisFont.glyphForId_(left).name
        except AttributeError:
            leftGlyphName = groupsDict['right'][left]

        if not leftGlyphName:
            print(left)

        for right, value in rights.items():
            try:
                rightGlyphName = thisFont.glyphForId_(right).name
            except AttributeError:
                rightGlyphName = groupsDict['left'][right]

            if script:
                if thisFont.glyphs[leftGlyphName].script == script and thisFont.glyphs[rightGlyphName].script == script:
                    masterValuesDict[value] = (thisFont.glyphs[leftGlyphName].layers[master.id], thisFont.glyphs[rightGlyphName].layers[master.id])
            else:
                masterValuesDict[value] = (thisFont.glyphs[leftGlyphName].layers[master.id], thisFont.glyphs[rightGlyphName].layers[master.id])

    valuesDict.append(masterValuesDict)

if valuesDict:
    Glyphs.font.newTab()
    for valDict in valuesDict:
        for val in sorted(valDict.keys())[:10]:
            glyphs = valDict[val]
            Glyphs.font.tabs[-1].layers.append(glyphs[0])
            Glyphs.font.tabs[-1].layers.append(glyphs[1])
            Glyphs.font.tabs[-1].layers.append(GSControlLayer(0x0020))

        Glyphs.font.tabs[-1].layers.append(GSControlLayer(10))

thisFont.enableUpdateInterface()
