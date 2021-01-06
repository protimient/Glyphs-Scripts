# MenuTitle: Compare Classes
# -*- coding: utf-8 -*-
__doc__ = """
Compares the kerning groups in all glyphs in the front font with the other opened fonts.
Any glyphs with differences are coloured accordingly.
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

key_font = Glyphs.font
# key_font = max(Glyphs.fonts, key=lambda x: len(x.glyphs))

class_dict = dict((g.name, (g.leftKerningGroup, g.rightKerningGroup)) for g in key_font.glyphs)

for f in Glyphs.fonts:

    for g in f.glyphs:
        if f == key_font:
            g.color = 9223372036854775807
            continue

        key_classes = class_dict.get(g.name)
        if key_classes is not None:
            if key_classes[0] != g.leftKerningGroup and key_classes[1] != g.rightKerningGroup:
                g.color = 9
                # Pink - Both sides are different
            elif key_classes[0] != g.leftKerningGroup:
                g.color = 6
                # Blue - Left side class is different
            elif key_classes[1] != g.rightKerningGroup:
                g.color = 2
                # Brown - Right side class is different
            else:
                g.color = 9223372036854775807

print('Orange - Right side class is different')
print('Blue - Left side class is different')
print('Brown - Both sides are different')
