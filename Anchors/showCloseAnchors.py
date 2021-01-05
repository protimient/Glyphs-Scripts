# MenuTitle: Show Close Anchors
# -*- coding: utf-8 -*-
__doc__ = """
Checks every glyph in the font and shows them if their anchors are closely placed but not exact.
"""

from collections import defaultdict
Glyphs.clearLog()
Glyphs.showMacroWindow()

selectedMaster = Glyphs.currentDocument.selectedFontMaster()

fuzziness = 10  # This sets the proximity of anchors in font units.

Glyphs.font.disableUpdateInterface()

anchors_grouping = defaultdict(lambda: defaultdict(list))
for g in [x for x in Glyphs.font.glyphs if x.export]:
    l = g.layers[selectedMaster.id]
    if l.paths:
        for a in l.anchors:
            if not a.name.startswith('#') and not a.name.startswith('_#'):
                anchors_grouping[a.name][(a.x, a.y)].append(g)

for anchor_name, anchor_coords in anchors_grouping.items():
    coordinates = sorted(anchor_coords.keys())
    coord_clusters = defaultdict(set)
    for this_coord in coordinates:
        is_set = False
        for coord in coord_clusters.keys():
            minmax_x, minmax_y = coord
            min_x, max_x = minmax_x
            min_y, max_y = minmax_y
            if min_x < this_coord[0] < max_x and min_y < this_coord[1] < max_y:
                coord_clusters[coord] |= set(anchor_coords[this_coord])
                is_set = True
                break

        if not is_set:
            for other_coord in coordinates:
                if this_coord[0] != other_coord[0] and this_coord[1] != other_coord[1]:
                    if (abs(this_coord[0] - other_coord[0]) < fuzziness) and (abs(this_coord[1] - other_coord[1]) < fuzziness):
                        min_x = (this_coord[0] + other_coord[0] - fuzziness) / 2
                        max_x = (this_coord[0] + other_coord[0] + fuzziness) / 2
                        min_y = (this_coord[1] + other_coord[1] - fuzziness) / 2
                        max_y = (this_coord[1] + other_coord[1] + fuzziness) / 2
                        coord = ((min_x, max_x), (min_y, max_y))
                        coord_clusters[coord] |= set(anchor_coords[this_coord])

    strings = []
    for cluster in coord_clusters.values():
        if len(cluster) > 1:
            glyph_string = ''.join(['/' + g.name for g in cluster])
            strings.append(glyph_string)

    if strings:
        string = anchor_name + '\n' + '\n'.join(strings)
        Glyphs.font.newTab(string)

# for coordi, this_coord in enumerate(coordinates):
# 	try:
# 		next_coord = coordinates[coordi + 1]
# 		if this_coord[0] != next_coord[0] and this_coord[1] != next_coord[1] and this_coord[2] == next_coord[2]:
# 			if (abs(this_coord[0] - next_coord[0]) < fuzziness) and (abs(this_coord[1] - next_coord[1]) < fuzziness):
# 				print(this_coord, next_coord, anchors_grouping[this_coord], anchors_grouping[next_coord])
# 				strings[this_coord[2]].append('{0} -{1}\n'.format(''.join(['/' + x.name for x in anchors_grouping[this_coord]]), ''.join(['/' + x.name for x in anchors_grouping[next_coord]])))
# 	except IndexError:
# 		pass

# for anchor_name, glyph_name_strings in strings.items():
# 	string = anchor_name + '\n' + ''.join(glyph_name_strings)
# 	Glyphs.font.newTab(string)

Glyphs.font.enableUpdateInterface()
