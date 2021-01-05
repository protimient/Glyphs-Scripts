# MenuTitle: Show All Accents
# -*- coding: utf-8 -*-
__doc__ = """
Opens a new tab listing all accents in the whole font and the glyphs that use them as a component.
"""

accents = {}
for g in Glyphs.font.glyphs:
    for l in g.layers:
        try:
            if '_' in [x[0] for x in l.anchors.keys()]:
                accents[g.name] = set()
        except TypeError:
            pass

for g in Glyphs.font.glyphs:
    for l in g.layers:
        try:
            for c in l.components:
                if c.componentName in accents.keys():
                    accents[c.componentName].add(g.name)
        except TypeError:
            raise
            pass

strings = []
for a, gs in accents.items():
    strings.append('/{0}  /{1}'.format(a, '/'.join(sorted(gs))))

string = '\n'.join(strings)
Glyphs.font.newTab(string)
