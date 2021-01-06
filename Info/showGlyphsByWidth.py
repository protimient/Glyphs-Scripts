# MenuTitle: Show Selected Glyphs Sorted by Width
Glyphs.clearLog()

selectedGlyphs = [l.parent for l in Glyphs.font.selectedLayers]

listedGlyphs = [x[1] for x in sorted([(l.width, '/' + l.parent.name) for l in Glyphs.font.selectedLayers])]

# pre = '/iMatra-deva'
# post = '/reph-deva/ra-deva/eMatra-deva'
pre = ''
post = ''

for gi, g in enumerate(listedGlyphs):
    listedGlyphs[gi] = '{pre}{glyph}{post}'.format(pre=pre, glyph=g, post=post)

joiner = '\n' if pre or post else ' '
string = joiner.join(listedGlyphs)

if string:
    Glyphs.font.newTab(string)
