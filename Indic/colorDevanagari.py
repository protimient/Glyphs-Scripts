# MenuTitle: Color Devanagari
# -*- coding: utf-8 -*-
__doc__ = """
Colours the Devanagari glyphs according to their category.
"""

Glyphs.clearLog()
Glyphs.showMacroWindow()

vowel_names = [
    "aCandra-deva",
    "aShort-deva",
    "a-deva",
    "aa-deva",
    "i-deva",
    "ii-deva",
    "ii_anusvara-deva",
    "u-deva",
    "uu-deva",
    "rVocalic-deva",
    "rrVocalic-deva",
    "lVocalic-deva",
    "llVocalic-deva",
    "eCandra-deva",
    "eShort-deva",
    "e-deva",
    "ai-deva",
    "oCandra-deva",
    "oShort-deva",
    "o-deva",
    "au-deva",
    "oe-deva",
    "ooe-deva",
    "aw-deva",
    "ue-deva",
    "uue-deva",
]

base_names = [
    "ka-deva",
    "kha-deva",
    "ga-deva",
    "gha-deva",
    "nga-deva",
    "ca-deva",
    "cha-deva",
    "ja-deva",
    "jha-deva",
    "nya-deva",
    "tta-deva",
    "ttha-deva",
    "dda-deva",
    "ddha-deva",
    "nna-deva",
    "ta-deva",
    "tha-deva",
    "da-deva",
    "dha-deva",
    "na-deva",
    "pa-deva",
    "pha-deva",
    "ba-deva",
    "bha-deva",
    "ma-deva",
    "ya-deva",
    "ra-deva",
    "rra-deva",
    "la-deva",
    "lla-deva",
    "va-deva",
    "sha-deva",
    "ssa-deva",
    "sa-deva",
    "ha-deva",
    "gga-deva",
    "jja-deva",
    "ddda-deva",
    "bba-deva",
    "la-deva.loclMAR",
    "sha-deva.loclMAR",
]

numeral_names = [
    "zero-deva",
    "one-deva",
    "two-deva",
    "three-deva",
    "four-deva",
    "five-deva",
    "six-deva",
    "seven-deva",
    "eight-deva",
    "nine-deva",
]

symbol_names = [
    "avagraha-deva",
    "om-deva",
    "rupeeIndian-deva",
]

abv_names = [
    "eCandraMatra-deva",
    "eCandraMatra_reph-deva",
    "candraBindu-deva",
    "candraBindu_reph-deva",
    "invertedCandraBindu-deva",
    "eShortMatra-deva",
    "eShortMatra_reph-deva",
    "eShortMatra_reph_anusvara-deva",
    "eMatra-deva",
    "eMatra_anusvara-deva",
    "eMatra_reph-deva",
    "eMatra_reph_anusvara-deva",
    "aiMatra-deva",
    "aiMatra_anusvara-deva",
    "aiMatra_reph-deva",
    "aiMatra_reph_anusvara-deva",
    "anusvara-deva",
    "reph-deva",
    "reph_anusvara-deva",
    "eLongCandra-deva",
    "oeMatra-deva",
    "udatta-deva",
    "grave-deva",
    "acute-deva",
]

blw_names = [
    "uMatra-deva",
    "uuMatra-deva",
    "rVocalicMatra-deva",
    "rrVocalicMatra-deva",
    "lVocalicMatra-deva",
    "llVocalicMatra-deva",
    "halant-deva",
    "nukta-deva",
    "nukta_uMatra-deva",
    "nukta_uuMatra-deva",
    "nukta_rVocalicMatra-deva",
    "nukta_rrVocalicMatra-deva",
    "nukta_lVocalicMatra-deva",
    "nukta_llVocalicMatra-deva",
    "nukta_halant-deva",
    "nukta_rakar-deva",
    "nukta_rakar_uMatra-deva",
    "nukta_rakar_uuMatra-deva",
    "nukta_rakar_halant-deva",
    "rakar-deva",
    "rakar_uMatra-deva",
    "rakar_uuMatra-deva",
    "rakar_halant-deva",
    "ueMatra-deva",
    "uueMatra-deva",
    "anudatta-deva",
]

pre_pst_names = [
    "aaMatra-deva",
    "iMatra-deva",
    "iMatra_anusvara-deva",
    "iMatra_reph-deva",
    "iMatra_reph_anusvara-deva",
    "iiMatra-deva",
    "iiMatra_anusvara-deva",
    "iiMatra_reph-deva",
    "iiMatra_reph_anusvara-deva",
    "oCandraMatra-deva",
    "oCandraMatra_anusvara_reph-deva",
    "oCandraMatra_reph-deva",
    "oShortMatra-deva",
    "oShortMatra_reph-deva",
    "oShortMatra_reph_anusvara-deva",
    "oMatra-deva",
    "oMatra_anusvara-deva",
    "oMatra_reph-deva",
    "oMatra_reph_anusvara-deva",
    "auMatra-deva",
    "auMatra_anusvara-deva",
    "auMatra_reph-deva",
    "auMatra_reph_anusvara-deva",
    "prishthaMatraE-deva",
    "ooeMatra-deva",
    "awMatra-deva",
]

halfform_names = [
    "k-deva",
    "k_ss-deva",
    "kh-deva",
    "g-deva",
    "gh-deva",
    "ng-deva",
    "c-deva",
    "ch-deva",
    "j-deva",
    "j_ny-deva",
    "jh-deva",
    "ny-deva",
    "tt-deva",
    "tth-deva",
    "dd-deva",
    "ddh-deva",
    "nn-deva",
    "t-deva",
    "th-deva",
    "d-deva",
    "dh-deva",
    "n-deva",
    "nnn-deva",
    "p-deva",
    "ph-deva",
    "b-deva",
    "bh-deva",
    "m-deva",
    "y-deva",
    "rr-deva",
    "l-deva",
    "ll-deva",
    "lll-deva",
    "v-deva",
    "sh-deva",
    "ss-deva",
    "s-deva",
    "h-deva",
    "q-deva",
    "khh-deva",
    "ghh-deva",
    "z-deva",
    "f-deva",
    "yy-deva",
    "l-deva.loclMAR",
    "sh-deva.loclMAR",
    "jh-deva.loclNEP",

]

rakar_names = [
    "k_rakar-deva",
    "kh_rakar-deva",
    "g_rakar-deva",
    "gh_rakar-deva",
    "ng_rakar-deva",
    "c_rakar-deva",
    "ch_rakar-deva",
    "j_rakar-deva",
    "jh_rakar-deva",
    "ny_rakar-deva",
    "tt_rakar-deva",
    "tth_rakar-deva",
    "dd_rakar-deva",
    "ddh_rakar-deva",
    "nn_rakar-deva",
    "t_rakar-deva",
    "th_rakar-deva",
    "d_rakar-deva",
    "dh_rakar-deva",
    "n_rakar-deva",
    "nnn_rakar-deva",
    "p_rakar-deva",
    "ph_rakar-deva",
    "b_rakar-deva",
    "bh_rakar-deva",
    "m_rakar-deva",
    "y_rakar-deva",
    "l_rakar-deva",
    "ll_rakar-deva",
    "v_rakar-deva",
    "sh_rakar-deva",
    "ss_rakar-deva",
    "s_rakar-deva",
    "h_rakar-deva",
    "q_rakar-deva",
    "khh_rakar-deva",
    "ghh_rakar-deva",
    "z_rakar-deva",
    "f_rakar-deva",
    "yy_rakar-deva",

    "ka_ra-deva",
    "k_ssa_ra-deva",
    "kha_ra-deva",
    "ga_ra-deva",
    "gha_ra-deva",
    "nga_ra-deva",
    "ca_ra-deva",
    "cha_ra-deva",
    "ja_ra-deva",
    "jha_ra-deva",
    "nya_ra-deva",
    "tta_ra-deva",
    "ttha_ra-deva",
    "dda_ra-deva",
    "ddha_ra-deva",
    "nna_ra-deva",
    "ta_ra-deva",
    "tha_ra-deva",
    "da_ra-deva",
    "dha_ra-deva",
    "na_ra-deva",
    "nnna_ra-deva",
    "pa_ra-deva",
    "pha_ra-deva",
    "ba_ra-deva",
    "bha_ra-deva",
    "ma_ra-deva",
    "ya_ra-deva",
    "ra_ra-deva",
    "la_ra-deva",
    "lla_ra-deva",
    "va_ra-deva",
    "sha_ra-deva",
    "ssa_ra-deva",
    "sa_ra-deva",
    "ha_ra-deva",
    "qa_ra-deva",
    "khha_ra-deva",
    "ghha_ra-deva",
    "za_ra-deva",
    "fa_ra-deva",
    "yya_ra-deva",
    "ka_ra-deva.loclNEP",
]


def assign_color(g, color_val):
    for l in g.layers:
        if l.color not in [9223372036854775807, None]:
            l.color = 9223372036854775807

    if g.color != color_val:
        g.color = color_val


for g in Glyphs.font.glyphs:
    if g.name in vowel_names:
        assign_color(g, 2)

    elif g.name in base_names:
        assign_color(g, 6)

    elif g.name in halfform_names:
        assign_color(g, 4)

    elif g.name in rakar_names:
        assign_color(g, 5)

    elif g.name in numeral_names + symbol_names or g.name.split('.')[0] in numeral_names + symbol_names:
        assign_color(g, 3)

    elif g.name in abv_names:
        assign_color(g, 9)

    elif g.name in blw_names:
        assign_color(g, 7)

    elif g.name in pre_pst_names or g.name.split('.')[0] in pre_pst_names:
        assign_color(g, 8)

    elif g.script == 'devanagari' and g.category == 'Letter':
        assign_color(g, 1)

    elif g.script == 'devanagari':
        assign_color(g, 11)

    else:
        assign_color(g, None)
