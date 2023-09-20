# -*- coding: utf-8 -*-

from .unifiedglyphinfo import CollectedGlyphInfos, xpos, ypos


def collect_infos(infos_dict):
    return infos_dict.update(ugi.unified_infos)


ugi = CollectedGlyphInfos()
x = ugi('Ayb-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)  # 'Ayb-arm'
x.addMetrics(left='Seh-arm', right='Ayb-arm')  # Ayb-arm
x.addKerning(left='Seh-arm', right='Ayb-arm')  # Ayb-arm
x.addRecipe('Seh-arm', 'eh-arm decompose')  # Ayb-arm

x = ugi('Ben-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # 'Ben-arm'
x.addMetrics(left='Vo-arm', right='Ben-arm')  # Ben-arm
x.addKerning(left='Vo-arm', right='Vo-arm')  # Ben-arm
x.addRecipe('Reh-arm', '_part.bar')  # Ben-arm

x = ugi('Ca-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)  # Ca-arm
x.addKerning(left='Ca-arm', right='Ca-arm')  # Ca-arm
x.addRecipe('O decompose', 'Liwn-arm decompose')  # Ca-arm
x.addBuildString('/Za-arm/Cheh-arm/Piwr-arm/Keh-arm/Ca-arm/ca-arm')

x = ugi('Cha-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # 'Cha-arm'
x.addKerning(left='Cha-arm', right='Cha-arm')  # Cha-arm
x.addRecipe('Ja-arm decompose', 'Yiwn-arm decompose')  # Cha-arm
x.addBuildString('/Gim-arm/Za-arm/Jheh-arm/Ja-arm/Cha-arm/Sha-arm/Eh-arm')

x = ugi('Cheh-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # 'Cheh-arm'
x.addKerning(left='Cheh-arm', right='Cheh-arm')  # Cheh-arm
x.addRecipe('cheh-arm decompose')  # Cheh-arm
x.addBuildString('/Ca-arm/Cheh-arm/Jheh-arm/Ja-arm/cheh-arm')

x = ugi('Co-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # 'Co-arm'
x.addKerning(left='Co-arm', right='Co-arm')  # Co-arm
x.addRecipe('o decompose')  # Co-arm
x.addBuildString('/three/Yi-arm/Co-arm')

x = ugi('Da-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.capHeight)  # Da-arm
x.addMetrics(left='Da-arm', right='Da-arm')  # Da-arm
x.addKerning(left='Da-arm', right='Da-arm')  # Da-arm
x.addRecipe('Ben-arm decompose')  # Da-arm

x = ugi('Ech-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.capHeight)  # Ech-arm
x.addMetrics(left='Seh-arm', right='Seh-arm')  # Ech-arm
x.addKerning(left='Seh-arm', right='Seh-arm')  # Ech-arm
x.addRecipe('Ben-arm decompose flip_vertical')  # Ech-arm

x = ugi('Eh-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.capHeight)  # Eh-arm
x.addMetrics(left='Liwn-arm', right='Eh-arm')  # Eh-arm
x.addKerning(left='Eh-arm', right='Eh-arm')  # Eh-arm
x.addRecipe('eh-arm decompose', 'Ech-arm decompose')  # Eh-arm
x.addBuildString('/Gim-arm/Za-arm/Jheh-arm/Ja-arm/Cha-arm/Eh-arm')

x = ugi('Et-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # Et-arm
x.addKerning(left='Vo-arm', right='Vo-arm')  # Et-arm
x.addMetrics(left='Vo-arm', right='Vo-arm')  # Et-arm
x.addRecipe('Ben-arm decompose')  # Et-arm

x = ugi('Feh-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)  # Feh-arm
x.addKerning(left='Feh-arm', right='Feh-arm')  # Feh-arm
x.addRecipe('feh-arm decompose')  # Feh-arm

x = ugi('Ghad-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # Ghad-arm
x.addMetrics(left='Da-arm', right='Ghad-arm')  # Ghad-arm
x.addKerning(left='Da-arm', right='Ghad-arm')  # Ghad-arm
x.addRecipe('Da-arm decompose')  # Ghad-arm

x = ugi('Gim-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.capHeight)  # Gim-arm
x.addKerning(left='Da-arm', right='Da-arm')  # Gim-arm
x.addMetrics(left='Da-arm', right='Da-arm')  # Gim-arm
x.addRecipe('Da-arm decompose')  # Gim-arm
x.addBuildString('/Gim-arm/Za-arm/Jheh-arm/Ja-arm/Cha-arm/Eh-arm')

x = ugi('Ho-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)  # Ho-arm
x.addKerning(left='Ho-arm', right='Ho-arm')  # Ho-arm
x.addRecipe('Liwn-arm decompose', 'cheh-arm decompose')  # Ho-arm
x.addBuildString('/Ech-arm/Ho-arm/Eh-arm/ho-arm')

x = ugi('Ini-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)  # Ini-arm
x.addKerning(left='Eh-arm', right='Ini-arm')  # Ini-arm
x.addMetrics(left='Liwn-arm', right='Ini-arm')  # Ini-arm
x.addRecipe('Reh-arm decompose', '_part.stem')  # Ini-arm

x = ugi('Ja-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # Ja-arm
x.addKerning(left='Ja-arm', right='Ja-arm')  # Ja-arm
x.addRecipe('Sha-arm decompose')  # Ja-arm
x.addBuildString('/Gim-arm/Za-arm/Jheh-arm/Ja-arm/Cha-arm/Eh-arm')

x = ugi('Jheh-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)  # Jheh-arm
x.addMetrics(left='Za-arm', right='Za-arm')  # Jheh-arm
x.addKerning(left='Za-arm', right='Za-arm')  # Jheh-arm
x.addRecipe('Za-arm decompose')  # Jheh-arm
x.addBuildString('/Gim-arm/Za-arm/Jheh-arm/Ja-arm/Cha-arm/Eh-arm')

x = ugi('Keh-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # Keh-arm
x.addKerning(left='Keh-arm', right='Keh-arm')  # Keh-arm
x.addRecipe('Gim-arm flip_horizontal decompose', '_part.bar')  # Keh-arm
x.addBuildString('/keh-arm/Keh-arm/Gim-arm')

x = ugi('Ken-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.capHeight)  # Ken-arm
x.addMetrics(left='Seh-arm', right='Vo-arm')  # Ken-arm
x.addKerning(left='Ken-arm', right='Ken-arm')  # Ken-arm
x.addRecipe('Ini-arm flip_horizontal flip_vertical decompose')  # Ken-arm

x = ugi('Liwn-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)  # Liwn-arm
x.addMetrics(left='Liwn-arm', right='Liwn-arm')  # Liwn-arm
x.addKerning(left='Eh-arm', right='Liwn-arm')  # Liwn-arm
x.addRecipe('Eh-arm decompose', 'Ghad-arm decompose')  # Liwn-arm
x.addBuildString('/Eh-arm/Liwn-arm/Et-arm')

x = ugi('Men-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)  # Men-arm
x.addKerning(left='Seh-arm', right='Men-arm')  # Men-arm
x.addMetrics(left='Seh-arm')  # Men-arm
x.addRecipe('Da-arm decompose', 'Seh-arm')  # Men-arm

x = ugi('Now-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.capHeight)  # Now-arm
x.addKerning(left='Now-arm', right='Now-arm')  # Now-arm
x.addRecipe('Ghad-arm flip_horizontal flip_vertical decompose')  # Now-arm

x = ugi('Oh-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # Oh-arm
x.addKerning(left='Oh-arm', right='Oh-arm')  # Oh-arm
x.addRecipe('O decompose')  # Oh-arm

x = ugi('Peh-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # Peh-arm
x.addKerning(left='Da-arm', right='Vo-arm')  # Peh-arm
x.addMetrics(left='Da-arm', right='Vo-arm')  # Peh-arm
x.addRecipe('Reh-arm flip_horizontal decompose', '_part.stem disable_alignment')  # Peh-arm

x = ugi('Piwr-arm')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.capHeight)  # Piwr-arm
x.addKerning(left='Piwr-arm', right='Piwr-arm')  # Piwr-arm
x.addRecipe('Phi decompose')  # Piwr-arm

x = ugi('Ra-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.capHeight)  # Ra-arm
x.addMetrics(left='Vo-arm', right='Da-arm')  # Ra-arm
x.addKerning(left='Vo-arm', right='Da-arm')  # Ra-arm
x.addRecipe('Vo-arm', 'Da-arm decompose')  # Ra-arm
x.addRecipe('_part.Vo-arm', '_part.bar')  # Ra-arm

x = ugi('Reh-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # Reh-arm
x.addMetrics(left='Vo-arm', right='Reh-arm')  # Reh-arm
x.addKerning(left='Vo-arm', right='Reh-arm')  # Reh-arm
x.addRecipe('Vo-arm decompose')  # Reh-arm

x = ugi('Seh-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)  # Seh-arm
x.addKerning(left='Seh-arm', right='Seh-arm')  # Seh-arm
x.addMetrics(left='Seh-arm', right='Seh-arm')  # Seh-arm
x.addRecipe('U decompose')  # Seh-arm

x = ugi('Sha-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)  # Sha-arm
x.addKerning(left='Sha-arm', right='Sha-arm')  # Sha-arm
x.addRecipe('Cha-arm flip_horizontal flip_vertical')  # Sha-arm
x.addRecipe('Ech-arm decompose', 'tilde decompose')  # Sha-arm
x.addBuildString('/Ho-arm/Ja-arm/Sha-arm/Cha-arm/Jheh-arm')

x = ugi('Tiwn-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # Tiwn-arm
x.addKerning(left='Tiwn-arm', right='Tiwn-arm')  # Tiwn-arm
x.addBuildString('/Ben-arm/Tiwn-arm/Feh-arm/feh-arm')

x = ugi('To-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # To-arm
x.addKerning(left='Vo-arm', right='To-arm')  # To-arm
x.addMetrics(left='Vo-arm', right='To-arm')  # To-arm
x.addRecipe('Ben-arm decompose', 'to-arm decompose')  # To-arm

x = ugi('Vew-arm')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.capHeight)  # Vew-arm
x.addMetrics(left='Ken-arm', right='Ghad-arm')  # Vew-arm
x.addKerning(left='Ken-arm', right='Ghad-arm')  # Vew-arm
x.addRecipe('Ken-arm', 'Ghad-arm decompose')  # Vew-arm
x.addBuildString('/Ken-arm/Vew-arm/vew-arm')

x = ugi('Vo-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # Vo-arm
x.addMetrics(left='Vo-arm', right='Vo-arm')  # Vo-arm
x.addKerning(left='Vo-arm', right='Vo-arm')  # Vo-arm
x.addRecipe('Seh-arm decompose flip_vertical flip_horizontal')  # Vo-arm

x = ugi('Xeh-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.capHeight)  # Xeh-arm
x.addMetrics(left='Liwn-arm', right='Xeh-arm')  # Xeh-arm
x.addKerning(left='Eh-arm', right='Xeh-arm')  # Xeh-arm
x.addRecipe('Eh-arm decompose', 'Seh-arm decompose')  # Xeh-arm

x = ugi('Yi-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # Yi-arm
x.addKerning(left='Yi-arm', right='Yi-arm')  # Yi-arm
x.addRecipe('three decompose')  # Yi-arm
x.addRecipe('B decompose')  # Yi-arm
x.addBuildString('/three/Yi-arm/Co-arm')

x = ugi('Yiwn-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.capHeight)  # Yiwn-arm
x.addMetrics(left='Liwn-arm', right='Yiwn-arm')  # Yiwn-arm
x.addKerning(left='Eh-arm', right='Yiwn-arm')  # Yiwn-arm
x.addRecipe('Xeh-arm decompose')  # Yiwn-arm

x = ugi('Za-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)  # Za-arm
x.addKerning(left='Za-arm', right='Za-arm')  # Za-arm
x.addMetrics(left='Za-arm', right='Za-arm')  # Za-arm
x.addRecipe('nine decompose', 'Eh-arm decompose')  # Za-arm
x.addBuildString('/Gim-arm/Za-arm/Jheh-arm/Ja-arm/Cha-arm/Eh-arm')

x = ugi('Zhe-arm')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.capHeight)  # Zhe-arm
x.addKerning(left='Zhe-arm', right='To-arm')  # Zhe-arm
x.addMetrics(left='Zhe-arm', right='To-arm')  # Zhe-arm
x.addRecipe('Gim-arm flip_vertical decompose')  # Zhe-arm


x = ugi('Ayb_Now-arm')
x.addKerning(left='Ayb-arm', right='Now-arm')  # Ayb_Now-arm

x = ugi('Yiwn_Keh-arm')
x.addKerning(left='Yiwn-arm', right='Keh-arm')  # Yiwn_Keh-arm

x = ugi('To_Yi-arm')
x.addKerning(left='To-arm', right='Yi-arm')  # To_Yi-arm

x = ugi('Men_Now-arm')
x.addKerning(left='Men-arm', right='Now-arm')  # Men_Now-arm

x = ugi('Cheh_Now-arm')
x.addKerning(left='Cheh-arm', right='Now-arm')  # Cheh_Now-arm

#
# --------------------------------
#
#   Lowercase
#
# --------------------------------
#

x = ugi('ayb-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'ayb-arm'
x.addKerning(left='ayb-arm', right='ayb-arm')  # ayb-arm
x.addMetrics(left='ayb-arm', right='ayb-arm')  # ayb-arm
x.addRecipe('seh-arm decompose', 'seh-arm decompose')  # ayb-arm
x.addBuildString('/ayb-arm/seh-arm/vo-arm')

x = ugi('ben-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'ben-arm'
x.addMetrics(left='ben-arm', right='ben-arm')  # ben-arm
x.addKerning(left='ben-arm', right='ben-arm')  # ben-arm
x.addRecipe('reh-arm decompose', '_part.bar')  # ben-arm
x.addRecipe('vo-arm decompose', 'p decompose', '_part.bar')  # ben-arm
x.addBuildString('/ech-arm/ben-arm/vo-arm')

x = ugi('ca-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.outline_top)  # 'ca-arm'
x.addMetrics(left='oh-arm', right='zhe-arm')  # ca-arm
x.addKerning(left='za-arm', right='zhe-arm')  # ca-arm
x.addRecipe('zhe-arm decompose')  # ca-arm

x = ugi('cha-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'cha-arm'
x.addKerning(left='cha-arm', right='cha-arm')  # cha-arm
x.addRecipe('sha-arm decompose', 's decompose')  # cha-arm

x = ugi('cheh-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.outline_top)  # 'cheh-arm'
x.addKerning(left='cheh-arm', right='cheh-arm')  # cheh-arm
x.addRecipe('ja-arm decompose', '_part.bar')  # cheh-arm

x = ugi('co-arm')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.xHeight)  # 'co-arm'
x.addKerning(left='za-arm', right='co-arm')  # co-arm
x.addMetrics(left='oh-arm', right='co-arm')  # co-arm
x.addRecipe('q decompose', 'e decompose')  # co-arm

x = ugi('da-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'da-arm'
x.addKerning(left='vo-arm', right='gim-arm')  # da-arm
x.addMetrics(left='vo-arm', right='gim-arm')  # da-arm
x.addRecipe('vo-arm decompose', '_part.bar')  # da-arm

x = ugi('ech-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.xHeight)  # 'ech-arm'
x.addMetrics(left='ech-arm', right='ayb-arm')  # ech-arm
x.addKerning(left='ech-arm', right='ayb-arm')  # ech-arm
x.addRecipe('seh-arm decompose', 'l decompose', '_part.bar')  # ech-arm
x.addBuildString('/ben-arm/ech-arm/vo-arm')

x = ugi('ech_yiwn-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.xHeight)  # 'ech_yiwn-arm'
x.addMetrics(left='ech-arm', right='gim-arm')  # ech_yiwn-arm
x.addKerning(left='ech-arm', right='gim-arm')  # ech_yiwn-arm
x.addRecipe('ken-arm decompose', 'yiwn-arm decompose')  # ech_yiwn-arm

x = ugi('eh-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.xHeight)  # 'eh-arm'
x.addMetrics(left='ech-arm', right='eh-arm')  # eh-arm
x.addKerning(left='eh-arm', right='eh-arm')  # eh-arm
x.addRecipe('ech-arm decompose', 'cedillacomb decompose')  # eh-arm
x.addRecipe('l decompose', '_part.bar', 'e decompose')  # eh-arm

x = ugi('et-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.xHeight)  # 'et-arm'
x.addMetrics(left='ben-arm', right='vo-arm')  # et-arm
x.addKerning(left='ben-arm', right='vo-arm')  # et-arm
x.addRecipe('reh-arm', '_part.bar')  # et-arm

x = ugi('feh-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.outline_top)  # 'feh-arm'
x.addKerning(left='feh-arm', right='feh-arm')  # feh-arm
x.addRecipe('B decompose', 's decompose')  # feh-arm

x = ugi('ghad-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.xHeight)  # 'ghad-arm'
x.addMetrics(left='vo-arm', right='za-arm')  # ghad-arm
x.addKerning(left='vo-arm', right='za-arm')  # ghad-arm
x.addRecipe('da-arm decompose')  # ghad-arm
x.addRecipe('vo-arm decompose', 'liwn-arm decompose')  # ghad-arm

x = ugi('gim-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'gim-arm'
x.addKerning(left='za-arm', right='gim-arm')  # gim-arm
x.addMetrics(left='oh-arm', right='gim-arm')  # gim-arm
x.addRecipe('q disable_alignment', '_part.bar')  # gim-arm

x = ugi('ho-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.outline_top)  # 'ho-arm'
x.addMetrics(left='ho-arm', right='ho-arm')  # ho-arm
x.addKerning(left='ho-arm', right='ho-arm')  # ho-arm
x.addRecipe('f decompose', 'eh-arm decompose')  # ho-arm

x = ugi('ini-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.xHeight)  # 'ini-arm'
x.addMetrics(left='ini-arm', right='vo-arm')  # ini-arm
x.addKerning(left='ini-arm', right='vo-arm')  # ini-arm
x.addRecipe('ho-arm decompose')  # ini-arm

x = ugi('ja-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.outline_top)  # 'ja-arm'
x.addKerning(left='ja-arm', right='ja-arm')  # ja-arm
x.addRecipe('a decompose', 'eh-arm decompose')  # ja-arm

x = ugi('jheh-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.xHeight)  # 'jheh-arm'
x.addKerning(left='jheh-arm', right='jheh-arm')  # jheh-arm
x.addRecipe('sha-arm decompose')  # jheh-arm

x = ugi('keh-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.xHeight)  # 'keh-arm'
x.addMetrics(left='keh-arm', right='oh-arm')  # keh-arm
x.addKerning(left='ben-arm', right='ben-arm')  # keh-arm
x.addRecipe('p decompose', '_part.bar')  # keh-arm

x = ugi('ken-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.xHeight)  # 'ken-arm'
x.addMetrics(left='ech-arm', right='peh-arm')  # ken-arm
x.addKerning(left='ech-arm', right='peh-arm')  # ken-arm
x.addRecipe('seh-arm decompose', 'l decompose', 'q decompose')  # ken-arm

x = ugi('liwn-arm')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.xHeight)  # 'liwn-arm'
x.addMetrics(left='ben-arm', right='za-arm')  # liwn-arm
x.addKerning(left='ben-arm', right='za-arm')  # liwn-arm
x.addRecipe('za-arm decompose', 'idotless decompose')  # liwn-arm

x = ugi('men-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.outline_top)  # 'men-arm'
x.addMetrics(left='ayb-arm', right='men-arm')  # men-arm
x.addKerning(left='ayb-arm', right='men-arm')  # men-arm
x.addRecipe('seh-arm decompose')  # men-arm

x = ugi('now-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.xHeight)  # 'now-arm'
x.addMetrics(left='now-arm', right='ayb-arm')  # now-arm
x.addKerning(left='now-arm', right='ayb-arm')  # now-arm
x.addRecipe('seh-arm decompose', 'eh-arm decompose')  # now-arm

x = ugi('oh-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.xHeight)  # 'oh-arm'
x.addMetrics(left='oh-arm', right='oh-arm')  # oh-arm
x.addKerning(left='za-arm', right='oh-arm')  # oh-arm
x.addRecipe('o decompose')  # oh-arm

x = ugi('peh-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'peh-arm'
x.addMetrics(left='ayb-arm', right='peh-arm')  # peh-arm
x.addKerning(left='ayb-arm', right='peh-arm')  # peh-arm
x.addRecipe('ayb-arm decompose')  # peh-arm

x = ugi('piwr-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.xHeight)  # 'piwr-arm'
x.addKerning(left='ayb-arm', right='vo-arm')  # piwr-arm
x.addMetrics(left='ayb-arm', right='vo-arm')  # piwr-arm
x.addRecipe('tiwn-arm decompose', 'l decompose')  # piwr-arm

x = ugi('ra-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.xHeight)  # 'ra-arm'
x.addKerning(left='vo-arm', right='da-arm')  # ra-arm
x.addMetrics(left='vo-arm', right='ra-arm')  # ra-arm
x.addRecipe('vo-arm decompose', '_part.bar')  # ra-arm

x = ugi('reh-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.xHeight)  # 'reh-arm'
x.addKerning(left='ben-arm', right='vo-arm')  # reh-arm
x.addMetrics(left='ben-arm', right='vo-arm')  # reh-arm
x.addRecipe('vo-arm decompose')  # reh-arm

x = ugi('seh-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'seh-arm'
x.addKerning(left='ayb-arm', right='ayb-arm')  # seh-arm
x.addMetrics(left='ayb-arm', right='ayb-arm')  # seh-arm
x.addRecipe('u decompose')  # seh-arm
x.addBuildString('/Seh-arm/seh-arm/vo-arm')

x = ugi('sha-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.xHeight)  # 'sha-arm'
x.addKerning(left='sha-arm', right='sha-arm')  # sha-arm
x.addRecipe('two decompose')  # sha-arm

x = ugi('tiwn-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'tiwn-arm'
x.addKerning(left='ayb-arm', right='vo-arm')  # tiwn-arm
x.addMetrics(left='ayb-arm', right='vo-arm')  # tiwn-arm
x.addRecipe('seh-arm decompose', 'vo-arm decompose')  # tiwn-arm

x = ugi('to-arm')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.xHeight)  # 'to-arm'
x.addKerning(left='ben-arm', right='to-arm')  # to-arm
x.addMetrics(left='ben-arm', right='to-arm')  # to-arm
x.addRecipe('p decompose', 'e decompose')  # to-arm

x = ugi('vew-arm')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.outline_top)  # 'vew-arm'
x.addMetrics(left='ayb-arm', right='za-arm')  # vew-arm
x.addKerning(left='ayb-arm', right='za-arm')  # vew-arm
x.addRecipe('seh-arm decompose', 'za-arm decompose', 'd decompose')  # vew-arm

x = ugi('vo-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'vo-arm'
x.addMetrics(left='vo-arm', right='vo-arm')  # vo-arm
x.addKerning(left='vo-arm', right='vo-arm')  # vo-arm
x.addRecipe('n decompose')  # vo-arm
x.addBuildString('/seh-arm/vo-arm')

x = ugi('xeh-arm')
x.addAnchor('top', position_x=xpos.width_75, position_y=ypos.xHeight)  # 'xeh-arm'
x.addMetrics(left='ini-arm', right='ayb-arm')  # xeh-arm
x.addKerning(left='ini-arm', right='ayb-arm')  # xeh-arm
x.addRecipe('ini-arm decompose', 'seh-arm decompose')  # xeh-arm

x = ugi('yi-arm')
x.addAnchor('top', position_x=xpos.width_50, position_y=ypos.xHeight)  # 'yi-arm'
x.addKerning(left='yi-arm', right='yi-arm')  # yi-arm

x = ugi('yiwn-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'yiwn-arm'
x.addKerning(left='vo-arm', right='gim-arm')  # yiwn-arm
x.addMetrics(left='vo-arm', right='gim-arm')  # yiwn-arm
x.addRecipe('liwn-arm decompose')  # yiwn-arm

x = ugi('za-arm')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'za-arm'
x.addKerning(left='za-arm', right='za-arm')  # za-arm
x.addMetrics(left='oh-arm', right='za-arm')  # za-arm
x.addRecipe('gim-arm decompose')  # za-arm
x.addRecipe('q', '_part.bar')  # za-arm

x = ugi('zhe-arm')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.outline_top)  # 'zhe-arm'
x.addKerning(left='za-arm', right='zhe-arm')  # zhe-arm
x.addMetrics(left='oh-arm', right='zhe-arm')  # zhe-arm
x.addRecipe('eth', 'd decompose', '_part.bar')  # zhe-arm


x = ugi('za_yi-arm')
x.addKerning(left='za-arm', right='yi-arm')  # za_yi-arm

x = ugi('liwn_yi-arm')
x.addKerning(left='liwn-arm', right='yi-arm')  # liwn_yi-arm

x = ugi('ghad_yi-arm')
x.addKerning(left='ghad-arm', right='peh-arm')  # ghad_yi-arm

x = ugi('cheh_now-arm')
x.addKerning(left='cheh-arm', right='ayb-arm')  # cheh_now-arm

x = ugi('men_ken-arm')
x.addKerning(left='ayb-arm', right='peh-arm')  # men_ken-arm

x = ugi('sha_yi-arm')
x.addKerning(left='sha-arm', right='yi-arm')  # sha_yi-arm

x = ugi('cha_yi-arm')
x.addKerning(left='cha-arm', right='yi-arm')  # cha_yi-arm

x = ugi('jheh_yi-arm')
x.addKerning(left='jheh-arm', right='yi-arm')  # jheh_yi-arm

x = ugi('vew_yi-arm')
x.addKerning(left='ayb-arm', right='yi-arm')  # vew_yi-arm

x = ugi('men_now-arm')
x.addKerning(left='ayb-arm', right='ayb-arm')  # men_now-arm

x = ugi('men_ech-arm')
x.addKerning(left='ayb-arm', right='ayb-arm')  # men_ech-arm

x = ugi('men_ini-arm')
x.addKerning(left='ayb-arm', right='vo-arm')  # men_ini-arm

x = ugi('vew_now-arm')
x.addKerning(left='ayb-arm', right='ayb-arm')  # vew_now-arm

x = ugi('men_xeh-arm')
x.addKerning(left='ayb-arm', right='ayb-arm')  # men_xeh-arm


x = ugi('ayb_emphasis-arm')
x.addKerning(left='ayb-arm', right='ayb-arm')  # ayb_emphasis-arm

x = ugi('ayb_exclam-arm')
x.addKerning(left='ayb-arm', right='ayb-arm')  # ayb_exclam-arm

x = ugi('ayb_question-arm')
x.addKerning(left='ayb-arm', right='ayb-arm')  # ayb_question-arm

x = ugi('ech_emphasis-arm')
x.addKerning(left='ech-arm', right='ayb-arm')  # ech_emphasis-arm

x = ugi('ech_exclam-arm')
x.addKerning(left='ech-arm', right='ayb-arm')  # ech_exclam-arm

x = ugi('ech_question-arm')
x.addKerning(left='ech-arm', right='ayb-arm')  # ech_question-arm

x = ugi('ini_emphasis-arm')
x.addKerning(left='ini-arm', right='vo-arm')  # ini_emphasis-arm

x = ugi('ini_exclam-arm')
x.addKerning(left='ini-arm', right='vo-arm')  # ini_exclam-arm

x = ugi('ini_question-arm')
x.addKerning(left='ini-arm', right='vo-arm')  # ini_question-arm

x = ugi('eh_emphasis-arm')
x.addKerning(left='eh-arm', right='eh-arm')  # eh_emphasis-arm

x = ugi('eh_exclam-arm')
x.addKerning(left='eh-arm', right='eh-arm')  # eh_exclam-arm

x = ugi('eh_question-arm')
x.addKerning(left='eh-arm', right='eh-arm')  # eh_question-arm

x = ugi('et_emphasis-arm')
x.addKerning(left='ben-arm', right='vo-arm')  # et_emphasis-arm

x = ugi('et_exclam-arm')
x.addKerning(left='ben-arm', right='vo-arm')  # et_exclam-arm

x = ugi('et_question-arm')
x.addKerning(left='ben-arm', right='vo-arm')  # et_question-arm

x = ugi('vo_emphasis-arm')
x.addKerning(left='vo-arm', right='vo-arm')  # vo_emphasis-arm

x = ugi('vo_exclam-arm')
x.addKerning(left='vo-arm', right='vo-arm')  # vo_exclam-arm

x = ugi('vo_question-arm')
x.addKerning(left='vo-arm', right='vo-arm')  # vo_question-arm

x = ugi('oh_emphasis-arm')
x.addKerning(left='za-arm', right='oh-arm')  # oh_emphasis-arm

x = ugi('oh_exclam-arm')
x.addKerning(left='za-arm', right='oh-arm')  # oh_exclam-arm

x = ugi('oh_question-arm')
x.addKerning(left='za-arm', right='oh-arm')  # oh_question-arm

x = ugi('et_emphasis-arm.short')
x.addKerning(right='vo-arm')  # et_emphasis-arm.short

x = ugi('et_exclam-arm.short')
x.addKerning(right='vo-arm')  # et_exclam-arm.short

x = ugi('et_question-arm.short')
x.addKerning(right='vo-arm')  # et_question-arm.short

x = ugi('ini_emphasis-arm.short')
x.addKerning(right='vo-arm')  # ini_emphasis-arm.short

x = ugi('ini_exclam-arm.short')
x.addKerning(right='vo-arm')  # ini_exclam-arm.short

x = ugi('ini_question-arm.short')
x.addKerning(right='vo-arm')  # ini_question-arm.short


x = ugi('ben-arm.short')
x.addKerning(right='ben-arm')  # ben-arm.short
x.addMetrics(left='ben-arm', right='ben-arm')  # ben-arm.short
x.addRecipe('ben-arm decompose')  # ben-arm.short

x = ugi('cha-arm.long')
x.addKerning(left='cha-arm', right='liwn-arm.long')  # cha-arm.long

x = ugi('co-arm.short')
x.addKerning(right='co-arm')  # co-arm.short
x.addRecipe('co-arm decompose')  # co-arm.short
x.addMetrics(left='co-arm', right='co-arm')  # co-arm.short

x = ugi('et-arm.short')
x.addKerning(right='vo-arm')  # et-arm.short
x.addMetrics(left='et-arm', right='et-arm')  # et-arm.short
x.addRecipe('et-arm decompose')  # et-arm.short

x = ugi('ghad-arm.long')
x.addKerning(left='vo-arm', right='liwn-arm.long')  # ghad-arm.long
x.addMetrics(left='ghad-arm')  # ghad-arm.long
x.addRecipe('ghad-arm decompose')  # ghad-arm.long

x = ugi('ini-arm.short')
x.addKerning(right='vo-arm')  # ini-arm.short
x.addMetrics(left='ini-arm', right='ini-arm')  # ini-arm.short
x.addRecipe('ini-arm decompose')  # ini-arm.short

x = ugi('jheh-arm.long')
x.addKerning(left='jheh-arm', right='liwn-arm.long')  # jheh-arm.long

x = ugi('liwn-arm.long')
x.addKerning(left='ben-arm', right='liwn-arm.long')  # liwn-arm.long
x.addMetrics(left='liwn-arm')  # liwn-arm.long
x.addRecipe('liwn-arm decompose')  # liwn-arm.long

x = ugi('reh-arm.short')
x.addKerning(right='vo-arm')  # reh-arm.short
x.addMetrics(left='reh-arm', right='reh-arm')  # reh-arm.short
x.addRecipe('reh-arm decompose')  # reh-arm.short

x = ugi('sha-arm.long')
x.addKerning(left='sha-arm', right='liwn-arm.long')  # sha-arm.long

x = ugi('vew-arm.long')
x.addKerning(left='ayb-arm', right='liwn-arm.long')  # vew-arm.long
x.addMetrics(left='vew-arm')  # vew-arm.long
x.addRecipe('vew-arm decompose')  # vew-arm.long

x = ugi('xeh-arm.short')
x.addKerning(right='ayb-arm')  # xeh-arm.short
x.addMetrics(left='xeh-arm', right='xeh-arm')  # xeh-arm.short
x.addRecipe('xeh-arm decompose')  # xeh-arm.short

x = ugi('yi-arm.short')
x.addKerning(right='yi-arm')  # yi-arm.short
x.addMetrics(left='yi-arm', right='yi-arm')  # yi-arm.short
x.addRecipe('yi-arm decompose')  # yi-arm.short

x = ugi('za-arm.long')
x.addKerning(left='za-arm', right='liwn-arm.long')  # za-arm.long
x.addMetrics(left='za-arm')  # za-arm.long
x.addRecipe('za-arm decompose')  # za-arm.long

x = ugi('za-arm.short')
x.addMetrics(left='za-arm', right='za-arm.short')
x.addRecipe('za-arm decompose')
x.addKerning(left='za-arm', right='liwn-arm.short')  # za-arm.long

x = ugi('liwn-arm.short')
x.addMetrics(left='liwn-arm', right='za-arm.short')
x.addRecipe('liwn-arm decompose')
x.addKerning(left='ben-arm', right='liwn-arm.short')  # liwn-arm.long

x = ugi('ghad-arm.short')
x.addMetrics(left='ghad-arm', right='za-arm.short')
x.addRecipe('ghad-arm decompose')
x.addKerning(left='vo-arm', right='liwn-arm.short')  # ghad-arm.long

x = ugi('vew-arm.short')
x.addMetrics(left='vew-arm', right='za-arm.short')
x.addRecipe('vew-arm decompose')
x.addKerning(left='ayb-arm', right='liwn-arm.short')  # vew-arm.long


x = ugi('ech_yiwn_emphasis-arm')
x.addKerning(left='ech-arm', right='gim-arm')  # ech_yiwn_emphasis-arm

x = ugi('ech_yiwn_exclam-arm')
x.addKerning(left='ech-arm', right='gim-arm')  # ech_yiwn_exclam-arm

x = ugi('ech_yiwn_question-arm')
x.addKerning(left='ech-arm', right='gim-arm')  # ech_yiwn_question-arm


x = ugi('men_ech_emphasis-arm')
x.addKerning(left='ayb-arm', right='ayb-arm')  # men_ech_emphasis-arm

x = ugi('men_ech_exclam-arm')
x.addKerning(left='ayb-arm', right='ayb-arm')  # men_ech_exclam-arm

x = ugi('men_ech_question-arm')
x.addKerning(left='ayb-arm', right='ayb-arm')  # men_ech_question-arm

x = ugi('men_ini_emphasis-arm')
x.addKerning(left='ayb-arm', right='vo-arm')  # men_ini_emphasis-arm

x = ugi('men_ini_exclam-arm')
x.addKerning(left='ayb-arm', right='vo-arm')  # men_ini_exclam-arm

x = ugi('men_ini_question-arm')
x.addKerning(left='ayb-arm', right='vo-arm')  # men_ini_question-arm


#
# --------------------------------
#
#   Punctuation
#
# --------------------------------
#

x = ugi('abbreviation-arm')
x.addAnchor('_top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'ayb-arm'
x.addRecipe('question-arm rotate_180 decompose')  # abbreviation-arm

x = ugi('apostrophe-arm')
x.addMetrics(left='quoteright', right='quoteright')  # apostrophe-arm
x.addRecipe('quoteright')  # apostrophe-arm

x = ugi('comma-arm')
x.addRecipe('emphasis-arm flip_horizontal')  # comma-arm
x.addMetrics(left='emphasis-arm', right='emphasis-arm')  # comma-arm

x = ugi('dram-arm')
x.addRecipe('Da-arm decompose')  # dram-arm
x.addBuildString('/yen/liraturkish/Euro/dram-arm/Ben-arm')

x = ugi('emphasis-arm')
x.addRecipe('acute decompose')  # emphasis-arm
x.addAnchor('_top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'ayb-arm'

x = ugi('exclam-arm')
x.addRecipe('tilde decompose')  # exclam-arm
x.addAnchor('_top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'ayb-arm'

x = ugi('hyphen-arm')
x.addRecipe('quotesingle rotate_90', 'hyphen')  # hyphen-arm
x.addMetrics(left='hyphen', right='hyphen')  # hyphen-arm
x.addBuildString('արք֊դուքս')

x = ugi('leftFacingEternity-arm')
x.addRecipe('rightFacingEternity-arm flip_horizontal')  # leftFacingEternity-arm

x = ugi('period-arm')
x.addRecipe('colon')  # period-arm
x.addBuildString('բայց։')

x = ugi('question-arm')
x.addRecipe('brevecomb flip_vertical decompose', 'ringcomb decompose')  # question-arm
x.addAnchor('_top', position_x=xpos.outline_center, position_y=ypos.xHeight)  # 'ayb-arm'

x = ugi('rightFacingEternity-arm')
x.addRecipe('leftFacingEternity-arm flip_horizontal')  # rightFacingEternity-arm

x = ugi('ringhalfleft-arm')
x.addRecipe('brevecomb rotate_90 flip_vertical')  # ringhalfleft-arm
x.addMetrics(left='=50', right='=50')  # ringhalfleft-arm
