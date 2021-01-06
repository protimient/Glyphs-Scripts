# MenuTitle: Show Selected Glyphs Grouped by Width
from collections import defaultdict
Glyphs.clearLog()

widths = defaultdict(list)
for l in Glyphs.font.selectedLayers:
    widths[int(l.width)].append('/' + l.parent.name)

string = 'Total Widths: {0}\n\n'.format(len(widths))
for width in sorted(widths.keys()):
    x = widths[width]
    string += '{0}: {1}\n'.format(width, '  '.join(x))

if string:
    Glyphs.font.newTab(string)
