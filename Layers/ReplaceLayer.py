# MenuTitle: Replace named Layer...
# -*- coding: utf-8 -*-
__doc__ = """
Replace the named layer in All glyphs in the front font with the first layer of the corresponding glyph in the other open font.
"""

import copy
from vanilla import (
    Window,
    EditText,
    CheckBox,
    Button,
)

# Glyphs.clearLog()
# Glyphs.showMacroWindow()


class makeItSo(object):
    def __init__(self):
        self.w = Window((550, 140), "Replace named Layer")
        self.w.editText = EditText((10, 15, -10, 22), placeholder="Layer Name", text='{170}')
        self.w.correct_path_direction = CheckBox((10, 50, -10, 18), "Correct Path Direction", value=True, sizeStyle='small')
        self.w.sync_metrics = CheckBox((210, 50, -10, 18), "Sync Metrics", value=True, sizeStyle='small')
        self.w.add_if_missing = CheckBox((10, 70, -10, 18), "Add layer if missing", value=True, sizeStyle='small')
        self.w.copybutton = Button((10, 100, -10, 17), "Replace layer", callback=self.buttonCallback)
        self.w.open()

    def buttonCallback(self, sender):
        self.w.close()

        target_font = Glyphs.font
        source_font = Glyphs.fonts[1]

        target_font.disableUpdateInterface()

        target_layer_name = self.w.editText.get()

        for source_glyph in source_font.glyphs:
            target_glyph = target_font.glyphs[source_glyph.name]
            if target_glyph is None:
                continue

            source_layer = source_glyph.layers[0]

            newL = copy.copy(source_layer)

            extant = True
            try:
                target_layer = [x for x in target_glyph.layers if x.name == target_layer_name][0]
                newL.associatedMasterId = target_layer.associatedMasterId
            except IndexError:
                if not self.w.add_if_missing.get():
                    continue
                source_weightValue = source_font.instances[0].weightValue
                mid = target_font.masters[0].id
                for m in target_font.masters:
                    if m.weightValue > source_weightValue:
                        break
                    mid = m.id
                newL.associatedMasterId = mid
                extant = False

            newL.name = target_layer_name
            for c in newL.components:
                c.automaticAlignment = False
                if target_font.glyphs[c.componentName] is None:
                    newLayerPaths = source_layer.copyDecomposedLayer()
                    newL.paths = newLayerPaths.paths
                    newL.components = []
                    break

            if self.w.correct_path_direction:
                newL.correctPathDirection()

            if extant:
                target_glyph.layers[target_layer.layerId] = newL
            else:
                target_glyph.layers.append(newL)

            if self.w.sync_metrics and extant:
                target_glyph.layers[target_layer.layerId].syncMetrics()

        target_font.enableUpdateInterface()


makeItSo()
