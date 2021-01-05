# MenuTitle: Display Non Grouped Kerning
# -*- coding: utf-8 -*-
__doc__ = """
Displays glyphs in the selection that do not have a kerning group.
"""
Glyphs.clearLog()


leftGroup = []
rightGroup = []

for l in Glyphs.font.selectedLayers:
    if not l.parent.rightKerningGroup:
        rightGroup.append('/' + l.parent.name)

    if not l.parent.leftKerningGroup:
        leftGroup.append('/' + l.parent.name)


strings = []
strings.append('No Left Kerning Group:\n' + ' '.join(leftGroup))
strings.append('No Right Kerning Group:\n' + ' '.join(rightGroup))


string = '\n\n'.join(strings)

if string:
    Glyphs.font.newTab(string)
