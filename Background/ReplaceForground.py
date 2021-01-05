# MenuTitle: Replace Foreground with Background Paths
# -*- coding: utf-8 -*-
__doc__ = """
Replaces only the paths in the current active layer with those from the background.
"""


for l in Glyphs.font.selectedLayers[0].parent.layers:
    for pi in reversed(range(len(l.paths))):
        del l.paths[pi]

    for p in l.background.paths:
        l.paths.append(p)
