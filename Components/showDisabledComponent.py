# MenuTitle: Show Current Glyph with Disabled Alignment in Composites
# -*- coding: utf-8 -*-
__doc__ = """
Opens a new tab with all glyphs containing the current glyph as a component where automatic alignment is disabled.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

try:
    current_g = Glyphs.font.selectedLayers[0].parent
except (IndexError, AttributeError):
    current_g = None

show_layers = []
is_used = False

if current_g:
    for g in Glyphs.font.glyphs:
        for l in g.layers:
            for c in l.components:
                if c.name == current_g.name:
                    is_used = True
                    if not c.automaticAlignment:
                        show_layers.append(l)
                        break


# layers_to_show = []
# for x in show_layers:
#     layers_to_show += [GSControlLayer(10)]
#     layers_to_show += x

if show_layers:
    if not Glyphs.font.tabs:
        Glyphs.font.newTab()

    Glyphs.font.tabs[-1].layers = show_layers
elif is_used:
    Glyphs.showNotification('Show Current Glyph with Disabled Alignment', 'The current glyph is automatically aligned in all the glyphs that use it as a component.')
else:
    Glyphs.showNotification('Show Current Glyph with Disabled Alignment', 'The current glyph is not used as a component in any other glyphs.')
