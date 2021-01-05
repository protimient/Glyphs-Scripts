# MenuTitle: Copy Current Layer From Other Font
# -*- coding: utf-8 -*-
__doc__ = """
With 2 open fonts, copies the corresponding layer (either name or brace values) from the other font to the currently selected layer(s).
"""

import re
import copy

Glyphs.clearLog()
# Glyphs.showMacroWindow()

try:
    other_font = [f for f in Glyphs.fonts if f != Glyphs.font][0]
except IndexError:
    Glyphs.showNotification('Copy Current Layer From Other Font', 'You only have 1 font open!')


def get_values_from_brace_layer(layer_name):
    try:
        this_layer_val = re.search('{(.+)}', layer_name).group(1)
    except AttributeError:
        return None

    return tuple(float(x) for x in this_layer_val.split(','))


def get_other_master(this_layer):
    for m in other_font.masters:
        if this_layer.name == m.name:
            return m


def get_other_layer(this_layer, other_g):
    for l in other_g.layers:
        if l.name == this_layer.name:
            return l

    brace_val = get_values_from_brace_layer(this_layer.name)
    if brace_val:
        for l in other_g.layers:
            if get_values_from_brace_layer(l.name) == brace_val:
                return l

    if this_layer.layerId == this_layer.associatedMasterId:
        this_m_i = Glyphs.font.masters.index(this_layer.master)
        other_m_id = other_font.masters[this_m_i].id
        return other_g.layers[other_m_id]


for l in Glyphs.font.selectedLayers:
    other_m = get_other_master(l)
    other_g = other_font.glyphs[l.parent.name]
    other_l = get_other_layer(l, other_g)

    if other_l:
        if other_l.paths:
            l.paths = copy.copy(other_l.paths)

        if other_l.components:
            l.components = copy.copy(other_l.components)

        if other_l.anchors:
            l.anchors = copy.copy(other_l.anchors)

        if other_l.LSB is not None:
            l.LSB = copy.copy(other_l.LSB)

        if other_l.width is not None:
            l.width = copy.copy(other_l.width)

        if other_l.leftMetricsKey is not None:
            l.leftMetricsKey = copy.copy(other_l.leftMetricsKey)

        if other_l.rightMetricsKey is not None:
            l.rightMetricsKey = copy.copy(other_l.rightMetricsKey)

        if other_l.widthMetricsKey is not None:
            l.widthMetricsKey = copy.copy(other_l.widthMetricsKey)

        if other_l.hints:
            l.hints = copy.copy(other_l.hints)
