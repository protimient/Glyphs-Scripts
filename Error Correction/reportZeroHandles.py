# MenuTitle: Report Zero Handles
# -*- coding: utf-8 -*-
__doc__ = """
Reports zero size handles. Also selects the handles.
"""

from collections import defaultdict

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

eff_layers = defaultdict(list)


def reportZeroHandle(l, node):
    myLayer.selection.append(node)
    if l not in eff_layers[l.name]:
        eff_layers[l.name].append(l)


Glyphs.font.disableUpdateInterface()

for myGlyph in Glyphs.font.glyphs:
    for myLayer in myGlyph.layers:
        myLayer.selection = []
        for myPath in myLayer.paths:
            myNodes = myPath.nodes
            nodeCount = len(myNodes)

            for nodeIndex in range(nodeCount):
                currentNode = myNodes[nodeIndex]

                if currentNode.type == OFFCURVE:
                    previousIndex = nodeIndex - 1
                    previousNode = myNodes[previousIndex]
                    if previousNode.type != OFFCURVE:
                        if previousNode.x == currentNode.x and previousNode.y == currentNode.y:
                            reportZeroHandle(myLayer, currentNode)

                    else:
                        nextIndex = nodeIndex + 1
                        nextNode = myNodes[nextIndex]
                        if nextNode.type != OFFCURVE:
                            if nextNode.x == currentNode.x and nextNode.y == currentNode.y:
                                reportZeroHandle(myLayer, currentNode)


layers = []
for x in eff_layers.values():
    layers += [GSControlLayer(10)]
    layers += x

if layers:
    Glyphs.font.newTab()
    Glyphs.font.tabs[-1].layers = layers
else:
    Glyphs.showNotification('Zero Size Handles', 'All good. No glyphs have zero handles.')

Glyphs.font.enableUpdateInterface()
