# MenuTitle: Add brace layers from component
# -*- coding: utf-8 -*-
__doc__ = """
Adds the selected component or the first component's brace layers to each selected glyph.
"""

import copy

Glyphs.clearLog()
# Glyphs.showMacroWindow()


class addBraceLayers(object):
    def __init__(self):
        self.makeitso()

    def makeitso(self):
        Glyphs.font.disableUpdateInterface()

        for sl in Glyphs.font.selectedLayers:
            this_g = sl.parent
            if not sl.selection:
                try:
                    c = sl.components[0]
                except IndexError:
                    continue
            else:
                try:
                    c = [x for x in sl.selection if type(x) == GSComponent][0]
                except IndexError:
                    continue
            if not c:
                continue

            parent_g = c.component

            added_layers = []
            for l in parent_g.layers:
                if not this_g.layers[l.name]:
                    this_master = this_g.layers[l.associatedMasterId]
                    newL = copy.copy(this_master)
                    newL.name = l.name
                    newL.associatedMasterId = l.associatedMasterId
                    added_layers.append(newL)
                    this_g.layers.append(newL)

            for l in added_layers:
                l.reinterpolate()
        Glyphs.font.enableUpdateInterface()


addBraceLayers()
