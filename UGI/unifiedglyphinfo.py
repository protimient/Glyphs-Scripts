# from collections import defaultdict
import math
from Foundation import NSPoint
from GlyphsApp import Glyphs


class xpos:
    outline_right = 'xpos_outline_right'
    outline_center = 'xpos_outline_center'
    outline_left = 'xpos_outline_left'
    apex_bottom = 'xpos_apex_bottom'
    apex_top = 'xpos_apex_top'
    stem_top_center = 'xpos_stem_top_center'
    stem_top_right = 'xpos_stem_top_right'
    stem_top_left = 'xpos_stem_top_left'
    stem_bottom_center = 'xpos_stem_bottom_center'
    stem_bottom_right = 'xpos_stem_bottom_right'
    stem_bottom_left = 'xpos_stem_bottom_left'
    width_25 = 'xpos_width_25'
    width_33 = 'xpos_width_33'
    width_50 = 'xpos_width_50'
    width_66 = 'xpos_width_66'
    width_75 = 'xpos_width_75'
    indic_right_stem = 'indic_right_stem'
    LSB = 'xpos_LSB'
    RSB = 'xpos_RSB'


class ypos:
    capHeight = 'ypos_capHeight'
    base_line = 'ypos_base_line'
    height_25 = 'ypos_height_25'
    height_50 = 'ypos_height_50'
    height_75 = 'ypos_height_75'
    outline_top = 'ypos_outline_top'
    outline_middle = 'ypos_outline_middle'
    outline_bottom = 'ypos_outline_bottom'
    smallcapHeight = 'ypos_smallcapHeight'
    xHeight = 'xHeight'
    indic_headline_top = 'indic_headline_top'
    descender_half = 'descender_half'
    ascender = 'ascender'


# global unified_infos
# unified_infos = dict()


def italic_angle(layer):
    try:
        return Glyphs.font.masters[layer.associatedMasterId].italicAngle
    except AttributeError:
        return 0


class CollectedGlyphInfos:
    def __init__(self, unified_infos=dict()):
        self.unified_infos = unified_infos

    def __call__(self, gn):
        ugi = UnifiedGlyphInfo(gn)
        self.unified_infos[gn] = ugi
        return ugi


class UnifiedGlyphInfo:
    def __init__(self, gn):
        self.glyph_name = gn

        self.recipes = []
        self.recipes_italic = []

        self.anchors = dict()

        self.metrics_left = None
        self.metrics_right = None
        self.metrics_width = None
        self.metrics_italic_left = None
        self.metrics_italic_right = None
        self.metrics_italic_width = None
        self.has_metrics = False

        self.kerning_left = None
        self.kerning_right = None
        self.kerning_italic_left = None
        self.kerning_italic_right = None
        self.has_kerning = False

        self.build_string = None

    class recipeComponent:
        def __init__(self, comp_args):
            comp_recipe = comp_args.split(' ')
            self.name = comp_recipe.pop(0)
            for at in comp_recipe:
                setattr(self, at, True)

        def __str__(self):
            return self.name

        def __repr__(self):
            return 'recipeComponent({})'.format(self.name)

        def __getattr__(self, attrname):
            return False

    def _compensate_italic_angle(self, pos_y, italic_angle):
        """
        Takes the height/y position and the italic angle and returns the corrected x position.
        """
        if not italic_angle:
            return 0
        return round(math.tan(math.radians(italic_angle)) * pos_y)

    def _italic_angle(self, layer):
        """
        Returns the italic angle for the given layer.
        """
        try:
            return Glyphs.font.masters[layer.associatedMasterId].italicAngle
        except AttributeError:
            return 0

    def _transform_position_y(self, from_coords, to_coords, italic_angle=0):
        """
        Returns the italic-corrected coordinates for a change in y.
        """
        newy = to_coords.y - from_coords.y
        new_coords = NSPoint(self._compensate_italic_angle(newy, italic_angle), newy)
        return new_coords

    def _add_components(self, this_l):
        """
        Adds the default components to the given layer if their parent glyphs are present in the font.
        """
        this_g = this_l.parent
        glyph_components = this_g.glyphInfo.components
        if glyph_components:
            component_glyphs = [Glyphs.font.glyphs[info.name] for info in glyph_components]
            if None not in component_glyphs:
                for cg in component_glyphs:
                    this_l.components.append(GSComponent(cg))

    @staticmethod
    def layer_is_empty(layer):
        return not any([layer.bounds.origin.x, layer.bounds.origin.y, layer.bounds.size.height, layer.bounds.size.width])

    def get_accent_top(self, this_l):
        """
        Returns a dictionary mapping masters to the top coordinate of the dieresis.
        """
        g = Glyphs.font.glyphs['00A8']
        if g is None:
            for gn in ['dieresis', 'dieresiscomb', '00A8']:
                g = Glyphs.font.glyphs[gn]
                if g is not None:
                    break
        if g is None:
            return None

        accent_layer = g.layers[this_l.associatedMasterId]
        if not self.layer_is_empty(accent_layer):
            return accent_layer.bounds.origin

        return None

    def get_accent_bottom(self, this_l):
        g = Glyphs.font.glyphs['0326']
        if g is None:
            for gn in ['commaaccent', 'commaaccentcomb', 'uni0326']:
                g = Glyphs.font.glyphs[gn]
                if g is not None:
                    break

        if g is None:
            return

        accent_layer = g.layers[this_l.associatedMasterId]
        if not self.layer_is_empty(accent_layer):
            return NSPoint(0, accent_layer.bounds.origin.y + accent_layer.bounds.size.height)

        return None

    def addRecipe(self, *args, **kwargs):
        comp_objs = [self.recipeComponent(x) for x in args]
        if kwargs.get('italic'):
            self.recipes_italic.append(comp_objs)
        else:
            self.recipes.append(comp_objs)

    def addAnchor(self, anchor_name, *args, **kwargs):
        self.anchors[anchor_name] = kwargs

    def addMetrics(self, left=None, right=None, width=None, **kwargs):
        self.has_metrics = True
        self.metrics_italic_left = kwargs.get('italic_left', left)
        self.metrics_italic_right = kwargs.get('italic_right', right)
        self.metrics_italic_width = kwargs.get('italic_width', width)
        self.metrics_left = left
        self.metrics_right = right
        self.metrics_width = width

    def addKerning(self, left=None, right=None, **kwargs):
        self.has_kerning = True
        self.kerning_italic_left = kwargs.get('italic_left', left)
        self.kerning_italic_right = kwargs.get('italic_right', right)
        self.kerning_left = left
        self.kerning_right = right

    def addBuildString(self, string):
        self.build_string = string

    def make_glyph(self):
        pass
