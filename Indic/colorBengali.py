# MenuTitle: Color Bengali
# -*- coding: utf-8 -*-
__doc__ = """
Colours the Bengali glyphs according to their category.
"""

Glyphs.clearLog()
Glyphs.showMacroWindow()

vowel_names = [
    "a-beng",
    "aa-beng",
    "i-beng",
    "ii-beng",
    "u-beng",
    "uu-beng",
    "rVocalic-beng",
    "lVocalic-beng",
    "e-beng",
    "ai-beng",
    "o-beng",
    "au-beng",
]

base_names = [
    "ka-beng",
    "kha-beng",
    "ga-beng",
    "gha-beng",
    "nga-beng",
    "ca-beng",
    "cha-beng",
    "ja-beng",
    "jha-beng",
    "nya-beng",
    "tta-beng",
    "ttha-beng",
    "dda-beng",
    "ddha-beng",
    "nna-beng",
    "ta-beng",
    "tha-beng",
    "da-beng",
    "dha-beng",
    "na-beng",
    "pa-beng",
    "pha-beng",
    "ba-beng",
    "bha-beng",
    "ma-beng",
    "ya-beng",
    "ra-beng",
    "la-beng",
    "sha-beng",
    "ssa-beng",
    "sa-beng",
    "ha-beng",
    "avagraha-beng",
    "taKhanda-beng",
    "rra-beng",
    "rha-beng",
    "yya-beng",
    "rrVocalic-beng",
    "llVocalic-beng",
    "ramiddlediagonal-beng",
    "ralowerdiagonal-beng",
]

numeral_names = [
    "oneNumr-beng",
    "twoNumr-beng",
    "threeNumr-beng",
    "fourNumr-beng",
    "oneLessNumr-beng",
    "sixteenDnom-beng",
    "zero-beng",
    "one-beng",
    "two-beng",
    "three-beng",
    "four-beng",
    "five-beng",
    "six-beng",
    "seven-beng",
    "eight-beng",
    "nine-beng",
]

symbol_names = [
    "rupeeMark-beng",
    "rupeeSign-beng",
    "isshar-beng",
    "ganda-beng",
    "rupeeIndian-beng",
]

abv_names = [
    "candraBindu-beng",
    "reph-beng",
]

blw_names = [
    "nukta-beng",
    "uMatra-beng",
    "uuMatra-beng",
    "rVocalicMatra-beng",
    "rrVocalicMatra-beng",
    "halant-beng",
    "lVocalicMatra-beng",
    "llVocalicMatra-beng",
    "baphala-beng",
    "raphala-beng",
]

pre_pst_names = [
    "anusvara-beng",
    "visarga-beng",
    "aaMatra-beng",
    "iMatra-beng",
    "iiMatra-beng",
    "eMatra-beng",
    "aiMatra-beng",
    "oMatra-beng",
    "auMatra-beng",
    "auLength-beng",
    "eMatra-beng.init",
    "aiMatra-beng.init",
    "iiMatra.alt-beng",
    "iiMatra.alt2-beng",
    "iiMatrareph-beng",
    "iiMatrareph.alt-beng",
    "iiMatrareph.alt2-beng",
    "auLengthreph-beng",
    "yaphala-beng",
] + [g.name for g in Glyphs.font.glyphs if g.name.startswith('iiMatra')] + [g.name for g in Glyphs.font.glyphs if g.name.startswith('iMatra')]


def assign_color(g, color_val):
    for l in g.layers:
        if l.color not in [9223372036854775807, None]:
            l.color = 9223372036854775807

    if g.color != color_val:
        g.color = color_val


for g in Glyphs.font.glyphs:
    if g.name in vowel_names:
        assign_color(g, 4)

    elif g.name in base_names:
        assign_color(g, 5)

    elif g.name in numeral_names + symbol_names:
        assign_color(g, 3)

    elif g.name in abv_names:
        assign_color(g, 9)

    elif g.name in blw_names:
        assign_color(g, 7)

    elif g.name in pre_pst_names:
        assign_color(g, 8)

    elif g.script == 'bengali' and g.category == 'Letter':
        assign_color(g, 1)

    else:
        assign_color(g, None)
