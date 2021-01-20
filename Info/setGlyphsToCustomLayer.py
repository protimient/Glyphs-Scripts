# MenuTitle: Set Tab to Current Custom Layer
# -*- coding: utf-8 -*-
__doc__ = """
Sets all the glyphs in the current editor tab to the same non-master layer as the current glyph/layer.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()

layer_name = Glyphs.font.selectedLayers[0].name

layers_in_tab = Glyphs.font.currentTab.layers

new_layers = []
non_layers = []
all_layers = []
for l in layers_in_tab:
    all_layers.append(l.parent.layers[layer_name] or l)
    # if new_l:
    #     new_layers.append(new_l)
    # else:
    #     non_layers.append(l)

# Glyphs.font.currentTab.layers = new_layers + [GSControlLayer(10)] + non_layers
Glyphs.font.currentTab.layers = all_layers
