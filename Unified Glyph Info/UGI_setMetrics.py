# MenuTitle: Set UGI Metrics
# -*- coding: utf-8 -*-
__doc__ = """
Sets the metrics keys for the selected glyphs using the UGI.
"""

from UGI.unifiedglyphinfo import italic_angle
from AppKit import NSEvent

from UGI.UGI_importer import import_scripts
unified_infos = import_scripts(Glyphs.font)

Glyphs.clearLog()
# Glyphs.showMacroWindow()

# --- From mekkablue ---
keysPressed = NSEvent.modifierFlags()
capslockKey = 65536
capslockKeyPressed = keysPressed & capslockKey == capslockKey
# ---


def make_sc_2_uc_name(gn):
    return gn[0].upper() + gn[1:].replace('.sc', '')


def make_smallcap_name(gn):
    arbitrary_initial_letters_len = 3
    try:
        return gn[:arbitrary_initial_letters_len].lower() + gn[arbitrary_initial_letters_len:] + '.sc'
    except TypeError:
        return gn


for sl in Glyphs.font.selectedLayers:
    is_smallcapped = False
    g = sl.parent
    ugi = unified_infos.get(g.name)

    if ugi is None:
        uc_name = g.name
        ugi = unified_infos.get(make_sc_2_uc_name(g.name))
        if ugi is not None:
            is_smallcapped = True

    if ugi is not None:
        if not ugi.has_metrics and not is_smallcapped:
            ugi = unified_infos.get(make_sc_2_uc_name(g.name))
            is_smallcapped = True
            if ugi is None:
                continue

        if italic_angle(sl):
            metrics_left = ugi.metrics_italic_left or ugi.metrics_left
            metrics_right = ugi.metrics_italic_right or ugi.metrics_right
            metrics_width = ugi.metrics_italic_width or ugi.metrics_width
        else:
            metrics_left = ugi.metrics_left
            metrics_right = ugi.metrics_right
            metrics_width = ugi.metrics_width

        g.leftMetricsKey = None
        g.rightMetricsKey = None
        g.widthMetricsKey = None
        if is_smallcapped:
            metrics_left = make_smallcap_name(metrics_left)
            metrics_right = make_smallcap_name(metrics_right)
            metrics_width = make_smallcap_name(metrics_width)

        if metrics_left == g.name:
            metrics_left = None
        if metrics_right == g.name:
            metrics_right = None
        if metrics_width == g.name:
            metrics_width = None

        try:
            if Glyphs.font.glyphs[metrics_left] is None and not metrics_left.startswith('='):
                metrics_left = None
        except AttributeError:
            pass

        try:
            if Glyphs.font.glyphs[metrics_right] is None and not metrics_right.startswith('='):
                metrics_right = None
        except AttributeError:
            pass

        try:
            if Glyphs.font.glyphs[metrics_width] is None and not metrics_width.startswith('='):
                metrics_width = None
        except AttributeError:
            pass

        if metrics_left is not None:
            if isinstance(metrics_left, int):
                for l in g.layers:
                    l.LSB = metrics_left
            else:
                g.leftMetricsKey = metrics_left

        if metrics_width is not None:
            if isinstance(metrics_width, int):
                for l in g.layers:
                    l.width = metrics_width
            else:
                g.widthMetricsKey = metrics_width

        if metrics_right is not None and (metrics_width is None or metrics_left is None):
            if isinstance(metrics_right, int):
                for l in g.layers:
                    l.RSB = metrics_right
            else:
                g.rightMetricsKey = metrics_right

    elif '_' in g.name:
        baseName1, _, styleSuffix = g.name.partition('.')

        if styleSuffix and styleSuffix not in ['liga', 'dlig', 'rlig']:
            styleSuffix = '.' + styleSuffix
        else:
            styleSuffix = ''

        baseName, x, suffix = baseName1.partition('-')
        if suffix:
            suffix = '-' + suffix

        nameParts = baseName.split('_')
        leftGN = nameParts[0] + suffix + styleSuffix
        rightGN = nameParts[-1] + suffix + styleSuffix

        if Glyphs.font.glyphs[leftGN]:
            g.leftMetricsKey = leftGN
        if Glyphs.font.glyphs[rightGN]:
            g.rightMetricsKey = rightGN

    elif g.category == 'Mark':
        g.leftMetricsKey = '=50'
        g.rightMetricsKey = '=50'

    for l in g.layers:
        l.syncMetrics()
