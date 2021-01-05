# MenuTitle: Add Length Layer
import copy
__doc__ = """
Adds a layer named length to each master and adds the parameter to the smart glyph settings.
"""

Glyphs.clearLog()
Glyphs.showMacroWindow()

g = Glyphs.font.selectedLayers[0].parent

for m in Glyphs.font.masters:
    newL_name = '{} length'.format(m.name)
    if not g.layers[newL_name]:
        newL = copy.copy(g.layers[m.id])
        newL.name = newL_name
        g.layers.append(newL)

# Add the length anchor
for l in g.layers:
    if not l.anchors['length']:
        xPos = l.bounds.origin.x + l.bounds.size.width
        yPos = l.bounds.origin.y
        newA = GSAnchor('length', NSPoint(xPos, yPos))
        l.anchors.append(newA)


if not g.smartComponentAxes or not g.smartComponentAxes['length']:
    length_axis = GSSmartComponentAxis()
    length_axis.name = 'length'
    length_axis.topValue = 100
    length_axis.bottomValue = 0
    g.smartComponentAxes.append(length_axis)

    # Assign the layers to each axis
    for l in g.layers:
        if l.name.endswith('length'):
            l.smartComponentPoleMapping[length_axis.id] = 2
        else:
            l.smartComponentPoleMapping[length_axis.id] = 1
