# MenuTitle: Correct Transformed Components
# -*- coding: utf-8 -*-
__doc__ = """
Searches all glyphs for any component with a transformation other than shift, and sets it to decompose on export if found.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()

decomposables = set()
for g in Glyphs.font.glyphs:
    deco = False
    for l in g.layers:
        if l.components:
            for c in l.components:
                if [x for x in c.transform[:-2]] != [1.0, 0.0, 0.0, 1.0]:
                    decomposables.add(g.name)

            if g.category == 'Mark':
                decomposables.add(g.name)

g = Glyphs.font.glyphs['i']
if any([c for l in g.layers for c in l.components]):
    decomposables.add(g.name)

g = Glyphs.font.glyphs['j']
if any([c for l in g.layers for c in l.components]):
    decomposables.add(g.name)

if decomposables:
    for inst in Glyphs.font.instances:
        inst.customParameters['Decompose Glyphs'] = tuple(decomposables)


Glyphs.font.enableUpdateInterface()
