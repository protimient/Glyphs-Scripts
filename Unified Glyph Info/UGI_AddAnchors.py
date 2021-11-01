# MenuTitle: Add UGI anchors
# -*- coding: utf-8 -*-
from AppKit import NSEvent
from UGI import LayerPositions
__doc__ = """
Adds Anchors using the UGI.
"""

from UGI.UGI_importer import import_scripts
unified_infos = import_scripts(Glyphs.font)

Glyphs.clearLog()
# Glyphs.showMacroWindow()

# --- From mekkablue ---
keysPressed = NSEvent.modifierFlags()
capslockKey = 65536
capslockKeyPressed = keysPressed & capslockKey == capslockKey
shiftKey = 131072
shiftKeyPressed = keysPressed & shiftKey == shiftKey
# ---

for sl in Glyphs.font.selectedLayers:
    g = sl.parent
    ugi = unified_infos.get(g.name)

    if not ugi.anchors:
        if g.script == 'devanagari' and g.category == 'Letter':
            ugi = unified_infos.get('default-deva')

        test_g_name = g.name.partition('.')[0]
        ugi = unified_infos.get(test_g_name)

    for l in g.layers:
        if capslockKeyPressed:
            l.anchors = []

        extant_anchors = [a.name for a in l.anchors]

        if g.script not in ['devanagari']:
            l.addMissingAnchors()

        suppressable_anchors = []
        if ugi:
            lp = LayerPositions.layerPositions(l)
            for aname, parameters in ugi.anchors.items():
                if shiftKeyPressed:
                    if aname in extant_anchors:
                        continue

                if l.anchors[aname] is None:
                    l.anchors[aname] = GSAnchor()

                if parameters.get('suppress_auto'):
                    suppressable_anchors.append(aname)
                    continue

                apos = lp.get_coords(parameters.get('position_x', l.anchors[aname].x), parameters.get('position_y', l.anchors[aname].y))
                if apos is None:
                    apos = (lp.xpos_outline_center, lp.ypos_xHeight)

                if apos[0] is not None:
                    l.anchors[aname].x = apos[0]

                if apos[1] is not None:
                    l.anchors[aname].y = apos[1]

        for an in suppressable_anchors:
            del(l.anchors[an])
