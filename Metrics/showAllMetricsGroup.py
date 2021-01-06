# MenuTitle: Show all Metrics group members
# -*- coding: utf-8 -*-
__doc__ = """
Opens a tab with all glyphs that share a KeyMetric with the glyphs in the current selection.
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

lefts = dict((g.parent.leftMetricsKey, [g.parent.leftMetricsKey]) for g in Glyphs.font.selectedLayers if g.parent.leftMetricsKey)
rights = dict((g.parent.rightMetricsKey, [g.parent.rightMetricsKey]) for g in Glyphs.font.selectedLayers if g.parent.rightMetricsKey)

for g in Glyphs.font.glyphs:
    try:
        lefts[g.leftMetricsKey].append(g.name)
    except KeyError:
        pass

    try:
        rights[g.rightMetricsKey].append(g.name)
    except KeyError:
        pass


strings = []
strings.append('Leftside Metrics Group(s):\n' + '\n'.join(['  '.join(map(lambda x: '/' + x, gn)) for gn in sorted(lefts.values())]))
strings.append('Rightside Metrics Group(s):\n' + '\n'.join(['  '.join(map(lambda x: '/' + x, gn)) for gn in sorted(rights.values())]))


string = '\n\n'.join(strings)

if string:
    Glyphs.font.newTab(string)
