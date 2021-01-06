# MenuTitle: Make Tabular Numerals
# -*- coding: utf-8 -*-
__doc__ = """
Adds missing and replaces existing tabular numerals and fits all tabular glyphs.
"""

from collections import defaultdict
Glyphs.clearLog()
Glyphs.showMacroWindow()


linPropSuffix = ""
linTabSuffix = '.tf'
oldPropSuffix = '.osf'
oldTabSuffix = '.tosf'

measureable_glyph_names = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

makeable_glyph_names = measureable_glyph_names + [
    'cent',
    'dollar',
    'euro',
    'florin',
    'sterling',
    'yen',
]

suffixes = [(linPropSuffix, linTabSuffix), (oldPropSuffix, oldTabSuffix)]

Font = Glyphs.currentDocument.font
Glyphs.font.disableUpdateInterface()
masterIds = [m.id for m in Glyphs.font.masters]

layers_number = range(len(Font.glyphs[0].layers))
tabnums = []
for suffix in suffixes:
    for gn in makeable_glyph_names:
        prop_glyph = Font.glyphs[gn + suffix[0]]
        tab_glyph = Font.glyphs[gn + suffix[1]]

        if prop_glyph is None:
            continue

        if tab_glyph is not None:
            del(Font.glyphs[gn + suffix[1]])

        tab_glyph = GSGlyph()
        tab_glyph.name = gn + suffix[1]
        Font.glyphs.append(tab_glyph)
        tab_glyph.updateGlyphInfo()

        for l in prop_glyph.layers:
            if l.layerId not in masterIds:
                continue

            tab_glyph_layer = tab_glyph.layers[l.layerId]
            if (l.paths or l.components) and not (tab_glyph_layer.paths or tab_glyph_layer.components):
                tab_glyph_layer.components.append(GSComponent(gn + suffix[0]))
                tab_glyph_layer.width = l.width

        tabnums.append(tab_glyph.name)


def fitTabNums(measureable_glyph_names=None, linPropSuffix=".lf", linTabSuffix='.tf', oldPropSuffix='.osf', oldTabSuffix='.tosf'):
    tabular_numerals = [g for g in Font.glyphs if g.name.endswith(linTabSuffix) or g.name.endswith(oldTabSuffix)]
    measureable_glyphs = [Font.glyphs[gn] for gn in measureable_glyph_names]

    maxWidths = defaultdict(list)
    for g in measureable_glyphs:
        for l in g.layers:
            if l.layerId not in masterIds:
                continue
            maxWidths[l.layerId].append(l.width)
    print(maxWidths)

    maxWidth = dict((k, max(v)) for k, v in maxWidths.items())

    # Set the widths
    for g in tabular_numerals:
        for l in g.layers:
            addToSides = (maxWidth[l.layerId] - l.width) / 2

            new_LSB = l.LSB + addToSides

            for c in l.components:
                c.setDisableAlignment_(True)

            l.LSB = new_LSB
            l.width = maxWidth[l.layerId]


fitTabNums(measureable_glyph_names=measureable_glyph_names)

Glyphs.font.enableUpdateInterface()
