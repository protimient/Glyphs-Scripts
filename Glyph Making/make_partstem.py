# MenuTitle: Make _part.stem
# Author: Ben Jones

__doc__ = """
Makes a _part.stem glyph if not already present.
"""

import math

Glyphs.clearLog()
# Glyphs.showMacroWindow()


def get_nodes_height(m, glyph_names=[]):
    return m.xHeight


def get_nodes_width(m, glyph_names=[]):
    widths = []

    for gn in glyph_names:
        test_g = Glyphs.font.glyphs[gn]
        if test_g is not None:
            if test_g.subCategory == 'Uppercase':
                dimensions_val = 'HV'
            else:
                dimensions_val = 'nV'
            try:
                width = Glyphs.font.userData["GSDimensionPlugin.Dimensions"][m.id].get(dimensions_val)
            except TypeError:
                width = None
            if width:
                return int(width)

            layer = test_g.layers[m.id]
            intersections = layer.intersectionsBetweenPoints((-1000, 100), (layer.width + 1000, 100))
            try:
                widths.append(abs(intersections[-2].x - intersections[1].x))
            except IndexError:
                pass
    if widths:
        return int(sum(widths) / len(widths))

    return 100


def compensate_italic_angle(pos_y, italic_angle):
    if not italic_angle:
        return 0
    return round(math.tan(math.radians(italic_angle)) * pos_y)


def get_point(x, y):
    # return NSPoint(x + compensate_italic_angle(y), y)
    return NSPoint(x, y)


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
        GSAnchor('#bar', middle_center),
        GSAnchor('#center', middle_center),
        GSAnchor('#topleft_1', top_left),
        GSAnchor('#topleft_2', top_center),
        GSAnchor('top', top_center),
        GSAnchor('#left_1', middle_left),
        GSAnchor('#left_2', middle_center),
        GSAnchor('#bottomleft_1', bottom_left),
        GSAnchor('#bottomleft_2', bottom_center),
        GSAnchor('#topright', top_right),
        GSAnchor('#right', middle_right),
        GSAnchor('#bottomright', bottom_right),
        GSAnchor('bottom', bottom_center),
        GSAnchor('_#stemcenter', middle_center),
        GSAnchor('_#stemtopleft', top_left),
        GSAnchor('_#stemtop', top_center),
        GSAnchor('_#stemleft', middle_left),
        GSAnchor('_#stembottomleft', bottom_left),
        GSAnchor('_#stemtopright', top_right),
        GSAnchor('_#stemright', middle_right),
        GSAnchor('_#stembottomright', bottom_right),
        GSAnchor('_#stembottom', bottom_center),
        GSAnchor('width', get_point(xMax, yMin)),
        GSAnchor('height', get_point(xMax, yMax)),
        GSAnchor('xoffset', get_point(xMax, int(sum((yMax, yMin)) / 2))),
        GSAnchor('yoffset', get_point(int(sum((xMax, xMin)) / 2), yMax)),
    ]


nodes_height = dict((m.id, get_nodes_height(m)) for m in Glyphs.font.masters)
nodes_width = dict((m.id, get_nodes_width(m, ('l',))) for m in Glyphs.font.masters)

nodes_height_max = dict((m.id, nodes_height[m.id] + 100) for m in Glyphs.font.masters)
nodes_width_max = dict((m.id, get_nodes_width(m, ('I',))) for m in Glyphs.font.masters)

offset = 100

origin = NSPoint(0, 0)


def make_layer(m, newG, nodes_coords, anchor_extremes, layer_name=None, x_offset=0, y_offset=0):
    italic_angle = m.italicAngle
    if layer_name is None:
        newL = newG.layers[m.id] or GSLayer()
    else:
        newL = newG.layers[layer_name] or GSLayer()
        newL.name = layer_name
    newL.associatedMasterId = m.id
    newL.paths = []

    newP = GSPath()
    for nc in nodes_coords:
        newP.nodes.append(GSNode(get_point(nc[0], nc[1]), LINE))
    newP.closed = True
    newL.paths.append(newP)

    newL.anchors = get_anchors(*anchor_extremes, x_offset=x_offset, y_offset=y_offset)
    newL.applyTransform((1, 0, math.radians(italic_angle), 1, 0, 0))
    if layer_name is None:
        newG.layers[m.id] = newL
    else:
        newG.layers.append(newL)


newG = Glyphs.font.glyphs['_part.stem']
if newG is None:
    newG = GSGlyph('_part.stem')
    newG.export = False
    Glyphs.font.glyphs.append(newG)

newG.updateGlyphInfo()

# To clear the glyph
# newG.layers = []
# newG.smartComponentAxes = []

for m in Glyphs.font.masters:
    # Add the base Layer
    nodes_coords = [
        (origin.x + nodes_width[m.id], origin.y),
        (origin.x + nodes_width[m.id], origin.y + nodes_height[m.id]),
        (origin.x, origin.y + nodes_height[m.id]),
        (origin.x, origin.y),
    ]
    anchor_extremes = (origin.x, origin.y, origin.x + nodes_width[m.id], origin.y + nodes_height[m.id])
    make_layer(m, newG, nodes_coords, anchor_extremes, layer_name=None)

    # Add the height Layer
    newL_name = '{} height'.format(m.name)
    nodes_coords = [
        (origin.x + nodes_width[m.id], origin.y),
        (origin.x + nodes_width[m.id], origin.y + nodes_height_max[m.id]),
        (origin.x, origin.y + nodes_height_max[m.id]),
        (origin.x, origin.y),
    ]
    anchor_extremes = (origin.x, origin.y, origin.x + nodes_width[m.id], origin.y + nodes_height_max[m.id])
    make_layer(m, newG, nodes_coords, anchor_extremes, layer_name=newL_name)

    # Add the width Layer
    newL_name = '{} width'.format(m.name)
    nodes_coords = [
        (origin.x + nodes_width_max[m.id], origin.y),
        (origin.x + nodes_width_max[m.id], origin.y + nodes_height[m.id]),
        (origin.x, origin.y + nodes_height[m.id]),
        (origin.x, origin.y),
    ]
    anchor_extremes = (origin.x, origin.y, origin.x + nodes_width_max[m.id], origin.y + nodes_height[m.id])
    make_layer(m, newG, nodes_coords, anchor_extremes, layer_name=newL_name)

    # Add the X Offset Layer
    newL_name = '{} xoffset'.format(m.name)
    nodes_coords = [
        (offset + origin.x + nodes_width[m.id], origin.y),
        (offset + origin.x + nodes_width[m.id], origin.y + nodes_height[m.id]),
        (offset + origin.x, origin.y + nodes_height[m.id]),
        (offset + origin.x, origin.y),
    ]
    anchor_extremes = (origin.x + offset, origin.y, origin.x + nodes_width[m.id] + offset, origin.y + nodes_height[m.id])
    make_layer(m, newG, nodes_coords, anchor_extremes, layer_name=newL_name, x_offset=-offset)

    # Add the Y Offset Layer
    newL_name = '{} yoffset'.format(m.name)
    nodes_coords = [
        (origin.x + nodes_width[m.id], offset + origin.y),
        (origin.x + nodes_width[m.id], offset + origin.y + nodes_height[m.id]),
        (origin.x, offset + origin.y + nodes_height[m.id]),
        (origin.x, offset + origin.y),
    ]
    anchor_extremes = (origin.x, origin.y + offset, origin.x + nodes_width[m.id], origin.y + nodes_height[m.id] + offset)
    make_layer(m, newG, nodes_coords, anchor_extremes, layer_name=newL_name, y_offset=-offset)

# Set up the SmartComponentAxis
try:
    height_axis = newG.smartComponentAxes['height']
except TypeError:
    height_axis = None
if height_axis is None:
    height_axis = GSSmartComponentAxis()
    newG.smartComponentAxes.append(height_axis)
height_axis.name = 'height'
height_axis.topValue = 100
height_axis.bottomValue = 0

try:
    width_axis = newG.smartComponentAxes['width']
except TypeError:
    width_axis = None
if width_axis is None:
    width_axis = GSSmartComponentAxis()
    newG.smartComponentAxes.append(width_axis)
width_axis.name = 'width'
width_axis.topValue = 100
width_axis.bottomValue = 0

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
        height_axis,
        width_axis,
        xoffset_axis,
        yoffset_axis,
    ]:
        l.smartComponentPoleMapping[axis.id] = 2 if l.name.endswith(axis.name) else 1
