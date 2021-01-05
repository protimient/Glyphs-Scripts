# MenuTitle: Copy Smart Component Settings to other layers
# -*- coding: utf-8 -*-
__doc__ = """
For each smart component on the current layer, copies the settings to the respective smart component on the other layers.
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

for l in Glyphs.font.selectedLayers:
    g = l.parent
    for c in l.components:
        if c.smartComponentValues:
            part_glyph = Glyphs.font.glyphs[c.componentName]
            for axis in part_glyph.smartComponentAxes:
                try:
                    this_value = c.smartComponentValues[axis.name]
                except KeyError:
                    print(g, c, c.smartComponentValues)
                    raise

                for l_other in g.layers:
                    if l_other != l:
                        for c_other in l_other.components:
                            if c_other.componentName == c.componentName:
                                c_other.smartComponentValues[axis.name] = this_value
