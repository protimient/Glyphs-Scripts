# MenuTitle: Rename Anchors...
# -*- coding: utf-8 -*-
__doc__ = """
Renames the Anchors in the Selected Glyphs.
"""
import vanilla

Glyphs.clearLog()
# Glyphs.showMacroWindow()


class replaceAnchorNames(object):

    def __init__(self):
        width = 300
        height = 200
        left = 15
        right = width - (left * 2)
        margin = 5

        self.thisFont = Glyphs.font

        self.all_anchor_names = self.allAnchorNames()

        self.w = vanilla.FloatingWindow((width, height), "Rename Anchors in Selected Glyphs")

        self.w.text_1 = vanilla.TextBox((left, 12, right, 22), "Replace:", sizeStyle='small')
        self.w.nameFind = vanilla.PopUpButton((left, 30 + margin, right - margin, 17), self.all_anchor_names, sizeStyle='regular', callback=self.changetext)

        self.w.text_2 = vanilla.TextBox((left, 65 + margin, right / 2 - margin, 17), "With:", sizeStyle='small')
        self.w.nameReplace = vanilla.EditText((left, 85 + margin, right - margin, 20), self.all_anchor_names[0], sizeStyle='small')

        self.w.xcurrent = vanilla.CheckBox((left, 120 + margin, right - margin, 17), "Rename only in the Current Layer", value=False, sizeStyle='small')

        self.w.cancelbutton = vanilla.Button((left, 160 + margin, right / 2 - margin, 17), "Cancel", sizeStyle='small', callback=self.cancelCallback)
        self.w.addbutton = vanilla.Button((width / 2 + margin, 160 + margin, right / 2 - margin, 17), "Rename", sizeStyle='small', callback=self.buttonCallback)

        self.w.setDefaultButton(self.w.addbutton)

        self.w.open()
        self.w.center()

    def changetext(self, sender):
        self.w.nameReplace.set(sender.getItem())

    def allAnchorNames(self):
        aan = set()
        for g in [x.parent for x in self.thisFont.selectedLayers]:
            for l in g.layers:
                for a in l.anchors:
                    aan.add(a.name)

        return sorted(aan)

    def cancelCallback(self, sender):
        self.w.close()

    def buttonCallback(self, sender):
        nameFind = self.all_anchor_names[self.w.nameFind.get()]
        nameReplace = self.w.nameReplace.get()

        self.thisFont.disableUpdateInterface()

        if self.w.xcurrent.get():
            for l in self.thisFont.selectedLayers:
                for a in l.anchors:
                    if a.name == nameFind:
                        a.name = nameReplace
        else:
            for g in [x.parent for x in self.thisFont.selectedLayers]:
                for l in g.layers:
                    for a in l.anchors:
                        if a.name == nameFind:
                            a.name = nameReplace

        self.w.close()
        self.thisFont.enableUpdateInterface()


replaceAnchorNames()
