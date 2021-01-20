# MenuTitle: Add Brace/Bracket trick Layers...
# -*- coding: utf-8 -*-
__doc__ = """
Open tab containing Kerning strings for the selected glyphs.
"""

import os
import copy
from collections import OrderedDict

from vanilla import (
    Window,
    TextBox,
    RadioGroup,
    Button,
    PopUpButton,
    EditText,
)

Glyphs.clearLog()
# Glyphs.showMacroWindow()


class makeDisplay(object):
    def __init__(self):
        self.all_layer_combos = self.get_all_layer_combos()
        self.instance_values = self.get_instance_values()
        item_height = 24.0
        w_width = 300.0
        w_height = item_height * 10
        margin = 10
        next_y = margin
        col_1_width = w_width - (margin * 2)
        col_2_width = (w_width / 2) - (margin * 1.5)
        item_height = 24

        radio_height = 20 * 2
        self.get_prefs('addBraceLayers.pref')

        self.w = Window((w_width, w_height), "Add Layers")

        self.w.text_1 = TextBox((margin, next_y, col_1_width, item_height), "Layer Combinations:", sizeStyle='regular')
        next_y += item_height
        self.w.parent_layers = PopUpButton((margin, next_y, col_1_width, item_height), self.all_layer_combos, sizeStyle='regular')
        self.set_all_layer_combos()
        next_y += item_height + margin

        self.w.brace_or_bracket = RadioGroup((margin, next_y, col_1_width, radio_height), ['Bracket Layer [X]', 'Brace Layer {X}'], sizeStyle='regular')
        self.w.brace_or_bracket.set(int(self.prefs.get('brace_or_bracket', 0)))
        next_y += radio_height + margin

        self.w.text_2 = TextBox((margin, next_y, col_1_width, item_height), "Layer Value:", sizeStyle='regular')
        next_y += item_height
        self.w.layer_value = EditText((margin, next_y, col_2_width, item_height), '', sizeStyle='small', placeholder='e.g. 700')
        self.w.instance_value_popup = PopUpButton((margin + margin + col_2_width, next_y, col_2_width, item_height), self.instance_values, sizeStyle='regular', callback=self.changeinstance_value)
        next_y += item_height + margin
        if self.prefs.get('layer_value') is not None:
            self.w.layer_value.set(self.prefs.get('layer_value'))

        self.w.gobutton = Button((margin + (col_1_width / 4), next_y, col_1_width / 2, item_height), 'Add Layers', callback=self.makeitso)

        self.w.setDefaultButton(self.w.gobutton)
        self.w.center()
        self.w.open()
        # self.makeitso(None)

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

    def get_all_layer_combos(self):
        master_combos = OrderedDict()
        for mi, m in enumerate(Glyphs.font.masters):
            try:
                next_m = Glyphs.font.masters[mi + 1]
                if not next_m:
                    break
                combo_tup = (m, next_m)
                master_combos['{}-{}'.format(*[x.name for x in combo_tup])] = combo_tup
            except IndexError:
                break

        return master_combos

    def set_all_layer_combos(self):
        selection_index = Glyphs.font.masterIndex
        if selection_index >= len(self.all_layer_combos):
            selection_index = len(self.all_layer_combos) - 1
        self.w.parent_layers.set(selection_index)

    def get_instance_values(self):
        return [''] + [', '.join([str(x) for x in list(i.axes)]) for i in Glyphs.font.instances]

    def changeinstance_value(self, sender):
        self.w.layer_value.set(sender.getItem())

    def makeitso(self, sender):
        try:
            self.w.close()
        except AttributeError:
            pass

        parent_layers = self.w.parent_layers.getItem()
        brace_or_bracket = self.w.brace_or_bracket.get()
        layer_value = float(self.w.layer_value.get().strip())
        if int(layer_value) - layer_value == 0:
            layer_value = int(layer_value)

        self.set_prefs(
            parent_layers=parent_layers,
            brace_or_bracket=brace_or_bracket,
            layer_value=layer_value,
        )

        layer_name_template = '{master_name} {{{layer_value}}}' if brace_or_bracket else '{master_name} [{layer_value}]'

        master_names = parent_layers.split('-')
        masters = [m for m in Glyphs.font.masters if m.name in master_names]

        for sl in Glyphs.font.selectedLayers:
            g = sl.parent

            for m in masters:
                newL = copy.copy(g.layers[m.id])
                newL.layerId = None
                newL.associatedMasterId = m.id
                newL.name = layer_name_template.format(
                    master_name=m.name,
                    layer_value=layer_value,
                )
                g.layers.append(newL)

        # Glyphs.showMacroWindow()


makeDisplay()
print('Done.')
