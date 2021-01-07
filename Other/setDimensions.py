# MenuTitle: Set Dimensions
# -*- coding: utf-8 -*-
__doc__ = """
Sets the Latin values for each master in the Dimesions pallette in the top right.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()


class getMeasurements:
    def __init__(self, m):
        self.m = m
        if Glyphs.font.userData["GSDimensionPlugin.Dimensions"] is None:
            Glyphs.font.userData["GSDimensionPlugin.Dimensions"] = {}
        if Glyphs.font.userData["GSDimensionPlugin.Dimensions"].get(self.m.id) is None:
            Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id] = {}

    def get_HH(self):
        l = Glyphs.font.glyphs['H'].layers[self.m.id].copyDecomposedLayer()
        p1 = NSPoint(l.width / 2, 0)
        p2 = NSPoint(l.width / 2, self.m.capHeight)
        vals = l.intersectionsBetweenPoints(p1, p2, components=True)[1:-1]
        if vals:
            return int(vals[1].y - vals[0].y)

    def get_HV(self):
        l = Glyphs.font.glyphs['H'].layers[self.m.id].copyDecomposedLayer()
        p1 = NSPoint(0, self.m.capHeight / 3)
        p2 = NSPoint(l.width / 2, self.m.capHeight / 3)
        vals = l.intersectionsBetweenPoints(p1, p2, components=True)[1:-1]
        if vals:
            return int(vals[1].x - vals[0].x)

    def get_OH(self):
        l = Glyphs.font.glyphs['O'].layers[self.m.id].copyDecomposedLayer()
        l.removeOverlap()

        c1 = l.paths[0]
        c2 = l.paths[1]
        c1_top = c1.bounds.origin.y + c1.bounds.size.height
        c2_top = c2.bounds.origin.y + c2.bounds.size.height
        val = int(abs(c1_top - c2_top))
        return val

    def get_OV(self):
        l = Glyphs.font.glyphs['O'].layers[self.m.id].copyDecomposedLayer()
        l.removeOverlap()

        c1 = l.paths[0]
        c2 = l.paths[1]
        c1_top = c1.bounds.origin.x
        c2_top = c2.bounds.origin.x
        val = int(abs(c1_top - c2_top))
        return val

    def get_nV(self):
        l = Glyphs.font.glyphs['i'].layers[self.m.id].copyDecomposedLayer()
        p1 = NSPoint(0, self.m.xHeight / 2)
        p2 = NSPoint(l.width, self.m.xHeight / 2)
        vals = l.intersectionsBetweenPoints(p1, p2, components=True)[1:-1]
        if vals:
            return int(vals[1].x - vals[0].x)

    def get_oH(self):
        l = Glyphs.font.glyphs['o'].layers[self.m.id].copyDecomposedLayer()
        l.removeOverlap()
        c1 = l.paths[0]
        c2 = l.paths[1]
        c1_top = c1.bounds.origin.y + c1.bounds.size.height
        c2_top = c2.bounds.origin.y + c2.bounds.size.height
        val = int(abs(c1_top - c2_top))
        return val

    def get_oV(self):
        l = Glyphs.font.glyphs['o'].layers[self.m.id].copyDecomposedLayer()
        l.removeOverlap()
        c1 = l.paths[0]
        c2 = l.paths[1]
        c1_top = c1.bounds.origin.x
        c2_top = c2.bounds.origin.x
        val = int(abs(c1_top - c2_top))
        return val

    def get_tH(self):
        l = Glyphs.font.glyphs['t'].layers[self.m.id].copyDecomposedLayer()
        p1 = NSPoint(l.width * 0.75, self.m.ascender)
        p2 = NSPoint(l.width * 0.75, self.m.xHeight / 2)
        vals = l.intersectionsBetweenPoints(p1, p2, components=True)[1:-1]
        if vals:
            return abs(int(vals[1].y - vals[0].y))

    @staticmethod
    def report(msg):
        print(msg)

    def set_vals(self):
        Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['HH'] = self.get_HH() or ''
        self.report('Set HH to {}'.format(Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['HH']))
        Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['HV'] = self.get_HV() or ''
        self.report('Set HV to {}'.format(Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['HV']))
        Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['OH'] = self.get_OH() or ''
        self.report('Set OH to {}'.format(Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['OH']))
        Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['OV'] = self.get_OV() or ''
        self.report('Set OV to {}'.format(Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['OV']))
        Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['nV'] = self.get_nV() or ''
        self.report('Set nV to {}'.format(Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['nV']))
        Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['oH'] = self.get_oH() or ''
        self.report('Set oH to {}'.format(Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['oH']))
        Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['oV'] = self.get_oV() or ''
        self.report('Set oV to {}'.format(Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['oV']))
        Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['tH'] = self.get_tH() or ''
        self.report('Set tH to {}'.format(Glyphs.font.userData["GSDimensionPlugin.Dimensions"][self.m.id]['tH']))


for m in Glyphs.font.masters:
    x = getMeasurements(m)
    x.set_vals()
