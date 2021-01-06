# MenuTitle: Set Kerning Groups for Selected
# -*- coding: utf-8 -*-
__doc__ = """
Sets the left and/or right kerning group to the predefined key.
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

from _kernClasses import kern_classes


class mKeys:
    def __init__(self, font):
        self.glyphDict = {}
        self.font = font
        self.isItalic = self.font.fontMasterAtIndex_(0).italicAngle != 0

    class glyph_kerning:
        def __init__(self, gname):
            self.name = gname
            self.left = None
            self.right = None

    def __call__(self, gname, **kwargs):
        g = self.font.glyphForName_(gname)
        if g:
            ng = self.glyph_kerning(gname)

            if self.isItalic:
                ng.left = kwargs.get('italic_left', kwargs.get('left'))
                ng.right = kwargs.get('italic_right', kwargs.get('right'))
            else:
                ng.left = kwargs.get('left')
                ng.right = kwargs.get('right')

            self.glyphDict[ng.name] = ng

            sc_name = self.make_smallcap_name(gname)
            if gname[0].isupper() and self.font.glyphForName_(sc_name):
                ngsc = self.glyph_kerning(sc_name)
                if ng.right is not None:
                    ngsc.right = self.make_smallcap_name(ng.right)
                if ng.left is not None:
                    ngsc.left = self.make_smallcap_name(ng.left)

                self.glyphDict[ngsc.name] = ngsc

    def make_smallcap_name(self, gn):
        arbitrary_initial_letters_len = 3
        return gn[:arbitrary_initial_letters_len].lower() + gn[arbitrary_initial_letters_len:] + '.sc'

    def get_ligature_keys(self, gname):
        left, right = (None, None)
        if '_' in gname:
            main_name, x, suffix = gname.partition('-')
            gn_parts = main_name.split('_')
            first_gn = gn_parts[0] + '-' + suffix
            last_gn = gn_parts[-1] + '-' + suffix
            first_g = Glyphs.font.glyphs[first_gn]
            last_g = Glyphs.font.glyphs[last_gn]
            print(first_gn, last_g)
            if first_g is not None:
                left = first_g.leftKerningGroup
                if left is None:
                    left = self.glyphDict.get(first_gn)

            if last_g is not None:
                right = last_g.rightKerningGroup
                if right is None:
                    right = self.glyphDict.get(last_gn)

        self.__call__(gname, left=left, right=right)
        return left, right


grouping = mKeys(Glyphs.font)
for gn, kwargs in kern_classes:
    grouping(gn, **kwargs)


for gn in [x.parent.name for x in Glyphs.font.selectedLayers]:
    g = grouping.glyphDict.get(gn)
    if g is None and '_' in gn:
        grouping.get_ligature_keys(gn)
        g = grouping.glyphDict.get(gn)

    if g:
        Glyphs.font.glyphs[g.name].leftKerningGroup = g.left
        Glyphs.font.glyphs[g.name].rightKerningGroup = g.right
