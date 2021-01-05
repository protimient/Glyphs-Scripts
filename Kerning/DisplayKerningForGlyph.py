# MenuTitle: Display Kerning for Glyph
# -*- coding: utf-8 -*-
__doc__ = """
When a glyph is selected, this will open a new tab listing all the glyphs it kerns with.
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()


def getKeyGlyph(groupName, side=None):
    if groupName.startswith('@MMK_'):
        groupName = groupName[7:]
    else:
        return Glyphs.font.glyphForId_(groupName)

    gx = Glyphs.font.glyphs[groupName]

    if not gx:
        if side == 'right':
            for g in Glyphs.font.glyphs:
                if g.rightKerningGroup == groupName:
                    return g

        elif side == 'left':
            for g in Glyphs.font.glyphs:
                if g.leftKerningGroup == groupName:
                    return g

    return gx


l = Glyphs.font.selectedLayers[0]
g = l.parent
gn = g.name
lid = l.layerId

leftGroup = g.leftKerningGroup
rightGroup = g.rightKerningGroup

if not leftGroup:
    leftGroup = g.id
else:
    leftGroup = '@MMK_R_' + leftGroup

if not rightGroup:
    rightGroup = g.id
else:
    rightGroup = '@MMK_L_' + rightGroup

try:
    rightSideGlyphNames = [getKeyGlyph(grn, side='left').name for grn in Glyphs.font.kerning[lid][rightGroup].keys()]
except AttributeError:
    rightSideGlyphNames = None

leftSideGlyphNames = []
for lgn, rs in Glyphs.font.kerning[lid].iteritems():
    if leftGroup in rs:
        leftSideGlyphNames.append(getKeyGlyph(lgn, side='right').name)

leftString = '* No Right side kerning *'
rightString = '* No Left side kerning *'
if rightSideGlyphNames:
    leftString = '  '.join(map(lambda x: '/{1}/{0}'.format(x, gn), rightSideGlyphNames))

if leftSideGlyphNames:
    rightString = '  '.join(map(lambda x: '/{0}/{1}'.format(x, gn), leftSideGlyphNames))

string = '/' + gn + '\n\n' + leftString + '\n\n' + rightString

if string:
    Glyphs.font.newTab(string)
