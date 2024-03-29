# MenuTitle: Report xMin xMax yMin yMax
from collections import OrderedDict
from AppKit import NSEvent

Glyphs.clearLog()

extremes = OrderedDict()

# --- From mekkablue ---
keysPressed = NSEvent.modifierFlags()
shiftKey = 131072
shiftKeyPressed = keysPressed & shiftKey == shiftKey
# ---

for m in Glyphs.font.masters:
    extremes[m.id] = {
        'xMin_val': None,
        'yMin_val': None,
        'xMax_val': None,
        'yMax_val': None,
        'xMin_layer': None,
        'yMin_layer': None,
        'xMax_layer': None,
        'yMax_layer': None,
    }

    for g in [x for x in Glyphs.font.glyphs if x.export]:
        l = g.layers[m.id]
        if shiftKeyPressed and not l.width:
            continue
        if extremes[m.id]['xMin_val'] is None or extremes[m.id]['xMin_val'] > l.bounds.origin.x:
            extremes[m.id]['xMin_val'] = l.bounds.origin.x
            extremes[m.id]['xMin_layer'] = l

        if extremes[m.id]['yMin_val'] is None or extremes[m.id]['yMin_val'] > l.bounds.origin.y:
            extremes[m.id]['yMin_val'] = l.bounds.origin.y
            extremes[m.id]['yMin_layer'] = l

        if extremes[m.id]['xMax_val'] is None or extremes[m.id]['xMax_val'] < l.bounds.origin.x + l.bounds.size.width:
            extremes[m.id]['xMax_val'] = l.bounds.origin.x + l.bounds.size.width
            extremes[m.id]['xMax_layer'] = l

        if extremes[m.id]['yMax_val'] is None or extremes[m.id]['yMax_val'] < l.bounds.origin.y + l.bounds.size.height:
            extremes[m.id]['yMax_val'] = l.bounds.origin.x + l.bounds.size.height
            extremes[m.id]['yMax_layer'] = l


def convert_text_to_layers(string):
    current_master_id = Glyphs.font.selectedFontMaster.id
    glyphs = list(string)
    layers = []
    for gn in glyphs:
        g = Glyphs.font.glyphs[gn]
        if g is not None:
            layers.append(g.layers[current_master_id])
        
    return layers


layers = []
for li, data in enumerate(extremes.items()):
    mid, extremes = data
    layers += convert_text_to_layers('Layer {li}: {layerName}'.format(li=li, layerName=Glyphs.font.masters[str(mid)].name)) + [GSControlLayer(10)]
    layers += convert_text_to_layers('xMin: {} '.format(extremes['xMin_val'])) + [extremes['xMin_layer'], GSControlLayer(10)]
    layers += convert_text_to_layers('yMin: {} '.format(extremes['yMin_val'])) + [extremes['yMin_layer'], GSControlLayer(10)]
    layers += convert_text_to_layers('xMax: {} '.format(extremes['xMax_val'])) + [extremes['xMax_layer'], GSControlLayer(10)]
    layers += convert_text_to_layers('yMax: {} '.format(extremes['yMax_val'])) + [extremes['yMax_layer'], GSControlLayer(10)]
    layers += [GSControlLayer(10)]

if layers:
    Glyphs.font.newTab()
    Glyphs.font.tabs[-1].layers = layers
