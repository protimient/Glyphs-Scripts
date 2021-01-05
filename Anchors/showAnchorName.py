# MenuTitle: Show Glyphs with named anchor...
# -*- coding: utf-8 -*-
__doc__ = """
Opens a new tab showing all the glyphs in the selected glyphs that have the chosen anchor.
"""

import vanilla
# Glyphs.clearLog()
# Glyphs.showMacroWindow()


class replaceAnchorNames(object):

    def __init__(self):
        width = 300
        height = 120
        left = 15
        right = width - (left * 2)
        margin = 5

        self.thisFont = Glyphs.font

        self.all_anchor_names = self.allAnchorNames()

        self.w = vanilla.FloatingWindow((width, height), "Rename Anchors in Selected Glyphs")

        self.w.text_1 = vanilla.TextBox((left, 12, right, 22), "Show Glyphs with Anchor:", sizeStyle='small')
        self.w.nameFind = vanilla.PopUpButton((left, 30 + margin, right - margin, 17), self.all_anchor_names, sizeStyle='regular')

        self.w.cancelbutton = vanilla.Button((left, 80 + margin, right / 2 - margin, 17), "Cancel", sizeStyle='small', callback=self.cancelCallback)
        self.w.addbutton = vanilla.Button((width / 2 + margin, 80 + margin, right / 2 - margin, 17), "Show", sizeStyle='small', callback=self.buttonCallback)

        self.w.setDefaultButton(self.w.addbutton)

        self.w.open()
        self.w.center()

    def allAnchorNames(self):
        aan = set()
        for l in self.thisFont.selectedLayers:
            if l.anchors:
                for a in l.anchors:
                    aan.add(a.name)

        return sorted(aan)

    def cancelCallback(self, sender):
        self.w.close()

    def buttonCallback(self, sender):
        nameFind = self.all_anchor_names[self.w.nameFind.get()]

        self.thisFont.disableUpdateInterface()

        string = []
        for l in self.thisFont.selectedLayers:
            if nameFind in [a.name for a in l.anchors]:
                string.append(l.parent.name)

        Glyphs.font.newTab('  '.join(['/' + gn for gn in string]))

        self.w.close()
        self.thisFont.enableUpdateInterface()


replaceAnchorNames()
