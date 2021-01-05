# MenuTitle: Swap Foreground with Background
# -*- coding: utf-8 -*-
__doc__ = """
Copies the background to the active layer and puts the active layer in the background.
"""

for l in Glyphs.font.selectedLayers[0].parent.layers:
    old_paths = []
    for p in l.paths:
        np = GSPath()
        for n in p.nodes:
            nn = GSNode()
            nn.type = n.type
            nn.connection = n.connection
            nn.setPosition_((n.x, n.y))
            np.addNode_(nn)

        np.closed = p.closed
        old_paths.append(np)

    for pi in reversed(range(len(l.paths))):
        del l.paths[pi]

    for p in l.background.paths:
        l.paths.append(p)

    for pi in reversed(range(len(l.background.paths))):
        del l.background.paths[pi]

    for p in old_paths:
        l.background.paths.append(p)
