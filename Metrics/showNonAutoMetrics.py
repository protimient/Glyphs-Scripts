# MenuTitle: Show Non-Auto Metrics
# -*- coding: utf-8 -*-
__doc__ = """
Opens a tab listing glyphs in the selection with automatic metrics.
"""

Glyphs.clearLog()

Doc = Glyphs.currentDocument


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
            if not l.leftMetricsKey or l.rightMetricsKey:
                if not l.paths and all([c.automaticAlignment for c in l.components]):
                    b = True
                    break
    return b


def hasManualMetrics(g):
    b = True
    if all([g.leftMetricsKey, g.rightMetricsKey]):
        b = False

    if not b:
        for l in g.layers:
            if any([l.leftMetricsKey, l.rightMetricsKey]) and not all([l.leftMetricsKey, l.rightMetricsKey]):
                b = True

    if hasAutoMetrics(g):
        b = False

    return b


def isOnlyManual(g):
    return not any([hasMetricsKey(g), hasAutoMetrics(g)])


def isOnlyMetrics(g):
    return not any([hasManualMetrics(g), hasAutoMetrics(g)])


strings = []
for g in [x.parent for x in Glyphs.font.selectedLayers]:
    if not hasAutoMetrics(g):
        strings.append('/{0}  '.format(g.name))

string = ''.join(sorted(strings))
Doc.windowController().addTabWithString_(string)
