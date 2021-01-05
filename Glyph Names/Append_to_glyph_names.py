# MenuTitle: Append to Glyph Names...
# -*- coding: utf-8 -*-
__doc__ = """
Adds the supplied text to the end of the glyph name for the selected glyphs.
"""

import vanilla

Glyphs.clearLog()


class MasterFiller(object):

    def __init__(self):
        width = 300
        height = 90
        left = 15
        right = width - (left * 2)
        margin = 5

        self.w = vanilla.FloatingWindow((width, height), "Append text to Glyph Names")

        self.w.text_1 = vanilla.TextBox((left, 12, right, 22), "Text to add:", sizeStyle='small')
        self.w.addtext = vanilla.EditText((left, 30, right, 20), ".liga", sizeStyle='small')

        self.w.cancelbutton = vanilla.Button((left, 50 + margin, right / 2 - margin, 17), "Cancel", sizeStyle='small', callback=self.cancelCallback)
        self.w.addbutton = vanilla.Button((width / 2 + margin, 50 + margin, right / 2 - margin, 17), "Append", sizeStyle='small', callback=self.buttonCallback)

        self.w.setDefaultButton(self.w.addbutton)

        self.w.open()
        self.w.center()

    def cancelCallback(self, sender):
        self.w.close()

    def buttonCallback(self, sender):
        add_text = self.w.addtext.get()

        Glyphs.font.disableUpdateInterface()
        for g in [x.parent for x in Glyphs.font.selectedLayers]:

            newName = str(g.name + add_text)
            # print g.name,' -> ', g.name + add_text
            g.name = newName

        Glyphs.font.enableUpdateInterface()

        self.w.close()


MasterFiller()
