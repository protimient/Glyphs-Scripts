# MenuTitle: Replace In Anchor Names...
# -*- coding: utf-8 -*-
__doc__ = """
Regex find and replace for anchor names in all layers for the selected glyphs.
"""
import re
import vanilla

Glyphs.clearLog()
# Glyphs.showMacroWindow()


class replaceInAnchorNames(object):

    def __init__(self):
        item_height = 24.0
        w_width = 350.0
        w_height = item_height * 7
        margin = 10
        next_y = margin
        col_1_width = w_width - (margin * 2)
        item_height = 24

        self.thisFont = Glyphs.font

        self.w = vanilla.Window((w_width, w_height), "Find/Replace in Anchor Names")

        self.w.text_find = vanilla.TextBox((margin, next_y, col_1_width, item_height), "Find:")
        next_y += item_height
        self.w.val_find = vanilla.EditText((margin, next_y, col_1_width, item_height), sizeStyle='regular')
        next_y += item_height + margin

        self.w.text_replace = vanilla.TextBox((margin, next_y, col_1_width, item_height), "Replace:")
        next_y += item_height
        self.w.val_replace = vanilla.EditText((margin, next_y, col_1_width, item_height), sizeStyle='regular')
        next_y += item_height + margin

        self.w.gobutton = vanilla.Button((margin + (col_1_width / 4), next_y, col_1_width / 2, item_height), 'Replace', callback=self.makeitso)

        self.w.setDefaultButton(self.w.gobutton)
        self.w.center()
        self.w.open()

    def makeitso(self, sender):
        self.w.close()

        nameFind = self.w.val_find.get()
        nameReplace = self.w.val_replace.get()

        self.thisFont.disableUpdateInterface()

        for sl in self.thisFont.selectedLayers:
            for l in sl.parent.layers:
                for a in l.anchors:
                    a.name = re.sub(nameFind, nameReplace, a.name)

        self.thisFont.enableUpdateInterface()


replaceInAnchorNames()
