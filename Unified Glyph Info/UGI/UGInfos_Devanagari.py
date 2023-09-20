# -*- coding: utf-8 -*-

from .unifiedglyphinfo import CollectedGlyphInfos, xpos, ypos


def collect_infos(infos_dict):
    return infos_dict.update(ugi.unified_infos)


ugi = CollectedGlyphInfos()

x = ugi('default-deva')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.indic_right_stem, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_25, position_y=ypos.base_line)

x = ugi('ka-deva')
x.addAnchor('top', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('candrabindu', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('candrabindu_alt', position_x=xpos.indic_right_stem, position_y=ypos.indic_headline_top)
x.addAnchor('nukta', position_x=xpos.width_25, position_y=ypos.base_line)
x.addKerning(left='ka-deva', right='ka-deva')

x = ugi('ca-deva')
x.addAnchor('candra', position_x=xpos.width_50, position_y=ypos.xHeight)
x.addAnchor('anusvara', position_x=xpos.width_50, position_y=ypos.indic_headline_top)

x = ugi('cha-deva')
x.addAnchor('candra', position_x=xpos.width_50, position_y=ypos.xHeight)
x.addAnchor('anusvara', position_x=xpos.width_50, position_y=ypos.indic_headline_top)

x = ugi('k-deva')
x.addKerning(left='ka-deva', right='k-deva')

x = ugi('q-deva')
x.addKerning(left='ka-deva', right='k-deva')

x = ugi('kh-deva')
x.addKerning(left='kha-deva', right='kh-deva')

x = ugi('khh-deva')
x.addKerning(left='kha-deva', right='kh-deva')

x = ugi('j-deva')
x.addKerning(left='ja-deva', right='j-deva')

x = ugi('z-deva')
x.addKerning(left='ja-deva', right='j-deva')

x = ugi('ph-deva')
x.addKerning(left='ka-deva', right='k-deva')

x = ugi('f-deva')
x.addKerning(left='ka-deva', right='k-deva')

x = ugi('y-deva')
x.addKerning(left='ya-deva', right='y-deva')

x = ugi('yy-deva')
x.addKerning(left='ya-deva', right='y-deva')

x = ugi('q_ra-deva')
x.addRecipe('k_ra-deva', 'nukta-deva enable_alignment')

x = ugi('nnn_ra-deva')
x.addRecipe('n_ra-deva', 'nukta-deva enable_alignment')

x = ugi('lll_ra-deva')
x.addRecipe('ll_ra-deva', 'nukta-deva enable_alignment')

x = ugi('dddh_ra-deva')
x.addRecipe('dd_ra-deva', 'nukta-deva enable_alignment')

x = ugi('rh_ra-deva')
x.addRecipe('ddh_ra-deva', 'nukta-deva enable_alignment')

x = ugi('khh_ra-deva')
x.addRecipe('kh_ra-deva', 'nukta-deva enable_alignment')

x = ugi('ghh_ra-deva')
x.addRecipe('g_ra-deva', 'nukta-deva enable_alignment')

x = ugi('z_ra-deva')
x.addRecipe('j_ra-deva', 'nukta-deva enable_alignment')

x = ugi('f_ra-deva')
x.addRecipe('ph_ra-deva', 'nukta-deva enable_alignment')

x = ugi('yy_ra-deva')
x.addRecipe('y_ra-deva', 'nukta-deva enable_alignment')


x = ugi('q_rakar-deva')
x.addRecipe('k_rakar-deva', 'nukta-deva enable_alignment')

x = ugi('nnn_rakar-deva')
x.addRecipe('n_rakar-deva', 'nukta-deva enable_alignment')

x = ugi('ll_rakar-deva')
x.addRecipe('ll_ra-deva decompose')
x.addRecipe('ll-deva', 'rakar-deva')


x = ugi('lll_rakar-deva')
x.addRecipe('ll_rakar-deva', 'nukta-deva enable_alignment')
x.addRecipe('ll-deva', 'rakar-deva', 'nukta-deva enable_alignment')

x = ugi('dddh_rakar-deva')
x.addRecipe('dddh_ra-deva', 'halant-deva enable_alignment')

x = ugi('rh_rakar-deva')
x.addRecipe('ddh_ra-deva', 'nukta-deva disable_alignment', 'halant-deva enable_alignment')


x = ugi('khh_rakar-deva')
x.addRecipe('kh_rakar-deva', 'nukta-deva enable_alignment')

x = ugi('ghh_rakar-deva')
x.addRecipe('g_rakar-deva', 'nukta-deva enable_alignment')

x = ugi('z_rakar-deva')
x.addRecipe('j_rakar-deva', 'nukta-deva enable_alignment')

x = ugi('f_rakar-deva')
x.addRecipe('ph_rakar-deva', 'nukta-deva enable_alignment')

x = ugi('yy_rakar-deva')
x.addRecipe('y_rakar-deva', 'nukta-deva enable_alignment')


x = ugi('dddh-deva')
x.addRecipe('dddha-deva.shifted', 'halant-deva')
x.addRecipe('dda-deva', 'nukta-deva disable_alignment', 'halant-deva disable_alignment')

x = ugi('rh-deva')
x.addRecipe('rha-deva.shifted', 'halant-deva')
x.addRecipe('ddha-deva', 'nukta-deva disable_alignment', 'halant-deva disable_alignment')


x = ugi('tt-deva')
x.addRecipe('tta-deva', 'halant-deva enable_alignment')

x = ugi('tth-deva')
x.addRecipe('ttha-deva', 'halant-deva enable_alignment')
#
# --------------------------------
#
#   MARKS
#
# --------------------------------
#

x = ugi('nukta-deva')
x.addAnchor('_nukta', position_x=xpos.outline_center, position_y=ypos.outline_middle)
x.addAnchor('_bottom', position_x=xpos.outline_center, position_y=ypos.outline_bottom)

x = ugi('highspacingdot-deva')
x.addRecipe('nukta-deva disable_alignment')
x.addBuildString('/highspacingdot-deva/ka-deva')
