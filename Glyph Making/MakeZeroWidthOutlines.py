# MenuTitle: Make Zero-Width Outlines
__doc__ = """
Makes generic outline for: lefttorightmark, righttoleftmark, zerowidthnonjoiner, zerowidthjoiner, lefttorightembedding,
righttoleftembedding, popdirectionalformatting, lefttorightoverride, righttoleftoverride
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()


class makeGlyphs():
    def __init__(self):
        self.glyph_outlines = {
            # lefttorightmark
            '200E': [
                [
                    ((90.0, 69.0), LINE, 0),
                    ((21.0, 138.0), LINE, 0),
                    ((4.0, 120.0), LINE, 0),
                    ((45.0, 81.0), LINE, 0),
                    ((-80.0, 81.0), LINE, 0),
                    ((-80.0, 58.0), LINE, 0),
                    ((45.0, 58.0), LINE, 0),
                    ((4.0, 18.0), LINE, 0),
                    ((21.0, 0.0), LINE, 0)
                ]
            ],
            # righttoleftmark
            '200F': [
                [
                    ((-4.0, 24.0), LINE, 0),
                    ((-45.0, 64.0), LINE, 0),
                    ((80.0, 64.0), LINE, 0),
                    ((80.0, 87.0), LINE, 0),
                    ((-45.0, 87.0), LINE, 0),
                    ((-4.0, 126.0), LINE, 0),
                    ((-21.0, 144.0), LINE, 0),
                    ((-90.0, 75.0), LINE, 0),
                    ((-21.0, 6.0), LINE, 0)
                ]
            ],
            # zerowidthnonjoiner
            '200C': [
                [
                    ((0.0, 51.0), LINE, 0),
                    ((52.0, 0.0), LINE, 0),
                    ((68.0, 16.0), LINE, 0),
                    ((16.0, 68.0), LINE, 0),
                    ((68.0, 120.0), LINE, 0),
                    ((52.0, 136.0), LINE, 0),
                    ((0.0, 84.0), LINE, 0),
                    ((-53.0, 137.0), LINE, 0),
                    ((-69.0, 120.0), LINE, 0),
                    ((-17.0, 68.0), LINE, 0),
                    ((-69.0, 16.0), LINE, 0),
                    ((-53.0, -1.0), LINE, 0)
                ]
            ],
            # zerowidthjoiner
            '200D': [
                [
                    ((-76.0, 0.0), LINE, 0),
                    ((-76.0, 46.0), LINE, 0),
                    ((77.0, 46.0), LINE, 0),
                    ((77.0, 0.0), LINE, 0),
                    ((100.0, 0.0), LINE, 0),
                    ((100.0, 69.0), LINE, 0),
                    ((-99.0, 69.0), LINE, 0),
                    ((-99.0, 0.0), LINE, 0)
                ]
            ],
            # lefttorightembedding
            '202A': [
                [
                    ((95.0, 69.0), LINE, 0),
                    ((26.0, 137.0), LINE, 0),
                    ((10.0, 120.0), LINE, 0),
                    ((50.0, 81.0), LINE, 0),
                    ((1.0, 81.0), LINE, 0),
                    ((1.0, 58.0), LINE, 0),
                    ((50.0, 58.0), LINE, 0),
                    ((10.0, 17.0), LINE, 0),
                    ((26.0, 0.0), LINE, 0)
                ],
                [
                    ((-28.0, 58.0), LINE, 0),
                    ((-28.0, 81.0), LINE, 0),
                    ((-84.0, 81.0), LINE, 0),
                    ((-84.0, 58.0), LINE, 0)
                ]
            ],
            # righttoleftembedding
            '202B': [
                [
                    ((-10.0, 16.0), LINE, 0),
                    ((-50.0, 57.0), LINE, 0),
                    ((-1.0, 57.0), LINE, 0),
                    ((-1.0, 80.0), LINE, 0),
                    ((-50.0, 80.0), LINE, 0),
                    ((-10.0, 121.0), LINE, 0),
                    ((-26.0, 136.0), LINE, 0),
                    ((-95.0, 68.0), LINE, 0),
                    ((-26.0, 0.0), LINE, 0)
                ],
                [
                    ((84.0, 57.0), LINE, 0),
                    ((84.0, 80.0), LINE, 0),
                    ((28.0, 80.0), LINE, 0),
                    ((28.0, 57.0), LINE, 0)
                ]
            ],
            # popdirectionalformatting
            '202C': [
                [
                    ((11.0, 0.0), LINE, 0),
                    ((11.0, 101.0), LINE, 0),
                    ((51.0, 61.0), LINE, 0),
                    ((68.0, 77.0), LINE, 0),
                    ((0.0, 145.0), LINE, 0),
                    ((-68.0, 77.0), LINE, 0),
                    ((-51.0, 61.0), LINE, 0),
                    ((-12.0, 101.0), LINE, 0),
                    ((-12.0, 0.0), LINE, 0)
                ]
            ],
            # lefttorightoverride
            '202D': [
                [
                    ((48.0, 69.0), LINE, 0),
                    ((-21.0, 137.0), LINE, 0),
                    ((-37.0, 120.0), LINE, 0),
                    ((3.0, 81.0), LINE, 0),
                    ((-103.0, 81.0), LINE, 0),
                    ((-103.0, 58.0), LINE, 0),
                    ((4.0, 58.0), LINE, 0),
                    ((-37.0, 17.0), LINE, 0),
                    ((-21.0, 0.0), LINE, 0)
                ],
                [
                    ((112.0, 69.0), LINE, 0),
                    ((43.0, 137.0), LINE, 0),
                    ((28.0, 120.0), LINE, 0),
                    ((81.0, 69.0), LINE, 0),
                    ((28.0, 17.0), LINE, 0),
                    ((43.0, 0.0), LINE, 0)
                ]
            ],
            # righttoleftoverride
            '202E': [
                [
                    ((37.0, 17.0), LINE, 0),
                    ((-3.0, 58.0), LINE, 0),
                    ((103.0, 58.0), LINE, 0),
                    ((103.0, 79.0), LINE, 0),
                    ((-3.0, 79.0), LINE, 0),
                    ((37.0, 121.0), LINE, 0),
                    ((21.0, 138.0), LINE, 0),
                    ((-47.0, 69.0), LINE, 0),
                    ((21.0, 0.0), LINE, 0)
                ],
                [
                    ((-28.0, 17.0), LINE, 0),
                    ((-80.0, 69.0), LINE, 0),
                    ((-28.0, 121.0), LINE, 0),
                    ((-43.0, 138.0), LINE, 0),
                    ((-112.0, 69.0), LINE, 0),
                    ((-43.0, 0.0), LINE, 0)
                ]
            ],
        }
        self.ymaxs = self.get_yMax()

    def get_yMax(self):
        ymaxs = dict((m.id, 0) for m in Glyphs.font.masters)
        for mid in ymaxs.keys():
            for g in Glyphs.font.glyphs:
                if g.unicode not in self.glyph_outlines and g.name not in self.glyph_outlines:
                    l = g.layers[mid]
                    ymaxs[mid] = max((ymaxs[mid], l.bounds.origin.y + l.bounds.size.height))

        return ymaxs

    @staticmethod
    def is_empty(l):
        return not any((l.paths, l.components))

    def make_glyphs(self):
        Glyphs.font.disableUpdateInterface()
        for gm, paths_nodes in self.glyph_outlines.items():
            g = Glyphs.font.glyphs[gm]
            if g is None:
                g = GSGlyph('uni' + gm)
                Glyphs.font.glyphs.append(g)

            for l in g.layers:
                l.paths = []
                l.width = 0
                if not self.is_empty(l):
                    continue

                if self.ymaxs.get(l.layerId) is None:
                    continue

                for p in paths_nodes:
                    newP = GSPath()
                    for n in p:
                        newP.nodes.append(GSNode(*n))
                    newP.closed = True
                    newP

                    l.paths.append(newP)
                repos_val = self.ymaxs.get(l.layerId) - l.bounds.size.height if self.ymaxs.get(l.layerId) else None
                l.applyTransform((1, 0, 0, 1, 0, repos_val))

        Glyphs.font.enableUpdateInterface()


x = makeGlyphs()
x.make_glyphs()
