# MenuTitle: Fit Tabular Numerals - Family
# -*- coding: utf-8 -*-
__doc__ = """
Determines the greatest width of the fitted numerals and then sets the width of the tabular numerals to that width by adding the difference equally to the sidebearings.
This effectively increases the width proportionally. (This is a good thing.)
Values are calculated for the whole font.
"""

import re

linPropSuffix = ''
linTabSuffix = '.tf'
oldPropSuffix = '.osf'
oldTabSuffix = '.tosf'

nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

Font = Glyphs.currentDocument.font


def fitTabNums(tabnumslist=False, **kwargs):
    linPropSuffix = kwargs.get('linPropSuffix', ".lf")
    linTabSuffix = kwargs.get('linTabSuffix', '.tf')
    oldPropSuffix = kwargs.get('oldPropSuffix', '.osf')
    oldTabSuffix = kwargs.get('oldTabSuffix', '.tosf')

    # Get the maximum width
    maxWidth = 0
    for suffix in [linPropSuffix, oldPropSuffix]:
        for gn in nums:
            if Font.glyphs[gn + suffix] is not None:
                g = Font.glyphs[gn]
                for l in g.layers:
                    if l.width > maxWidth:
                        maxWidth = l.width

    # Set the widths
    if not tabnumslist:
        tabnumslist = []
        for g in Font.glyphs:
            if g.name.endswith(linTabSuffix) or g.name.endswith(oldTabSuffix):
                tabnumslist.append(g.name)

    for gn in tabnumslist:
        g = Font.glyphs[gn]
        prop_gn = re.sub(linTabSuffix + '$', linPropSuffix, re.sub(oldTabSuffix + '$', oldPropSuffix, g.name))
        prop_g = Font.glyphs[prop_gn]

        for li, l in enumerate(g.layers):
            addToSides = float(maxWidth - prop_g.layers[li].width) / 2
            new_LSB = float(prop_g.layers[li].LSB + addToSides)

            for c in l.components:
                c.setDisableAlignment_(True)

            l.LSB = new_LSB
            l.width = maxWidth


Glyphs.font.disableUpdateInterface()

fitTabNums(linPropSuffix=linPropSuffix, linTabSuffix=linTabSuffix, oldPropSuffix=oldPropSuffix, oldTabSuffix=oldTabSuffix)

Glyphs.font.enableUpdateInterface()
