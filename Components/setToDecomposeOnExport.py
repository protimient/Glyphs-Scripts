# MenuTitle: Set to Decompose on Export
# -*- coding: utf-8 -*-
__doc__ = """
Sets the selected glyph(s) to decompose on export via a custom parameter.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

decomposables = tuple(sorted(set([l.parent.name for l in Glyphs.font.selectedLayers])))

for inst in Glyphs.font.instances:
    if inst.customParameters['Decompose Glyphs'] is None:
        inst.customParameters['Decompose Glyphs'] = decomposables
    else:
        inst_decomposables = tuple(gn for gn in decomposables if gn not in inst.customParameters['Decompose Glyphs'])
        inst.customParameters['Decompose Glyphs'] += inst_decomposables
