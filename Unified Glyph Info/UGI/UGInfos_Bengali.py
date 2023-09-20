# -*- coding: utf-8 -*-

from .unifiedglyphinfo import CollectedGlyphInfos, xpos, ypos


def collect_infos(infos_dict):
    return infos_dict.update(ugi.unified_infos)


ugi = CollectedGlyphInfos()

x = ugi('ka-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_25, position_y=ypos.base_line)

x = ugi('kha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)

x = ugi('ga-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)

x = ugi('gha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)

x = ugi('nga-beng')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('nukta', position_x=xpos.apex_bottom, position_y=ypos.descender_half)
x.addAnchor('candrabindu', position_x=xpos.apex_top, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.apex_top, position_y=ypos.indic_headline_top)

x = ugi('ca-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.apex_bottom, position_y=ypos.descender_half)

x = ugi('cha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.width_50, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.descender_half)

x = ugi('ja-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.descender_half)

x = ugi('jha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_25, position_y=ypos.base_line)

x = ugi('nya-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_25, position_y=ypos.descender_half)

x = ugi('tta-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.apex_bottom, position_y=ypos.descender_half)

x = ugi('ttha-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.apex_bottom, position_y=ypos.descender_half)

x = ugi('dda-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.apex_bottom, position_y=ypos.descender_half)

x = ugi('ddha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.apex_bottom, position_y=ypos.descender_half)

x = ugi('nna-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)

x = ugi('ta-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.apex_bottom, position_y=ypos.descender_half)

x = ugi('tha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)

x = ugi('da-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_25, position_y=ypos.base_line)

x = ugi('dha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)

x = ugi('na-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)

x = ugi('pa-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)

x = ugi('pha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_25, position_y=ypos.base_line)

x = ugi('ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)

x = ugi('bha-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.apex_bottom, position_y=ypos.descender_half)

x = ugi('ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)

x = ugi('ya-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)

x = ugi('ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)

x = ugi('la-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_25, position_y=ypos.base_line)

x = ugi('sha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_25, position_y=ypos.base_line)

x = ugi('ssa-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)

x = ugi('sa-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_33, position_y=ypos.base_line)

x = ugi('ha-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.width_50, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_25, position_y=ypos.descender_half)

x = ugi('ramiddlediagonal-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x='ba-beng', position_y='ba-beng')

x = ugi('ralowerdiagonal-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x='ba-beng', position_y=ypos.descender_half)

x = ugi('yya-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)

x = ugi('rha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)

x = ugi('rra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)

x = ugi('aaMatra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)

x = ugi('k_ka-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('k_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('k_tta-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('k_tt_ra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('k_ta-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('k_t_ba-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('k_t_ra-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('k_na-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('k_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('k_ra-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('k_la-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('k_ssa-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)
x.addAnchor('nukta', position_x=xpos.width_75, position_y=ypos.base_line)

x = ugi('k_ss_nna-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('k_ss_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('k_ss_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('k_ss_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('k_sa-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('kh_ba-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('kh_ra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_ga-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_da-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_dha-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_dh_ba-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_dh_ra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_na-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_ba-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_ma-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_ra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_ra_uMatra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_ra_uuMatra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('g_la-beng')
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x='candrabindu', position_y='candrabindu')
x.addAnchor('nukta', position_x=xpos.width_25, position_y=ypos.base_line)


x = ugi('gh_na-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('gh_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('gh_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('ng_ka-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ng_ga-beng')
x.addAnchor('top', position_x=xpos.width_66, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ng_gha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('ng_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('ng_ra-beng')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('c_ca-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('c_ch_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('c_ch_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('c_nya-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('c_ba-beng')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('c_ra-beng')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ch_ba-beng')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ch_ra-beng')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('j_ja-beng')
x.addAnchor('top', position_x=xpos.width_66, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('j_j_ba-beng')
x.addAnchor('top', position_x=xpos.width_66, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('j_jha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('j_nya-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('nukta', position_x=xpos.width_75, position_y=ypos.descender_half)

x = ugi('j_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('j_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ny_ca-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ny_cha-beng')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.outline_center, position_y=ypos.outline_bottom)

x = ugi('ny_ja-beng')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ny_jha-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ny_dha-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('tt_tta-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('tt_tt_ra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('tt_ba-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('tt_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('tt_ra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('tth_ra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('dd_ga-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('dd_dda-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('dd_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('dd_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('dd_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ddh_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('nn_tta-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('nn_tt_ra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('nn_ttha-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('nn_tth_ra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('nn_dda-beng')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('nn_ddh_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('nn_nna-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('nn_ba-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('nn_ma-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('nn_ra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('t_ta-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('t_t_ba-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('t_tha-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('t_na-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('t_ba-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('t_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('t_ra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('t_ra_uMatra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('t_ra_uuMatra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('t_la-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('th_ra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('th_ra_uMatra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('th_ra_uuMatra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('d_gha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('d_da-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('d_d_ba-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('d_d_ra-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('d_dha-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('d_dh_ba-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('d_na-beng')
x.addAnchor('top', position_x=xpos.width_66, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('d_ba-beng')
x.addAnchor('top', position_x=xpos.width_66, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('d_bha-beng')
x.addAnchor('top', position_x=xpos.width_66, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('d_bh_ra-beng')
x.addAnchor('top', position_x=xpos.width_66, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('d_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('d_ra-beng')
x.addAnchor('top', position_x=xpos.width_66, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('dh_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('dh_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('dh_ra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('dh_ra_uMatra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_k_ta-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('n_tta-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('n_tt_ra-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_ttha-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('n_dda-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('n_dd_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_ta-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_ta_uMatra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_t_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_t_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_tha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.width_50, position_y=ypos.outline_bottom)

x = ugi('n_th_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_da-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_d_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_dha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_dh_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_dh_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_na-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('n_sa-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('p_tta-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('p_t_ra-beng')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('b_dda-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('b_ddha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('b_da-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('b_d_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('b_dha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('b_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('b_bha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('b_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('b_ra_uMatra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('b_la-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('m_ta-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('m_da-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('l_ka-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('l_ga-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('l_ga_uMatra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('l_tta-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('l_tt_ra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('sh_tta-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('sh_ta-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y='top')
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y='top')
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('sh_na-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y='top')
x.addAnchor('candrabindu_alt', position_x='top', position_y='top')

x = ugi('sh_ba-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y='top')
x.addAnchor('candrabindu_alt', position_x='top', position_y='top')

x = ugi('sh_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y='top')
x.addAnchor('candrabindu_alt', position_x='top', position_y='top')

x = ugi('sh_la-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.outline_bottom)

x = ugi('ss_tta-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('ss_tt_ba-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ss_tt_ra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ss_ttha-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('ss_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ss_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('s_tta-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)

x = ugi('s_tt_ra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('s_ta-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y='top')
x.addAnchor('candrabindu_alt', position_x='top', position_y='top')

x = ugi('s_ta_uMatra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y='top')
x.addAnchor('candrabindu_alt', position_x='top', position_y='top')

x = ugi('s_t_ba-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y='top')
x.addAnchor('candrabindu_alt', position_x='top', position_y='top')

x = ugi('s_tha-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.width_75, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y='top')
x.addAnchor('candrabindu_alt', position_x='top', position_y='top')

x = ugi('s_pha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y='top')
x.addAnchor('candrabindu_alt', position_x='top', position_y='top')

x = ugi('s_ra_uuMatra-beng')
x.addAnchor('top', position_x='s_ra-beng', position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x='s_ra-beng', position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='s_ra-beng', position_y='s_ra-beng')
x.addAnchor('candrabindu_alt', position_x='s_ra-beng', position_y='s_ra-beng')

x = ugi('s_la-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('h_nna-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('h_na-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x='ha-beng', position_y='ha-beng')

x = ugi('h_ba-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('h_ma-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('h_ya-beng')
x.addAnchor('top', position_x='ha-beng', position_y='ha-beng')
x.addAnchor('bottom', position_x='ha-beng', position_y='ha-beng')
x.addAnchor('candrabindu', position_x='ha-beng', position_y='ha-beng')
x.addAnchor('candrabindu_alt', position_x='ha-beng', position_y='ha-beng')

x = ugi('h_ra-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('h_la-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('rr_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('rh_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('yy_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ralowerdiagonal_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ng_kra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ng_kssa-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ng_kssra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ng_ghra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ra_uMatra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ra_uuMatra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('sha_uMatra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y='top')
x.addAnchor('candrabindu_alt', position_x='top', position_y='top')

x = ugi('s_tra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ha_uMatra-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x='ha-beng', position_y='ha-beng')

x = ugi('ha_rVocalicMatra-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x='ha-beng', position_y='ha-beng')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x='ha-beng', position_y='ha-beng')

x = ugi('ralowerdiagonal_uMatra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ralowerdiagonal_uuMatra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('ng_k_ra-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x='candrabindu', position_y='candrabindu')
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)

x = ugi('c_cha-beng')
x.addAnchor('top', position_x=xpos.width_66, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.width_66, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x=xpos.width_66, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x='candrabindu', position_y='candrabindu')

x = ugi('nn_ddha-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x='top', position_y=ypos.indic_headline_top)

x = ugi('n_d_ra-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x='top', position_y=ypos.indic_headline_top)

x = ugi('ph_tta-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x='top', position_y=ypos.indic_headline_top)

x = ugi('b_ja-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x='top', position_y=ypos.indic_headline_top)

x = ugi('bh_ra_uuMatra-beng')
x.addAnchor('top', position_x='bh_ra-beng', position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x='top', position_y=ypos.indic_headline_top)

x = ugi('m_bha-beng')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x='top', position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x='top', position_y=ypos.indic_headline_top)

x = ugi('sh_cha-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.width_75, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)

x = ugi('sh_ca-beng')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.width_75, position_y=ypos.outline_bottom)
x.addAnchor('candrabindu', position_x=xpos.width_75, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.width_75, position_y=ypos.indic_headline_top)

x = ugi('raphala-beng')
x.addAnchor('_bottom', position_x=xpos.outline_right, position_y=ypos.outline_top)

x = ugi('baphala-beng')
x.addAnchor('_bottom', position_x=xpos.outline_right, position_y=ypos.outline_top)

x = ugi('halant-beng')
x.addAnchor('_bottom', position_x=xpos.outline_center, position_y=ypos.base_line)
x.addAnchor('_halant', position_x=xpos.outline_center, position_y=ypos.base_line)

x = ugi('reph-beng')
x.addAnchor('_reph', position_x=xpos.stem_bottom_center, position_y=ypos.xHeight)

x = ugi('reph_candraBindu-beng')
x.addAnchor('_candrabindu', position_x=xpos.apex_bottom, position_y=ypos.indic_headline_top)


x = ugi('candraBindu-beng')
x.addAnchor('_top', position_x=xpos.apex_bottom, position_y=ypos.xHeight)
x.addAnchor('_candrabindu', position_x=xpos.apex_bottom, position_y=ypos.xHeight)

x = ugi('auLength-beng')
x.addAnchor('top', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)

x = ugi('iiMatra-beng')
x.addAnchor('candrabindu', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)

x = ugi('iiMatra_reph-beng')
x.addAnchor('candrabindu', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)

x = ugi('iiMatra-beng.alt')
x.addAnchor('candrabindu', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)

x = ugi('iiMatra_reph-beng.alt')
x.addAnchor('candrabindu', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)

x = ugi('iiMatra-beng.alt.2')
x.addAnchor('candrabindu', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)

x = ugi('iiMatra_reph-beng.alt.2')
x.addAnchor('candrabindu', position_x=xpos.stem_bottom_center, position_y=ypos.indic_headline_top)

x = ugi('uMatra-beng')
x.addAnchor('_bottom', position_x=xpos.apex_top, position_y=ypos.base_line)

x = ugi('uuMatra-beng')
x.addAnchor('_bottom', position_x=xpos.apex_top, position_y=ypos.base_line)

x = ugi('uMatra-beng.alt')
x.addAnchor('_bottom', position_x=xpos.apex_top, position_y=ypos.base_line)

x = ugi('uuMatra-beng.alt')
x.addAnchor('_bottom', position_x=xpos.apex_top, position_y=ypos.base_line)

x = ugi('nukta-beng')
# x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.outline_bottom)
x.addAnchor('bottom', supress_auto=True)
x.addAnchor('_nukta', position_x=xpos.outline_center, position_y=ypos.outline_middle)

x = ugi('rVocalicMatra-beng')
x.addAnchor('_bottom', position_x=xpos.apex_top, position_y=ypos.base_line)

x = ugi('rrVocalicMatra-beng')
x.addAnchor('_bottom', position_x='rVocalicMatra-beng', position_y='rVocalicMatra-beng')

x = ugi('lVocalicMatra-beng')
x.addAnchor('_bottom', position_x=xpos.apex_top, position_y=ypos.base_line)

x = ugi('llVocalicMatra-beng')
x.addAnchor('_bottom', position_x='lVocalicMatra-beng', position_y='lVocalicMatra-beng')

x = ugi('avagraha-beng')
x.addAnchor('nukta', position_x='ha-beng', position_y='ha-beng')
