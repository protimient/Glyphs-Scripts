# MenuTitle: Show Build String
# -*- coding: utf-8 -*-
__doc__ = """
Displays a string with the current glyph containing useful or comparable glyphs.
"""

from AppKit import NSEvent
from collections import defaultdict
from UGI.UGI_importer import import_scripts
unified_infos = import_scripts(Glyphs.font)

Glyphs.clearLog()
# Glyphs.showMacroWindow()

# --- From mekkablue ---
keysPressed = NSEvent.modifierFlags()
capslockKey = 65536
capslockKeyPressed = keysPressed & capslockKey == capslockKey
# ---


def make_sc_2_uc_name(gn):
    return gn[0].upper() + gn[1:].replace('.sc', '')


def make_lc_2_uc_name(gn):
    return gn[0].upper() + gn[1:]


def make_smallcap_name(gn):
    arbitrary_initial_letters_len = 3
    try:
        return gn[:arbitrary_initial_letters_len].lower() + gn[arbitrary_initial_letters_len:] + '.sc'
    except TypeError:
        return gn


def glyph_exists(gn):
    if Glyphs.font.glyphs[gn]:
        return Glyphs.font.glyphs[gn].name
    return ''


sl = Glyphs.font.selectedLayers[0]
g = sl.parent
ugi = unified_infos.get(g.name)

default_strings = defaultdict(dict)
default_strings['cyrillic']['Uppercase'] = '/En-cy/{}/Ie-cy/Be-cy'
default_strings['cyrillic']['Lowercase'] = '/en-cy/{}/ie-cy/be-cy'
default_strings['cyrillic']['Smallcaps'] = '/en-cy.sc/{}/ie-cy.sc/be-cy.sc'

build_string = None
if ugi:
    build_string = ugi.build_string

if build_string is None:
    if g.subCategory == 'Smallcaps':
        rbs = glyph_exists(make_sc_2_uc_name(g.name))
        lbs = glyph_exists(g.name.replace('.sc', ''))
    elif g.subCategory == 'Lowercase':
        rbs = glyph_exists(make_lc_2_uc_name(g.name))
        lbs = glyph_exists(g.name + '.sc')
    elif g.subCategory == 'Uppercase':
        rbs = glyph_exists(g.name.lower())
        lbs = glyph_exists(g.name.lower() + '.sc')

    build_string = '/{}/{}/{}'.format(rbs, g.name, lbs).replace('//', '/')

    current_string = ''
    if Glyphs.font.currentTab is not None:
        current_string = [l.parent.name for l in Glyphs.font.currentTab.layers]
        
    if current_string == [rbs, g.name, lbs]:
        default_build_string = default_strings.get(g.script, {}).get(g.subCategory)
        if default_build_string:
            build_string = default_build_string.format(g.name)

build_string = build_string.decode('utf-8')

if Glyphs.font.currentTab:
    Glyphs.font.currentTab.text = build_string
else:
    Glyphs.font.newTab(build_string)

Glyphs.font.currentTab.textCursor = Glyphs.font.currentTab.layers.index(sl)
