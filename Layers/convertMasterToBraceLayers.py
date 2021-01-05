# MenuTitle: Convert Master to Brace Layers...
# -*- coding: utf-8 -*-
__doc__ = """
Converts a Master into Brace layers.
"""

import copy
from vanilla import (
    Window,
    TextBox,
    Button,
    PopUpButton,
)

Glyphs.clearLog()
# Glyphs.showMacroWindow()


class convertMasterToBraceLayers(object):
    def __init__(self):
        self.master_names = [m.name for m in Glyphs.font.masters][1:]

        item_height = 24.0
        w_width = 350.0
        w_height = item_height * 5
        margin = 10
        next_y = margin
        col_1_width = w_width - (margin * 2)
        item_height = 24

        self.w = Window((w_width, w_height), "Convert Master to Brace Layers")

        next_y = margin
        self.w.master_names_label = TextBox((margin, next_y + 2, col_1_width, item_height), "Master to Convert (Cannot be the first Master)", sizeStyle='regular')
        next_y += item_height
        self.w.master_names = PopUpButton((margin, next_y, col_1_width, item_height), self.master_names)
        next_y += item_height + margin
        selected_master_index = Glyphs.font.masters.index(Glyphs.font.selectedFontMaster)
        self.w.master_names.set(selected_master_index - 1)

        self.w.gobutton = Button((margin + (col_1_width / 4), next_y, col_1_width / 2, item_height), 'Add Brace Layers', callback=self.makeitso)

        self.w.setDefaultButton(self.w.gobutton)

        self.w.open()

    def makeitso(self, sender):
        self.w.close()

        Glyphs.font.disableUpdateInterface()

        selected_master_index = self.w.master_names.get() + 1
        selected_master = Glyphs.font.masters[selected_master_index]
        layer_name = '{{{}}}'.format(', '.join([bytes(x) for x in selected_master.axes]))
        master_to_attach_to = Glyphs.font.masters[selected_master_index - 1]

        for g in Glyphs.font.glyphs:
            for l in g.layers:
                if l.associatedMasterId == selected_master.id:
                    if l.isSpecialLayer:
                        l.associatedMasterId = master_to_attach_to.id
                        continue

                    newL = copy.copy(l)
                    newL.associatedMasterId = master_to_attach_to.id
                    newL.name = layer_name
                    g.layers.append(newL)

        del(Glyphs.font.masters[selected_master_index])

        Glyphs.font.enableUpdateInterface()
        Glyphs.showMacroWindow()


convertMasterToBraceLayers()
