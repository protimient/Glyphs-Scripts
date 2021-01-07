# MenuTitle: Print name and unicode of selected as Python
# -*- coding: utf-8 -*-
__doc__ = """
Prints the name and unicode of selected glyphs as a python list.
"""

Glyphs.clearLog()

print('unicodes = [')
for g in [x.parent for x in Glyphs.font.selectedLayers]:
    string = '\t0x{gunicode}, \t# {gname}'
    if g.unicode is None:
        string = '\t{gunicode}, \t# {gname}'

    print(string.format(
        gname=g.name,
        gunicode=g.unicode,
    ))
print(']')

Glyphs.showMacroWindow()
