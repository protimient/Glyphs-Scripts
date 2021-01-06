# MenuTitle: Correct Legacy Accent Usage
# -*- coding: utf-8 -*-
__doc__ = """
Fixes glyphs that are using the old, legacy accents instead of combining marks.
"""

Glyphs.clearLog()
Glyphs.showMacroWindow()

unicodes = {
    '00B4': '0301', 	# acute
    '02D8': '0306', 	# breve
    '02C7': '030C', 	# caron
    '00B8': '0327', 	# cedilla
    '02C6': '0302', 	# circumflex
    '00A8': '0308', 	# dieresis
    '02D9': '0307', 	# dotaccent
    '02DD': '030B', 	# hungarumlaut
    '00AF': '0304', 	# macron
    '02DB': '0328', 	# ogonek
    '02DA': '030A', 	# ring
    '02DC': '0303', 	# tilde
    '0060': '0300', 	# grave
}

legacy_glyphs = [Glyphs.font.glyphs[gu] for gu in unicodes.keys() if Glyphs.font.glyphs[gu]]

cap_suffixes = ['.cap', '.case']


def get_correct_glyph(legacy_unicode, base_g):
    legacy_g = Glyphs.font.glyphs[legacy_unicode]
    if not legacy_g:
        return

    comb_glyph = Glyphs.font.glyphs[unicodes.get(legacy_unicode)]
    if base_g.category == 'Letter' and base_g.subCategory == 'Uppercase':
        if comb_glyph:
            for suffix in cap_suffixes:
                cap_accent = Glyphs.font.glyphs[comb_glyph.name + suffix]
                if cap_accent:
                    comb_glyph = cap_accent
                    break

    return comb_glyph


def get_glyph_offset(old_l, new_l):
    x = old_l.bounds.origin.x - new_l.bounds.origin.x
    y = old_l.bounds.origin.y - new_l.bounds.origin.y
    return NSPoint(x, y)


all_accent_glyphs = [b for a in unicodes.items() for b in a]

affected_layers = []
for g in [x for x in Glyphs.font.glyphs if x.unicode not in all_accent_glyphs]:
    for l in g.layers:
        for c in l.components:
            try:
                if c.component.unicode in unicodes.keys():
                    this_width = int(l.width)
                    new_g = get_correct_glyph(c.component.unicode, g)
                    glyph_offset = get_glyph_offset(c.componentLayer, new_g.layers[l.associatedMasterId])
                    component_offset = NSPoint(c.position.x + glyph_offset.x, c.position.y + glyph_offset.y)
                    c.automaticAlignment = False
                    c.componentName = new_g.name
                    c.position = component_offset
                    if l.width != this_width:
                        affected_layers.append(l)
            except AttributeError:
                print(g, l)
                raise

if affected_layers:
    Glyphs.font.newTab()
    Glyphs.font.tabs[-1].layers = affected_layers
else:
    Glyphs.showNotification('Legacy Accents', 'All good. No legacy accents are being used.')
    print('Legacy Accents', 'All good. No legacy accents are being used.')
