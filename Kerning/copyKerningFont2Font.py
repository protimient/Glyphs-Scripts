# MenuTitle: Copy Kerning Font2Font
# -*- coding: utf-8 -*-
__doc__ = """
Copies the entire kerning dictionary to the current font from the other opened font. Only 2 fonts can be open.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

if len(Glyphs.fonts) == 2:
    for fi, f in enumerate(Glyphs.fonts):
        if f == Glyphs.font:
            thisFont = f
            otherFont = Glyphs.fonts[abs(fi - 1)]
            break

    thisFont.disableUpdateInterface()  # suppresses UI updates in Font View
    thisFont.kerning = otherFont.kerning
    thisFont.enableUpdateInterface()  # re-enables UI updates in Font View
    print('Done.')
else:
    Glyphs.showNotification('Copy Kerning Font2Font', '2 and only 2 fonts can be open!')
