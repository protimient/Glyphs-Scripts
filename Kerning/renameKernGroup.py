# MenuTitle: Rename Kern Group

import re
from vanilla import Window, Button, TextBox, PopUpButton, EditText

Glyphs.clearLog()
# Glyphs.showMacroWindow()


class renameKerning(object):
    def __init__(self):
        item_height = 24.0
        w_width = 300.0
        w_height = item_height * 8
        margin = 10
        next_y = margin
        col_1_width = w_width - (margin * 2)
        item_height = 24

        self.messages = []
        self.interpolated_fonts = dict()
        self.current_glyph = None

        self.all_kern_groups = self.get_all_kern_groups()
        self.w = Window((w_width, w_height), "Rename Kern Groups")

        self.w.text_1 = TextBox((margin, next_y, w_width, item_height), "Rename:", sizeStyle='small')
        next_y += item_height
        self.w.nameFind = PopUpButton((margin, next_y, w_width - (margin * 2), item_height), self.all_kern_groups, sizeStyle='regular')
        next_y += item_height + item_height

        self.w.text_2 = TextBox((margin, next_y, w_width, item_height), "To:", sizeStyle='small')
        next_y += item_height
        self.w.nameReplace = EditText((margin, next_y, w_width - (margin * 2), item_height), "", sizeStyle='regular')
        next_y += item_height + margin

        self.w.gobutton = Button((margin + (col_1_width / 4), next_y, col_1_width / 2, item_height), 'Rename', callback=self.makeitso)

        self.w.setDefaultButton(self.w.gobutton)
        self.w.center()
        self.w.open()

    def sbuttonCallback(self, sender):
        self.s.close()

    def get_all_kern_groups(self):
        all_kern_groups = set()
        for g in Glyphs.font.glyphs:
            if g.leftKerningGroup is not None:
                all_kern_groups.add('{} - LEFT'.format(g.leftKerningGroup))
                if '{} - RIGHT'.format(g.leftKerningGroup) in all_kern_groups:
                    all_kern_groups.add('{} - BOTH'.format(g.leftKerningGroup))

            if g.rightKerningGroup is not None:
                all_kern_groups.add('{} - RIGHT'.format(g.rightKerningGroup))
                if '{} - LEFT'.format(g.rightKerningGroup) in all_kern_groups:
                    all_kern_groups.add('{} - BOTH'.format(g.rightKerningGroup))

        return sorted(all_kern_groups)

    def makeitso(self, sender):
        self.w.close()
        nameReplace = self.w.nameReplace.get()
        nameFind = self.w.nameFind.getItem()
        group_name, _, side = nameFind.partition(' - ')

        for g in Glyphs.font.glyphs:
            if side in ['LEFT', 'BOTH']:
                if g.leftKerningGroup == group_name:
                    g.leftKerningGroup = nameReplace

            if side in ['RIGHT', 'BOTH']:
                if g.rightKerningGroup == group_name:
                    g.rightKerningGroup = nameReplace

        if '{} - {}'.format(nameReplace, side) in self.all_kern_groups:
            Glyphs.showNotification('Kern Group Renaming Success!', 'Note: the kern group named "{}" already exists so it will keep its existing kerning values.'.format(nameReplace))
            return

        for m_id in Glyphs.font.kerning:
            for left_group in Glyphs.font.kerning[m_id]:
                if side in ['RIGHT', 'BOTH']:
                    group_prefix = self.is_group(left_group, group_name)
                    if group_prefix:
                        for right_group, val in Glyphs.font.kerning[m_id][left_group].items():
                            Glyphs.font.setKerningForPair(m_id, group_prefix + nameReplace, self.glyph_for_id(right_group), val)
                            Glyphs.font.removeKerningForPair(m_id, left_group, self.glyph_for_id(right_group))
                        left_group = group_prefix + nameReplace

                if side in ['LEFT', 'BOTH']:
                    for right_group, val in Glyphs.font.kerning[m_id][left_group].items():
                        group_prefix = self.is_group(right_group, group_name)
                        if group_prefix:
                            # print(m_id, left_group, right_group, self.glyph_for_id(left_group), group_prefix + nameReplace, val)
                            # with open('/Users/benjones/Desktop/test.txt', 'a') as f:
                            #     f.write('{}\n'.format([m_id, left_group, right_group, self.glyph_for_id(left_group), group_prefix + nameReplace, val]))
                            Glyphs.font.setKerningForPair(m_id, self.glyph_for_id(left_group), group_prefix + nameReplace, val)
                            Glyphs.font.removeKerningForPair(m_id, self.glyph_for_id(left_group), right_group)

    @staticmethod
    def is_group(group, group_name):
        found_group = re.match('^(@MMK_._){}$'.format(group_name), group)
        if found_group is None:
            return False

        return found_group.group(1)

    @staticmethod
    def glyph_for_id(some_name):
        try:
            return Glyphs.font.glyphForId_(some_name).name
        except AttributeError:
            return some_name


renameKerning()
