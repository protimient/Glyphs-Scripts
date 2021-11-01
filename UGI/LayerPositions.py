import math
import re
from collections import defaultdict
from GlyphsApp import Glyphs, OFFCURVE, GSLayer
from Foundation import NSPoint


class layerPositions:
    def __init__(self, l, all_indic_headlines=None):
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
        self._indic_headlines = all_indic_headlines or self._get_all_indic_headlines()
        self._indic_stem_widths = self._get_indic_stem_widths()

    def compensate_italic_angle(self, pos_y):
        if not self.italic_angle:
            return 0
        return round(math.tan(math.radians(self.italic_angle)) * pos_y)

    def all_layers_nodes(self):
        if self._all_layer_nodes is None:
            self._all_layer_nodes = [n for p in self.layer_flat.paths for n in p.nodes if n.type != OFFCURVE]
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

    def get_coords(self, pos_x_name, pos_y_name):
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
        if type(pos_y_name) in [int, float]:
            pos_y = pos_y_name

        elif pos_y_name is None:
            pos_y = None

        else:
            pos_y = self.layer_metrics.get(self.layer.layerId, {}).get(pos_y_name)
            if pos_y is None:
                try:
                    pos_y = getattr(self, pos_y_name)()
                except (AttributeError, IndexError):
                    pass

                self.layer_metrics[self.layer.layerId][pos_y_name] = pos_y

        pos_x = 0
        if type(pos_x_name) in [int, float]:
            pos_x = self.xpos_value(pos_x_name, pos_y)

        elif pos_x_name is None:
            pos_x = None

        else:
            if not self.italic_angle:
                pos_x = self.layer_metrics.get(self.layer.layerId, {}).get(pos_x_name)
            else:
                pos_x = None

            if pos_x is None:
                try:
                    pos_x = getattr(self, pos_x_name)(pos_y)
                except (AttributeError, IndexError):
                    pass

                self.layer_metrics[self.layer.layerId][pos_x_name] = pos_x

        return pos_x, pos_y

    # def _get_anchor_from_other_glyph(self, layer, aname):
    #     gname = self.aname_sub.sub('', pos_y_name)
    #     g = Glyphs.font.glyphs[gname]
    #     if g is not None:
    #         layer = g.layers[self.layer.associatedMasterId]
    #         _, pos_y = self._get_anchor_pos(layer, aname)
    #         pos_y_name += aname
    #     else:
    #         _, pos_y = self._get_anchor_pos(self.layer, pos_y_name)

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
                    top, bottom = self._get_indic_headline(l)
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
    def _get_indic_headline(layer):
        """
        Calculates the top and bottom y-values for the indic headline.
        """
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
    def _check_coord(comp_this, comp_against, fuzziness=2):
        """
        Checks whether a value is within the bounds of fuzziness.
        """
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
                if self._check_coord(coord_distance, stem_width, fuzziness=fuzziness):
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
