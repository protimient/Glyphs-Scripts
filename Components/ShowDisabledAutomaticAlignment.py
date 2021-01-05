# MenuTitle: Show Disabled Automatic Alignment
# -*- coding: utf-8 -*-
__doc__ = """
Opens a new tab with all glyphs containing components where automatic alignment is disabled.
"""

# from collections import defaultdict

# Glyphs.clearLog()
# Glyphs.showMacroWindow()


def sort_layers(l):
    return l.parent.name, [m.id for m in Glyphs.font.masters].index(l.associatedMasterId)


these_layers = [l for g in Glyphs.font.glyphs for l in g.layers for c in l.components if not c.automaticAlignment]
these_layers = sorted(set(these_layers), key=sort_layers)

Glyphs.font.newTab()
Glyphs.font.tabs[-1].layers = these_layers
