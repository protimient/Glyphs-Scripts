# MenuTitle: Convert Class Spaces to Newlines
# -*- coding: utf-8 -*-
__doc__ = """
Convert the Spaces in each class to Newlines, effectively converting it from a row into a column.
"""

Glyphs.clearLog()
Glyphs.showMacroWindow()

for c in Glyphs.font.classes:
    class_lines = c.code.split('\n')
    class_lines = [cl.strip().replace(' ', '\n') if '#' not in cl else cl.strip() for cl in class_lines]
    Glyphs.font.classes[c.name] = '\n'.join(class_lines)
