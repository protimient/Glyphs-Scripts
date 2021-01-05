# MenuTitle: Batch Rename...
# -*- coding: utf-8 -*-
__doc__ = """
When given 2 lists, from and to, renames the glyphs accordingly.
"""

import vanilla

Glyphs.clearLog()


class MasterFiller(object):

    def __init__(self):
        width = 300
        height = 290
        left = 15
        right = width - (left * 2)
        Hmargin = 5
        Vmargin_small = 4
        Vmargin_big = 20
        box_height = 60
        text_height = 18
        self.w = vanilla.FloatingWindow((width, height), "Batch Rename")

        self.w.text_0 = vanilla.TextBox((left, Vmargin_big, right, text_height), "(Each should be a space-separated list)", sizeStyle='small')
        self.w.text_1 = vanilla.TextBox((left, Vmargin_big + text_height + Vmargin_small, right, text_height), "Change glyph names FROM:", sizeStyle='small')
        self.w.fromtext = vanilla.EditText((left, Vmargin_big + text_height + Vmargin_small + text_height + Vmargin_small, right, box_height), "", sizeStyle='small')

        self.w.text_2 = vanilla.TextBox((left, Vmargin_big + text_height + Vmargin_small + text_height + Vmargin_small + box_height + Vmargin_big, right, text_height), "Change glyph names TO:", sizeStyle='small')  # NoQA: E501
        self.w.totext = vanilla.EditText((left, Vmargin_big + text_height + Vmargin_small + text_height + Vmargin_small + box_height + Vmargin_big + text_height + Vmargin_small, right, box_height), "", sizeStyle='small')  # NoQA: E501

        self.w.cancelbutton = vanilla.Button((left, Vmargin_big + text_height + Vmargin_small + text_height + Vmargin_small + box_height + Vmargin_big + text_height + Vmargin_small + box_height + Vmargin_big, right / 2 - Hmargin, 17), "Cancel", sizeStyle='small', callback=self.cancelCallback)  # NoQA: E501
        self.w.addbutton = vanilla.Button((width / 2 + Hmargin, Vmargin_big + text_height + Vmargin_small + text_height + Vmargin_small + box_height + Vmargin_big + text_height + Vmargin_small + box_height + Vmargin_big, right / 2 - Hmargin, 17), "Go", sizeStyle='small', callback=self.buttonCallback)  # NoQA: E501

        # self.w.setDefaultButton(self.w.addbutton)

        self.w.open()
        self.w.center()

    def cancelCallback(self, sender):
        self.w.close()

    def buttonCallback(self, sender):
        fromtext = self.w.fromtext.get().strip().split(' ')
        totext = self.w.totext.get().strip().split(' ')
        if len(fromtext) == len(totext):
            for gni, gn_from in enumerate(fromtext):
                try:
                    Glyphs.font.glyphs[gn_from].name = totext[gni]
                except AttributeError:
                    pass

        self.w.close()


MasterFiller()
