# MenuTitle: Display Unlocked Kerning
# -*- coding: utf-8 -*-
__doc__ = """
Opens a tab showing all kerning exceptions for all layers.
"""

from collections import defaultdict
Glyphs.clearLog()

kernDict = Glyphs.font.kerningDict()

leftGroups = defaultdict(list)
rightGroups = defaultdict(list)

for g in Glyphs.font.glyphs:
    if g.rightKerningGroup:
        group_name = '@MMK_L_{0}'.format(g.rightKerningGroup)
        leftGroups[group_name].append(g.name)

    if g.leftKerningGroup:
        group_name = '@MMK_R_{0}'.format(g.leftKerningGroup)
        rightGroups[group_name].append(g.name)


all_kerning_groups = dict(leftGroups.items() + rightGroups.items())

# make glyphname:groupname dictionaries
left_members = dict((item, group) for group, sublist in leftGroups.items() for item in sublist)
right_members = dict((item, group) for group, sublist in rightGroups.items() for item in sublist)

affected_layers = []
for mi, m in enumerate(Glyphs.font.masters):
    mi += 1
    # strings[m.id] = set()
    for left in kernDict[m.id].keys():
        for gn in kernDict[m.id][left].keys():
            if left in left_members.keys():
                try:
                    affected_layers.append(Glyphs.font.glyphs[left].layers[m.id])
                    affected_layers.append(Glyphs.font.glyphs[all_kerning_groups[gn][0]].layers[m.id])
                    affected_layers.append(GSControlLayer(0x0020))
                    # strings[m.id].add('/{0}/{1}'.format(left, all_kerning_groups[gn][0]))
                except (KeyError, AttributeError):
                    affected_layers.append(Glyphs.font.glyphs[left].layers[m.id])
                    affected_layers.append(Glyphs.font.glyphs[gn].layers[m.id])
                    affected_layers.append(GSControlLayer(0x0020))

            elif gn in right_members.keys():
                try:
                    affected_layers.append(Glyphs.font.glyphs[all_kerning_groups[left][0]].layers[m.id])
                    affected_layers.append(Glyphs.font.glyphs[gn].layers[m.id])
                    affected_layers.append(GSControlLayer(0x0020))
                except (KeyError, AttributeError):
                    affected_layers.append(Glyphs.font.glyphs[left].layers[m.id])
                    affected_layers.append(Glyphs.font.glyphs[gn].layers[m.id])
                    affected_layers.append(GSControlLayer(0x0020))
    affected_layers.append(GSControlLayer(10))

Glyphs.font.newTab()
Glyphs.font.tabs[-1].layers = affected_layers
