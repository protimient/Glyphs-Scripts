# MenuTitle: Display all kerning group members
# -*- coding: utf-8 -*-
__doc__ = """
Opens a tab containing all the members of the currently selected glyphs kerning groups.
"""
Glyphs.clearLog()
# Glyphs.showMacroWindow()


lefts = dict((g.parent.leftKerningGroup, []) for g in Glyphs.font.selectedLayers if g.parent.leftKerningGroup)
rights = dict((g.parent.rightKerningGroup, []) for g in Glyphs.font.selectedLayers if g.parent.rightKerningGroup)

for g in Glyphs.font.glyphs:
    try:
        lefts[g.leftKerningGroup].append(g.name)
    except KeyError:
        pass

    try:
        rights[g.rightKerningGroup].append(g.name)
    except KeyError:
        pass


# thisGlyph = Glyphs.font.selectedLayers[0].parent
# leftGroup = ['/' + g.name for g in Glyphs.font.glyphs if g.leftKerningGroup == thisGlyph.leftKerningGroup]
# rightGroup = ['/' + g.name for g in Glyphs.font.glyphs if g.rightKerningGroup == thisGlyph.rightKerningGroup]

# print rightGroup


strings = []
strings.append('Leftside Kerning Group(s):\n' + '\n'.join(['  '.join(map(lambda x: '/' + x, gn)) for gn in sorted(lefts.values())]))
strings.append('Rightside Kerning Group(s):\n' + '\n'.join(['  '.join(map(lambda x: '/' + x, gn)) for gn in sorted(rights.values())]))


string = '\n\n'.join(strings)

if string:
    Glyphs.font.newTab(string)
