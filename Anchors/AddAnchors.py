# MenuTitle: Add Anchors
# -*- coding: utf-8 -*-

import math
import re
from collections import defaultdict

__doc__ = """
Adds missing anchors to the selected glyphs on all layers.
"""
# Author: Ben Jones 2018

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

reset_anchors = 0  # When True, this completely clears all anchors in the glyph and starts afresh.
replace_anchors = 0  # When True, any anchors that are defined below will be repositioned. Undefined anchors will not be touched.


def font_has(script_name):
    for g in Glyphs.font.glyphs:
        if g.script == script_name:
            return True

    return False


class layerPositions:
    def __init__(self, l):
        self.layer = l

        self.layer_flat = l.copyDecomposedLayer()
        self.layer_flat.removeOverlap()

        try:
            self.italic_angle = Glyphs.font.masters[self.layer.associatedMasterId].italicAngle
        except AttributeError:
            self.italic_angle = 0

        self.is_smallcaps = l.parent.subCategory == 'Smallcaps'
        self.layer_metrics = defaultdict(dict)
        self.aname_sub = re.compile('^[xy]pos_')

        self._leftmost_node = None
        self._rightmost_node = None
        self._topmost_node = None
        self._bottommost_node = None
        self._all_layer_nodes = None
        self._top_two_nodes = None
        self._bottom_two_nodes = None
        self._bottom_two_nodes_consecutive = None
        self._indic_headlines = self._get_all_indic_headlines()
        self._indic_stem_widths = self._get_indic_stem_widths()

    def compensate_italic_angle(self, pos_y):
        if not self.italic_angle:
            return 0
        return round(math.tan(math.radians(self.italic_angle)) * pos_y)

    def all_layers_nodes(self):
        if self._all_layer_nodes is None:
            self._all_layer_nodes = [n for p in self.layer_flat.paths for n in p.nodes if n.type != OFFCURVE]
            # for c in self.layer.components:
            # 	this_l = c.component.layers[self.layer.layerId]
            # 	if this_l:
            # 		nodes += [NSPoint(n.x + c.position.x, n.y + c.position.y) for p in this_l.paths for n in p.nodes if n.type != OFFCURVE]
            # 		for c2 in this_l.components:
            # 			this_l2 = c2.component.layers[self.layer.layerId]
            # 			if this_l2:
            #                nodes += [NSPoint(
            #                    n.x + c.position.x + c2.position.x,
            #                    n.y + c.position.y + c2.position.y
            #                    ) for p in this_l2.paths for n in p.nodes if n.type != OFFCURVE]
            # self._all_layer_nodes = nodes
        return self._all_layer_nodes

    @staticmethod
    def get_next_node(node):
        next_node = node.nextNode
        while next_node.type == OFFCURVE:
            next_node = next_node.nextNode
        return next_node

    @staticmethod
    def get_prev_node(node):
        prev_node = node.prevNode
        while prev_node.type == OFFCURVE:
            prev_node = prev_node.nextNode
        return prev_node

    def leftmost_node(self):
        if self._leftmost_node is None:
            nodes = [(n.x - self.compensate_italic_angle(n.y), n.x, n.y) for n in self.all_layers_nodes()]
            nodes.sort(key=lambda x: x[0])
            self._leftmost_node = NSPoint(nodes[0][1], nodes[0][2])
        return self._leftmost_node

    def rightmost_node(self):
        if self._rightmost_node is None:
            nodes = [(n.x - self.compensate_italic_angle(n.y), n.x, n.y) for n in self.all_layers_nodes()]
            nodes.sort(key=lambda x: x[0])
            self._rightmost_node = NSPoint(nodes[-1][1], nodes[-1][2])
        return self._rightmost_node

    def topmost_node(self):
        if self._topmost_node is None:
            self._topmost_node = sorted(self.all_layers_nodes(), key=lambda x: x.y)[-1]
        return self._topmost_node

    def bottommost_node(self):
        if self._bottommost_node is None:
            self._bottommost_node = sorted(self.all_layers_nodes(), key=lambda x: x.y)[0]
        return self._bottommost_node

    def top_two_nodes(self):
        if self._top_two_nodes is None:
            self._top_two_nodes = sorted(self.all_layers_nodes(), key=lambda x: x.y, reverse=True)[:2]
            self._top_two_nodes.sort(key=lambda x: x.x)
        return self._top_two_nodes

    def bottom_two_nodes(self):
        if self._bottom_two_nodes is None:
            self._bottom_two_nodes = sorted(self.all_layers_nodes(), key=lambda x: x.y)[:2]
            self._bottom_two_nodes.sort(key=lambda x: x.x)
        return self._bottom_two_nodes

    def bottom_two_nodes_consecutive(self):
        if self._bottom_two_nodes_consecutive is None:
            other_node = min([self.get_next_node(self.bottommost_node()), self.get_prev_node(self.bottommost_node())], key=lambda n: n.y)
            self._bottom_two_nodes_consecutive = sorted([self.bottommost_node(), other_node], key=lambda x: x.y)
            self._bottom_two_nodes_consecutive.sort(key=lambda x: x.x)
        return self._bottom_two_nodes_consecutive

    def get_coords(self, aname, pos_x_name, pos_y_name):
        try:
            if not pos_x_name.startswith('xpos'):
                pos_x_name = 'xpos_' + pos_x_name
        except AttributeError:
            pass
        try:
            if not pos_y_name.startswith('ypos'):
                pos_y_name = 'ypos_' + pos_y_name
        except AttributeError:
            pass

        pos_y = 0
        if type(pos_y_name) == int:
            pos_y = pos_y_name

        elif pos_y_name is None:
            extant_a = self.layer.anchors[aname]
            if extant_a:
                pos_y = extant_a.y
        else:
            pos_y = self.layer_metrics.get(self.layer.layerId, {}).get(pos_y_name)
            if pos_y is None:
                try:
                    pos_y = getattr(self, pos_y_name)()
                except (AttributeError, IndexError):
                    gname = self.aname_sub.sub('', pos_y_name)
                    g = Glyphs.font.glyphs[gname]
                    if g is not None:
                        layer = g.layers[self.layer.associatedMasterId]
                        _, pos_y = self._get_anchor_pos(layer, aname)
                        pos_y_name += aname
                    else:
                        _, pos_y = self._get_anchor_pos(self.layer, pos_y_name)
                self.layer_metrics[self.layer.layerId][pos_y_name] = pos_y

        pos_x = 0
        if type(pos_x_name) == int:
            pos_x = self.xpos_value(pos_x_name, pos_y)

        elif pos_x_name is None:
            extant_a = self.layer.anchors[aname]
            if extant_a:
                pos_x = extant_a.x
        else:
            if not self.italic_angle:
                pos_x = self.layer_metrics.get(self.layer.layerId, {}).get(pos_x_name)
            else:
                pos_x = None

            if pos_x is None:
                try:
                    pos_x = getattr(self, pos_x_name)(pos_y)
                except (AttributeError, IndexError):
                    gname = self.aname_sub.sub('', pos_x_name)
                    g = Glyphs.font.glyphs[gname]
                    if g is not None:
                        layer = g.layers[self.layer.associatedMasterId]
                        pos_x, _ = self._get_anchor_pos(layer, aname)
                        pos_x_name += aname
                    else:
                        pos_x, _ = self._get_anchor_pos(self.layer, pos_x_name)
                self.layer_metrics[self.layer.layerId][pos_x_name] = pos_x

        return pos_x, pos_y

    def _get_anchor_pos(self, layer, aname):
        aname = self.aname_sub.sub('', aname)

        a = layer.anchors[aname]
        if a is None:
            layer = layer.copyDecomposedLayer()
            a = layer.anchors[aname]

        if a is None:
            return 0, 0

        return a.position

    def _get_all_indic_headlines(self):
        """
        Builds a dictionary holding the x-coordinates for the top and bottom of the headline for each master.
        dict[script][master ID][top or bottom]
        """
        headline_dict = {}
        for gn in ['ka-beng', 'ka-deva']:
            g = Glyphs.font.glyphs[gn]
            if g:
                headline_dict[g.script] = {}
                for l in g.layers:
                    top, bottom = self.get_indic_headline(l)
                    headline_dict[g.script][l.associatedMasterId] = {
                        'top': top,
                        'bottom': bottom,
                    }

        return headline_dict

    def _get_indic_stem_widths(self):
        """
        Builds a dictionary holding the stem width for each master.
        dict[script][master ID] = stem width
        """
        temp_dict = defaultdict(dict)
        for gn in ['iMatra-beng', 'iMatra-deva']:
            g = Glyphs.font.glyphs[gn]
            if g:
                for l in g.layers:
                    stem_coords = l.intersectionsBetweenPoints((0, 300), (l.width, 300), components=True)[1:-1]
                    try:
                        stem_width = stem_coords[1].x - stem_coords[0].x
                        temp_dict[g.script][l.associatedMasterId] = stem_width
                    except IndexError:
                        temp_dict[g.script][l.associatedMasterId] = None

        return temp_dict

    @staticmethod
    def get_indic_headline(layer):
        layer = layer.copyDecomposedLayer()
        layer.removeOverlap()

        all_nodes = [n for p in layer.paths for n in p.nodes if not n.type == OFFCURVE]
        all_nodes.sort(key=lambda n: n.y, reverse=True)

        top = None
        for n in all_nodes:
            if (n.nextNode.y == n.y and not n.nextNode.type == OFFCURVE) or (n.prevNode.y == n.y and not n.prevNode.type == OFFCURVE):
                top = n.y
                break

        bottom = None
        for n in all_nodes:
            if ((n.nextNode.y == n.y and not n.nextNode.type == OFFCURVE) or (n.prevNode.y == n.y and not n.prevNode.type == OFFCURVE)) and n.y != top:
                bottom = n.y
                break

        return top, bottom

    @staticmethod
    def check_coord(comp_this, comp_against, fuzziness=2):
        return comp_against + fuzziness > comp_this > comp_against - fuzziness

    def _get_indic_rightmost_stem(self, l):
        stem_center = None
        number_of_samples = 12

        stem_width = self._indic_stem_widths.get(l.parent.script, {}).get(l.associatedMasterId)
        if stem_width is None:
            return

        fuzziness = stem_width * 0.1

        measure_interval = int(l.bounds.size.height / number_of_samples)
        measure_heights = range(int(l.bounds.origin.y), int(l.bounds.origin.y + l.bounds.size.height), measure_interval)

        potential_stems = defaultdict(list)
        measured_points = []
        # l.guides = []
        for height in measure_heights:
            for p in l.paths:
                measure_l = GSLayer()
                measure_l.width = l.width
                measure_l.paths.append(p)
                measured_points.append(measure_l.intersectionsBetweenPoints((0, height), (measure_l.width, height), components=True)[1:-1])
            for c in l.components:
                measure_l = c.componentLayer.copyDecomposedLayer()
                measure_l.removeOverlap()
                measure_l.applyTransform(c.transform)
                measured_points.append(measure_l.intersectionsBetweenPoints((0, height), (measure_l.width + c.transform[4], height), components=True)[1:-1])
            # if 1:
            #     ngl = GSGuideLine()
            #     ngl.position = NSPoint(0, height)
            #     ngl.setShowMeasurement_(1)
            #     l.guides.append(ngl)

        # print(l, stem_width)
        for measure_coords in measured_points:
            for ci, coord in enumerate(measure_coords):
                try:
                    next_coord = measure_coords[ci + 1]
                except IndexError:
                    break
                coord_distance = next_coord.x - coord.x
                # print(coord_distance, measure_coords)
                if self.check_coord(coord_distance, stem_width, fuzziness=fuzziness):
                    stem_mid_point = round((next_coord.x + coord.x) / 2)
                    stem_mid_point_max = stem_mid_point + fuzziness
                    stem_mid_point_min = stem_mid_point - fuzziness

                    added = False
                    for min_max in potential_stems.keys():
                        pmin, pmax = min_max
                        if pmax > stem_mid_point_max > pmin or pmax > stem_mid_point_min > pmin:
                            potential_stems[min_max].append(stem_mid_point)
                            added = True
                            break

                    if not added:
                        potential_stems[(stem_mid_point_min, stem_mid_point_max)].append(stem_mid_point)

        vals = potential_stems.values()
        vals.sort(reverse=True)
        vals.sort(key=len, reverse=True)
        stem_center = round(sum(vals[0]) / len(vals[0]))

        return stem_center

    # X positions
    # The below methods calculate x-coordinate positions.
    # If the font is italic, the x position needs to be adjusted (the y position is unaffected by italic).

    def xpos_stem_top_center(self, pos_y):
        """
        Finds the 2 highest nodes and returns the x position between them
        """
        x_pos = sum([x.x for x in self.top_two_nodes()]) / 2
        if self.italic_angle:
            measure_node = sum([x.y for x in self.top_two_nodes()]) / 2
            x_pos += self.compensate_italic_angle(pos_y - measure_node)
        return int(x_pos)

    def xpos_stem_top_left(self, pos_y):
        """
        Finds the 2 highest nodes and returns the x position of the leftmost one.
        """
        x_pos = int(self.top_two_nodes()[0].x)
        if self.italic_angle:
            measure_node = self.top_two_nodes()[0]
            x_pos += self.compensate_italic_angle(pos_y - measure_node.y)
        return x_pos

    def xpos_stem_top_right(self, pos_y):
        """
        Finds the 2 highest nodes and returns the x position of the rightmost one.
        """
        x_pos = int(self.top_two_nodes()[-1].x)
        if self.italic_angle:
            measure_node = self.top_two_nodes()[-1]
            x_pos += self.compensate_italic_angle(pos_y - measure_node.y)
        return x_pos

    def xpos_stem_bottom_center(self, pos_y):
        """
        Finds the 2 lowest nodes and returns the x position between them
        """
        x_pos = sum([x.x for x in self.bottom_two_nodes_consecutive()]) / 2
        if self.italic_angle:
            measure_node = sum([x.y for x in self.bottom_two_nodes_consecutive()]) / 2
            x_pos += self.compensate_italic_angle(pos_y - measure_node)
        return int(x_pos)

    def xpos_stem_bottom_right(self, pos_y):
        """
        Finds the 2 lowest nodes and returns the x position of the leftmost one.
        """
        x_pos = int(self.bottom_two_nodes_consecutive()[-1].x)
        if self.italic_angle:
            measure_node = self.bottom_two_nodes_consecutive()[-1]
            x_pos += self.compensate_italic_angle(pos_y - measure_node.y)
        return x_pos

    def xpos_stem_bottom_left(self, pos_y):
        """
        Finds the 2 lowest nodes and returns the x position of the rightmost one.
        """
        x_pos = int(self.bottom_two_nodes_consecutive()[0].x)
        if self.italic_angle:
            measure_node = self.bottom_two_nodes_consecutive()[0]
            x_pos += self.compensate_italic_angle(pos_y - measure_node.y)
        return x_pos

    def xpos_outline_center(self, pos_y):
        """
        Finds the leftmost node and rightmost node and returns the x position of their centre.
        """
        # pos_x = int(sum([self.layer.bounds.origin.x, self.layer.bounds.size.width, self.layer.bounds.origin.x]) / 2)
        pos_x = int((self.layer.bounds.size.width / 2) + self.layer.bounds.origin.x)
        if self.italic_angle:
            measure_node = ((self.leftmost_node().x + self.rightmost_node().x) / 2, (self.leftmost_node().y + self.rightmost_node().y) / 2)
            italic_compensation = self.compensate_italic_angle(pos_y - measure_node[1])
            pos_x = measure_node[0] + italic_compensation
        return int(pos_x)

    def xpos_outline_left(self, pos_y):
        """
        Returns the x position of the leftmost node.
        """
        pos_x = self.layer.bounds.origin.x
        if self.italic_angle:
            measure_node = self.leftmost_node()
            italic_compensation = self.compensate_italic_angle(pos_y - measure_node.y)
            pos_x = measure_node.x + italic_compensation
        return int(pos_x)

    def xpos_outline_right(self, pos_y):
        """
        Returns the x position of the rightmost node.
        """
        pos_x = self.layer.bounds.size.width + self.layer.bounds.origin.x
        if self.italic_angle:
            measure_node = self.rightmost_node()
            italic_compensation = self.compensate_italic_angle(pos_y - measure_node.y)
            pos_x = measure_node.x + italic_compensation
        return int(pos_x)

    def xpos_LSB(self, pos_y):
        """
        Returns the x position of the left sidebearing.
        In upright fonts, this will always be 0.
        """
        pos_x = 0
        if self.italic_angle:
            pos_x = self.compensate_italic_angle(pos_y - (self.ypos_xHeight() / 2))
        return int(pos_x)

    def xpos_RSB(self, pos_y):
        """
        Returns the x position of the right sidebearing.
        """
        pos_x = self.layer.width
        if self.italic_angle:
            pos_x = self.compensate_italic_angle(pos_y - (self.ypos_xHeight() / 2))
        return int(pos_x)

    def xpos_apex_top(self, pos_y):
        """
        Returns the x position of the highest node.
        """
        pos_x = self.topmost_node().x
        if self.italic_angle:
            pos_x += self.compensate_italic_angle(pos_y - self.topmost_node().y)
        return int(pos_x)

    def xpos_apex_bottom(self, pos_y):
        """
        Returns the x position of the lowest node.
        """
        pos_x = self.bottommost_node().x
        if self.italic_angle:
            pos_x += self.compensate_italic_angle(pos_y - self.bottommost_node().y)
        return int(pos_x)

    def xpos_width_75(self, pos_y):
        """
        Returns 75% of the advance width.
        """
        pos_x = self.layer.width * 0.75
        if self.italic_angle:
            pos_x += self.compensate_italic_angle(pos_y)
        return int(pos_x)

    def xpos_width_60(self, pos_y):
        """
        Returns 50% of the advance width.
        """
        pos_x = self.layer.width * 0.60
        if self.italic_angle:
            pos_x += self.compensate_italic_angle(pos_y)
        return int(pos_x)

    def xpos_width_50(self, pos_y):
        """
        Returns 50% of the advance width.
        """
        pos_x = self.layer.width * 0.50
        if self.italic_angle:
            pos_x += self.compensate_italic_angle(pos_y)
        return int(pos_x)

    def xpos_width_25(self, pos_y):
        """
        Returns 25% of the advance width.
        """
        pos_x = self.layer.width * 0.25
        if self.italic_angle:
            pos_x += self.compensate_italic_angle(pos_y)
        return int(pos_x)

    def xpos_width_33(self, pos_y):
        """
        Returns 25% of the advance width.
        """
        pos_x = self.layer.width * 0.33
        if self.italic_angle:
            pos_x += self.compensate_italic_angle(pos_y)
        return int(pos_x)

    def xpos_width_66(self, pos_y):
        """
        Returns 25% of the advance width.
        """
        pos_x = self.layer.width * 0.66
        if self.italic_angle:
            pos_x += self.compensate_italic_angle(pos_y)
        return int(pos_x)

    def xpos_indic_right_stem(self, pos_y):
        stem_center = self._get_indic_rightmost_stem(self.layer)
        if stem_center is None:
            stem_center = self.xpos_width_50(self.ypos_indic_headline_top())

        return stem_center

    def xpos_value(self, pos_x, pos_y):
        if self.italic_angle:
            pos_x += self.compensate_italic_angle(pos_y)
        return int(pos_x)

    # Y positions
    # The below methods calculate key y-coordinate positions.

    def ypos_xHeight(self):
        """
        Returns the xheight as defined in the Master's font info panel.
        """
        return Glyphs.font.masters[self.layer.associatedMasterId].xHeight

    def ypos_ascender(self):
        """
        Returns the ascender as defined in the Master's font info panel.
        """
        return Glyphs.font.masters[self.layer.associatedMasterId].ascender

    def ypos_capHeight(self):
        """
        Returns the capHeight as defined in the Master's font info panel.
        """
        return Glyphs.font.masters[self.layer.associatedMasterId].capHeight

    def ypos_descender(self):
        """
        Returns the descender as defined in the Master's font info panel.
        """
        return Glyphs.font.masters[self.layer.associatedMasterId].descender

    def ypos_descender_half(self):
        """
        Returns the mid point between the baseline and the descender, as defined in the Master's font info panel.
        """
        return int(sum((self.ypos_descender(), self.ypos_base_line())) / 2)

    def ypos_base_line(self):
        """
        Returns 0, duh.
        """
        return 0

    def ypos_outline_top(self):
        """
        Returns the y position of the hightest node.
        """
        return self.layer.bounds.size.height + self.layer.bounds.origin.y

    def ypos_outline_middle(self):
        """
        Finds the highest and lowest nodes and returns the y position of their vertical centre.
        """
        return int((self.layer.bounds.size.height / 2) + self.layer.bounds.origin.y)

    def ypos_outline_bottom(self):
        """
        Returns the y position of the lowest node.
        """
        return self.layer.bounds.origin.y

    def ypos_smallcapHeight(self):
        test_g = Glyphs.font.glyphs['h.sc']
        if test_g:
            return test_g.layers[self.layer.associatedMasterId].bounds.size.height
        else:
            return self.ypos_xHeight()

    def ypos_height_25(self):
        """
        Returns 25% of total outline height.
        """
        return int(self.layer.bounds.size.height * 0.25)

    def ypos_height_50(self):
        """
        Returns 50% of total outline height.
        """
        return int(self.layer.bounds.size.height * 0.5)

    def ypos_height_75(self):
        """
        Returns 75% of total outline height.
        """
        return int(self.layer.bounds.size.height * 0.75)

    def ypos_indic_headline_top(self):
        try:
            pos_y = self._indic_headlines[self.layer.parent.script][self.layer.associatedMasterId]['top']
        except KeyError:
            pos_y = self.ypos_xHeight()

        return pos_y


class anchorLister:
    def __init__(self):
        self.glyph_names = {}

    def __call__(self, gname, **kwargs):
        if kwargs:
            self._add_anchor(gname, **kwargs)

        return self.glyph_names.get(gname)

    def _add_anchor(self, gname, **kwargs):
        pos_x_name = kwargs.get('position_x')
        pos_y_name = kwargs.get('position_y')
        pos_x_name_italic = kwargs.get('position_x_italic')
        pos_y_name_italic = kwargs.get('position_y_italic')
        suppress_auto = kwargs.get('suppress_auto', False)
        aname = kwargs.get('name')

        if self.glyph_names.get(gname) is None:
            self.glyph_names[gname] = {'anchors': {}, }

        if aname is None:
            if not self.glyph_names[gname].get('suppress_auto', False):
                self.glyph_names[gname]['suppress_auto'] = suppress_auto

        if not aname:
            return

        self.glyph_names[gname]['anchors'][aname] = {'upright': (pos_x_name, pos_y_name), 'italic': (pos_x_name_italic, pos_y_name_italic), 'suppress_auto': suppress_auto}

    def apply_anchors(self, l, **kwargs):
        gname = l.parent.name

        if kwargs.get('reset'):
            l.anchors = []
            extant_anchors = []
        elif kwargs.get('force'):
            extant_anchors = []
        else:
            extant_anchors = [a.name for a in l.anchors]
        glyph_data = self.glyph_names.get(gname, {}) or {}

        if not glyph_data.get('anchors'):
            self.add_default(l)
            glyph_data = self.glyph_names.get(gname) or {}

        if not glyph_data.get('anchors'):
            if l.parent.subCategory == 'Smallcaps' or '.sc' in gname:
                extant_top_anchors = [a for a in l.anchors if 'top' in a.name]
                l.addMissingAnchors()
                top_anchors = [a for a in l.anchors if 'top' in a.name and a not in extant_top_anchors]

                if top_anchors:
                    lpos = layerPositions(l)
                    for top_anchor in top_anchors:
                        new_x = top_anchor.x + lpos.compensate_italic_angle(lpos.ypos_smallcapHeight() - top_anchor.y) if lpos.italic_angle else top_anchor.x
                        if l.parent.category == 'Mark':
                            if top_anchor.name.startswith('_'):
                                top_anchor.position = NSPoint(new_x, lpos.ypos_smallcapHeight())
                        else:
                            top_anchor.position = NSPoint(new_x, lpos.ypos_smallcapHeight())
            else:
                l.addMissingAnchors()

        else:
            if not glyph_data.get('suppress_auto'):
                l.addMissingAnchors()

            lpos = layerPositions(l)

            for aname, pos_names in glyph_data['anchors'].items():
                if pos_names.get('suppress_auto'):
                    del(l.anchors[aname])
                    continue

                if aname in extant_anchors:
                    continue

                pos_x_name = pos_names['italic'][0] if lpos.italic_angle and pos_names['italic'][0] is not None else pos_names['upright'][0]
                pos_y_name = pos_names['italic'][1] if lpos.italic_angle and pos_names['italic'][1] is not None else pos_names['upright'][1]

                pos_x, pos_y = lpos.get_coords(aname, pos_x_name, pos_y_name)

                if None not in [pos_x, pos_y]:
                    newA = GSAnchor(aname)
                    newA.position = NSPoint(pos_x, pos_y)
                    l.anchors[aname] = newA
            
        print(l.anchors)
        if l.anchors['ogonek']:
            l.anchors['ogonek'].name = '#ogonek'
        if l.anchors['_ogonek']:
            l.anchors['_ogonek'].name = '_#ogonek'

    def add_default(self, l):
        g = l.parent
        if g.script == 'bengali' and g.category == 'Letter':
            self._add_anchor(g.name, name='top', position_x='xpos_indic_right_stem', position_y='ypos_indic_headline_top')
            self._add_anchor(g.name, name='candrabindu', position_x='xpos_indic_right_stem', position_y='ypos_indic_headline_top')
            self._add_anchor(g.name, name='candrabindu_alt', position_x='xpos_indic_right_stem', position_y='ypos_indic_headline_top')
            self._add_anchor(g.name, name='bottom', position_x='xpos_indic_right_stem', position_y=ypos_base_line)
            self._add_anchor(g.name, name='nukta', position_x='xpos_width_25', position_y=ypos_base_line)

        if g.category == 'Mark' and g.subCategory == 'Nonspacing' and l.width == 0 and 'top' in (g.glyphInfo.anchors or []):
            if g.name.endswith('.sc'):
                py = 'ypos_smallcapHeight'
            elif g.name.endswith('.case'):
                py = 'ypos_capHeight'
            else:
                py = 'ypos_xHeight'

            self._add_anchor(g.name, name='_top', position_x='xpos_LSB', position_y=py)
            self._add_anchor(g.name, name='top', position_x='xpos_LSB', position_y='ypos_outline_top')

        if g.category == 'Letter' and g.subCategory == 'Smallcaps' and 'top' in (g.glyphInfo.anchors or []):
            self._add_anchor(g.name, name='top', position_y='ypos_smallcapHeight')


"""
After running the built in .addMissingAnchors(), the script processes any defined custom_anchors.

Use custom_anchors() to add anchors that Glyphs does not add natively,
or to modify the position of native Glyph's anchors.
The first argument is the nice name of the glyph.

Possible keyword arguments -

name:
    The name of the anchor

position_x:
    Must be the name of one of the methods defined in layerPositions().
    Ideally one of the x position methods, but not necessarily.
    Or the name of another glyph with that already contains the same named anchor.
    Or an integer.

position_y:
    Must be the name of one of the methods defined in layerPositions().
    Ideally one of the y position methods, but not necessarily.
    Or the name of another glyph with that already contains the same named anchor.
    Or an integer.

position_x_italic:
    To define an alternative position if the font is italic.
    Mainly for when the glyph takes a different shape compared to the upright, e.g. ge-cy.

position_y_italic:
    To define an alternative position if the font is italic.
    Mainly for when the glyph takes a different shape compared to the upright, e.g. ge-cy.

suppress_auto:
    Prevents Glyphs automatic anchor placement from being called.
"""


custom_anchors = anchorLister()

xpos_outline_right = 'xpos_outline_right'
xpos_outline_center = 'xpos_outline_center'
xpos_outline_left = 'xpos_outline_left'
xpos_apex_bottom = 'xpos_apex_bottom'
xpos_apex_top = 'xpos_apex_top'
xpos_stem_top_center = 'xpos_stem_top_center'
xpos_stem_top_right = 'xpos_stem_top_right'
xpos_stem_bottom_center = 'xpos_stem_bottom_center'
xpos_width_75 = 'xpos_width_75'
xpos_LSB = 'xpos_LSB'
xpos_RSB = 'xpos_RSB'

ypos_capHeight = 'ypos_capHeight'
ypos_base_line = 'ypos_base_line'
ypos_height_25 = 'ypos_height_25'
ypos_height_75 = 'ypos_height_75'
ypos_outline_middle = 'ypos_outline_middle'

# Latin
custom_anchors('A', name='top', position_x=xpos_stem_top_center, position_y=ypos_capHeight)
custom_anchors('A', name='ogonek', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('AE', name='top', position_x=xpos_stem_top_center, position_y=ypos_capHeight)
custom_anchors('C', name='bottom', position_x=xpos_apex_bottom)
custom_anchors('C', name='top', position_x=xpos_apex_top, position_y=ypos_capHeight)
custom_anchors('E', name='top', position_x=xpos_outline_center, position_y=ypos_capHeight)
custom_anchors('E', name='bottom', position_x=xpos_stem_bottom_center, position_y=ypos_base_line)
custom_anchors('F', name='bottom', position_x=xpos_stem_bottom_center, position_y=ypos_base_line)
custom_anchors('F', name='top', position_x=xpos_outline_center, position_y=ypos_capHeight)
custom_anchors('F', name='#bar', position_x=xpos_stem_bottom_center, position_y=ypos_height_25)
custom_anchors('G', name='bottom', position_x=xpos_apex_bottom)
custom_anchors('G', name='top', position_x=xpos_apex_top, position_y=ypos_capHeight)
custom_anchors('H', name='#bar', position_x=xpos_outline_center, position_y=ypos_height_75)
custom_anchors('I', name='top', position_x=xpos_outline_center, position_y=ypos_capHeight)
custom_anchors('I', name='ogonek', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('I', name='topleft', position_x=xpos_outline_left, position_y=ypos_capHeight)
custom_anchors('J', name='bottom', position_x=xpos_apex_bottom, position_y=ypos_base_line)
custom_anchors('J', name='top', position_x=xpos_stem_top_center, position_y=ypos_capHeight)
custom_anchors('K', name='bottom', position_x=xpos_outline_center, position_y=ypos_base_line)
custom_anchors('L', name='bottom', position_x=xpos_outline_center, position_y=ypos_base_line)
custom_anchors('L', name='top', position_x=xpos_stem_top_center, position_y=ypos_capHeight)
custom_anchors('L', name='topright', position_x=xpos_stem_top_right, position_y=ypos_capHeight)
custom_anchors('L', name='#dot', position_x=xpos_width_75, position_y=ypos_outline_middle)
custom_anchors('O', name='bottom', position_x=xpos_apex_bottom, position_y=ypos_base_line)
custom_anchors('O', name='top', position_x=xpos_apex_top, position_y=ypos_capHeight)
custom_anchors('N', name='top', position_x=xpos_outline_center, position_y=ypos_capHeight)
custom_anchors('N', name='bottom', position_x=xpos_outline_center)
custom_anchors('P', name='bottom', position_x=xpos_stem_bottom_center, position_y=ypos_base_line)
custom_anchors('Q', name='top', position_x=xpos_apex_top, position_y=ypos_capHeight)
custom_anchors('S', name='bottom', position_x=xpos_apex_bottom, position_y=ypos_base_line)
custom_anchors('S', name='top', position_x=xpos_apex_top, position_y=ypos_capHeight)
custom_anchors('S', name='#center', position_x=xpos_outline_center, position_y=ypos_outline_middle)
custom_anchors('T', name='top', position_x=xpos_outline_center)
custom_anchors('T', name='#center', position_x=xpos_stem_bottom_center, position_y=ypos_outline_middle)
custom_anchors('T', name='bottom', position_x=xpos_stem_bottom_center, position_y=ypos_base_line)
custom_anchors('U', name='top', position_x=xpos_outline_center, position_y=ypos_capHeight)
custom_anchors('U', name='bottom', position_x=xpos_apex_bottom, position_y=ypos_base_line)
custom_anchors('W', name='top', position_x=xpos_outline_center, position_y=ypos_capHeight)
custom_anchors('W', name='bottom', position_x=xpos_outline_center)
custom_anchors('Y', name='bottom', position_x=xpos_stem_bottom_center, position_y=ypos_base_line)
custom_anchors('Y', name='top', position_x=xpos_outline_center, position_y=ypos_capHeight)
custom_anchors('a', name='ogonek', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('b', name='top', position_x=xpos_outline_center, position_y='ypos_ascender')
custom_anchors('c', name='bottom', position_x=xpos_apex_bottom)
custom_anchors('c', name='top', position_x=xpos_apex_top, position_y='ypos_xHeight')
custom_anchors('d', name='top', position_x=xpos_outline_center, position_y='ypos_ascender')
custom_anchors('d', name='topright', position_x=xpos_stem_top_right, position_y='ypos_ascender')
custom_anchors('e', name='ogonek', position_x=xpos_width_75, position_y=ypos_base_line)
custom_anchors('e', name='bottom', position_x=xpos_apex_bottom)
custom_anchors('e', name='top', position_x=xpos_apex_top)
custom_anchors('f', name='bottom', position_x=xpos_stem_bottom_center, position_y=ypos_base_line)
custom_anchors('f', name='top', position_x=xpos_apex_top, position_y='ypos_ascender')
custom_anchors('germandbls', name='top', position_x=xpos_apex_top, position_y='ypos_ascender')
custom_anchors('i', name='bottom', position_x=xpos_stem_bottom_center)
custom_anchors('i', name='ogonek', position_x='xpos_stem_bottom_right')
custom_anchors('idotless', name='bottom', position_x=xpos_outline_center)
custom_anchors('idotless', name='top', position_x=xpos_outline_center)
custom_anchors('idotless', name='ogonek', suppress_auto=True)
custom_anchors('jdotless', name='bottom', position_x=xpos_outline_center, position_y='ypos_outline_bottom')
custom_anchors('jdotless', name='top', position_x=xpos_stem_top_center, position_y='ypos_xHeight')
custom_anchors('k', name='top', position_x=xpos_stem_top_center, position_y='ypos_ascender')
custom_anchors('l', name='bottom', position_x=xpos_stem_bottom_center, position_y=ypos_base_line)
custom_anchors('l', name='top', position_x=xpos_stem_top_center)
custom_anchors('l', name='#dot', position_x='xpos_RSB', position_y=ypos_outline_middle)
custom_anchors('l', name='topright', position_x=xpos_stem_top_right)
custom_anchors('m', name='top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('m', name='bottom', position_x=xpos_outline_center)
custom_anchors('n', name='top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('n', name='bottom', position_x=xpos_outline_center)
custom_anchors('oe', name='top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('oe', name='bottom', position_x=xpos_outline_center)
custom_anchors('longs', name='top', position_x=xpos_apex_top, position_y='ypos_ascender')
custom_anchors('r', name='bottom', position_x=xpos_stem_bottom_center, position_y=ypos_base_line)
custom_anchors('r', name='top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('s', name='bottom', position_x=xpos_apex_bottom)
custom_anchors('s', name='top', position_x=xpos_apex_top)
custom_anchors('t', name='bottom', position_x=xpos_outline_center, position_y=ypos_base_line)
custom_anchors('t', name='top', position_x=xpos_stem_top_center, position_y='ypos_outline_top')
custom_anchors('t', name='topright', position_x=xpos_stem_top_right, position_y='ypos_ascender')
custom_anchors('u', name='top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('u', name='bottom', position_x=xpos_outline_center)
custom_anchors('u', name='topright', position_x=xpos_stem_top_right, position_y='ypos_xHeight')
custom_anchors('u', name='ogonek', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('y', name='bottom', position_x=xpos_width_75, position_y=ypos_base_line)
custom_anchors('g.sc', name='top', position_x=xpos_apex_top, position_y='ypos_smallcapHeight')
custom_anchors('g.salt.sc', name='top', position_x=xpos_apex_top, position_y='ypos_outline_top')

custom_anchors('a.sc', name='ogonek', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('a.sc', name='top', position_x=xpos_stem_top_center, position_y='ypos_smallcapHeight')
custom_anchors('ae.sc', name='top', position_x=xpos_stem_top_center, position_y='ypos_smallcapHeight')
custom_anchors('e.sc', name='top', position_x=xpos_outline_center, position_y='ypos_smallcapHeight')
custom_anchors('e.sc', name='bottom', position_x=xpos_outline_center, position_y=ypos_base_line)
custom_anchors('e.sc', name='ogonek', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('f.sc', name='top', position_x=xpos_outline_center, position_y='ypos_smallcapHeight')
custom_anchors('i.sc', name='top', position_x=xpos_stem_top_center, position_y='ypos_smallcapHeight')
custom_anchors('i.sc', name='ogonek', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('o.sc', name='top', position_x=xpos_outline_center, position_y='ypos_smallcapHeight')
custom_anchors('t.sc', name='top', position_x=xpos_outline_center, position_y='ypos_outline_top')
custom_anchors('t.sc', name='center', position_x=xpos_outline_center, position_y=ypos_outline_middle)
custom_anchors('t.sc', name='bottom', position_x=xpos_outline_center, position_y='ypos_stem_middle')
custom_anchors('u.sc', name='top', position_x=xpos_outline_center, position_y='ypos_outline_top')
custom_anchors('u.sc', name='center', position_x=xpos_outline_center, position_y=ypos_outline_middle)
custom_anchors('u.sc', name='bottom', position_x=xpos_outline_center, position_y=ypos_base_line)

# Cyrillic
custom_anchors('Che-cy', name='bottomright', suppress_auto=True)
custom_anchors('Che-cy', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('che-cy', name='bottomright', suppress_auto=True)
custom_anchors('che-cy', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('che-cy', name='top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('che-cy.sc', name='bottomright', suppress_auto=True)
custom_anchors('che-cy.sc', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('En-cy', name='bottomright', suppress_auto=True)
custom_anchors('En-cy', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('En-cy', name='topright', position_x=xpos_outline_right, position_y=ypos_capHeight)
custom_anchors('En-cy', name='#bartopright', position_x=xpos_outline_right, position_y=ypos_capHeight)
custom_anchors('El-cy', name='bottomright', suppress_auto=True)
custom_anchors('El-cy', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('en-cy', name='bottomright', suppress_auto=True)
custom_anchors('en-cy', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('en-cy.sc', name='bottomright', suppress_auto=True)
custom_anchors('en-cy.sc', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('Ereversed-cy', name='top', position_x=xpos_apex_top)
custom_anchors('ereversed-cy', name='top', position_x=xpos_apex_top)
custom_anchors('Es-cy', name='bottomright', suppress_auto=True)
custom_anchors('Es-cy', name='#bottomright', position_x=xpos_outline_right)
custom_anchors('es-cy.sc', name='bottomright', suppress_auto=True)
custom_anchors('es-cy.sc', name='#bottomright', position_x=xpos_outline_right)
custom_anchors('es-cy', name='bottomright', suppress_auto=True)
custom_anchors('es-cy', name='#bottomright', position_x=xpos_outline_right)
custom_anchors('Ge-cy', name='bottom', position_x=xpos_stem_bottom_center, position_y=ypos_base_line)
custom_anchors('ge-cy', name='bottom', position_x=xpos_stem_bottom_center, position_y=ypos_base_line, position_x_italic='xpos_apex_bottom')
custom_anchors('Ge-cy', name='bottomright', suppress_auto=True)
custom_anchors('Ge-cy', name='#bottomright', position_x='xpos_stem_bottom_right')
custom_anchors('ge-cy', name='bottomright', suppress_auto=True)
custom_anchors('ge-cy', name='#bottomright', position_x='xpos_stem_bottom_right', position_y=ypos_base_line, position_x_italic='xpos_width_75')
custom_anchors('Ge-cy', name='#center', position_x=xpos_stem_bottom_center, position_y=ypos_outline_middle)
custom_anchors('Ge-cy', name='top', position_x=xpos_outline_center, position_y=ypos_capHeight)
custom_anchors('ge-cy', name='top', position_x=xpos_outline_center, position_y='ypos_xHeight', position_x_italic='xpos_apex_top')
custom_anchors('ge-cy.sc', name='bottom', position_x=xpos_stem_bottom_center, position_y=ypos_base_line)
custom_anchors('ge-cy.sc', name='bottomright', suppress_auto=True)
custom_anchors('ge-cy.sc', name='#bottomright', position_x='xpos_stem_bottom_right')
custom_anchors('ge-cy.sc', name='top', position_x=xpos_outline_center)
custom_anchors('ha-cy', name='bottomright', suppress_auto=True)
custom_anchors('ie-cy', name='top', position_x=xpos_apex_top)
custom_anchors('Ii-cy', name='bottomright', suppress_auto=True)
custom_anchors('Ii-cy', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('ii-cy', name='bottomright', suppress_auto=True)
custom_anchors('ii-cy', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('ii-cy.loclBGR', name='top', position_x=xpos_outline_center)
custom_anchors('ii-cy.loclBGR', name='bottomright', suppress_auto=True)
custom_anchors('ii-cy.loclBGR', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('ii-cy.sc', name='bottomright', suppress_auto=True)
custom_anchors('ii-cy.sc', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('iu-cy', name='top', position_x=xpos_apex_top)

custom_anchors('O-cy', name='top', position_x=xpos_apex_top, position_y=ypos_capHeight)
custom_anchors('Obarred-cy', name='top', position_x=xpos_apex_top, position_y=ypos_capHeight)
custom_anchors('obarred-cy', name='top', position_x=xpos_apex_top, position_y='ypos_xHeight')
custom_anchors('Pe-cy', name='bottomright', suppress_auto=True)
custom_anchors('Pe-cy', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('pe-cy', name='bottomright', suppress_auto=True)
custom_anchors('pe-cy', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('pe-cy.sc', name='bottomright', suppress_auto=True)
custom_anchors('pe-cy.sc', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('Schwa-cy', name='top', position_x=xpos_apex_top)
custom_anchors('schwa-cy', name='top', position_x=xpos_apex_top)
custom_anchors('Sha-cy', name='toothright', position_x=xpos_stem_top_center, position_y=ypos_base_line)
custom_anchors('sha-cy', name='top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('Shha-cy', name='bottomright', suppress_auto=True)
custom_anchors('Shha-cy', name='#bottomright', position_x=xpos_outline_right)
custom_anchors('shha-cy.sc', name='bottomright', suppress_auto=True)
custom_anchors('shha-cy.sc', name='#bottomright', position_x=xpos_outline_right)
custom_anchors('Te-cy', name='bottomright', suppress_auto=True)
custom_anchors('Te-cy', name='#bottomright', position_x='xpos_stem_bottom_right', position_y=ypos_base_line)
custom_anchors('te-cy', name='bottomright', suppress_auto=True)
custom_anchors('te-cy', name='#bottomright', position_x='xpos_stem_bottom_right', position_y=ypos_base_line)
custom_anchors('te-cy.sc', name='bottomright', suppress_auto=True)
custom_anchors('te-cy.sc', name='#bottomright', position_x='xpos_stem_bottom_right', position_y=ypos_base_line)
custom_anchors('Tsebase-cy', name='#toothcenter', position_x=xpos_outline_center)
custom_anchors('tsebase-cy', name='#toothcenter', position_x=xpos_outline_center, position_y=ypos_base_line)
custom_anchors('Tsebase-cy', name='bottom', position_x=xpos_outline_center)
custom_anchors('Tsebase-cy', name='toothright', position_x=xpos_stem_top_center)
custom_anchors('tsebase-cy', name='toothright', position_x=xpos_stem_top_center)
custom_anchors('Ze-cy', name='bottom', position_x=xpos_outline_center, position_y=ypos_base_line)
custom_anchors('Ze-cy', name='top', position_x=xpos_apex_top)
custom_anchors('Omega-cy', name='top', position_x=xpos_outline_center, position_y=ypos_capHeight)
custom_anchors('omega-cy', name='top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('Ha-cy', name='#center', position_x=xpos_outline_center, position_y=ypos_outline_middle)
custom_anchors('ha-cy', name='#center', position_x=xpos_outline_center, position_y=ypos_outline_middle)
custom_anchors('ka-cy.loclBGR', name='top', position_x=xpos_stem_top_center, position_y='ypos_ascender')
custom_anchors('pe-cy.loclBGR', name='bottomright', suppress_auto=True)
custom_anchors('pe-cy.loclBGR', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('te-cy.loclBGR', name='bottomright', suppress_auto=True)
custom_anchors('te-cy.loclBGR', name='#bottomright', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('zhe-cy.loclBGR', name='top', position_x=xpos_outline_center, position_y='ypos_ascender')
custom_anchors('zhe-cy.loclBGR', name='#bottomright', position_x=xpos_outline_right)
custom_anchors('zhe-cy.loclBGR', name='bottomright', suppress_auto=True)
custom_anchors('ze-cy.loclBGR', name='bottom', position_x=xpos_apex_bottom, position_y='ypos_outline_bottom')

# Greek
custom_anchors('Alpha', name='topleft', position_x=xpos_outline_left)
custom_anchors('Epsilon', name='topleft', position_x=xpos_outline_left)
custom_anchors('Rho', name='topleft', position_x=xpos_outline_left)
custom_anchors('Omega', name='topleft', position_x=xpos_outline_left)
custom_anchors('Omicron', name='topleft', position_x=xpos_outline_left)
custom_anchors('Eta', name='topleft', position_x=xpos_outline_left)
custom_anchors('Eta', name='bottom', position_x=xpos_outline_center)
custom_anchors('Iota', name='top', position_x=xpos_outline_center)
custom_anchors('epsilon', name='top', position_x=xpos_apex_top)
custom_anchors('Iota', name='topleft', position_x=xpos_outline_left)
custom_anchors('Upsilon', name='topleft', position_x=xpos_outline_left)
custom_anchors('Upsilon', name='top', position_x=xpos_outline_center)
custom_anchors('iota', name='top', position_x=xpos_stem_top_center, position_y='ypos_xHeight')


# Latin Marks
custom_anchors('caron.alt', name='_topright', position_x=xpos_outline_left, position_y='ypos_outline_top')
custom_anchors('caroncomb.alt', name='_topright', position_x=xpos_LSB, position_y='ypos_outline_top')
custom_anchors('cedillacomb', name='_bottom', position_x=xpos_stem_top_center, position_y=ypos_base_line)
custom_anchors('_part.bar', name='_#bartopleft', position_x='xpos_stem_top_left', position_y='ypos_outline_top')
custom_anchors('_part.bar', name='_#barleft', position_x='xpos_stem_top_left', position_y=ypos_outline_middle)
custom_anchors('_part.bar', name='_#barbottomleft', position_x='xpos_stem_bottom_left', position_y='ypos_outline_bottom')
custom_anchors('_part.bar', name='_#bartopright', position_x=xpos_stem_top_right, position_y='ypos_outline_top')
custom_anchors('_part.bar', name='_#barright', position_x=xpos_stem_top_right, position_y=ypos_outline_middle)
custom_anchors('_part.bar', name='_#barbottomright', position_x='xpos_stem_bottom_right', position_y='ypos_outline_bottom')
custom_anchors('_part.bar', name='_#topright', position_x='xpos_stem_top_left', position_y='ypos_outline_top')
custom_anchors('_part.bar', name='_#right', position_x='xpos_stem_top_left', position_y=ypos_outline_middle)
custom_anchors('_part.bar', name='_#bottomright', position_x='xpos_stem_bottom_left', position_y='ypos_outline_bottom')
custom_anchors('_part.bar', name='_#topleft', position_x=xpos_stem_top_right, position_y='ypos_outline_top')
custom_anchors('_part.bar', name='_#left', position_x=xpos_stem_top_right, position_y=ypos_outline_middle)
custom_anchors('_part.bar', name='_#bottomleft', position_x='xpos_stem_bottom_right', position_y='ypos_outline_bottom')
custom_anchors('_part.bar', name='_#bar', position_x=xpos_outline_center, position_y=ypos_outline_middle)
custom_anchors('_part.bar', name='_#center', position_x=xpos_outline_center, position_y=ypos_outline_middle)
custom_anchors('_part.bar', name='length', position_x='xpos_stem_bottom_right', position_y='ypos_outline_bottom')
custom_anchors('_part.barvertical', name='_center', position_x=xpos_outline_center, position_y=ypos_outline_middle)
custom_anchors('toothright-cy', name='_toothright', position_x=xpos_outline_left, position_y=ypos_base_line)
custom_anchors('toothright-cy', name='_bottomright', position_x=xpos_outline_left, position_y=ypos_base_line)
custom_anchors('Toothcenter-cy', name='_#toothcenter', position_x=xpos_outline_center, position_y=ypos_base_line)
custom_anchors('toothcenter-cy', name='_#toothcenter', position_x=xpos_outline_center, position_y=ypos_base_line)
custom_anchors('dotaccentcomb', name='_#dot', position_x=xpos_outline_center, position_y=ypos_outline_middle)
custom_anchors('circumflex_acute', name='_top', position_x='xpos_width_50', position_y='ypos_xHeight')
custom_anchors('circumflex_acutecomb', name='_top', position_x='xpos_width_50', position_y='ypos_xHeight')
custom_anchors('circumflex_grave', name='_top', position_x='xpos_width_50', position_y='ypos_xHeight')
custom_anchors('circumflex_gravecomb', name='_top', position_x='xpos_width_50', position_y='ypos_xHeight')
custom_anchors('circumflex_hookabove', name='_top', position_x='xpos_width_50', position_y='ypos_xHeight')
custom_anchors('circumflex_hookabovecomb', name='_top', position_x='xpos_width_50', position_y='ypos_xHeight')
custom_anchors('circumflex_tilde', name='_top', position_x='xpos_width_50', position_y='ypos_xHeight')
custom_anchors('circumflex_tildecomb', name='_top', position_x='xpos_width_50', position_y='ypos_xHeight')
custom_anchors('circumflex_acute.case', name='_top', position_x='xpos_width_50', position_y=ypos_capHeight)
custom_anchors('circumflex_acutecomb.case', name='_top', position_x='xpos_width_50', position_y=ypos_capHeight)
custom_anchors('circumflex_grave.case', name='_top', position_x='xpos_width_50', position_y=ypos_capHeight)
custom_anchors('circumflex_gravecomb.case', name='_top', position_x='xpos_width_50', position_y=ypos_capHeight)
custom_anchors('circumflex_hookabove.case', name='_top', position_x='xpos_width_50', position_y=ypos_capHeight)
custom_anchors('circumflex_hookabovecomb.case', name='_top', position_x='xpos_width_50', position_y=ypos_capHeight)
custom_anchors('circumflex_tilde.case', name='_top', position_x='xpos_width_50', position_y=ypos_capHeight)
custom_anchors('circumflex_tildecomb.case', name='_top', position_x='xpos_width_50', position_y=ypos_capHeight)
custom_anchors('breve_acute', name='_top', position_x=xpos_apex_bottom, position_y='ypos_xHeight')
custom_anchors('breve_acutecomb', name='_top', position_x=xpos_apex_bottom, position_y='ypos_xHeight')
custom_anchors('breve_grave', name='_top', position_x=xpos_apex_bottom, position_y='ypos_xHeight')
custom_anchors('breve_gravecomb', name='_top', position_x=xpos_apex_bottom, position_y='ypos_xHeight')
custom_anchors('breve_hook', name='_top', position_x=xpos_apex_bottom, position_y='ypos_xHeight')
custom_anchors('breve_hookcomb', name='_top', position_x=xpos_apex_bottom, position_y='ypos_xHeight')
custom_anchors('breve_tilde', name='_top', position_x=xpos_apex_bottom, position_y='ypos_xHeight')
custom_anchors('breve_tildecomb', name='_top', position_x=xpos_apex_bottom, position_y='ypos_xHeight')
custom_anchors('breve_acute.case', name='_top', position_x=xpos_apex_bottom, position_y=ypos_capHeight)
custom_anchors('breve_acutecomb.case', name='_top', position_x=xpos_apex_bottom, position_y=ypos_capHeight)
custom_anchors('breve_grave.case', name='_top', position_x=xpos_apex_bottom, position_y=ypos_capHeight)
custom_anchors('breve_gravecomb.case', name='_top', position_x=xpos_apex_bottom, position_y=ypos_capHeight)
custom_anchors('breve_hook.case', name='_top', position_x=xpos_apex_bottom, position_y=ypos_capHeight)
custom_anchors('breve_hookcomb.case', name='_top', position_x=xpos_apex_bottom, position_y=ypos_capHeight)
custom_anchors('breve_tilde.case', name='_top', position_x=xpos_apex_bottom, position_y=ypos_capHeight)
custom_anchors('breve_tildecomb.case', name='_top', position_x=xpos_apex_bottom, position_y=ypos_capHeight)
custom_anchors('titlocomb-cy', name='_top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('palatalizationcomb-cy', name='_top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('dasiapneumatacomb-cy', name='_top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('psilipneumatacomb-cy', name='_top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('pokrytiecomb-cy', name='_top', position_x=xpos_outline_center, position_y='ypos_xHeight')
custom_anchors('dotaccent.case', name='_top', position_x=xpos_outline_center, position_y=ypos_capHeight)

custom_anchors('acute', name='_top', position_x='xpos_stem_bottom_right', position_y='ypos_xHeight')
custom_anchors('acute.case', name='_top', position_x='xpos_stem_bottom_right', position_y=ypos_capHeight)
custom_anchors('acute.sc', name='_top', position_x='xpos_stem_bottom_right', position_y='ypos_smallcapHeight')
custom_anchors('tonos.cap', name='_topleft', position_x=xpos_outline_right, position_y='ypos_outline_top')
custom_anchors('commaaccentcomb', name='_bottom')
custom_anchors('commaaccentcomb', name='bottom')
custom_anchors('ogonekcomb', name='_ogonek', suppress_auto=True)
custom_anchors('ogonekcomb', name='_#ogonek', position_x=xpos_outline_right, position_y=ypos_base_line)
custom_anchors('dotbelowcomb', name='_bottom')
custom_anchors('dotbelowcomb', name='bottom')
custom_anchors('periodcentered.loclCAT', name='#dot', position_x=xpos_RSB, position_y=ypos_outline_middle)

# Other
custom_anchors('dottedCircle', name='top', position_x=xpos_outline_center, position_y='ypos_outline_top')
custom_anchors('dottedCircle', name='bottom', position_x=xpos_outline_center, position_y='ypos_outline_bottom')

custom_anchors('ca-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('ca-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('kha-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('kha-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('cha-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('cha-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('ja-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('ja-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('nya-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('nya-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('ta-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('ta-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('tha-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('tha-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('dha-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('dha-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('na-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('na-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('ba-deva', name='candra', position_x='xpos_width_50', position_y='ypos_xHeight')
custom_anchors('ba-deva', name='anusvara', position_x='xpos_width_50', position_y='ypos_xHeight')

custom_anchors('bha-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('bha-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('la-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('la-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('va-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('va-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('sha-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('sha-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('jja-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('jja-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')


custom_anchors('k_ss_ra-deva', suppress_auto=True)
custom_anchors('k_ss_ra-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('k_ss_ra-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')

custom_anchors('k_ss_ra-deva', name='candra', position_x='xpos_width_60', position_y='ypos_xHeight')
custom_anchors('k_ss_ra-deva', name='anusvara', position_x='xpos_width_60', position_y='ypos_xHeight')


if font_has('armenian'):
    try:
        from AddAnchors_definitions.AnchorsArmenian import ArmenianAnchors
        for gn, adefs in ArmenianAnchors.anchors.items():
            for adef in adefs:
                custom_anchors(gn, **adef)
    except ImportError:
        print('Could not find the externally defined Armenian Anchors')

if font_has('bengali'):
    try:
        from AddAnchors_definitions.AnchorsBengali import BengaliAnchors
        for gn, adefs in BengaliAnchors.anchors.items():
            for adef in adefs:
                custom_anchors(gn, **adef)
    except ImportError:
        print('Could not find the externally defined Bengali Anchors')

if font_has('devanagari'):
    try:
        from AddAnchors_definitions.AnchorsDevanagari import DevanagariAnchors
        for gn, adefs in DevanagariAnchors.anchors.items():
            for adef in adefs:
                custom_anchors(gn, **adef)
    except ImportError:
        print('Could not find the externally defined Bengali Anchors')

if __name__ == "__main__":
    for g in [x.parent for x in Glyphs.font.selectedLayers]:
        for l in g.layers:
            try:
                custom_anchors.apply_anchors(l, force=replace_anchors, reset=reset_anchors)
            except:  # noqa: E722
                Glyphs.clearLog()
                Glyphs.showMacroWindow()
                raise
