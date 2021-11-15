# MenuTitle: Make Kerning Display
# -*- coding: utf-8 -*-
__doc__ = """
Open tab containing Kerning strings for the selected glyphs.
"""

import re
from collections import defaultdict, OrderedDict
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

from vanilla import (
    Window,
    TextBox,
    RadioGroup,
    Button,
    CheckBox,
)
import _kerningStrings

Glyphs.clearLog()
# Glyphs.showMacroWindow()

quotations = [
    ('/parenleft', '/parenright'),
    ('/bracketleft', '/bracketright'),
    ('/braceleft', '/braceright'),
    ('/quoteleft', '/quoteright'),
    ('/quotedblleft', '/quotedblright'),
    ('/quotesinglbase', '/quoteleft'),
    ('/quotedblbase', '/quotedblleft'),
    ('/quotedblbase', '/quotedblright'),
    ('/quoteright', '/quoteright'),
    ('/guillemetleft', '/guillemetright'),
    ('/guilsinglleft', '/guilsinglright'),
    ('/guillemetright', '/guillemetleft'),
    ('/guilsinglright', '/guilsinglleft')
]
# punctuations = ['period', 'comma', 'colon', 'semicolon', 'hyphen']
punctuations = {}
punctuations['dflt'] = '. , : ; -'.split(' ')
punctuations['greek'] = ["/comma", "/period", "/anoteleia", "/questiongreek"]
punctuations['armenian'] = ["/comma-arm", '/period-arm', '/hyphen-arm', "/emphasis-arm", "/exclam-arm", "/question-arm", "/abbreviation-arm", ]


class makeDisplay(object):
    def __init__(self):
        self.verboten = {
            'right': ['napostrophe', 'Omegadasiavaria'],
            'left': ['ldot', 'Ldot', 'ldot.sc', 'sigmafinal'],
            'both': ['*.tf', '*.tosf', '.notdef', 'NULL', 'CR']
        }
        self.category = None
        self.messages = []
        self.interpolated_fonts = dict()
        self.use_real = True
        self.use_selection = False
        self.ignore_red = False
        self.current_glyph = None
        self.leftside_kerning_groups = None
        self.rightside_kerning_groups = None
        self.all_kern_categories = self.get_all_kern_categories()
        self.categories_leftside = self.get_categorised_glyphs('left')
        self.categories_rightside = self.get_categorised_glyphs('right')

        item_height = 24.0
        w_width = 300.0
        w_height = item_height * (7 + len(self.all_kern_categories))
        margin = 10
        next_y = margin
        col_1_width = w_width - (margin * 2)
        item_height = 24

        radio_height = item_height * len(self.all_kern_categories)

        self.w = Window((w_width, w_height), "Make Kerning Strings")

        self.w.text_1 = TextBox((margin, next_y, w_width, item_height), "Kern with:", sizeStyle='regular')
        next_y += item_height
        self.w.radioCategories = RadioGroup((margin, next_y, col_1_width, radio_height), self.all_kern_categories, sizeStyle='regular')
        self.w.radioCategories.set(0)
        next_y += radio_height + margin

        self.w.use_real = CheckBox((margin, next_y, col_1_width, item_height), "Use real words", value=True, sizeStyle='regular')
        next_y += item_height

        self.w.use_selected = CheckBox((margin, next_y, col_1_width, item_height), "Use the selected glyphs verbatum", value=False, sizeStyle='regular')
        next_y += item_height

        self.w.ignore_red = CheckBox((margin, next_y, col_1_width, item_height), "Ignore red marked glyphs", value=False, sizeStyle='regular')
        next_y += item_height + margin

        self.w.gobutton = Button((margin + (col_1_width / 4), next_y, col_1_width / 2, item_height), 'Make Strings', callback=self.makeitso)

        self.w.setDefaultButton(self.w.gobutton)
        self.w.center()
        self.w.open()
        # self.makeitso(None)

    def sbuttonCallback(self, sender):
        self.s.close()

    @staticmethod
    def has_smallcaps():
        for g in Glyphs.font.glyphs:
            if g.subCategory == 'Smallcaps':
                return True

        return False

    def get_all_kern_categories(self):
        kcats = [
            'Uppercase',
            'Lowercase',
        ]
        if self.has_smallcaps:
            kcats.append('Smallcaps')
        kcats += [
            'Quotes',
            'Number',
            'Punctuation',
            'Other',
        ]
        return kcats

    def get_canonincal_kerning_glyph(self, layer, pair_side):
        g = layer.parent

        if self.use_selection:
            return g

        if pair_side == 'left':
            g = Glyphs.font.glyphs[layer.parent.rightKerningGroup] or layer.parent
        if pair_side == 'right':
            g = Glyphs.font.glyphs[layer.parent.leftKerningGroup] or layer.parent

        if g is None:
            g = layer.parent

        return g

    @staticmethod
    def make_list_unique(this_list):
        unique_list = []
        for x in this_list:
            if x in unique_list or x is None:
                continue
            unique_list.append(x)

        return unique_list

    def get_categorised_glyphs(self, side):
        # cats = defaultdict(lambda: defaultdict(list))
        cats = dict((k, defaultdict(list)) for k in self.all_kern_categories)
        for g in [x for x in Glyphs.font.glyphs if self.is_elligable(x)]:
            l = cats.get(g.category, cats.get(g.subCategory, cats['Other']))
            l[g.script].append(self.get_canonincal_kerning_glyph(g.layers[0], side))

        for cat in cats.keys():
            for script in cats[cat].keys():
                cats[cat][script] = self.make_list_unique(cats[cat][script])

        return cats

    def get_string(self, left_g, right_g):
        string = None

        if self.category == 'Quotes':
            cat = left_g.subCategory if left_g.subCategory != 'Other' else left_g.category
            pattern = _kerningStrings.patterns.get(left_g.script, _kerningStrings.patterns.get('latin')).get(cat + '-Quotes', '')
            strings = [pattern.format(right=right_g.name, left=left_g.name, qL=quote_pair[0], qR=quote_pair[1]).replace(' /', '/') for quote_pair in _kerningStrings.quotations]
            string = '  '.join(strings)

        if not string and self.use_real:
            base_name_left, _, suffix_left = left_g.name.partition('.')
            base_name_right, _, suffix_right = right_g.name.partition('.')

            potentials = [
                base_name_left + base_name_right,
                base_name_left + '/' + base_name_right,
                '/' + base_name_left + ' ' + base_name_right,
                '/' + base_name_left + '/' + base_name_right,
            ]
            for s in potentials:
                string = _kerningStrings.strings.get(s)
                if string:
                    break
                print(s)

        if not string:
            pattern = self.get_pattern(left_g, right_g)
            string = pattern.format(right=right_g.name, left=left_g.name).replace(' /', '/')

        if not string:
            string = '/' + left_g.name + '/' + right_g.name

        return string

    def get_category_for_glyph(self, glyph):
        if glyph.category in self.all_kern_categories:
            return glyph.category

        if glyph.subCategory in self.all_kern_categories:
            return glyph.subCategory

        if glyph.subCategory == 'Currancy':
            return 'Number'

        return 'Other'

    def get_pattern(self, main_glyph, other_glyph):
        scripts_patterns = _kerningStrings.patterns.get(main_glyph.script, {})
        # print(self.get_category_for_glyph(main_glyph))
        # print(self.get_category_for_glyph(main_glyph) + '-' + self.get_category_for_glyph(other_glyph), self.all_kern_categories)
        pattern = scripts_patterns.get(self.get_category_for_glyph(main_glyph) + '-' + self.get_category_for_glyph(other_glyph), '')

        if self.category == 'Number':
            suffix = ''.join(main_glyph.name.partition('.')[1:])
        else:
            suffix = ''

        try:
            pattern = pattern.format(
                suffix=suffix,
                left='{left}',
                right='{right}',
            )
        except KeyError:
            pass

        return pattern

    def is_elligable(self, glyph, side='both'):
        if self.ignore_red and glyph.color == 0:
            return False

        if not glyph.export:
            return False

        for vgn in self.verboten[side]:
            if re.match(vgn.replace('.', '\\.').replace('*', '.*'), glyph.name):
                return False
        return True

    def makeitso(self, sender):
        try:
            self.w.close()
        except AttributeError:
            pass
        self.category = self.all_kern_categories[self.w.radioCategories.get()]

        self.use_real = self.w.use_real.get()
        self.use_selection = self.w.use_selected.get()
        self.ignore_red = self.w.ignore_red.get()
        all_strings = []

        if self.category == 'Quotes':
            left_of_string_glyphs = self.make_list_unique([self.get_canonincal_kerning_glyph(sl, 'right') for sl in Glyphs.font.selectedLayers if self.is_elligable(sl.parent, 'right')])
            right_of_string_glyphs = self.make_list_unique([self.get_canonincal_kerning_glyph(sl, 'left') for sl in Glyphs.font.selectedLayers if self.is_elligable(sl.parent, 'left')])
            pairs = zip_longest(left_of_string_glyphs, right_of_string_glyphs)
            for p in pairs:
                gl, gr = p
                if gl is None:
                    gl = gr if gr in left_of_string_glyphs else left_of_string_glyphs[0]
                if gr is None:
                    gr = gl if gl in left_of_string_glyphs else right_of_string_glyphs[0]

                kerning_string = self.get_string(gl, gr)
                if kerning_string not in all_strings:
                    all_strings.append(kerning_string)

        else:
            # Holds kerning key glyphs that have been seen already, to avoid duplicates
            processed_main_glyphs_left = OrderedDict()
            processed_main_glyphs_right = OrderedDict()
            # print([(k, self.categories_rightside[k].keys()) for k in self.categories_rightside.keys()])
            for sl in Glyphs.font.selectedLayers:
                # Process the selected glyph on the left side
                main_g_left = self.get_canonincal_kerning_glyph(sl, 'left')
                pair_strings_left = []
                if self.is_elligable(main_g_left, 'left'):
                    if main_g_left.name not in processed_main_glyphs_left.keys():
                        processed_main_glyphs_left[main_g_left.name] = [sl.parent.name]
                        try:
                            if sl.parent.script:
                                other_glyphs_rightside = self.categories_rightside[self.category].get(sl.parent.script, self.categories_rightside[self.category].get(None))
                            else:
                                other_glyphs_rightside = self.categories_rightside[self.category].get(None, self.categories_rightside[self.category].get('latin'))
                        except KeyError:
                            other_glyphs_rightside = []
                        # print(self.category, self.categories_rightside.keys())
                        print(sl.parent.script, self.category, self.categories_rightside[self.category].keys())

                        for g in other_glyphs_rightside:
                            if not self.is_elligable(g, 'right'):
                                continue
                            other_g = self.get_canonincal_kerning_glyph(g.layers[sl.associatedMasterId], 'right')
                            kerning_string_left = self.get_string(main_g_left, other_g)
                            if kerning_string_left not in pair_strings_left:
                                pair_strings_left.append(kerning_string_left)
                    else:
                        processed_main_glyphs_left[main_g_left.name].append(sl.parent.name)

                    if pair_strings_left:
                        pair_strings_left.insert(0, main_g_left.name)

                # Process the selected glyph on the right side
                main_g_right = self.get_canonincal_kerning_glyph(sl, 'right')
                pair_strings_right = []
                if self.is_elligable(main_g_right, 'right'):
                    if main_g_right.name not in processed_main_glyphs_right.keys():
                        processed_main_glyphs_right[main_g_right.name] = [sl.parent.name]

                        if self.category == 'Quotes':
                            other_glyphs_leftside = [main_g_right]
                            main_g_right = self.get_canonincal_kerning_glyph(sl, 'left')
                        else:
                            if sl.parent.script:
                                other_glyphs_leftside = self.categories_leftside[self.category].get(sl.parent.script, self.categories_leftside[self.category].get(None, []))
                            else:
                                other_glyphs_leftside = self.categories_leftside[self.category].get(None, self.categories_leftside[self.category].get('latin', []))

                        for g in other_glyphs_leftside:
                            if not self.is_elligable(g, 'left'):
                                continue
                            other_g = self.get_canonincal_kerning_glyph(g.layers[sl.associatedMasterId], 'left')
                            kerning_string_right = self.get_string(other_g, main_g_right)
                            if kerning_string_right not in pair_strings_right:
                                pair_strings_right.append(kerning_string_right)
                    else:
                        processed_main_glyphs_right[main_g_right.name].append(sl.parent.name)

                    if pair_strings_right:
                        pair_strings_right.insert(0, main_g_right.name)

                left_string = '  '.join(self.make_list_unique(pair_strings_left))
                right_string = '  '.join(self.make_list_unique(pair_strings_right))
                if all([left_string, right_string]):
                    pair_strings = '\n'.join([left_string, right_string])
                else:
                    pair_strings = left_string or right_string

                # print(':', pair_strings, ':')

                if pair_strings:
                    all_strings.append(pair_strings)

        Glyphs.font.newTab('\n\n'.join(all_strings))
        Glyphs.font.currentTab.previewInstances = 'live'
        Glyphs.font.currentTab.scale = 0.065
        Glyphs.font.currentTab.textCursor = 3
        Glyphs.font.tool = 'TextTool'
        # Glyphs.showMacroWindow()


makeDisplay()
print('Done.')
