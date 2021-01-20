
# MenuTitle: Slant Component Positions
# -*- coding: utf-8 -*-
__doc__ = """
Moves the components to the position they would be in if slanted, without actually slanting them.
"""

import os
import math
from vanilla import TextBox, Button, EditText, Window, CheckBox

Glyphs.clearLog()
# Glyphs.showMacroWindow()


class replaceNamedComponent:
    def __init__(self):
        item_height = 24.0
        margin = 10
        w_width = 350.0
        w_height = (item_height * 5) + margin
        next_y = margin
        col_1_width = w_width - (margin * 2)
        item_height = 24

        self.get_prefs('SlantComponentPositions.pref')

        self.w = Window((w_width, w_height), "Slant Angle")

        self.w.slant_angle_text = TextBox((margin, next_y + 2, col_1_width, item_height), "Slant Angle:", sizeStyle='regular')
        next_y += item_height
        self.w.slant_angle = EditText((margin, next_y, col_1_width, item_height), self.prefs.get('slant_angle', ''))
        next_y += item_height + margin

        self.w.slant_all_layers = CheckBox((margin, next_y, col_1_width, item_height), "Slant All Layers", value=int(self.prefs.get('slant_all_layers')), sizeStyle='regular')
        next_y += item_height + margin

        self.w.makeitso = Button((w_width / 4.0, next_y, col_1_width / 2.0, item_height), 'Slant Components', callback=self.makeitso)
        self.w.setDefaultButton(self.w.makeitso)

        self.w.open()
        self.w.center()

    def get_prefs(self, filename):
        self.pref_folder = os.path.expanduser('~/Library/Application Support/Glyphs/Prefs')
        self.pref_filepath = os.path.join(self.pref_folder, filename)
        self.prefs = {}
        if os.path.exists(self.pref_filepath):
            with open(self.pref_filepath) as f:
                preflines = f.readlines()
            self.prefs = dict(line.split('\t') for line in preflines if line[0] != '#' and line.strip())

    def set_prefs(self, **kwargs):
        try:
            if not os.path.exists(self.pref_folder):
                os.makedirs(self.pref_folder)

            pref_string = '\n'.join(['\t'.join(str(b) for b in a) for a in kwargs.items()])
            with open(self.pref_filepath, 'w') as f:
                f.write(pref_string)
        except AttributeError:
            print('The Preference filename has not been set.')

    def get_reference_point(self, selection, layer=None):
        return self.get_center_of_selection(selection)
        # return NSPoint(self.get_obj_center(layer).x, Glyphs.font.selectedFontMaster.xHeight / 2)

    def get_obj_center(self, obj):
        return NSPoint(obj.bounds.origin.x + (obj.bounds.size.width / 2), obj.bounds.origin.y + (obj.bounds.size.height / 2))

    def get_center_of_selection(self, selection):
        all_points = []
        for obj in selection:
            try:
                all_points.append(self.get_obj_center(obj))
            except AttributeError:
                all_points.append(obj.position)

        all_xs = [x.x for x in all_points]
        all_ys = [x.x for x in all_points]

        x_average = sum(all_xs) / len(all_xs)
        y_average = sum(all_ys) / len(all_ys)

        return NSPoint(int(x_average), int(y_average))

    def makeitso(self, sender):
        self.w.close()
        slant_all_layers = self.w.slant_all_layers.get()
        # print(slant_all_layers, type(slant_all_layers))
        try:
            slant_angle = float(self.w.slant_angle.get())
        except TypeError:
            Glyphs.showNotification('Slant Component Positions', 'The slant angle was not a number!')
            return

        self.set_prefs(
            slant_angle=slant_angle,
            slant_all_layers=slant_all_layers
            )

        if not Glyphs.font.selectedLayers:
            return
        
        for sl in Glyphs.font.selectedLayers:
            if slant_all_layers:
                layers = [l for l in sl.parent.layers]
            else:
                layers = [sl]

            for l in layers:
                comps = [c for c in l.components if c.selected] or [c for c in l.components]
                if not comps:
                    Glyphs.showNotification('Slant Component Positions', 'You haven\'t selected any Components!')
                    return

                reference_point = self.get_reference_point(comps, l)
                for c in comps:
                    x_shift = math.tan(math.radians(slant_angle)) * (self.get_obj_center(c).y - reference_point.y)
                    c.position = NSPoint(c.position.x + x_shift, c.position.y)


replaceNamedComponent()
