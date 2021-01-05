# MenuTitle: Copy kerning for Class from Other Font
# -*- coding: utf-8 -*-
__doc__ = """
Copies the kerning for the chosen class from the other open font.
"""

from vanilla import Window, Button, TextBox, PopUpButton, RadioGroup

Glyphs.clearLog()
Glyphs.showMacroWindow()


class copyKerning(object):
    # TODO: Add class to different class name copying.
    # TODO: Allow left or right or both selection.
    # TODO: Allow open font selection.
    # TODO: Allow from/to layer selection.

    def __init__(self):
        item_height = 24.0
        margin = 10
        next_y = margin
        w_width = 400.0
        w_height = item_height * 7 + margin
        col_1_width = w_width - (margin * 2)

        self.this_font = Glyphs.font
        try:
            self.other_font = [f for f in Glyphs.fonts if f != self.this_font][0]
        except IndexError:
            Glyphs.showNotification('Copy kerning for Class from Other Font:', 'There is only 1 file open!')
            raise

        self.other_fonts_classes = self.get_other_fonts_classes()
        self.w = Window((w_width, w_height), "Copy kerning for Class from Other Font")

        self.w.text_1 = TextBox((margin, next_y, w_width, item_height), "Copy the kerning for this class to this font:", sizeStyle='small')
        next_y += item_height
        self.w.class_to_copy = PopUpButton((margin, next_y, w_width - (margin * 2), item_height), self.other_fonts_classes, sizeStyle='regular')
        next_y += item_height + item_height

        self.w.copy_for_all = RadioGroup((margin, next_y, w_width, item_height * 2), [
            ' Copy only for the current Master',
            ' Copy for All masters',
        ])
        self.w.copy_for_all.set(0)
        next_y += (item_height * 2) + margin

        self.w.gobutton = Button((margin + (col_1_width / 4), next_y, col_1_width / 2, item_height), 'Copy', callback=self.makeitso)

        self.w.setDefaultButton(self.w.gobutton)
        self.w.center()
        self.w.open()

    def get_other_fonts_classes(self):
        all_kern_groups = set()
        for g in self.other_font.glyphs:
            if g.leftKerningGroup is not None:
                all_kern_groups.add(g.leftKerningGroup)

            if g.rightKerningGroup is not None:
                all_kern_groups.add(g.rightKerningGroup)

        return sorted(all_kern_groups)

    def get_other_master(self, this_master):
        try:
            other_master = [m for m in self.other_font.masters if m.name == this_master.name][0]
            return other_master
        except IndexError:
            pass

        return self.other_font.selectedFontMaster

    @staticmethod
    def glyph_for_id(font, some_name):
        try:
            return font.glyphForId_(some_name).name
        except AttributeError:
            return some_name

    def get_this_glyphname(self, some_name):
        try:
            return Glyphs.font.glyphForId_(some_name).name
        except AttributeError:
            return some_name

    def copy_left_kerning(self, this_master, class_name):
        mmk_class_name = '@MMK_L_{}'.format(class_name)
        for right, val in self.other_font.kerning[self.get_other_master(this_master).id][mmk_class_name].items():
            if right.startswith('@MMK'):
                right_name = right
            else:
                right_name = self.other_font.glyphForId_(right).name

            self.this_font.setKerningForPair(this_master.id, mmk_class_name, right_name, val)

    def copy_right_kerning(self, this_master, class_name):
        # TODO: This. Like, it's not done.
        print('No left-side kerning was copied because the function hasn\'t been written yet.')
        pass

    def makeitso(self, sender):
        self.w.close()
        class_name = self.w.class_to_copy.getItem()
        print(bool(self.w.copy_for_all.get()))
        chosen_masters = self.this_font.masters if self.w.copy_for_all.get() else [self.this_font.selectedFontMaster]
        for m in chosen_masters:
            self.copy_left_kerning(m, class_name)
            self.copy_right_kerning(m, class_name)


copyKerning()
