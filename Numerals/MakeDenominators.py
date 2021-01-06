# MenuTitle: Make Denominators from Numerators
# -*- coding: utf-8 -*-
__doc__ = """
Adds the Denominator glyphs to the font as composite glyphs using the Numerators as vertically shifted components.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

suffixes = ('.numr', '.dnom')
Glyphs.font.disableUpdateInterface()

layers_number = range(len(Glyphs.font.glyphs[0].layers))

important_glyphs = (
    'one',
    'two',
    'four',
    'seven',
)
important_glyphs = [x + suffixes[0] for x in important_glyphs]

theseGlyphs = [g for g in Glyphs.font.glyphs if g.name.endswith(suffixes[0])]

measure_glyph = False
for gn in important_glyphs:
    measure_glyph = Glyphs.font.glyphs[gn]
    if measure_glyph is not None:
        if all([bool(l.paths) for l in measure_glyph.layers]):
            break

if measure_glyph:
    for numr_g in theseGlyphs:
        dnom_g = Glyphs.font.glyphs[numr_g.name.replace(suffixes[0], suffixes[1])]

        if not dnom_g:
            dnom_g = GSGlyph(numr_g.name.replace(suffixes[0], suffixes[1]))
            Glyphs.font.glyphs.append(dnom_g)

        if numr_g and dnom_g:
            for li, numr_l in enumerate(numr_g.layers):
                offset = -(measure_glyph.layers[li].bounds.origin.y)
                print(measure_glyph)
                comp = GSComponent(numr_g.name)
                comp.automaticAlignment = False
                comp.position = NSPoint(0, offset)
                dnom_g.layers[li].components = [comp]

                dnom_g.layers[li].LSB = numr_l.LSB
                dnom_g.layers[li].RSB = numr_l.RSB

            dnom_g.leftMetricsKey = numr_g.name
            dnom_g.rightMetricsKey = numr_g.name
else:
    print('You are missing some key numerator glyphs!')

Glyphs.font.enableUpdateInterface()
