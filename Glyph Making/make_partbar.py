# MenuTitle: Make _part.bar
# -*- coding: utf-8 -*-
__doc__ = """
Makes a _part.bar glyph if not already present.
"""

import math

Glyphs.clearLog()
# Glyphs.showMacroWindow()


def get_nodes_height(m, glyph_names=[]):
    heights = []
    for gn in glyph_names:
        test_g = Glyphs.font.glyphs[gn]
        if test_g is not None:
            test_layer = test_g.layers[m.id]
            # test_nodes = sorted([n for p in l.paths for n in p.nodes if n.type != OFFCURVE], key = lambda x: x.x)  # Leftmost Nodes
            test_nodes = sorted([n for p in test_layer.paths for n in p.nodes if n.type != OFFCURVE], key=lambda x: x.y)  # Lowest Nodes
            try:
                heights.append(abs(test_nodes[0].y - test_nodes[1].y))
            except IndexError:
                pass

    if heights:
        return int(sum(heights) / len(heights))

    return 2


def get_nodes_width(m, glyph_names=[]):
    # widths = []
    return 100


def compensate_italic_angle(pos_y):
    if not italic_angle:
        return 0
    return round(math.tan(math.radians(italic_angle)) * pos_y)


def get_point(x, y):
    return NSPoint(x + compensate_italic_angle(y), y)


def get_anchors(xMin, yMin, xMax, yMax, x_offset=0, y_offset=0):
    top = yMax + y_offset
    bottom = yMin + y_offset
    left = xMin + x_offset
    right = xMax + x_offset
    middle = int(sum((top, bottom)) / 2)
    center = int(sum((left, right)) / 2)

    top_left = get_point(left, top)
    top_center = get_point(center, top)
    top_right = get_point(right, top)
    middle_left = get_point(left, middle)
    middle_center = get_point(center, middle)
    middle_right = get_point(right, middle)
    bottom_left = get_point(left, bottom)
    bottom_center = get_point(center, bottom)
    bottom_right = get_point(right, bottom)

    return [
        GSAnchor('_#bar', middle_center),
        GSAnchor('_#center', middle_center),
        GSAnchor('_#topleft', top_left),
        GSAnchor('_top', top_center),
        GSAnchor('_#left', middle_left),
        GSAnchor('_#bottomleft', bottom_left),
        GSAnchor('_#topright', top_right),
        GSAnchor('_#right', middle_right),
        GSAnchor('_#bottomright', bottom_right),
        GSAnchor('_bottom', bottom_center),
        GSAnchor('_#barcenter', middle_center),
        GSAnchor('_#bartopleft', top_left),
        GSAnchor('_#bartop', top_center),
        GSAnchor('_#barleft', middle_left),
        GSAnchor('_#barbottomleft', bottom_left),
        GSAnchor('_#bartopright', top_right),
        GSAnchor('_#barright', middle_right),
        GSAnchor('_#barbottomright', bottom_right),
        GSAnchor('_#barbottom', bottom_center),
        GSAnchor('length', get_point(xMax, yMin)),
        GSAnchor('thickness', get_point(xMax, yMax)),
        GSAnchor('xoffset', get_point(xMax, int(sum((yMax, yMin)) / 2))),
        GSAnchor('yoffset', get_point(int(sum((xMax, xMin)) / 2), yMax)),
    ]


# nodes_height = dict((m.id, get_nodes_height(m, ('t', 'f'))) for m in Glyphs.font.masters)
dimensions = Glyphs.font.userData["GSDimensionPlugin.Dimensions"] or {}
nodes_height = dict(
    (m.id, int(dimensions.get(m.id, {}).get('tH') or get_nodes_height(m, ('o',)))) for m in Glyphs.font.masters
)
nodes_width = dict((m.id, get_nodes_width(m)) for m in Glyphs.font.masters)

nodes_height_max = dict(
    (m.id, int(dimensions.get(m.id, {}).get('HH') or get_nodes_height(m, ('O',)))) for m in Glyphs.font.masters
)
nodes_width_max = dict((m.id, nodes_width[m.id] + 100) for m in Glyphs.font.masters)

offset = 100

origin = NSPoint(0, 0)


newG = Glyphs.font.glyphs['_part.bar']
if newG is None:
    newG = GSGlyph('_part.bar')
    newG.export = False
    Glyphs.font.glyphs.append(newG)

newG.updateGlyphInfo()

# To clear the glyph
# newG.layers = []
# newG.smartComponentAxes = []

for m in Glyphs.font.masters:
    italic_angle = m.italicAngle
    newL = newG.layers[m.id] or GSLayer()
    newL.associatedMasterId = m.id
    newP = GSPath()
    print(origin.y, nodes_height[m.id])
    newP.nodes = [
        GSNode(get_point(origin.x + nodes_width[m.id], origin.y), LINE),
        GSNode(get_point(origin.x + nodes_width[m.id], origin.y + nodes_height[m.id]), LINE),
        GSNode(get_point(origin.x, origin.y + nodes_height[m.id]), LINE),
        GSNode(get_point(origin.x, origin.y), LINE),
    ]
    newP.closed = True
    newL.paths.append(newP)
    newL.anchors = get_anchors(origin.x, origin.y, origin.x + nodes_width[m.id], origin.y + nodes_height[m.id])
    newG.layers[m.id] = newL

    # Add the Thickness Layer
    newL_name = '{} thickness'.format(m.name)
    newL = newG.layers[newL_name] or GSLayer()
    newL.name = newL_name
    newL.associatedMasterId = m.id
    newP = GSPath()
    newP.nodes = [
        GSNode(get_point(origin.x + nodes_width[m.id], origin.y), LINE),
        GSNode(get_point(origin.x + nodes_width[m.id], origin.y + nodes_height_max[m.id]), LINE),
        GSNode(get_point(origin.x, origin.y + nodes_height_max[m.id]), LINE),
        GSNode(get_point(origin.x, origin.y), LINE),
    ]
    newP.closed = True
    newL.anchors = get_anchors(origin.x, origin.y, origin.x + nodes_width[m.id], origin.y + nodes_height_max[m.id])
    newL.paths.append(newP)
    newG.layers.append(newL)

    # Add the length Layer
    newL_name = '{} length'.format(m.name)
    newL = newG.layers[newL_name] or GSLayer()
    newL.name = newL_name
    newL.associatedMasterId = m.id
    newP = GSPath()
    newP.nodes = [
        GSNode(get_point(origin.x + nodes_width_max[m.id], origin.y), LINE),
        GSNode(get_point(origin.x + nodes_width_max[m.id], origin.y + nodes_height[m.id]), LINE),
        GSNode(get_point(origin.x, origin.y + nodes_height[m.id]), LINE),
        GSNode(get_point(origin.x, origin.y), LINE),
    ]
    newP.closed = True
    newL.anchors = get_anchors(
        origin.x, origin.y, origin.x + nodes_width_max[m.id], origin.y + nodes_height[m.id])
    newL.paths.append(newP)
    newG.layers.append(newL)

    # Add the X Offset Layer
    newL_name = '{} xoffset'.format(m.name)
    newL = newG.layers[newL_name] or GSLayer()
    newL.name = newL_name
    newL.associatedMasterId = m.id
    newP = GSPath()
    newP.nodes = [
        GSNode(get_point(offset + origin.x + nodes_width[m.id], origin.y), LINE),
        GSNode(get_point(offset + origin.x + nodes_width[m.id], origin.y + nodes_height[m.id]), LINE),
        GSNode(get_point(offset + origin.x, origin.y + nodes_height[m.id]), LINE),
        GSNode(get_point(offset + origin.x, origin.y), LINE),
    ]
    newP.closed = True
    newL.anchors = get_anchors(
        origin.x + offset,
        origin.y,
        origin.x + nodes_width[m.id] + offset,
        origin.y + nodes_height[m.id],
        x_offset=-offset
    )
    newL.paths.append(newP)
    newG.layers.append(newL)

    # Add the Y Offset Layer
    newL_name = '{} yoffset'.format(m.name)
    newL = newG.layers[newL_name] or GSLayer()
    newL.name = newL_name
    newL.associatedMasterId = m.id

    newP = GSPath()
    newP.nodes = [
        GSNode(get_point(origin.x + nodes_width[m.id], offset + origin.y), LINE),
        GSNode(get_point(origin.x + nodes_width[m.id], offset + origin.y + nodes_height[m.id]), LINE),
        GSNode(get_point(origin.x, offset + origin.y + nodes_height[m.id]), LINE),
        GSNode(get_point(origin.x, offset + origin.y), LINE),
    ]
    newP.closed = True
    newL.anchors = get_anchors(
        origin.x,
        origin.y + offset,
        origin.x + nodes_width[m.id],
        origin.y + nodes_height[m.id] + offset,
        y_offset=-offset
    )
    newL.paths.append(newP)
    newG.layers.append(newL)

# Set up the SmartComponentAxis
try:
    thickness_axis = newG.smartComponentAxes['thickness']
except TypeError:
    thickness_axis = None
if thickness_axis is None:
    thickness_axis = GSSmartComponentAxis()
    newG.smartComponentAxes.append(thickness_axis)
thickness_axis.name = 'thickness'
thickness_axis.topValue = 100
thickness_axis.bottomValue = 0

try:
    length_axis = newG.smartComponentAxes['length']
except TypeError:
    length_axis = None
if length_axis is None:
    length_axis = GSSmartComponentAxis()
    newG.smartComponentAxes.append(length_axis)
length_axis.name = 'length'
length_axis.topValue = 100
length_axis.bottomValue = 0

try:
    xoffset_axis = newG.smartComponentAxes['xoffset']
except TypeError:
    xoffset_axis = None
if xoffset_axis is None:
    xoffset_axis = GSSmartComponentAxis()
    newG.smartComponentAxes.append(xoffset_axis)
xoffset_axis.name = 'xoffset'
xoffset_axis.topValue = 100
xoffset_axis.bottomValue = 0

try:
    yoffset_axis = newG.smartComponentAxes['yoffset']
except TypeError:
    yoffset_axis = None
if yoffset_axis is None:
    yoffset_axis = GSSmartComponentAxis()
    newG.smartComponentAxes.append(yoffset_axis)
yoffset_axis.name = 'yoffset'
yoffset_axis.topValue = 100
yoffset_axis.bottomValue = 0

# Assign the layers to each axis
for l in newG.layers:
    for axis in [
        thickness_axis,
        length_axis,
        xoffset_axis,
        yoffset_axis,
    ]:
        l.smartComponentPoleMapping[axis.id] = 2 if l.name.endswith(axis.name) else 1
