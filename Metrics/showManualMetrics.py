# MenuTitle: Show Glyphs with Manual Metrics
# -*- coding: utf-8 -*-
__doc__ = """
Opens a tab listing glyphs in the selection with manual metrics.
"""

Glyphs.clearLog()

alphabetical = False


def hasMetricsKey(g):
    b = False
    if (g.leftMetricsKey or g.rightMetricsKey):
        b = True
    else:
        for l in g.layers:
            if (l.leftMetricsKey or l.rightMetricsKey):
                b = True
    return b


def hasAutoMetrics(g):
    b = False
    if not (g.leftMetricsKey or g.rightMetricsKey):
        for l in g.layers:
            if isAutoMetrics(l):
                b = True
                break
    return b


def isAutoMetrics(l):
    b = False
    if not l.leftMetricsKey or l.rightMetricsKey:
        if not l.paths and all([c.automaticAlignment for c in l.components if c.component.category != 'Mark']):
            b = True

    return b


def hasManualMetrics(g):
    b = True
    if all([g.leftMetricsKey, g.rightMetricsKey]):
        b = False

    if not b:
        for l in g.layers:
            if any([l.leftMetricsKey, l.rightMetricsKey]) and not all([l.leftMetricsKey, l.rightMetricsKey]):
                b = True

    if all([isAutoMetrics(l) for l in g.layers]):
        b = False

    return b


def isOnlyManual(g):
    return not any([hasMetricsKey(g), hasAutoMetrics(g)])


def isOnlyMetrics(g):
    return not any([hasManualMetrics(g), hasAutoMetrics(g)])


strings = []
for g in [x.parent for x in Glyphs.font.selectedLayers]:
    if hasManualMetrics(g):
        strings.append('/{0}  '.format(g.name))

if alphabetical:
    strings.sort()

string = ''.join(strings)
Glyphs.font.newTab(string)
