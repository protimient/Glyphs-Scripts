# MenuTitle: Print Selected Dependant Glyphs
# -*- coding: utf-8 -*-
__doc__ = """
Prints the glyph names of the selected glyphs and any glyphs used as components.
"""

Glyphs.clearLog()
Glyphs.showMacroWindow()


def get_component_components(l):
    temp = []

    if l is not None:
        lid = l.layerId
        for c in l.components:
            temp.append(c)
            temp += get_component_components(c.component.layers[lid])

    return temp


names = set()
for g in [l.parent for l in Glyphs.font.selectedLayers]:
    for l in g.layers:
        names.add(l.parent.name)
        names |= set([x.name for x in get_component_components(l)])

print('\n'.join(names))
