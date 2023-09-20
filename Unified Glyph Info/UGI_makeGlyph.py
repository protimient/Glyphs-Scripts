# MenuTitle: Make UGI Glyph
# -*- coding: utf-8 -*-
__doc__ = """
Makes Glyphs using the UGI.
Hold alt to bring up options.
Press caps-lock to clear all layers first.
"""
import vanilla

from UGI.unifiedglyphinfo import italic_angle
from AppKit import NSEvent
from collections import OrderedDict
from GlyphsApp import Glyphs

from UGI.UGI_importer import import_scripts
unified_infos = import_scripts(Glyphs.font)

Glyphs.clearLog()
# Glyphs.showMacroWindow()

# --- From mekkablue ---
keysPressed = NSEvent.modifierFlags()
capslockKey = 65536
altKey = 524288
capslockKeyPressed = keysPressed & capslockKey == capslockKey
altKeyPressed = keysPressed & altKey == altKey
# ---


class makeGlyphChooser(object):
    def __init__(self, this_glyph, recipes):
        item_height = 22.0
        w_width = 350.0
        w_height = item_height * 5
        margin = 10
        next_y = margin
        col_1_width = w_width - (margin * 2)

        self.recipes = recipes
        self.recipes_dict = OrderedDict([(', '.join([str(i) for i in r]), r) for r in recipes])
        self.this_glyph = this_glyph

        self.w = vanilla.FloatingWindow((w_width, w_height), "Edit Bracket Layers in Selected Glyphs")

        next_y = margin

        self.w.text_1 = vanilla.TextBox((margin, next_y, col_1_width, item_height), "Recipe:", sizeStyle='regular')
        next_y += item_height
        self.w.recipe_str = vanilla.PopUpButton((margin, next_y, col_1_width, item_height), self.recipes_dict.keys(), sizeStyle='regular')
        next_y += item_height + margin

        self.w.cancelbutton = vanilla.Button((margin, next_y, col_1_width / 2 - margin, item_height), "Cancel", sizeStyle='regular', callback=self.cancelCallback)
        self.w.addbutton = vanilla.Button((col_1_width / 2 + margin, next_y, col_1_width / 2, item_height),
                                          "Make Glyph", sizeStyle='regular', callback=self.makeitso)

        self.w.setDefaultButton(self.w.addbutton)

        if capslockKeyPressed:
            self.empty_glyph(self.this_glyph)

        if altKeyPressed:
            self.w.open()
            self.w.center()
        else:
            self.makeitso(None)

    def cancelCallback(self, sender):
        self.w.close()

    def makeitso(self, sender):
        recipe = None
        if sender:
            self.w.close()
            selected_recipe = self.w.recipe_str.getItem()
            recipe = self.recipes_dict[selected_recipe]
        else:
            try:
                recipe = self.recipes[0]
            except IndexError:
                pass

        if recipe is not None:
            print('Making \'{}\' using: {}'.format(self.this_glyph.name, ''.join('/' + str(x) for x in recipe)))
            for l in self.this_glyph.layers:
                self.make_recipe(l, recipe)

    @staticmethod
    def layer_is_empty(layer):
        return not any([layer.bounds.origin.x, layer.bounds.origin.y, layer.bounds.size.height, layer.bounds.size.width])

    @staticmethod
    def empty_glyph(g):
        for l in g.layers:
            l.paths = []
            l.anchors = []
            l.components = []

    def make_recipe(self, l, recipe):
        if not self.layer_is_empty(l):
            return

        for ingredient in recipe:
            new_comp = GSComponent(ingredient.name)

            if self.layer_is_empty(Glyphs.font.glyphs[ingredient.name].layers[l.associatedMasterId]):
                print('Source Layer ({}) is empty'.format(ingredient.name))
                continue

            parent_layer = Glyphs.font.glyphs[ingredient.name].layers[l.associatedMasterId]
            new_comp.automaticAlignment = False
            l.components.append(new_comp)

            if ingredient.rotate_90:
                this_rotation = -90
            elif ingredient.rotate_180:
                this_rotation = 180
            elif ingredient.rotate_270:
                this_rotation = 90
            else:
                this_rotation = 0

            if ingredient.flip_horizontal and ingredient.flip_vertical:
                this_scale_x = -1
                this_scale_y = -1
            elif ingredient.flip_horizontal:
                this_scale_x = -1
                this_scale_y = 1
            elif ingredient.flip_vertical:
                this_scale_x = 1
                this_scale_y = -1
            else:
                this_scale_x = 1
                this_scale_y = 1

            if abs(this_rotation) == 90:
                this_scale_x, this_scale_y = (this_scale_y, this_scale_x)

            # new_comp.setScaleX_scaleY_rotation_(this_scale_x, this_scale_y, this_rotation)
            new_comp.scale = (this_scale_x, this_scale_y)
            new_comp.rotation = this_rotation

            offset_x = parent_layer.bounds.origin.x - new_comp.bounds.origin.x
            offset_y = parent_layer.bounds.origin.y - new_comp.bounds.origin.y
            new_comp.setPosition_(NSPoint(offset_x, offset_y))

            if ingredient.accent_top:
                new_coords = ugi._transform_position_y(
                    new_comp.bounds.origin,
                    ugi.get_accent_top(l),
                    italic_angle=ugi._italic_angle(l)
                )
            elif ingredient.accent_bottom:
                new_coords = ugi._transform_position_y(
                    NSPoint(new_comp.bounds.origin.x + new_comp.bounds.size.width, new_comp.bounds.origin.y + new_comp.bounds.size.height),
                    ugi.get_accent_bottom(l),
                    italic_angle=ugi._italic_angle(l)
                )
            else:
                new_coords = NSPoint(0, 0)

            new_comp.applyTransform((1, 0, 0, 1, new_coords.x, new_coords.y))

            if ingredient.enable_alignment:
                new_comp.automaticAlignment = True

            if new_comp.position == NSPoint(0, 0) and not ingredient.disable_alignment:
                new_comp.automaticAlignment = True

            if ingredient.decompose:
                try:
                    list(l.components)[-1].decompose()
                except Exception as e:
                    print(e)

        l.width = Glyphs.font.glyphs[recipe[0].name].layers[l.associatedMasterId].width

        l.syncMetrics()
        l.anchors = []


if altKeyPressed:
    these_layers = [Glyphs.font.selectedLayers[0]]
else:
    these_layers = Glyphs.font.selectedLayers

for sl in these_layers:
    g = sl.parent

    ugi = unified_infos.get(g.name)
    # print(sorted(unified_infos.keys()))
    # print(unified_infos.get(g.name))

    if ugi is None:
        print('No info for {}'.format(g.name))
        continue

    if italic_angle(sl):
        recipe_book = ugi.recipes + ugi.recipes_italic
    else:
        recipe_book = ugi.recipes

    all_valid_recipes = [r for r in recipe_book if all([Glyphs.font.glyphs[ingredient.name] for ingredient in r])]

    makeGlyphChooser(g, all_valid_recipes)

    g.updateGlyphInfo()
