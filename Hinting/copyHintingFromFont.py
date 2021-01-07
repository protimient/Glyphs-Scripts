# MenuTitle: Copy All Hinting for Selected From Other Font
# -*- coding: utf-8 -*-
__doc__ = """
Copies the hints to the selected glyphs in the front opened font from the other opened font.
"""

import copy
import re

# Glyphs.clearLog()
# Glyphs.showMacroWindow()


def get_values_from_brace_layer(layer_name):
    try:
        this_layer_val = re.search('{(.+)}', layer_name).group(1)
    except AttributeError:
        return None

    return tuple(float(x) for x in this_layer_val.split(','))


if len(Glyphs.fonts) == 2:
    f1 = Glyphs.font
    f2 = [f for f in Glyphs.fonts if f != f1][0]

    for g1 in [l.parent for l in f1.selectedLayers]:
        g2 = f2.glyphs[g1.name]
        if g2 is None:
            print(f1, 'does not contain', g1)
            continue

        for li, l1 in enumerate(g1.layers):
            l2 = None
            if re.search('.*{.*}', l1.name):
                brace_val1 = get_values_from_brace_layer(l1.name)
                for l in g2.layers:
                    if brace_val1 == get_values_from_brace_layer(l.name):
                        l2 = l
                        break
            else:
                for l in g2.layers:
                    if l1.name == l.name:
                        l2 = l
                        break

            if l2 is None:
                try:
                    l2 = g2.layers[li]
                except IndexError:
                    l2 = None

            if l2 is None:
                print('Could not find the layer in the other font', l1)
                continue

            l1.hints = copy.copy(l2.hints)

else:
    print('Two, and only two, fonts can be open.')
