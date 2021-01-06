# MenuTitle: Copy Metrics to Selected From a font...
# -*- coding: utf-8 -*-
__doc__ = """
Copies the metrics from another font or layer to the currently selected master in the selected glyphs.
"""

import os
from vanilla import (
    Window,
    TextBox,
    Button,
    # EditText,
    PopUpButton,
    # CheckBox,
    RadioGroup,
    # TextEditor,
    # Sheet,
)
__doc__ = """
Copies the metrics from the chosen font layer to the selected layer.
"""
Glyphs.clearLog()
# Glyphs.showMacroWindow()


class copyMetrics(object):
    def __init__(self):
        item_height = 24.0
        w_width = 500.0
        w_height = item_height * 12
        margin = 10
        next_y = margin
        col_1_width = w_width - (margin * 2)
        item_height = 24

        self.get_prefs('copyMetricsFromFont.pref')

        self.available_layers = dict(('{} - {}'.format(os.path.basename(font.filepath), master), master) for font in Glyphs.fonts for master in font.masters)

        self.w = Window((w_width, w_height), "Copy Metrics")

        self.w.hText_2 = TextBox((margin, next_y, col_1_width, item_height), "Copy metrics from this font/layer:", sizeStyle='regular')
        next_y += item_height
        self.w.available_layers = PopUpButton((margin, next_y, col_1_width, item_height), sorted(self.available_layers.keys()))  # , callback=self.update_brace_value)
        next_y += item_height + margin
        metrics_options = [
            'Left sidebearing Only',
            'Right sidebearing Only',
            'Width Only (keep LSB)',
            'Width Only (assign proportionally)',
            "Left sidebearing and Width",
            "Left sidebearing and Right sidebearing",
            'Width and Right sidebearing',
        ]
        self.w.metrics_to_copy = RadioGroup((margin, next_y, col_1_width, item_height * len(metrics_options)), metrics_options)
        self.w.metrics_to_copy.set(int(self.prefs.get('metrics_to_copy', 0)))
        next_y += item_height * len(metrics_options) + margin

        self.w.gobutton = Button((margin + (col_1_width / 4), next_y, col_1_width / 2, item_height), 'Copy Metrics', callback=self.makeitso)
        next_y += item_height

        self.w.setDefaultButton(self.w.gobutton)
        self.w.open()

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

    def makeitso(self, sender):
        metrics_to_copy_mode = self.w.metrics_to_copy.get()

        self.set_prefs(metrics_to_copy=metrics_to_copy_mode)

        selected_layer_name = self.w.available_layers.getItem()
        source_master = self.available_layers[selected_layer_name]

        for l in Glyphs.font.selectedLayers:
            gname = l.parent.name
            corresponding_glyph = source_master.font.glyphs[gname]
            if corresponding_glyph is None:
                continue

            corresponding_layer = corresponding_glyph.layers[source_master.id]

            print(l.LSB, l.width, l.RSB)
            print(corresponding_layer.LSB, corresponding_layer.width, corresponding_layer.RSB)

            if metrics_to_copy_mode == 0:
                l.LSB = corresponding_layer.LSB

            elif metrics_to_copy_mode == 1:
                l.RSB = corresponding_layer.RSB

            elif metrics_to_copy_mode == 2:
                l.width = corresponding_layer.width

            elif metrics_to_copy_mode == 3:
                diff = (corresponding_layer.width - l.width) / 2
                l.LSB += diff
                l.width = corresponding_layer.width

            elif metrics_to_copy_mode == 4:
                l.LSB = corresponding_layer.LSB
                l.width = corresponding_layer.width

            elif metrics_to_copy_mode == 5:
                l.LSB = corresponding_layer.LSB
                l.RSB = corresponding_layer.RSB

            elif metrics_to_copy_mode == 6:
                l.RSB = corresponding_layer.RSB
                l.width = corresponding_layer.width
            print(l.LSB, l.width, l.RSB)

        self.w.close()


copyMetrics()
