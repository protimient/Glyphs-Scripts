# MenuTitle: Fit Tabular Numerals
# -*- coding: utf-8 -*-
__doc__ = """
Determines the greatest width of the fitted numerals and then sets the width of the tabular numerals to that width by adding the difference equally to the sidebearings.
This effectively increases the width proportionally. (This is a good thing.)
Values are calculated per master.
"""

from collections import defaultdict

Glyphs.clearLog()
Glyphs.showMacroWindow()

linPropSuffix = ''
linTabSuffix = '.tf'
oldPropSuffix = '.osf'
oldTabSuffix = '.tosf'

nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def fitTabNums(tabnumslist=False, **kwargs):
    # linPropSuffix = kwargs.get('linPropSuffix', ".lf")
    linTabSuffix = kwargs.get('linTabSuffix', '.tf')
    # oldPropSuffix = kwargs.get('oldPropSuffix', '.osf')
    oldTabSuffix = kwargs.get('oldTabSuffix', '.tosf')
    set_value = kwargs.get('value')

    if not tabnumslist:
        tabnumslist = []
        for g in Glyphs.font.glyphs:
            if g.name.endswith(linTabSuffix) or g.name.endswith(oldTabSuffix):
                tabnumslist.append(g.name)

    maxWidth = defaultdict(int)
    for gn in tabnumslist:
        g = Glyphs.font.glyphs[gn]
        if g is not None:
            for l in g.layers:
                if set_value is not None:
                    maxWidth[l.associatedMasterId] = set_value
                elif l.width > maxWidth[l.associatedMasterId]:
                    maxWidth[l.associatedMasterId] = l.width

    # Set the widths
    for gn in tabnumslist:
        g = Glyphs.font.glyphs[gn]

        for l in g.layers:
            addToSides = (maxWidth[l.associatedMasterId] - l.width) / 2
            for c in l.components:
                c.setDisableAlignment_(True)

            l.LSB += addToSides
            l.width = maxWidth[l.associatedMasterId]


Glyphs.font.disableUpdateInterface()

fitTabNums(linPropSuffix=linPropSuffix, linTabSuffix=linTabSuffix, oldPropSuffix=oldPropSuffix, oldTabSuffix=oldTabSuffix, value=None)

Glyphs.font.enableUpdateInterface()
