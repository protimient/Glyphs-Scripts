# MenuTitle: Delete Named Anchor...
# -*- coding: utf-8 -*-
__doc__ = """
Deletes the anchor in the current or all layers in the selected glyphs.
"""

import vanilla


# Glyphs.clearLog()
# Glyphs.showMacroWindow()


class deleteNamedAnchor(object):

    def __init__(self):
        width = 300
        height = 140
        left = 15
        right = width - (left * 2)
        margin = 5

        self.this_font = Glyphs.font

        self.all_anchor_names = self.allAnchorNames()
        if self.all_anchor_names is None:
            Glyphs.showNotification('Delete Named Anchor', 'No glyphs were selected!')

        elif not self.all_anchor_names:
            Glyphs.showNotification('Delete Named Anchor:', 'None of the selected glyphs contains any anchors!')

        else:
            self.w = vanilla.FloatingWindow((width, height), "Delete Anchors")

            self.w.text_1 = vanilla.TextBox((left, 12, right, 22), "Delete:", sizeStyle='small')
            self.w.xFind = vanilla.PopUpButton((left, 30 + margin, right - margin, 17), self.all_anchor_names, sizeStyle='regular')

            self.w.xcurrent = vanilla.CheckBox((left, 60 + margin, right - margin, 17), "Delete only in the Current Layer", value=False, sizeStyle='small')

            self.w.cancelbutton = vanilla.Button((left, 100 + margin, right / 2 - margin, 17), "Close", sizeStyle='small', callback=self.cancelCallback)
            self.w.addbutton = vanilla.Button((width / 2 + margin, 100 + margin, right / 2 - margin, 17), "Delete", sizeStyle='small', callback=self.buttonCallback)

            self.w.setDefaultButton(self.w.addbutton)

            self.w.open()
            self.w.center()

    def allAnchorNames(self):
        if not self.this_font.selectedLayers:
            return None

        aan = set()
        for g in [x.parent for x in self.this_font.selectedLayers]:
            for l in g.layers:
                for a in l.anchors:
                    aan.add(a.name)

        return sorted(aan)

    def cancelCallback(self, sender):
        self.w.close()

    def buttonCallback(self, sender):
        xFind = self.all_anchor_names[self.w.xFind.get()]

        self.this_font.disableUpdateInterface()

        if self.w.xcurrent.get():
            for l in self.this_font.selectedLayers:
                del(l.anchors[xFind])
        else:
            for g in [x.parent for x in self.this_font.selectedLayers]:
                for l in g.layers:
                    del(l.anchors[xFind])

        self.w.close()
        deleteNamedAnchor()
        self.this_font.enableUpdateInterface()


deleteNamedAnchor()
