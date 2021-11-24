# -*- coding: utf-8 -*-

from unifiedglyphinfo import CollectedGlyphInfos, xpos, ypos


def collect_infos(infos_dict):
    return infos_dict.update(ugi.unified_infos)


ugi = CollectedGlyphInfos()

x = ugi('A-cy')
x.addKerning(left='A-cy', right='A-cy')  # 'A-cy',

x = ugi('Abreve-cy')
x.addMetrics(left='A-cy', right='A-cy')
x.addKerning(left='A-cy', right='A-cy')  # 'Abreve-cy',

x = ugi('Adieresis-cy')
x.addMetrics(left='A-cy', right='A-cy')  # Adieresis-cy
x.addKerning(left='A-cy', right='A-cy')  # 'Adieresis-cy',

x = ugi('Aie-cy')
x.addMetrics(right='Ie-cy')  # Aie-cy
x.addKerning(left='Aie-cy', right='Ie-cy')  # 'Aie-cy',

x = ugi('Be-cy')
x.addRecipe('Softsign-cy', '_part.bar')
x.addRecipe('Softsign-cy', 'F decompose')
x.addMetrics(left='En-cy')  # Be-cy
x.addKerning(left='En-cy', right='Be-cy')  # 'Be-cy',

x = ugi('Che-cy')
x.addRecipe('u decompose', 'I decompose')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('#bottomleft', position_x=xpos.stem_bottom_left, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(right='En-cy')  # Che-cy
x.addKerning(left='Che-cy', right='En-cy')  # 'Che-cy',

x = ugi('Cheabkhasian-cy')
x.addRecipe('ie-cy decompose', '_part.hook')
x.addKerning(left='Cheabkhasian-cy', right='Cheabkhasian-cy')  # 'Cheabkhasian-cy',

x = ugi('Chedescender-cy')
x.addRecipe('Che-cy disable_alignment', '_part.toothright-cy')
x.addRecipe('Che-cy', 'toothright-cy')
x.addMetrics(left='Che-cy', right='Tse-cy')  # Chedescender-cy
x.addKerning(left='Che-cy', right='De-cy')  # 'Chedescender-cy',

x = ugi('Chedescenderabkhasian-cy')
x.addRecipe('Cheabkhasian-cy', '_part.toothcentered-cy')
x.addRecipe('Cheabkhasian-cy', 'toothcentered-cy')
x.addMetrics(left='Cheabkhasian-cy', right='Cheabkhasian-cy')  # Chedescenderabkhasian-cy
x.addKerning(left='Cheabkhasian-cy', right='Cheabkhasian-cy')  # 'Chedescenderabkhasian-cy',

x = ugi('Chedieresis-cy')
x.addMetrics(left='Che-cy', right='En-cy')  # Chedieresis-cy
x.addKerning(left='Che-cy', right='En-cy')  # 'Chedieresis-cy',

x = ugi('Chekhakassian-cy')
x.addRecipe('Che-cy', '_part.toothleft-cy')
x.addRecipe('Che-cy', 'toothleft-cy')
x.addMetrics(left='Che-cy', right='En-cy')  # Chekhakassian-cy
x.addKerning(left='Che-cy', right='En-cy')  # 'Chekhakassian-cy',

x = ugi('Cheverticalstroke-cy')
x.addRecipe('Che-cy', '_part.stem')
x.addMetrics(left='Che-cy', right='En-cy')
x.addBuildString('/Che-cy/cheverticalstroke-cy/Cheverticalstroke-cy/cheverticalstroke-cy.sc')
x.addKerning(left='Che-cy', right='En-cy')  # 'Cheverticalstroke-cy',

x = ugi('De-cy')
x.addRecipe('El-cy decompose', 'Tse-cy decompose')
x.addMetrics(right='Tse-cy')  # De-cy
x.addKerning(left='De-cy', right='De-cy')  # 'De-cy',

x = ugi('De-cy.loclBGR')
x.addRecipe('De-cy decompose', 'Lambda')
x.addMetrics(left='De-cy', right='=|De-cy')  # De-cy.loclBGR
x.addKerning(left='De-cy')  # '',
x.addBuildString('/De-cy.loclBGR/De-cy/de-cy/de-cy.loclBGR.sc')

x = ugi('Dje-cy')
x.addRecipe('T decompose', 'b decompose')
x.addMetrics(left='Te-cy', right='Be-cy')  # Dje-cy
x.addKerning(left='Te-cy', right='Be-cy')  # 'Dje-cy',
x.addBuildString('/Softsign-cy/Hardsign-cy/Nje-cy/Tshe-cy/Dje-cy/Yat-cy/Ghemiddlehook-cy/Kabashkir-cy/Enghe-cy')

x = ugi('Dzeabkhasian-cy')
x.addRecipe('Ezh')
x.addRecipe('seven decompose', 'five decompose')
x.addMetrics(left='Ze-cy', right='Dzeabkhasian-cy')  # Dzeabkhasian-cy
x.addKerning(left='Ze-cy', right='Dzeabkhasian-cy')  # 'Dzeabkhasian-cy',

x = ugi('Dzhe-cy')
x.addRecipe('Tsebase-cy', '_part.toothcentered-cy')
x.addRecipe('Tsebase-cy', 'toothcentered-cy')
x.addMetrics(left='En-cy', right='En-cy')  # Dzhe-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Dzhe-cy',

x = ugi('Dze-cy')
x.addKerning(left='Dze-cy', right='Dze-cy')  # 'Dze-cy',

x = ugi('E-cy')
x.addRecipe('C', '_part.bar')
x.addRecipe('C', 'E decompose')
x.addMetrics(left='O-cy', right='Es-cy')  # E-cy
x.addKerning(left='O-cy', right='Es-cy')  # 'E-cy',

x = ugi('Edieresis-cy')
x.addMetrics(left='Ze-cy', right='O-cy')  # Edieresis-cy
x.addKerning(left='Ze-cy', right='O-cy')  # 'Edieresis-cy',

x = ugi('Ef-cy')
x.addRecipe('Phi')
x.addMetrics(left='Ef-cy', right='Ef-cy')  # Ef-cy
x.addKerning(left='Ef-cy', right='Ef-cy')  # 'Ef-cy',

x = ugi('Ef-cy.loclBGR')
x.addRecipe('O', 'I decompose')
x.addMetrics(left='O-cy', right='O-cy')  # Ef-cy.loclBGR
x.addKerning(left='O-cy', right='O-cy')  # 'Ef-cy.loclBGR',

x = ugi('Eiotified-cy')
x.addRecipe('Iu-cy decompose', 'E-cy')
x.addMetrics(left='H', right='E-cy')  # Eiotified-cy
x.addKerning(left='En-cy', right='Es-cy')  # 'Eiotified-cy',

x = ugi('El-cy')
x.addRecipe('el-cy decompose')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='El-cy', right='El-cy')  # El-cy
x.addKerning(left='El-cy', right='En-cy')  # 'El-cy',

x = ugi('El-cy.loclBGR')
x.addRecipe('Lambda')
x.addKerning(left='A-cy', right='A-cy')  # 'El-cy.loclBGR',

x = ugi('Elhook-cy')
x.addRecipe('El-cy decompose', 'J decompose')
x.addRecipe('El-cy', '_part.Hook flip_horizontal flip_vertical')
x.addMetrics(left='El-cy', right='El-cy')  # Elhook-cy
x.addKerning(left='El-cy', right='Je-cy')  # 'Elhook-cy',

x = ugi('Eltail-cy')
x.addRecipe('El-cy', 'tail-cy')
x.addMetrics(left='El-cy')  # Eltail-cy
x.addKerning(left='El-cy', right='Eltail-cy')  # 'Eltail-cy',

x = ugi('Em-cy')
x.addMetrics(left='En-cy', right='En-cy')  # Em-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Em-cy',

x = ugi('Emtail-cy')
x.addRecipe('Em-cy', 'tail-cy')
x.addMetrics(left='Em-cy', right='Eltail-cy')  # Emtail-cy
x.addKerning(left='En-cy', right='Eltail-cy')  # 'Emtail-cy',

x = ugi('En-cy')
x.addAnchor('#topright', position_x=xpos.outline_right, position_y=ypos.capHeight)
x.addAnchor('bottomright', suppress_auto=True)
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('topright', suppress_auto=True)
x.addAnchor('#topright', position_x=xpos.outline_right, position_y=ypos.capHeight)
x.addMetrics(left='H', right='=|En-cy')  # En-cy
x.addKerning(left='En-cy', right='En-cy')  # 'En-cy',

x = ugi('Endescender-cy')
x.addRecipe('En-cy', '_part.toothright-cy')
x.addMetrics(left='En-cy', right='Tse-cy')  # Endescender-cy
x.addKerning(left='En-cy', right='De-cy')  # 'Endescender-cy',

x = ugi('Enghe-cy')
x.addRecipe('En-cy disable_alignment', '_part.bar')
x.addRecipe('En-cy', 'Te-cy decompose')
x.addMetrics(left='En-cy', right='Ge-cy')  # Enghe-cy
x.addKerning(left='En-cy', right='Ge-cy')  # 'Enghe-cy',
x.addBuildString('/Softsign-cy/Hardsign-cy/Nje-cy/Tshe-cy/Dje-cy/Yat-cy/Ghemiddlehook-cy/Kabashkir-cy/Enghe-cy')

x = ugi('Enhook-cy')
x.addRecipe('En-cy', '_part.Hook flip_horizontal flip_vertical')
x.addMetrics(left='En-cy', right='En-cy')  # Enhook-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Enhook-cy',

x = ugi('Entail-cy')
x.addRecipe('En-cy', 'tail-cy')
x.addMetrics(left='En-cy', right='Eltail-cy')  # Entail-cy
x.addKerning(left='En-cy', right='Eltail-cy')  # 'Entail-cy',

x = ugi('Er-cy')
x.addMetrics(left='En-cy', right='Er-cy')  # Er-cy
x.addKerning(left='En-cy', right='Er-cy')  # 'Er-cy',

x = ugi('Ereversed-cy')
x.addRecipe('E-cy flip_horizontal')
x.addRecipe('C decompose', 'E decompose')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)
x.addMetrics(left='Ze-cy', right='O-cy')  # Ereversed-cy
x.addKerning(left='Ze-cy', right='O-cy')  # 'Ereversed-cy',

x = ugi('Ertick-cy')
x.addRecipe('Er-cy', '_part.bar')
x.addMetrics(left='En-cy', right='Er-cy')  # Ertick-cy
x.addKerning(left='En-cy', right='Er-cy')  # 'Ertick-cy',

x = ugi('Es-cy')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='O-cy', right='Es-cy')  # Es-cy
x.addKerning(left='O-cy', right='Es-cy')  # 'Es-cy',

x = ugi('Esdescender-cy')
x.addRecipe('Es-cy', '_part.toothcentered-cy')
x.addRecipe('Es-cy', 'Zedescender-cy decompose')
x.addMetrics(left='Es-cy', right='Es-cy')  # Esdescender-cy
x.addKerning(left='O-cy', right='Es-cy')  # 'Esdescender-cy',

x = ugi('Fita-cy')
x.addRecipe('O-cy', '_part.centertilde')
x.addRecipe('O-cy', 'asciitilde decompose')
x.addMetrics(left='O-cy', right='O-cy')  # Fita-cy
x.addKerning(left='O-cy', right='O-cy')  # 'Fita-cy',

x = ugi('Ge-cy')
x.addRecipe('Gamma')
x.addRecipe('F decompose')
x.addAnchor('#bottomright', position_x=xpos.stem_bottom_right, position_y=ypos.base_line)
x.addAnchor('#center', position_x=xpos.stem_bottom_center, position_y=ypos.outline_middle)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addMetrics(left='En-cy', right='Ge-cy')  # Ge-cy
x.addBuildString('/ge-cy/Ge-cy/ge-cy.sc/F')
x.addKerning(left='En-cy', right='Ge-cy')  # 'Ge-cy',

x = ugi('Gedescender-cy')
x.addRecipe('Ge-cy', '_part.toothright-cy')
x.addRecipe('Ge-cy', 'toothright-cy')
x.addMetrics(left='En-cy', right='Ge-cy')  # Gedescender-cy
x.addKerning(left='En-cy', right='Ge-cy')  # 'Gedescender-cy',

x = ugi('Gestrokehook-cy')
x.addRecipe('Ghestroke-cy', 'tail-cy')

x = ugi('Ghemiddlehook-cy')
x.addRecipe('Ge-cy', 'Dje-cy decompose')
x.addMetrics(left='En-cy', right='Be-cy')  # Ghemiddlehook-cy
x.addKerning(left='En-cy', right='Ghemiddlehook-cy')  # 'Ghemiddlehook-cy',
x.addBuildString('/Softsign-cy/Hardsign-cy/Nje-cy/Tshe-cy/Dje-cy/Yat-cy/Ghemiddlehook-cy/Kabashkir-cy/Enghe-cy')

x = ugi('Ghestroke-cy')
x.addRecipe('Ge-cy', '_part.bar')
x.addRecipe('Ge-cy', 'macroncomb decompose')
x.addMetrics(right='Ge-cy')  # Ghestroke-cy
x.addKerning(left='Ghestroke-cy', right='Ge-cy')  # 'Ghestroke-cy',

x = ugi('Gheupturn-cy')
x.addMetrics(left='En-cy', right='Ge-cy')  # Gheupturn-cy
x.addKerning(left='En-cy', right='Ge-cy')  # 'Gheupturn-cy',

x = ugi('Gje-cy')
x.addMetrics(left='En-cy', right='Ge-cy')  # Gje-cy
x.addKerning(left='En-cy', right='Ge-cy')  # 'Gje-cy',

x = ugi('Ha-cy')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('#center', position_x=xpos.outline_center, position_y=ypos.outline_middle)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='Ha-cy', right='Ha-cy')  # Ha-cy
x.addKerning(left='Ha-cy', right='Ha-cy')  # 'Ha-cy',

x = ugi('Haabkhasian-cy')
x.addRecipe('O decompose')
x.addMetrics(left='O-cy', right='Haabkhasian-cy')  # Haabkhasian-cy
x.addKerning(left='O-cy', right='Haabkhasian-cy')  # 'Haabkhasian-cy',

x = ugi('Hadescender-cy')
x.addRecipe('Ha-cy', '_part.toothright-cy')
x.addMetrics(left='Ha-cy', right='Kadescender-cy')  # Hadescender-cy
x.addKerning(left='Ha-cy', right='Ha-cy')  # 'Hadescender-cy',

x = ugi('Hahook-cy')
x.addRecipe('X decompose', '_part.hook flip_horizontal flip_vertical')
x.addMetrics(left='Ha-cy', right='Ha-cy')  # Hahook-cy
x.addKerning(left='Ha-cy', right='Ha-cy')  # 'Hahook-cy',

x = ugi('Hardsign-cy')
x.addRecipe('Softsign-cy', '_part.bar')
x.addRecipe('Softsign-cy', 'T decompose')
x.addMetrics(left='Te-cy', right='Softsign-cy')  # Hardsign-cy
x.addKerning(left='Te-cy', right='Softsign-cy')  # 'Hardsign-cy',
x.addBuildString('/Softsign-cy/Hardsign-cy/Nje-cy/Tshe-cy/Dje-cy/Yat-cy/Ghemiddlehook-cy/Kabashkir-cy/Enghe-cy')

x = ugi('Hastroke-cy')
x.addRecipe('Ha-cy', '_part.bar')
x.addKerning(left='En-cy', right='En-cy')  # 'Hastroke-cy',

x = ugi('I-cy')
x.addMetrics(left='En-cy', right='En-cy')  # I-cy
x.addKerning(left='En-cy', right='En-cy')  # 'I-cy',

x = ugi('Ia-cy')
x.addRecipe('Softsign-cy decompose', 'Zhe-cy decompose')
x.addMetrics(left='Ia-cy', right='En-cy')  # Ia-cy
x.addKerning(left='Ia-cy', right='En-cy')  # 'Ia-cy',

x = ugi('Idieresis-cy')
x.addMetrics(left='En-cy', right='En-cy')  # Idieresis-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Idieresis-cy',

x = ugi('Ie-cy')
x.addMetrics(left='En-cy', right='Ie-cy')  # Ie-cy
x.addKerning(left='En-cy', right='Ie-cy')  # 'Ie-cy',

x = ugi('Iebreve-cy')
x.addMetrics(left='En-cy', right='Ie-cy')  # Iebreve-cy
x.addKerning(left='En-cy', right='Ie-cy')  # 'Iebreve-cy',

x = ugi('Iegrave-cy')
x.addMetrics(left='En-cy', right='Ie-cy')  # Iegrave-cy
x.addKerning(left='En-cy', right='Ie-cy')  # 'Iegrave-cy',

x = ugi('Ii-cy')
x.addRecipe('H decompose')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='En-cy', right='En-cy')  # Ii-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Ii-cy',

x = ugi('Iigrave-cy')
x.addMetrics(left='Ii-cy', right='Ii-cy')  # Iigrave-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Iigrave-cy',

x = ugi('Iishort-cy')
x.addMetrics(left='Ii-cy', right='Ii-cy')  # Iishort-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Iishort-cy',

x = ugi('Iishorttail-cy')
x.addMetrics(left='En-cy', right='Eltail-cy')  # Iishorttail-cy
x.addKerning(left='En-cy', right='Eltail-cy')  # 'Iishorttail-cy',

x = ugi('Imacron-cy')
x.addMetrics(left='Ii-cy', right='Ii-cy')  # Imacron-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Imacron-cy',

x = ugi('Io-cy')
x.addMetrics(left='En-cy', right='Ie-cy')  # Io-cy
x.addKerning(left='En-cy', right='Ie-cy')  # 'Io-cy',

x = ugi('Ishorttail-cy')
x.addMetrics(left='En-cy', right='De-cy')  # Ishorttail-cy
x.addKerning(left='En-cy', right='De-cy')  # 'Ishorttail-cy',

x = ugi('Iu-cy')
x.addRecipe('I-cy', 'O-cy', 'macroncomb decompose')
x.addMetrics(left='En-cy', right='O-cy')  # Iu-cy
x.addKerning(left='En-cy', right='O-cy')  # 'Iu-cy',

x = ugi('Izhitsa-cy')
x.addRecipe('V decompose', 'izhitsa-cy decompose')
x.addMetrics(left='Ustraight-cy', right='Izhitsa-cy')  # Izhitsa-cy
x.addKerning(left='U-cy', right='Izhitsa-cy')  # 'Izhitsa-cy',

x = ugi('Izhitsadblgrave-cy')
x.addKerning(left='U-cy', right='Izhitsa-cy')  # 'Izhitsadblgrave-cy',

x = ugi('Je-cy')
x.addMetrics(left='Je-cy', right='Je-cy')  # Je-cy
x.addKerning(left='Je-cy', right='Je-cy')  # 'Je-cy',

x = ugi('Ka-cy')
x.addMetrics(left='En-cy')  # Ka-cy
x.addAnchor('#topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addKerning(left='En-cy', right='Zhe-cy')  # 'Ka-cy',

x = ugi('Kabashkir-cy')
x.addRecipe('Ka-cy disable_alignment', 'Hardsign-cy decompose')
x.addRecipe('Ka-cy disable_alignment', 'Te-cy decompose')
x.addMetrics(left='Te-cy', right='Zhe-cy')  # Kabashkir-cy
x.addKerning(left='Te-cy', right='Zhe-cy')  # 'Kabashkir-cy',
x.addBuildString('/Softsign-cy/Hardsign-cy/Nje-cy/Tshe-cy/Dje-cy/Yat-cy/Ghemiddlehook-cy/Kabashkir-cy/Enghe-cy')

x = ugi('Kadescender-cy')
x.addRecipe('Ka-cy disable_alignment', '_part.toothright-cy enable_alignment')
x.addRecipe('Ka-cy disable_alignment', 'toothright-cy')
x.addMetrics(left='En-cy', right='')  # Kadescender-cy
x.addKerning(left='En-cy', right='Zhe-cy')  # 'Kadescender-cy',

x = ugi('Kahook-cy')
x.addRecipe('Ka-cy decompose', 'Ghemiddlehook-cy decompose')
x.addMetrics(left='En-cy', right='Be-cy')  # Kahook-cy
x.addKerning(left='En-cy', right='Ghemiddlehook-cy')  # 'Kahook-cy',

x = ugi('Kastroke-cy')
x.addRecipe('Ka-cy', '_part.bar')
x.addMetrics(left='Yat-cy', right='Zhe-cy')  # Kastroke-cy
x.addKerning(left='Yat-cy', right='Zhe-cy')  # 'Kastroke-cy',

x = ugi('Kaverticalstroke-cy')
x.addRecipe('Ka-cy decompose', '_part.stem', '_part.bar')
x.addMetrics(left='En-cy', right='Zhe-cy')  # Kaverticalstroke-cy
x.addKerning(left='En-cy', right='Zhe-cy')  # 'Kaverticalstroke-cy',

x = ugi('Kje-cy')
x.addMetrics(left='En-cy', right='Zhe-cy')  # Kje-cy
x.addKerning(left='En-cy', right='Zhe-cy')  # 'Kje-cy',

x = ugi('Koppa-cy')
x.addRecipe('Es-cy', '_part.stem')
x.addKerning(left='O-cy', right='Es-cy')  # 'Koppa-cy',

x = ugi('Ksi-cy')
x.addRecipe('Ze-cy decompose', 'ogonekcomb decompose', 'ksiaccent')
x.addRecipe('Ze-cy decompose', 'ogonekcomb decompose', 'caroncomb decompose')
x.addMetrics(left='Ze-cy', right='Ze-cy')  # Ksi-cy
x.addKerning(left='Ze-cy', right='Ve-cy')  # 'Ksi-cy',

x = ugi('Lje-cy')
x.addRecipe('El-cy decompose', 'Softsign-cy')
x.addMetrics(left='El-cy', right='Softsign-cy')  # Lje-cy
x.addKerning(left='El-cy', right='Softsign-cy')  # 'Lje-cy',
x.addBuildString('/El-cy/Lje-cy/Softsign-cy/lje-cy')

x = ugi('Nje-cy')
x.addRecipe('H decompose', 'Softsign-cy decompose')
x.addMetrics(left='En-cy', right='Softsign-cy')  # Nje-cy
x.addKerning(left='En-cy', right='Softsign-cy')  # 'Nje-cy',
x.addBuildString('/Softsign-cy/Hardsign-cy/Nje-cy/Tshe-cy/Dje-cy/Yat-cy/Ghemiddlehook-cy/Kabashkir-cy/Enghe-cy')

x = ugi('O-cy')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)
x.addMetrics(left='O-cy', right='O-cy')  # O-cy
x.addKerning(left='O-cy', right='O-cy')  # 'O-cy',

x = ugi('Obarred-cy')
x.addRecipe('O-cy', '_part.bar disable_alignment')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)
x.addMetrics(left='O-cy', right='O-cy')  # Obarred-cy
x.addKerning(left='O-cy', right='O-cy')  # 'Obarred-cy',

x = ugi('Obarreddieresis-cy')
x.addMetrics(left='O-cy', right='O-cy')  # Obarreddieresis-cy
x.addKerning(left='O-cy', right='O-cy')  # 'Obarreddieresis-cy',

x = ugi('Odieresis-cy')
x.addMetrics(left='O-cy', right='O-cy')  # Odieresis-cy
x.addKerning(left='O-cy', right='O-cy')  # 'Odieresis-cy',

x = ugi('Omega-cy')
x.addRecipe('U decompose', 'V decompose')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addMetrics(left='U', right='=|U')  # Omega-cy
x.addKerning(left='Omega-cy', right='Er-cy')  # 'Omega-cy',

x = ugi('Palochka-cy')
x.addMetrics(left='En-cy', right='En-cy')  # Palochka-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Palochka-cy',

x = ugi('Pe-cy')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='En-cy', right='En-cy')  # Pe-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Pe-cy',

x = ugi('Pedescender-cy')
x.addRecipe('Pe-cy', '_part.toothright-cy')
x.addRecipe('Pe-cy', 'toothright-cy')
x.addMetrics(left='En-cy', right='Tse-cy')  # Pedescender-cy
x.addKerning(left='En-cy', right='De-cy')  # 'Pedescender-cy',

x = ugi('Pemiddlehook-cy')
x.addRecipe('Pe-cy', 'Ghemiddlehook-cy decompose')
x.addMetrics(left='En-cy', right='Be-cy')  # Pemiddlehook-cy
x.addKerning(left='En-cy', right='Softsign-cy')  # 'Pemiddlehook-cy',

x = ugi('Psi-cy')
x.addRecipe('Psi')
x.addKerning(left='Che-cy', right='Er-cy')  # 'Psi-cy',

x = ugi('Reversedze-cy')
x.addRecipe('Eopen')
x.addRecipe('Ze-cy')
x.addMetrics(left='=|Ve-cy', right='Es-cy')  # Reversedze-cy
x.addKerning(left='Reversedze-cy', right='Es-cy')  # 'Reversedze-cy',

x = ugi('Schwa-cy')
x.addRecipe('Schwa')
x.addAnchor('top', position_x=xpos.apex_top)
x.addMetrics(left='Schwa-cy', right='O-cy')  # Schwa-cy
x.addKerning(left='O-cy', right='O-cy')  # 'Schwa-cy',

x = ugi('Schwadieresis-cy')
x.addMetrics(left='Schwa-cy', right='O-cy')  # Schwadieresis-cy
x.addKerning(left='Schwa-cy', right='O-cy')  # 'Schwadieresis-cy',

x = ugi('Semisoftsign-cy')
x.addRecipe('Softsign-cy', '_part.bar')
x.addMetrics(left='Ghestroke-cy', right='Softsign-cy')  # Semisoftsign-cy
x.addKerning(left='En-cy', right='Softsign-cy')  # 'Semisoftsign-cy',

x = ugi('Sha-cy')
x.addRecipe('Tsebase-cy decompose', '_part.stem')
x.addAnchor('#toothright', position_x=xpos.stem_top_center, position_y=ypos.base_line)
x.addMetrics(left='En-cy', right='En-cy')  # Sha-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Sha-cy',

x = ugi('Shcha-cy')
x.addRecipe('Sha-cy', '_part.toothright-cy')
x.addRecipe('Sha-cy', 'toothright-cy')
x.addMetrics(left='En-cy', right='Tse-cy')  # Shcha-cy
x.addKerning(left='En-cy', right='De-cy')  # 'Shcha-cy',

x = ugi('Shha-cy')
x.addRecipe('Che-cy flip_horizontal flip_vertical')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='En-cy', right='Shha-cy')  # Shha-cy
x.addKerning(left='En-cy', right='Shha-cy')  # 'Shha-cy',

x = ugi('Shhadescender-cy')
x.addRecipe('Shha-cy', '_part.toothright-cy')
x.addRecipe('Shha-cy', 'toothright-cy')
x.addMetrics(left='En-cy', right='Tse-cy')  # Shhadescender-cy
x.addKerning(left='En-cy', right='Shha-cy')  # 'Shhadescender-cy',

x = ugi('Softsign-cy')
x.addRecipe('P decompose')
x.addAnchor('#topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addAnchor('#topright', position_x=xpos.stem_top_right, position_y=ypos.capHeight)
x.addMetrics(left='En-cy', right='Softsign-cy')  # Softsign-cy
x.addKerning(left='En-cy', right='Softsign-cy')  # 'Softsign-cy',
x.addBuildString('/Softsign-cy/Hardsign-cy/Nje-cy/Tshe-cy/Dje-cy/Yat-cy/Ghemiddlehook-cy/Kabashkir-cy/Enghe-cy')

x = ugi('Te-cy')
x.addAnchor('#bottomright', position_x=xpos.stem_bottom_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='Te-cy', right='Ge-cy')  # Te-cy
x.addKerning(left='Te-cy', right='Ge-cy')  # 'Te-cy',

x = ugi('Tedescender-cy')
x.addRecipe('Te-cy', '_part.toothright-cy')
x.addRecipe('Te-cy', 'toothright-cy')
x.addMetrics(left='Te-cy', right='Ge-cy')  # Tedescender-cy
x.addKerning(left='Te-cy', right='Ge-cy')  # 'Tedescender-cy',

x = ugi('Tetse-cy')
x.addRecipe('Tse-cy', 'Te-cy decompose')
x.addRecipe('Tse-cy', '_part.bar')
x.addMetrics(left='Te-cy', right='De-cy')  # Tetse-cy
x.addKerning(left='Te-cy', right='De-cy')  # 'Tetse-cy',

x = ugi('Tse-cy')
x.addRecipe('Tsebase-cy', '_part.toothright-cy')
x.addRecipe('Tsebase-cy', 'toothright-cy')
x.addMetrics(left='En-cy', right='')  # Tse-cy
x.addKerning(left='En-cy', right='De-cy')  # 'Tse-cy',

x = ugi('Tsebase-cy')
x.addRecipe('H decompose')
x.addAnchor('#toothcenter', position_x=xpos.outline_center)
x.addAnchor('#toothright', position_x=xpos.outline_right)
x.addAnchor('bottom', position_x=xpos.outline_center)
x.addAnchor('toothright', suppress_auto=True)
x.addMetrics(left='En-cy', right='En-cy')  # Tsebase-cy

x = ugi('Tshe-cy')
x.addRecipe('Shha-cy disable_alignment', '_part.bar disable_alignment')
x.addRecipe('Shha-cy disable_alignment', 'T decompose')
x.addMetrics(left='Te-cy', right='Shha-cy')  # Tshe-cy
x.addBuildString('/Te-cy/tshe-cy/Tshe-cy/tshe-cy.sc' + '/Softsign-cy/Hardsign-cy/Nje-cy/Tshe-cy/Dje-cy/Yat-cy/Ghemiddlehook-cy/Kabashkir-cy/Enghe-cy')
x.addKerning(left='Te-cy', right='Tshe-cy')  # 'Tshe-cy',

x = ugi('U-cy')
x.addRecipe('y decompose')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addMetrics(left='U-cy', right='U-cy')  # U-cy
x.addKerning(left='U-cy', right='U-cy')  # 'U-cy',

x = ugi('Udieresis-cy')
x.addMetrics(left='U-cy', right='U-cy')  # Udieresis-cy
x.addKerning(left='U-cy', right='U-cy')  # 'Udieresis-cy',

x = ugi('Uhungarumlaut-cy')
x.addMetrics(left='U-cy', right='U-cy')  # Uhungarumlaut-cy
x.addKerning(left='U-cy', right='U-cy')  # 'Uhungarumlaut-cy',

x = ugi('Uk-cy')
x.addRecipe('O-cy', 'u-cy')
x.addMetrics(left='O-cy', right='u-cy')  # Uk-cy
x.addKerning(left='O-cy', right='u-cy')  # 'Uk-cy',

x = ugi('Umacron-cy')
x.addMetrics(left='U-cy', right='U-cy')  # Umacron-cy
x.addKerning(left='U-cy', right='U-cy')  # 'Umacron-cy',

x = ugi('uni047A')
x.addRecipe('O-cy', '_part.stem')
x.addMetrics(left='O-cy', right='O-cy')  # uni047A
x.addKerning(left='O-cy', right='O-cy')  # 'uni047A',

x = ugi('uni047C')
x.addRecipe('Omega-cy.base', 'psilipneumatacomb-cy', 'pokrytiecomb-cy')
x.addMetrics(left='O-cy', right='O-cy')  # uni047C
x.addKerning(left='O-cy', right='O-cy')  # 'uni047C',

x = ugi('uni047E')
x.addRecipe('Omega-cy', 'T decompose')
x.addRecipe('Omega-cy', 't.sc decompose')
x.addRecipe('Omega-cy', 'tabovecomb-cy')
x.addKerning(left='Omega-cy', right='Er-cy')  # 'uni047E',

x = ugi('Ushort-cy')
x.addMetrics(left='U-cy', right='U-cy')  # Ushort-cy
x.addKerning(left='U-cy', right='U-cy')  # 'Ushort-cy',

x = ugi('Ustraight-cy')
x.addRecipe('Y')
x.addMetrics(left='Ustraight-cy', right='Ustraight-cy')  # Ustraight-cy
x.addAnchor('#bar', position_x=xpos.outline_center, position_y=ypos.outline_middle)
x.addKerning(left='Ustraight-cy', right='Ustraight-cy')  # 'Ustraight-cy',

x = ugi('Ustraightstroke-cy')
x.addRecipe('Ustraight-cy', '_part.bar')
x.addMetrics(left='Ustraight-cy', right='Ustraight-cy')  # Ustraightstroke-cy
x.addKerning(left='U-cy', right='Ustraight-cy')  # 'Ustraightstroke-cy',

x = ugi('Ve-cy')
x.addMetrics(left='En-cy', right='Ve-cy')  # Ve-cy
x.addKerning(left='En-cy', right='Ve-cy')  # 'Ve-cy',

x = ugi('We-cy')
x.addRecipe('W')
x.addKerning(left='U-cy', right='U-cy')  # 'We-cy',

x = ugi('Yat-cy')
x.addRecipe('Softsign-cy', '_part.bar')
x.addRecipe('Softsign-cy', 'T decompose')
x.addMetrics(left='Yat-cy', right='Softsign-cy')  # Yat-cy
x.addKerning(left='Yat-cy', right='Softsign-cy')  # 'Yat-cy',
x.addBuildString('/Softsign-cy/Hardsign-cy/Nje-cy/Tshe-cy/Dje-cy/Yat-cy/Ghemiddlehook-cy/Kabashkir-cy/Enghe-cy')

x = ugi('Yeru-cy')
x.addRecipe('Softsign-cy', 'I-cy')
x.addMetrics(left='En-cy', right='En-cy')  # Yeru-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Yeru-cy',

x = ugi('Yerudieresis-cy')
x.addMetrics(left='En-cy', right='En-cy')  # Yerudieresis-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Yerudieresis-cy',

x = ugi('Yi-cy')
x.addMetrics(left='En-cy', right='En-cy')  # Yi-cy
x.addKerning(left='En-cy', right='En-cy')  # 'Yi-cy',

x = ugi('Yi-cy.loclUKR')
x.addRecipe('I', 'dieresiscomb decompose')

x = ugi('Yusbig-cy')
x.addRecipe('A decompose', 'manat decompose')
x.addMetrics(left='=|Shha-cy', right='Shha-cy')  # Yusbig-cy
x.addKerning(left='Ia-cy', right='Ghemiddlehook-cy')  # 'Yusbig-cy',

x = ugi('Yusbigiotified-cy')
x.addRecipe('Iu-cy decompose', 'Yusbig-cy')
x.addMetrics(left='H', right='Yusbig-cy')  # Yusbigiotified-cy
x.addKerning(left='En-cy', right='Ghemiddlehook-cy')  # 'Yusbigiotified-cy',

x = ugi('Yuslittle-cy')
x.addRecipe('A decompose', 'I decompose')
x.addMetrics(left='A', right='A')  # Yuslittle-cy
x.addKerning(left='A-cy', right='A-cy')  # 'Yuslittle-cy',

x = ugi('Yuslittleiotified-cy')
x.addRecipe('Iu-cy decompose', 'Yuslittle-cy')
x.addMetrics(left='H', right='A')  # Yuslittleiotified-cy
x.addKerning(left='En-cy', right='A-cy')  # 'Yuslittleiotified-cy',

x = ugi('Ze-cy')
x.addRecipe('three decompose')
x.addAnchor('bottom', position_x=xpos.outline_center, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.apex_top)
x.addMetrics(left='Ze-cy', right='Ve-cy')  # Ze-cy
x.addKerning(left='Ze-cy', right='Ve-cy')  # 'Ze-cy',

x = ugi('Zedescender-cy')
x.addRecipe('Ze-cy', '_part.toothcentered-cy')
x.addRecipe('Ze-cy', 'ogonekcomb flip_horizontal decompose')
x.addMetrics(left='Ze-cy', right='Ze-cy')  # Zedescender-cy
x.addKerning(left='Ze-cy', right='Ve-cy')  # 'Zedescender-cy',

x = ugi('Zedieresis-cy')
x.addMetrics(left='Ze-cy', right='Ze-cy')  # Zedieresis-cy
x.addKerning(left='Ze-cy', right='Ve-cy')  # 'Zedieresis-cy',

x = ugi('Zhe-cy')
x.addRecipe('Ka-cy flip_horizontal decompose', 'Ka-cy')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='=|Ka-cy', right='Ka-cy')  # Zhe-cy
x.addKerning(left='Zhe-cy', right='Zhe-cy')  # 'Zhe-cy',

x = ugi('Zhebreve-cy')
x.addMetrics(left='Zhe-cy', right='Zhe-cy')  # Zhebreve-cy
x.addKerning(left='Zhe-cy', right='Zhe-cy')  # 'Zhebreve-cy',

x = ugi('Zhedescender-cy')
x.addRecipe('Zhe-cy', '_part.toothright-cy')
x.addRecipe('Zhe-cy', 'toothright-cy')
x.addMetrics(left='Zhe-cy', right='Kadescender-cy')  # Zhedescender-cy
x.addKerning(left='Zhe-cy', right='Zhe-cy')  # 'Zhedescender-cy',

x = ugi('Zhedieresis-cy')
x.addMetrics(left='Zhe-cy', right='Zhe-cy')  # Zhedieresis-cy
x.addKerning(left='Zhe-cy', right='Zhe-cy')  # 'Zhedieresis-cy',

#
# --------------------------------
#
#   Lowercase
#
# --------------------------------
#

x = ugi('a-cy')
x.addMetrics(left='a-cy', right='a-cy', italic_left='o-cy', italic_right='en-cy')  # a-cy
x.addKerning(left='a-cy', right='a-cy', italic_left='o-cy', italic_right='en-cy')  # 'a-cy',

x = ugi('abreve-cy')
x.addMetrics(left='a-cy', right='a-cy')  # abreve-cy
x.addKerning(left='a-cy', right='a-cy', italic_left='o-cy', italic_right='en-cy')  # 'abreve-cy',

x = ugi('adieresis-cy')
x.addMetrics(left='a-cy', right='a-cy')  # adieresis-cy
x.addKerning(left='a-cy', right='a-cy', italic_left='o-cy', italic_right='en-cy')  # 'adieresis-cy',

x = ugi('aie-cy')
x.addMetrics(left='a-cy', right='ie-cy')  # aie-cy
x.addKerning(left='a-cy', right='ie-cy', italic_left='o-cy')  # 'aie-cy',

x = ugi('be-cy')
x.addRecipe('six decompose')
x.addMetrics(left='be-cy', right='be-cy')  # be-cy
x.addKerning(left='be-cy', right='be-cy')  # 'be-cy',
x.addBuildString('/ie-cy/be-cy/o-cy/delta')

x = ugi('be-cy.loclMKD')
x.addRecipe('be-cy.loclSRB')
x.addKerning(left='be-cy', right='be-cy', italic_left='de-cy', italic_right='be-cy')  # 'be-cy.loclSRB',

x = ugi('be-cy.loclSRB')
x.addRecipe('delta decompose', 'be-cy decompose')
x.addMetrics(left='be-cy', right='be-cy', italic_left='de-cy', italic_right='be-cy')  # be-cy.loclSRB
x.addBuildString('/be-cy/be-cy.loclSRB/delta')
x.addKerning(left='be-cy', right='be-cy', italic_left='de-cy', italic_right='be-cy')  # 'be-cy.loclSRB',

x = ugi('che-cy')
x.addRecipe('u ', 'idotless decompose')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addAnchor('#bottomleft', position_x=xpos.stem_bottom_left, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)
x.addMetrics(left='che-cy', right='en-cy', italic_right='en-cy')  # che-cy
x.addKerning(left='che-cy', right='en-cy', italic_right='en-cy')  # 'che-cy',

x = ugi('cheabkhasian-cy')
x.addRecipe('ie-cy', '_part.hook rotate_90')
x.addMetrics(left='cheabkhasian-cy', right='ie-cy')  # cheabkhasian-cy
x.addKerning(left='cheabkhasian-cy', right='ie-cy')

x = ugi('chedescender-cy')
x.addRecipe('che-cy disable_alignment', '_part.toothright-cy')
x.addRecipe('che-cy disable_alignment', 'toothright-cy')
x.addMetrics(left='che-cy', right='tse-cy')  # chedescender-cy
x.addKerning(left='che-cy', right='de-cy', italic_right='tse-cy')

x = ugi('chedescenderabkhasian-cy')
x.addRecipe('cheabkhasian-cy', '_part.toothcentered-cy')
x.addRecipe('cheabkhasian-cy', 'toothcentered-cy')
x.addMetrics(left='cheabkhasian-cy', right='ie-cy')  # chedescenderabkhasian-cy
x.addKerning(left='cheabkhasian-cy', right='ie-cy')

x = ugi('chedieresis-cy')
x.addMetrics(left='che-cy', right='en-cy')  # chedieresis-cy
x.addKerning(left='che-cy', right='en-cy')

x = ugi('chekhakassian-cy')
x.addRecipe('che-cy', '_part.toothleft-cy enable_alignment')
x.addRecipe('che-cy', 'toothleft-cy')
x.addMetrics(left='che-cy', right='en-cy')  # chekhakassian-cy
x.addKerning(left='che-cy', right='en-cy')

x = ugi('cheverticalstroke-cy')
x.addRecipe('che-cy', '_part.stem disable_alignment')
x.addMetrics(left='che-cy', right='en-cy', italic_right='en-cy')  # cheverticalstroke-cy
x.addKerning(left='che-cy', right='en-cy', italic_right='en-cy')  # 'cheverticalstroke-cy',

x = ugi('de-cy')
x.addRecipe('el-cy decompose', 'tse-cy decompose')
x.addMetrics(right='tse-cy')  # de-cy
x.addKerning(left='de-cy', right='de-cy')  # 'de-cy',

x = ugi('de-cy.loclBGR')
x.addRecipe('de-cy.loclSRB', italic=True)
x.addRecipe('g')
x.addRecipe('q decompose', 'jdotless decompose')
x.addKerning(left='o-cy', right='de-cy.loclSRB')  # 'de-cy.loclBGR',

x = ugi('de-cy.loclMKD')
x.addRecipe('de-cy.loclSRB')
x.addKerning(left='de-cy.loclSRB', right='de-cy.loclSRB', italic_left='o-cy', italic_right='de-cy.loclSRB')  # 'de-cy.loclSRB',

x = ugi('de-cy.loclSRB')
x.addRecipe('g')
x.addMetrics(left='de-cy.loclSRB', right='de-cy.loclSRB', italic_left='o-cy', italic_right='de-cy.loclSRB')  # de-cy.loclSRB
x.addKerning(left='de-cy.loclSRB', right='de-cy.loclSRB', italic_left='o-cy', italic_right='de-cy.loclSRB')  # 'de-cy.loclSRB',

x = ugi('dje-cy')
x.addRecipe('hbar decompose', 'jdotless decompose')
x.addMetrics(left='hbar', right='eng')  # dje-cy
x.addKerning(left='tshe-cy', right='dje-cy')  # 'dje-cy',

x = ugi('dze-cy')
x.addMetrics(left='dze-cy', right='dze-cy')  # dze-cy

x = ugi('dzeabkhasian-cy')
x.addRecipe('ezh')
x.addRecipe('ze-cy decompose', 'seven decompose')
x.addMetrics(left='dzeabkhasian-cy', right='dzeabkhasian-cy')  # dzeabkhasian-cy
x.addKerning(left='dzeabkhasian-cy', right='dzeabkhasian-cy')  # 'dzeabkhasian-cy',

x = ugi('dzhe-cy')
x.addRecipe('tsebase-cy', '_part.toothcentered-cy')
x.addRecipe('tsebase-cy', 'toothcentered-cy')
x.addMetrics(left='en-cy', right='en-cy', italic_left='sha-cy', italic_right='en-cy')  # dzhe-cy
x.addKerning(left='en-cy', right='en-cy', italic_left='sha-cy', italic_right='en-cy')  # 'dzhe-cy',

x = ugi('e-cy')
x.addRecipe('c', '_part.bar disable_alignment')
x.addMetrics(left='o-cy', right='es-cy')  # e-cy
x.addKerning(left='o-cy', right='es-cy')  # 'e-cy',

x = ugi('edieresis-cy')
x.addMetrics(left='ereversed-cy', right='o-cy')  # edieresis-cy
x.addKerning(left='ze-cy', right='o-cy')  # 'edieresis-cy',

x = ugi('ef-cy')
x.addRecipe('d', 'p')
x.addMetrics(left='o-cy', right='o-cy')  # ef-cy
x.addKerning(left='o-cy', right='o-cy')  # 'ef-cy',

x = ugi('ef-cy.loclBGR')
x.addRecipe('phi')
x.addRecipe('o-cy decompose', 'thorn decompose')
x.addMetrics(left='o-cy', right='o-cy')  # ef-cy
x.addKerning(left='o-cy', right='o-cy')  # 'ef-cy.loclBGR',
x.addBuildString('/ef-cy.loclBGR/ef-cy')

x = ugi('eiotified-cy')
x.addRecipe('iu-cy decompose', 'e-cy')
x.addMetrics(left='n', right='e-cy')  # eiotified-cy
x.addKerning(left='en-cy', right='es-cy')  # 'eiotified-cy',

x = ugi('el-cy')
x.addRecipe('El-cy decompose')
x.addRecipe('_part.stem', '_part.bar', 'jdotless decompose')
x.addMetrics(left='el-cy', right='en-cy', italic_right='el-cy')  # el-cy
x.addKerning(left='el-cy', right='en-cy', italic_right='el-cy')  # 'el-cy',

x = ugi('el-cy.loclBGR')
x.addRecipe('v flip_horizontal flip_vertical')
x.addKerning(left='el-cy.loclBGR', right='el-cy.loclBGR')  # 'el-cy.loclBGR',

x = ugi('elhook-cy')
x.addRecipe('el-cy', '_part.hook flip_horizontal flip_vertical')
x.addRecipe('el-cy decompose', 'jdotless decompose')
x.addMetrics(left='el-cy', right='dje-cy')  # elhook-cy
x.addKerning(left='el-cy', right='dje-cy')  # 'elhook-cy',

x = ugi('eltail-cy')
x.addRecipe('el-cy', 'tail-cy')
x.addMetrics(left='el-cy')  # eltail-cy
x.addKerning(left='el-cy', right='eltail-cy')  # 'eltail-cy',

x = ugi('em-cy')
x.addRecipe('em-cy.sc decompose')
x.addRecipe('m.sc decompose')
x.addKerning(left='en-cy', right='en-cy', italic_right='en-cy')  # 'em-cy',

x = ugi('emtail-cy')
x.addRecipe('em-cy', 'tail-cy')
x.addMetrics(left='em-cy', right='eltail-cy', italic_right='eltail-cy')  # emtail-cy
x.addKerning(left='en-cy', right='eltail-cy')  # 'emtail-cy',

x = ugi('en-cy')
x.addRecipe('h.sc decompose')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('#topright', position_x=xpos.stem_top_right, position_y=ypos.xHeight)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='n', right='=|en-cy')  # en-cy
x.addKerning(left='en-cy', right='en-cy', italic_right='en-cy')  # 'en-cy',

x = ugi('endescender-cy')
x.addRecipe('en-cy disable_alignment', '_part.toothright-cy')
x.addRecipe('en-cy disable_alignment', 'toothright-cy')
x.addMetrics(left='en-cy', right='tse-cy', italic_right='tse-cy')  # endescender-cy
x.addKerning(left='en-cy', right='de-cy', italic_right='tse-cy')  # 'endescender-cy',

x = ugi('enghe-cy')
x.addRecipe('en-cy disable_alignment', '_part.bar')
x.addRecipe('en-cy disable_alignment', 'te-cy decompose')
x.addMetrics(left='en-cy', right='ge-cy', italic_right='gheupturn-cy')  # enghe-cy
x.addKerning(left='en-cy', right='ge-cy', italic_right='enghe-cy')  # 'enghe-cy',

x = ugi('enhook-cy')
x.addRecipe('en-cy', '_part.hook flip_horizontal flip_vertical')
x.addMetrics(left='en-cy', right='en-cy', italic_right='je-cy')  # enhook-cy
x.addKerning(left='en-cy', right='en-cy', italic_right='je-cy')  # 'enhook-cy',

x = ugi('entail-cy')
x.addRecipe('en-cy', 'tail-cy')
x.addMetrics(left='en-cy', right='eltail-cy')  # entail-cy
x.addKerning(left='en-cy', right='eltail')  # 'entail-cy',

x = ugi('er-cy')
x.addMetrics(left='er-cy', right='o-cy')  # er-cy
x.addKerning(left='er-cy', right='o-cy')  # 'er-cy',

x = ugi('ereversed-cy')
x.addRecipe('e-cy flip_horizontal')
x.addAnchor('top', position_x=xpos.apex_top)
x.addMetrics(left='ereversed-cy', right='o-cy')  # ereversed-cy
x.addKerning(left='ze-cy', right='o-cy')  # 'ereversed-cy',

x = ugi('ertick-cy')
x.addRecipe('er-cy', '_part.bar')
x.addMetrics(left='er-cy', right='o-cy')  # ertick-cy
x.addKerning(left='er-cy', right='o-cy')  # 'ertick-cy',

x = ugi('es-cy')
x.addRecipe('c')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='o-cy', right='es-cy')  # es-cy
x.addKerning(left='o-cy', right='es-cy')  # 'es-cy',

x = ugi('esdescender-cy')
x.addRecipe('es-cy', '_part.toothcentered-cy')
x.addRecipe('es-cy', 'zedescender-cy decompose')
x.addMetrics(left='es-cy', right='es-cy')  # esdescender-cy
x.addKerning(left='o-cy', right='es-cy')  # 'esdescender-cy',

x = ugi('fita-cy')
x.addRecipe('o-cy', '_part.centertilde')
x.addRecipe('o-cy', 'asciitilde disable_alignment')
x.addRecipe('o-cy', 'tildecomb disable_alignment')
x.addMetrics(left='o-cy', right='o-cy')  # fita-cy
x.addKerning(left='o-cy', right='o-cy')  # 'fita-cy',

x = ugi('ge-cy')
x.addRecipe('en-cy decompose')
x.addAnchor('#bottomright', position_x=xpos.stem_bottom_right, position_y=ypos.base_line, position_x_italic=xpos.width_75)
x.addAnchor('#bar', position_x=xpos.stem_bottom_center, position_y=ypos.height_50, position_x_italic=xpos.apex_bottom)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line, position_x_italic=xpos.apex_bottom)
x.addAnchor('bottomright', suppress_auto=True)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight, position_x_italic=xpos.apex_top)
x.addMetrics(left='en-cy', right='ge-cy', italic_left='ge-cy')  # ge-cy
x.addKerning(left='en-cy', right='ge-cy', italic_left='ge-cy')  # 'ge-cy',

x = ugi('ge-cy.loclBGR')
x.addRecipe('ge-cy', italic=True)
x.addRecipe('s decompose', 'c')
x.addRecipe('s decompose', 'c', 'schwa-cy')
x.addBuildString('/s/ge-cy.loclBGR/e')
x.addKerning(left='ge-cy.loclBGR', right='ge-cy.loclBGR', italic_left='ge-cy', italic_right='ge-cy')  # 'ge-cy.loclBGR',

x = ugi('ge-cy.loclMKD')
x.addRecipe('ge-cy.loclSRB')
x.addRecipe('imacron')
x.addKerning(left='yi-cy', right='yi-cy')  # 'ge-cy.loclSRB',

x = ugi('ge-cy.loclSRB')
x.addRecipe('imacron')
x.addMetrics(left='i-cy', right='i-cy', italic_right='i-cy')  # ge-cy.loclSRB
x.addKerning(left='yi-cy', right='yi-cy')  # 'ge-cy.loclSRB',

x = ugi('gedescender-cy')
x.addRecipe('ge-cy', '_part.toothright-cy')
x.addRecipe('ge-cy', 'toothright-cy')
x.addMetrics(left='en-cy', right='ge-cy', italic_left='ge-cy', italic_right='ge-cy')  # gedescender-cy
x.addKerning(left='en-cy', right='ge-cy', italic_left='ge-cy', italic_right='ge-cy')  # 'gedescender-cy',

x = ugi('gestrokehook-cy')
x.addRecipe('ghestroke-cy', 'tail-cy')

x = ugi('ghemiddlehook-cy')
x.addRecipe('ge-cy', 'dje-cy decompose')
x.addMetrics(left='en-cy', right='ghemiddlehook-cy')  # ghemiddlehook-cy
x.addKerning(left='en-cy', right='softsign-cy')  # 'ghemiddlehook-cy',
x.addBuildString('/dje-cy/ghemiddlehook-cy/')

x = ugi('ghestroke-cy')
x.addRecipe('ge-cy', '_part.bar')
x.addRecipe('ge-cy', 'macroncomb decompose')
x.addMetrics(right='ge-cy', italic_left='ge-cy', italic_right='ge-cy')  # ghestroke-cy
x.addKerning(left='en-cy', right='ge-cy', italic_left='ge-cy', italic_right='ge-cy')  # 'ghestroke-cy',

x = ugi('gheupturn-cy')
x.addRecipe('ge-cy', 'quoteleft decompose')
x.addMetrics(left='en-cy', right='ge-cy', italic_right='gheupturn-cy')  # gheupturn-cy
x.addKerning(left='en-cy', right='ge-cy', italic_right='gheupturn-cy')  # 'gheupturn-cy',

x = ugi('gje-cy')
x.addMetrics(left='en-cy', right='ge-cy', italic_left='ge-cy')  # gje-cy
x.addKerning(left='en-cy', right='ge-cy', italic_left='ge-cy')  # 'gje-cy',

x = ugi('ha-cy')
x.addRecipe('x')
x.addAnchor('#center', position_x=xpos.outline_center, position_y=ypos.outline_middle)
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='ha-cy', right='ha-cy')  # ha-cy
x.addKerning(left='ha-cy', right='ha-cy')  # 'ha-cy',

x = ugi('haabkhasian-cy')
x.addRecipe('o decompose')
x.addMetrics(left='o-cy', right='haabkhasian-cy')  # haabkhasian-cy
x.addKerning(left='o-cy', right='haabkhasian-cy')  # 'haabkhasian-cy',

x = ugi('hadescender-cy')
x.addRecipe('ha-cy', '_part.toothright-cy')
x.addRecipe('ha-cy', 'toothright-cy')
x.addMetrics(left='ha-cy', right='kadescender-cy')  # hadescender-cy
x.addKerning(left='ha-cy', right='ha-cy')  # 'hadescender-cy',

x = ugi('hahook-cy')
x.addRecipe('x decompose', '_part.hook flip_vertical flip_horizontal')
x.addMetrics(left='ha-cy', right='ha-cy')  # hahook-cy
x.addKerning(left='ha-cy', right='ha-cy')  # 'hahook-cy',

x = ugi('hardsign-cy')
x.addRecipe('softsign-cy', '_part.bar')
x.addRecipe('softsign-cy', 'Te-cy decompose')
x.addMetrics(left='te-cy', right='softsign-cy', italic_left='hardsign-cy')  # hardsign-cy
x.addKerning(left='te-cy', right='softsign-cy', italic_left='hardsign-cy')  # 'hardsign-cy',

x = ugi('hardsign-cy.loclBGR')
x.addRecipe('softsign-cy.loclBGR', 'hardsign-cy decompose')
x.addMetrics(left='te-cy', right='softsign-cy', italic_left='hardsign-cy')  # hardsign-cy.loclBGR
x.addKerning(left='te-cy', right='softsign-cy', italic_left='hardsign-cy')  # 'hardsign-cy.loclBGR',

x = ugi('hastroke-cy')
x.addRecipe('ha-cy', '_part.bar')
x.addKerning(left='en-cy', right='en-cy')  # 'hastroke-cy',

x = ugi('i-cy')
x.addMetrics(left='i-cy', right='i-cy')  # i-cy
x.addKerning(left='i-cy', right='i-cy')  # 'i-cy',

x = ugi('ia-cy')
x.addRecipe('r.sc flip_horizontal decompose')
x.addRecipe('softsign-cy flip_horizontal flip_vertical decompose', 'zhe-cy decompose')
x.addMetrics(left='ia-cy', right='en-cy', italic_right='en-cy')  # ia-cy
x.addKerning(left='ia-cy', right='en-cy', italic_right='en-cy')  # 'ia-cy',

x = ugi('idieresis-cy')
x.addMetrics(left='en-cy', right='en-cy')  # idieresis-cy
x.addKerning(left='en-cy', right='en-cy', italic_left='sha-cy', italic_right='en-cy')  # 'idieresis-cy',

x = ugi('ie-cy')
x.addAnchor('top', position_x=xpos.apex_top)
x.addMetrics(left='o-cy', right='ie-cy')  # ie-cy
x.addKerning(left='o-cy', right='ie-cy')  # 'ie-cy',

x = ugi('iebreve-cy')
x.addMetrics(width='ie-cy', right='ie-cy')  # iebreve-cy
x.addKerning(left='iegrave-cy', right='ie-cy')  # 'iebreve-cy',

x = ugi('iegrave-cy')
x.addMetrics(width='ie-cy', right='ie-cy')  # iegrave-cy
x.addKerning(left='iegrave-cy', right='ie-cy')  # 'iegrave-cy',

x = ugi('ii-cy')
x.addRecipe('en-cy decompose')
x.addRecipe('u', italic=True)
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='en-cy', right='en-cy', italic_left='sha-cy', italic_right='en-cy')  # ii-cy
x.addKerning(left='en-cy', right='en-cy', italic_left='sha-cy', italic_right='en-cy')  # 'ii-cy',

x = ugi('ii-cy.loclBGR')
x.addRecipe('u')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addAnchor('top', position_x=xpos.outline_center)
x.addKerning(left='ii-cy.loclBGR', right='en-cy')  # 'ii-cy.loclBGR',

x = ugi('iigrave-cy')
x.addMetrics(left='ii-cy', right='ii-cy')  # iigrave-cy
x.addKerning(left='en-cy', right='en-cy', italic_left='sha-cy', italic_right='en-cy')  # 'iigrave-cy',

x = ugi('iigrave-cy.loclBGR')
x.addKerning(left='ii-cy.loclBGR', right='en-cy')  # 'iigrave-cy.loclBGR',

x = ugi('iishort-cy')
x.addMetrics(left='ii-cy', right='ii-cy')  # iishort-cy
x.addKerning(left='en-cy', right='en-cy', italic_left='sha-cy', italic_right='en-cy')  # 'iishort-cy',

x = ugi('iishort-cy.loclBGR')
x.addKerning(left='ii-cy.loclBGR', right='en-cy')  # 'iishort-cy.loclBGR',

x = ugi('iishorttail-cy')
x.addMetrics(left='En-cy', right='eltail-cy')  # iishorttail-cy
x.addKerning(left='en-cy', right='eltail-cy', italic_left='sha-cy', italic_right='eltail-cy')  # 'iishorttail-cy',

x = ugi('imacron-cy')
x.addMetrics(left='ii-cy', right='ii-cy')  # imacron-cy
x.addKerning(left='en-cy', right='en-cy', italic_left='sha-cy', italic_right='en-cy')  # 'imacron-cy',

x = ugi('io-cy')
x.addMetrics(left='iegrave-cy', right='ie-cy')  # io-cy
x.addKerning(left='iegrave-cy', right='ie-cy')  # 'io-cy',

x = ugi('ishorttail-cy')
x.addMetrics(left='en-cy', right='en-cy', italic_right='tse-cy')  # ishorttail-cy

x = ugi('iu-cy')
x.addRecipe('idotless', 'o-cy', '_part.bar')
x.addRecipe('idotless', 'o-cy', 'macroncomb decompose')
x.addAnchor('top', position_x=xpos.apex_top)
x.addMetrics(left='en-cy', right='o-cy')  # iu-cy
x.addKerning(left='en-cy', right='o-cy')  # 'iu-cy',

x = ugi('iu-cy.loclBGR')
x.addRecipe('iu-cy decompose', 'l decompose')
x.addMetrics(left='l', right='o-cy')  # iu-cy.loclBGR
x.addKerning(left='shha-cy', right='o-cy')  # 'iu-cy.loclBGR',

x = ugi('izhitsa-cy')
x.addRecipe('v decompose', '_part.hook decompose')
x.addRecipe('vrighthook')
x.addRecipe('v decompose', 'f decompose')
x.addMetrics(left='v', right='izhitsa-cy')  # izhitsa-cy
x.addKerning(left='izhitsa-cy', right='izhitsa-cy')  # 'izhitsa-cy',

x = ugi('izhitsadblgrave-cy')
x.addKerning(left='izhitsa-cy', right='izhitsa-cy')  # 'izhitsadblgrave-cy',

x = ugi('je-cy')
x.addMetrics(left='je-cy', right='je-cy')  # je-cy
x.addKerning(left='je-cy', right='je-cy')  # 'je-cy',

x = ugi('ka-cy')
x.addRecipe('k decompose')
x.addAnchor('#topleft', position_x=xpos.outline_left, position_y=ypos.xHeight)
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='en-cy', right='ka-cy')  # ka-cy
x.addKerning(left='en-cy', right='ka-cy')  # 'ka-cy',

x = ugi('ka-cy.loclBGR')
x.addRecipe('ka-cy decompose', 'l decompose')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y='ypos.ascender')
x.addMetrics(left='h', right='ka-cy')  # ka-cy.loclBGR
x.addKerning(left='shha-cy', right='ka-cy')  # 'ka-cy.loclBGR',

x = ugi('kabashkir-cy')
x.addRecipe('ka-cy disable_alignment', 'hardsign-cy decompose')
x.addMetrics(left='te-cy', right='ka-cy', italic_left='hardsign-cy')  # kabashkir-cy
x.addKerning(left='te-cy', right='ka-cy', italic_left='hardsign-cy')  # 'kabashkir-cy',
x.addBuildString('/hardsign-cy/kabashkir-cy/ka-cy')

x = ugi('kadescender-cy')
x.addRecipe('ka-cy', '_part.toothright-cy')
x.addRecipe('ka-cy', 'toothright-cy')
x.addMetrics(left='en-cy', right='')  # kadescender-cy
x.addKerning(left='en-cy', right='ka-cy')  # 'kadescender-cy',

x = ugi('kahook-cy')
x.addRecipe('ka-cy decompose', 'ghemiddlehook-cy decompose')
x.addMetrics(left='en-cy', right='kahook-cy')  # kahook-cy
x.addKerning(left='en-cy', right='kahook-cy')  # 'kahook-cy',

x = ugi('kastroke-cy')
x.addRecipe('ka-cy', '_part.bar')
x.addMetrics(left='tshe-cy', right='ka-cy')  # kastroke-cy
x.addKerning(left='dje-cy', right='ka-cy')  # 'kastroke-cy',

x = ugi('kaverticalstroke-cy')
x.addRecipe('ka-cy decompose', '_part.stem disable_alignment', '_part.bar disable_alignment')
x.addMetrics(left='en-cy', right='ka-cy')  # kaverticalstroke-cy
x.addKerning(left='en-cy', right='ka-cy')  # 'kaverticalstroke-cy',

x = ugi('kje-cy')
x.addMetrics(left='en-cy', right='ka-cy')  # kje-cy
x.addKerning(left='en-cy', right='ka-cy')  # 'kje-cy',

x = ugi('koppa-cy')
x.addRecipe('es-cy', '_part.stem')
x.addKerning(left='o-cy', right='es-cy')  # 'koppa-cy',

x = ugi('ksi-cy')
x.addRecipe('ze-cy decompose', 'ogonekcomb decompose', 'ksiaccent')
x.addRecipe('ze-cy decompose', 'ogonekcomb decompose', 'caroncomb decompose')
x.addMetrics(left='ze-cy', right='ze-cy')  # ksi-cy
x.addKerning(left='ereversed-cy', right='ve-cy')  # 'ksi-cy',

x = ugi('lje-cy')
x.addRecipe('el-cy decompose', 'softsign-cy')
x.addMetrics(left='el-cy', right='softsign-cy')  # lje-cy
x.addBuildString('/el-cy/lje-cy/softsign-cy/Lje-cy')
x.addKerning(left='el-cy', right='softsign-cy')  # 'lje-cy',

x = ugi('nje-cy')
x.addRecipe('en-cy decompose', 'softsign-cy')
x.addMetrics(left='en-cy', right='softsign-cy')  # nje-cy
x.addKerning(left='en-cy', right='softsign-cy')  # 'nje-cy',

x = ugi('o-cy')
x.addMetrics(left='o-cy', right='o-cy')  # o-cy
x.addAnchor('#center', position_x=xpos.outline_center, position_y=ypos.outline_middle)
x.addKerning(left='o-cy', right='o-cy')  # 'o-cy',

x = ugi('obarred-cy')
x.addRecipe('o-cy', '_part.bar')
x.addAnchor('top', position_x=xpos.apex_top, position_y='ypos.xHeight')
x.addMetrics(left='o-cy', right='o-cy')  # obarred-cy
x.addKerning(left='o-cy', right='o-cy')  # 'obarred-cy',

x = ugi('obarreddieresis-cy')
x.addMetrics(left='o-cy', right='o-cy')  # obarreddieresis-cy
x.addKerning(left='iegrave-cy', right='o-cy')  # 'obarreddieresis-cy',

x = ugi('odieresis-cy')
x.addMetrics(left='o-cy', right='o-cy')  # odieresis-cy
x.addKerning(left='iegrave-cy', right='o-cy')  # 'odieresis-cy',

x = ugi('omega-cy')
x.addRecipe('Omega-cy decompose')
x.addAnchor('top', position_x=xpos.outline_center, position_y='ypos.xHeight')
x.addMetrics(left='u', right='=|u')  # omega-cy

x = ugi('palochka-cy')
x.addRecipe('I decompose')
x.addMetrics(left='shha-cy', right='=|shha-cy')  # palochka-cy
x.addKerning(left='En-cy', right='En-cy')  # 'palochka-cy',

x = ugi('pe-cy')
x.addRecipe('en-cy decompose')
x.addRecipe('n', italic=True)
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='en-cy', right='en-cy', italic_right='pe-cy')  # pe-cy
x.addKerning(left='en-cy', right='en-cy', italic_right='pe-cy')  # 'pe-cy',

x = ugi('pe-cy.loclBGR')
x.addRecipe('n')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addKerning(left='en-cy', right='tshe-cy')  # 'pe-cy.loclBGR',

x = ugi('pe-cy.loclMKD')
x.addRecipe('pe-cy.loclSRB')
x.addRecipe('umacron')
x.addKerning(left='a-cy', right='a-cy', italic_left='sha-cy', italic_right='en-cy')  # 'pe-cy.loclSRB',

x = ugi('pe-cy.loclSRB')
x.addRecipe('umacron')
x.addMetrics(left='a-cy', right='a-cy', italic_left='iishort-cy', italic_right='en-cy')  # pe-cy.loclSRB
x.addKerning(left='a-cy', right='a-cy', italic_left='sha-cy', italic_right='en-cy')  # 'pe-cy.loclSRB',

x = ugi('pedescender-cy')
x.addRecipe('pe-cy', '_part.toothright-cy')
x.addRecipe('pe-cy', 'toothright-cy')
x.addMetrics(left='en-cy', right='tse-cy')  # pedescender-cy
x.addKerning(left='en-cy', right='de-cy', italic_right='tse-cy')  # 'pedescender-cy',

x = ugi('pemiddlehook-cy')
x.addRecipe('pe-cy', 'ghemiddlehook-cy decompose')
x.addMetrics(left='en-cy', right='ghemiddlehook-cy')  # pemiddlehook-cy
x.addKerning(left='en-cy', right='softsign-cy')  # 'pemiddlehook-cy',

x = ugi('psi-cy')
x.addRecipe('u decompose', 'l decompose')
x.addMetrics(left='u', right='=|u')  # psi-cy
x.addKerning(left='ii-cy.loclBGR', right='dze-cy')  # 'psi-cy',

x = ugi('reversedze-cy')
x.addRecipe('ze-cy')
x.addMetrics(left='=|ve-cy', right='es-cy')  # reversedze-cy
x.addKerning(left='reversedze-cy', right='es-cy', italic_left='ge-cy')  # 'reversedze-cy',

x = ugi('schwa-cy')
x.addRecipe('schwa')
x.addAnchor('top', position_x=xpos.apex_top)
x.addMetrics(left='schwa-cy', right='o-cy')  # schwa-cy
x.addKerning(left='schwa-cy', right='o-cy')  # 'schwa-cy',

x = ugi('schwadieresis-cy')
x.addMetrics(left='schwa-cy', right='o-cy')  # schwadieresis-cy
x.addKerning(left='schwa-cy', right='o-cy')  # 'schwadieresis-cy',

x = ugi('semisoftsign-cy')
x.addRecipe('softsign-cy', '_part.stem', '_part.bar')
x.addMetrics(left='f', right='softsign-cy')  # semisoftsign-cy
x.addKerning(left='semisoftsign-cy', right='softsign-cy')  # 'semisoftsign-cy',

x = ugi('sha-cy')
x.addRecipe('tsebase-cy decompose')
x.addAnchor('#toothright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center, position_y='ypos.xHeight')
x.addMetrics(left='en-cy', right='en-cy', italic_left='sha-cy', italic_right='en-cy')  # sha-cy
x.addKerning(left='en-cy', right='en-cy', italic_left='sha-cy', italic_right='en-cy')  # 'sha-cy',

x = ugi('sha-cy.loclBGR')
x.addRecipe('u decompose')
x.addMetrics(left='u', right='u')  # sha-cy.loclBGR
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addKerning(left='ii-cy.loclBGR', right='en-cy')  # 'sha-cy.loclBGR',

x = ugi('shcha-cy')
x.addRecipe('sha-cy', '_part.toothright-cy')
x.addRecipe('sha-cy', 'toothright-cy')
x.addMetrics(left='en-cy', right='tse-cy', italic_left='sha-cy', italic_right='tse-cy')  # shcha-cy
x.addKerning(left='en-cy', right='de-cy', italic_left='sha-cy', italic_right='tse-cy')  # 'shcha-cy',

x = ugi('shcha-cy.loclBGR')
x.addRecipe('sha-cy.loclBGR disable_alignment', '_part.toothright-cy enable_alignment')
x.addRecipe('sha-cy.loclBGR', 'toothright-cy')
x.addMetrics(left='ii-cy.loclBGR', right='tse-cy')  # shcha-cy.loclBGR
x.addKerning(left='ii-cy.loclBGR', right='de-cy')  # 'shcha-cy.loclBGR',

x = ugi('shha-cy')
x.addMetrics(left='tshe-cy', right='tshe-cy', italic_left='dje-cy', italic_right='pe-cy')  # shha-cy
x.addKerning(left='shha-cy', right='shha-cy', italic_left='shha-cy', italic_right='pe-cy')  # 'shha-cy',

x = ugi('shhadescender-cy')
x.addRecipe('shha-cy', '_part.toothright-cy')
x.addRecipe('shha-cy', 'toothright-cy')
x.addMetrics(left='shha-cy', right='tse-cy')  # shhadescender-cy
x.addKerning(left='shha-cy', right='shha-cy', italic_right='tse-cy')  # 'shhadescender-cy',

x = ugi('softsign-cy')
x.addRecipe('Softsign-cy decompose')
x.addRecipe('b decompose')
x.addRecipe('p.sc decompose')
x.addRecipe('b.sc decompose')
x.addAnchor('#topleft', position_x=xpos.outline_left, position_y=ypos.xHeight)
x.addMetrics(left='en-cy', right='softsign-cy')  # softsign-cy
x.addKerning(left='en-cy', right='softsign-cy')  # 'softsign-cy',

x = ugi('softsign-cy.loclBGR')
x.addRecipe('softsign-cy decompose')
x.addMetrics(left='u', right='softsign-cy')  # softsign-cy.loclBGR
x.addKerning(left='en-cy', right='softsign-cy')  # 'softsign-cy.loclBGR',
x.addAnchor('#topleft', position_x=xpos.outline_left, position_y=ypos.xHeight)

x = ugi('te-cy')
x.addRecipe('ge-cy decompose', 'ge-cy flip_horizontal decompose')
x.addRecipe('m', italic=True)
x.addAnchor('#bottomright', position_x=xpos.stem_bottom_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addMetrics(left='=|ge-cy', right='ge-cy', italic_left='te-cy', italic_right='ge-cy')  # te-cy
x.addKerning(left='te-cy', right='ge-cy', italic_left='en-cy', italic_right='pe-cy')  # 'te-cy',

x = ugi('te-cy.loclBGR')
x.addRecipe('m')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addKerning(left='en-cy', right='tshe-cy')  # 'te-cy.loclBGR',

x = ugi('te-cy.loclMKD')
x.addRecipe('te-cy.loclSRB')
x.addRecipe('sha-cy', 'macroncomb')
x.addKerning(left='a-cy', right='a-cy', italic_left='sha-cy', italic_right='en-cy')  # 'te-cy.loclSRB',

x = ugi('te-cy.loclSRB')
x.addRecipe('sha-cy', 'macron')
x.addMetrics(left='a-cy', right='a-cy', italic_left='sha-cy', italic_right='en-cy')  # te-cy.loclSRB
x.addKerning(left='a-cy', right='a-cy', italic_left='sha-cy', italic_right='en-cy')  # 'te-cy.loclSRB',

x = ugi('tedescender-cy')
x.addRecipe('te-cy', '_part.toothright-cy')
x.addRecipe('te-cy', 'toothright-cy')
x.addMetrics(left='te-cy', right='ge-cy', italic_left='en-cy', italic_right='tse-cy')  # tedescender-cy
x.addKerning(left='te-cy', right='ge-cy', italic_left='en-cy', italic_right='tse-cy')  # 'tedescender-cy',

x = ugi('tetse-cy')
x.addRecipe('tse-cy', 'macroncomb')
x.addRecipe('tse-cy', 'te-cy decompose')
x.addMetrics(left='te-cy', right='tse-cy', italic_left='tetse-cy', italic_right='tse-cy')  # tetse-cy
x.addKerning(left='te-cy', right='de-cy', italic_left='hardsign-cy', italic_right='tse-cy')  # 'tetse-cy',

x = ugi('tse-cy')
x.addRecipe('tsebase-cy', '_part.toothright-cy')
x.addRecipe('tsebase-cy', 'toothright-cy')
x.addMetrics(left='en-cy', right='', italic_left='sha-cy', italic_right='tse-cy')  # tse-cy
x.addKerning(left='en-cy', right='de-cy', italic_left='sha-cy', italic_right='tse-cy')  # 'tse-cy',

x = ugi('tse-cy.loclBGR')
x.addRecipe('ii-cy.loclBGR disable_alignment', '_part.toothright-cy')
x.addRecipe('ii-cy.loclBGR', 'toothright-cy')
x.addMetrics(left='u', right='tse-cy')  # tse-cy.loclBGR
x.addKerning(left='ii-cy.loclBGR', right='de-cy')  # 'tse-cy.loclBGR',

x = ugi('tsebase-cy')
x.addRecipe('en-cy decompose')
x.addAnchor('#toothcenter', position_x=xpos.outline_center, position_y=ypos.base_line)
x.addAnchor('#toothright', position_x=xpos.outline_right)
x.addAnchor('toothright', suppress_auto=True)
x.addMetrics(left='en-cy', right='en-cy', italic_left='ii-cy', italic_right='')  # tsebase-cy

x = ugi('tshe-cy')
x.addRecipe('hbar')
x.addMetrics(left='tshe-cy', right='tshe-cy', italic_left='dje-cy', italic_right='pe-cy')  # tshe-cy
x.addKerning(left='dje-cy', right='tshe-cy', italic_right='pe-cy')  # 'tshe-cy',

x = ugi('u-cy')
x.addMetrics(left='u-cy', right='u-cy')  # u-cy
x.addKerning(left='u-cy', right='u-cy')  # 'u-cy',

x = ugi('udieresis-cy')
x.addMetrics(left='u-cy', right='u-cy')  # udieresis-cy
x.addKerning(left='u-cy', right='u-cy')  # 'udieresis-cy',

x = ugi('uhungarumlaut-cy')
x.addMetrics(left='u-cy', right='u-cy')  # uhungarumlaut-cy
x.addKerning(left='u-cy', right='u-cy')  # 'uhungarumlaut-cy',

x = ugi('umacron-cy')
x.addMetrics(left='u-cy', right='u-cy')  # umacron-cy
x.addKerning(left='u-cy', right='u-cy')  # 'umacron-cy',

x = ugi('uk-cy')
x.addRecipe('o-cy', 'u-cy')
x.addKerning(left='o-cy', right='u-cy')  # 'uk-cy',

x = ugi('uni047B')
x.addRecipe('o-cy', '_part.stem')
x.addMetrics(left='o-cy', right='o-cy')  # uni047B
x.addKerning(left='o-cy', right='o-cy')  # 'uni047B',

x = ugi('uni047D')
x.addRecipe('omega', 'psilipneumatacomb-cy', 'pokrytiecomb-cy')
x.addMetrics(left='o-cy', right='o-cy')  # uni047D
x.addKerning(left='o-cy', right='o-cy')  # 'uni047D',

x = ugi('uni047F')
x.addRecipe('omega-cy', 'T decompose')
x.addRecipe('omega-cy', 't.sc decompose')
x.addRecipe('omega-cy', 'tabovecomb-cy')
x.addKerning(left='ii-cy.loclBGR', right='dze-cy')  # 'uni047F',

x = ugi('ushort-cy')
x.addMetrics(left='u-cy', right='u-cy')  # ushort-cy
x.addKerning(left='u-cy', right='u-cy')  # 'ushort-cy',

x = ugi('ustraight-cy')
x.addRecipe('v decompose', 'idotless decompose')
x.addMetrics(left='u-cy', right='u-cy')  # ustraight-cy
x.addAnchor('#bar', position_x=xpos.outline_center, position_y=ypos.base_line)
x.addKerning(left='u-cy', right='u-cy', italic_left='izhitsa-cy', italic_right='ustraight-cy')  # 'ustraight-cy',

x = ugi('ustraightstroke-cy')
x.addRecipe('ustraight-cy', '_part.bar')
x.addMetrics(left='ustraight-cy', right='ustraight-cy')  # ustraightstroke-cy
x.addKerning(left='u-cy', right='u-cy', italic_left='izhitsa-cy', italic_right='ustraight-cy')  # 'ustraightstroke-cy',

x = ugi('ve-cy')
x.addRecipe('ve-cy.sc decompose')
x.addRecipe('b.sc decompose')
x.addMetrics(left='en-cy', right='ve-cy', italic_left='o-cy')  # ve-cy
x.addKerning(left='en-cy', right='ve-cy', italic_left='o-cy')  # 've-cy',

x = ugi('ve-cy.loclBGR')
x.addRecipe('beta decompose')
x.addRecipe('b decompose', 'germandbls decompose')

x = ugi('we-cy')
x.addRecipe('w')
x.addMetrics(left='u-cy', right='u-cy')  # we-cy
x.addKerning(left='izhitsa-cy', right='u-cy')  # 'we-cy',

x = ugi('yat-cy')
x.addRecipe('pe-cy', 'softsign-cy decompose', italic=True)
x.addRecipe('softsign-cy', '_part.stem', '_part.bar')
x.addRecipe('softsign-cy', 'T decompose')
x.addMetrics(left='yat-cy', right='softsign-cy', italic_left='en-cy')  # yat-cy
x.addKerning(left='yat-cy', right='softsign-cy', italic_left='en-cy')  # 'yat-cy',

x = ugi('yeru-cy')
x.addMetrics(left='en-cy', right='en-cy', italic_right='en-cy')  # yeru-cy
x.addKerning(left='en-cy', right='en-cy', italic_right='en-cy')  # 'yeru-cy',

x = ugi('yerudieresis-cy')
x.addMetrics(left='en-cy', right='en-cy')  # yerudieresis-cy
x.addKerning(left='en-cy', right='en-cy')  # 'yerudieresis-cy',

x = ugi('yi-cy')
x.addMetrics(left='i-cy', right='i-cy')  # yi-cy
x.addKerning(left='yi-cy', right='yi-cy')  # 'yi-cy',

x = ugi('yi-cy.loclUKR')
x.addRecipe('idotless', 'dieresiscomb decompose')

x = ugi('yusbig-cy')
x.addRecipe('v decompose', 'manat decompose', '_part.bar')
x.addMetrics(left='=|shha-cy', right='shha-cy')  # yusbig-cy
x.addKerning(left='zhe-cy', right='ka-cy')  # 'yusbig-cy',

x = ugi('yusbigiotified-cy')
x.addRecipe('iu-cy decompose', 'yusbig-cy')
x.addMetrics(left='h', right='yusbig-cy')  # yusbigiotified-cy
x.addKerning(left='en-cy', right='ka-cy')  # 'yusbigiotified-cy',

x = ugi('yuslittle-cy')
x.addRecipe('t decompose', 'i decompose', 'v decompose')
x.addMetrics(left='v', right='v')  # yuslittle-cy
x.addKerning(left='el-cy.loclBGR', right='el-cy.loclBGR')  # 'yuslittle-cy',

x = ugi('yuslittleiotified-cy')
x.addRecipe('iu-cy decompose', 'yuslittle-cy')
x.addMetrics(left='h', right='a')  # yuslittleiotified-cy
x.addKerning(left='en-cy', right='el-cy.loclBGR')  # 'yuslittleiotified-cy',

x = ugi('ze-cy')
x.addRecipe('Ze-cy decompose')
x.addRecipe('three decompose')
x.addMetrics(left='ze-cy', right='ve-cy')  # ze-cy
x.addKerning(left='ze-cy', right='ve-cy')  # 'ze-cy',

x = ugi('ze-cy.loclBGR')
x.addRecipe('schwa-cy decompose', 'dzeabkhasian-cy decompose')
x.addRecipe('three.osf decompose')
x.addRecipe('three decompose')
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y='ypos.outline_bottom')
x.addKerning(left='ze-cy.loclBGR', right='ze-cy.loclBGR')  # 'ze-cy.loclBGR',
x.addBuildString('За/pe-cy.loclBGR а/ze-cy.loclBGR ва')  # Запазва За/pecyr.loclBGR а/zecyr.loclBGR ва

x = ugi('zedescender-cy')
x.addRecipe('ze-cy', '_part.toothcentered-cy')
x.addRecipe('ze-cy', 'ogonekcomb flip_horizontal decompose')
x.addMetrics(left='ze-cy', right='ze-cy')  # zedescender-cy
x.addKerning(left='ze-cy', right='ve-cy')  # 'zedescender-cy',

x = ugi('zedieresis-cy')
x.addMetrics(left='ze-cy', right='ze-cy')  # zedieresis-cy
x.addKerning(left='ze-cy', right='ve-cy')  # 'zedieresis-cy',

x = ugi('zhe-cy')
x.addRecipe('ka-cy flip_horizontal decompose', 'ka-cy')
x.addMetrics(left='=|ka-cy', right='ka-cy', italic_right='zhe-cy')  # zhe-cy
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addKerning(left='zhe-cy', right='ka-cy', italic_right='ka-cy')  # 'zhe-cy',

x = ugi('zhe-cy.loclBGR')
x.addRecipe('zhe-cy decompose', 'ka-cy.loclBGR')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addAnchor('top', position_x=xpos.outline_center, position_y='ypos.ascender')
x.addMetrics(left='zhe-cy', right='zhe-cy')  # zhe-cy.loclBGR
x.addKerning(left='zhe-cy', right='ka-cy', italic_right='ka-cy')  # 'zhe-cy.loclBGR',

x = ugi('zhebreve-cy')
x.addMetrics(left='zhe-cy', right='ka-cy')  # zhebreve-cy
x.addKerning(left='zhe-cy', right='ka-cy', italic_right='ka-cy')  # 'zhebreve-cy',

x = ugi('zhedescender-cy')
x.addRecipe('zhe-cy', '_part.toothright-cy')
x.addRecipe('zhe-cy', 'toothright-cy')
x.addMetrics(left='zhe-cy', right='kadescender-cy', italic_right='kadescender-cy')  # zhedescender-cy
x.addKerning(left='zhe-cy', right='ka-cy', italic_right='ka-cy')  # 'zhedescender-cy',

x = ugi('zhedieresis-cy')
x.addMetrics(left='zhe-cy', right='ka-cy')  # zhedieresis-cy
x.addKerning(left='zhe-cy', right='ka-cy', italic_right='ka-cy')  # 'zhedieresis-cy',


#
# --------------------------------
#
#   Smallcaps
#
# --------------------------------
#


x = ugi('be-cy.sc')
x.addRecipe('softsign-cy.sc', '_part.bar disable_alignment')
x.addRecipe('softsign-cy.sc', 'f.sc decompose')

x = ugi('che-cy.sc')
x.addRecipe('u decompose', 'i.sc decompose')
x.addRecipe('che-cy decompose', 'i.sc decompose')
x.addAnchor('#bottomleft', position_x=xpos.stem_bottom_left, position_y=ypos.base_line)
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)

x = ugi('chedescender-cy.sc')
x.addRecipe('che-cy.sc disable_alignment', '_part.toothright-cy')
x.addRecipe('che-cy.sc', 'toothright-cy')
x.addMetrics(left='che-cy.sc', right='tse-cy.sc')  # chedescender-cy.sc
x.addKerning(left='che-cy.sc', right='de-cy.sc')  # 'chedescender-cy.sc',

x = ugi('cheverticalstroke-cy.sc')
x.addRecipe('che-cy.sc', '_part.stem disable_alignment')
x.addMetrics(left='che-cy.sc', right='en-cy.sc')  # cheverticalstroke-cy

x = ugi('chekhakassian-cy.sc')
x.addRecipe('che-cy.sc', '_part.toothleft-cy')

x = ugi('de-cy.sc')
x.addRecipe('el-cy.sc decompose', 'tse-cy.sc decompose')

x = ugi('de-cy.loclBGR.sc')
x.addRecipe('de-cy.sc decompose', 'lambda.sc')
x.addRecipe('de-cy.sc decompose', 'a.sc decompose')
x.addBuildString('/De-cy.loclBGR/de-cy.loclBGR.sc/de-cy.sc/tse-cy.sc')
x.addKerning(left='a-cy.sc', right='a-cy.sc')  # 'de-cy.loclBGR.sc',

x = ugi('dje-cy.sc')
x.addRecipe('t.sc decompose', 'b.sc decompose')
x.addBuildString('/Dje-cy/dje-cy.sc/tshe-cy.sc')

x = ugi('dzhe-cy.sc')
x.addRecipe('tsebase-cy.sc', '_part.toothcentered-cy')
x.addRecipe('tsebase-cy.sc', 'toothcentered-cy')

x = ugi('e-cy.sc')
x.addRecipe('c.sc', '_part.bar disable_alignment')
x.addRecipe('c.sc', 'e.sc decompose')

x = ugi('ef-cy.sc')
x.addRecipe('phi.sc')
x.addRecipe('o-cy.sc decompose', 'i-cy.sc')

x = ugi('ef-cy.loclBGR.sc')
x.addRecipe('o.sc decompose', 'i.sc decompose')
x.addKerning(left='o-cy.sc', right='o-cy.sc')  # 'ef-cy.loclBGR.sc',

x = ugi('el-cy.sc')
x.addRecipe('el-cy decompose')
x.addRecipe('El-cy decompose')
x.addMetrics(left='', right='en-cy.sc')

x = ugi('el-cy.loclBGR.sc')
x.addRecipe('lambda.sc')
x.addRecipe('a.sc decompose')
x.addMetrics(left='a-cy.sc', right='a-cy.sc')
x.addBuildString('/El-cy.loclBGR.sc/el-cy.loclBGR.sc')
x.addKerning(left='a-cy.sc', right='a-cy.sc')  # 'el-cy.loclBGR.sc',

x = ugi('en-cy.sc')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)

x = ugi('enghe-cy.sc')
x.addRecipe('en-cy.sc disable_alignment', '_part.bar')
x.addRecipe('en-cy.sc', 'te-cy.sc decompose')
x.addMetrics(left='en-cy.sc', right='ge-cy.sc')  # enghe-cy.sc
x.addKerning(left='en-cy.sc', right='ge-cy.sc')  # 'enghe-cy.sc',

x = ugi('enhook-cy.sc')
x.addRecipe('h.sc decompose', 'j.sc decompose')

x = ugi('endescender-cy.sc')
x.addRecipe('en-cy.sc disable_alignment', '_part.toothright-cy')
x.addRecipe('en-cy.sc disable_alignment', 'toothright-cy')

x = ugi('ereversed-cy.sc')
x.addRecipe('e-cy.sc flip_horizontal')
x.addRecipe('c.sc decompose', 'e.sc decompose')

x = ugi('ertick-cy.sc')
x.addRecipe('er-cy.sc', 'macron decompose')

x = ugi('es-cy.sc')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)

x = ugi('esdescender-cy.sc')
x.addRecipe('es-cy.sc', '_part.toothcentered-cy')
x.addRecipe('es-cy.sc decompose', 'ogonekcomb flip_horizontal decompose')

x = ugi('fita-cy.sc')
x.addRecipe('o-cy.sc', 'fita-cy decompose')
x.addRecipe('o-cy.sc', '_part.centertilde')
x.addRecipe('o-cy.sc', 'asciitilde decompose')
x.addMetrics(left='o-cy.sc', right='o-cy.sc')  # fita-cy.sc
x.addKerning(left='o-cy.sc', right='o-cy.sc')  # 'fita-cy.sc',

x = ugi('ge-cy.sc')
x.addRecipe('ge-cy decompose')
x.addAnchor('#bottomright', position_x=xpos.stem_bottom_right, position_y=ypos.base_line)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)
x.addAnchor('#bar', position_x=xpos.stem_bottom_center, position_y=ypos.height_25)

x = ugi('gedescender-cy.sc')
x.addRecipe('ge-cy.sc', '_part.toothright-cy')
x.addRecipe('ge-cy.sc', 'toothright-cy')
x.addMetrics(left='en-cy.sc', right='ge-cy.sc')  # gedescender-cy.sc
x.addKerning(left='en-cy.sc', right='ge-cy.sc')  # 'gedescender-cy.sc',

x = ugi('gheupturn-cy.sc')
x.addRecipe('ge-cy.sc', '_part.toothright-cy flip_vertical')
x.addMetrics(left='ge-cy.sc', right='ge-cy.sc', italic_right='gheupturn-cy.sc')  # gheupturn-cy

x = ugi('ghemiddlehook-cy.sc')
x.addRecipe('ge-cy.sc', 'dje-cy.sc decompose')

x = ugi('ghestroke-cy.sc')
x.addRecipe('ge-cy.sc', '_part.bar disable_alignment')
x.addRecipe('ge-cy.sc', 'macroncomb decompose')

x = ugi('ha-cy.sc')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)

x = ugi('hadescender-cy.sc')
x.addRecipe('ha-cy.sc disable_alignment', '_part.toothright-cy')
x.addRecipe('ha-cy.sc disable_alignment', 'toothright-cy')

x = ugi('hardsign-cy.sc')
x.addRecipe('softsign-cy.sc disable_alignment', '_part.bar disable_alignment')
x.addRecipe('softsign-cy.sc', 't.sc decompose')

x = ugi('ia-cy.sc')
x.addRecipe('r.sc flip_horizontal decompose')
x.addRecipe('softsign-cy.sc flip_horizontal flip_vertical decompose', 'zhe-cy.sc decompose')

x = ugi('ii-cy.sc')
x.addRecipe('n.sc flip_vertical')
x.addRecipe('h.sc decompose')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)
x.addAnchor('#toothright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)

x = ugi('iu-cy.sc')
x.addRecipe('i-cy.sc', 'o-cy.sc', '_part.bar')
x.addRecipe('i-cy.sc', 'o-cy.sc', 'macroncomb decompose')

x = ugi('izhitsa-cy.sc')
x.addRecipe('v.sc decompose', 'izhitsa-cy decompose')

x = ugi('ka-cy.sc')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)
x.addAnchor('bottomright', suppress_auto=True)
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)

x = ugi('kadescender-cy.sc')
x.addRecipe('ka-cy.sc disable_alignment', '_part.toothright-cy')
x.addRecipe('ka-cy.sc disable_alignment', 'toothright-cy')

x = ugi('kabashkir-cy.sc')
x.addRecipe('ka-cy.sc disable_alignment', 'hardsign-cy.sc decompose')

x = ugi('kahook-cy.sc')
x.addRecipe('ka-cy.sc decompose', 'ghemiddlehook-cy.sc decompose')

x = ugi('kaverticalstroke-cy.sc')
x.addRecipe('ka-cy.sc decompose', '_part.stem disable_alignment', '_part.bar disable_alignment')
x.addMetrics(left='en-cy.sc', right='ka-cy.sc')

x = ugi('lje-cy.sc')
x.addRecipe('el-cy.sc decompose', 'softsign-cy.sc')
x.addBuildString('/el-cy.sc/lje-cy.sc/softsign-cy.sc/Lje-cy/lje-cy')

x = ugi('nje-cy.sc')
x.addRecipe('h.sc decompose', 'softsign-cy.sc decompose')

x = ugi('o-cy.sc')
x.addAnchor('#center', position_x=xpos.outline_center, position_y=ypos.outline_middle)

x = ugi('obarred-cy.sc')
x.addRecipe('o-cy.sc', '_part.bar')
x.addRecipe('o-cy.sc', 'obarred-cy decompose')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)

x = ugi('pe-cy.sc')
x.addRecipe('en-cy.sc decompose')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)

x = ugi('pemiddlehook-cy.sc')
x.addRecipe('pi.sc', 'ghemiddlehook-cy.sc decompose')

x = ugi('schwa-cy.sc')
x.addRecipe('schwa.sc')

x = ugi('semisoftsign-cy.sc')
x.addRecipe('softsign-cy.sc decompose', 'hbar decompose')

x = ugi('shcha-cy.sc')
x.addRecipe('sha-cy.sc disable_alignment', '_part.toothright-cy')
x.addRecipe('sha-cy.sc', 'toothright-cy')

x = ugi('sha-cy.sc')
x.addRecipe('tsebase-cy.sc decompose')
x.addRecipe('h.sc decompose')
x.addAnchor('#toothright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)

x = ugi('shha-cy.sc')
x.addRecipe('che-cy.sc flip_vertical flip_horizontal decompose')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)

x = ugi('softsign-cy.sc')
x.addRecipe('p.sc decompose')
x.addRecipe('b.sc decompose')
x.addAnchor('#topleft', position_x=xpos.outline_left, position_y=ypos.smallcapHeight)
x.addAnchor('#topright', position_x=xpos.stem_top_right, position_y=ypos.smallcapHeight)

x = ugi('te-cy.sc')
x.addAnchor('#bottomright', position_x=xpos.stem_bottom_right, position_y=ypos.base_line)
x.addAnchor('bottomright', suppress_auto=True)

x = ugi('tsebase-cy.sc')
x.addRecipe('h.sc decompose')
x.addAnchor('#toothright', position_x=xpos.outline_right)
x.addAnchor('toothright', suppress_auto=True)

x = ugi('tshe-cy.sc')
x.addRecipe('shha-cy.sc disable_alignment', '_part.bar disable_alignment')
x.addRecipe('shha-cy.sc disable_alignment', 't.sc decompose')

x = ugi('u-cy.sc')
x.addRecipe('v.sc decompose', 'g decompose')
x.addRecipe('y.sc decompose')

x = ugi('ushort-cy.sc')
x.addRecipe('u-cy.sc', 'brevecomb-cy enable_alignment')

x = ugi('ustraight-cy.sc')
x.addRecipe('y.sc')

x = ugi('ustraightstroke-cy.sc')
x.addRecipe('ustraight-cy.sc', '_part.bar')
x.addMetrics(left='ustraight-cy.sc', right='ustraight-cy.sc')  # ustraightstroke-cy.sc
x.addKerning(left='u-cy.sc', right='ustraight-cy.sc')  # 'ustraightstroke-cy.sc',

x = ugi('ve-cy.sc')
x.addRecipe('b.sc')

x = ugi('yat-cy.sc')
x.addRecipe('softsign-cy.sc', '_part.bar disable_alignment')
x.addRecipe('softsign-cy.sc', 't.sc decompose')

x = ugi('yeru-cy.sc')
x.addRecipe('softsign-cy.sc', 'i-cy.sc')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)

x = ugi('ze-cy.sc')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.smallcapHeight)
x.addRecipe('ze-cy decompose')
x.addRecipe('three decompose')

x = ugi('zedescender-cy.sc')
x.addRecipe('ze-cy.sc', '_part.toothcentered-cy')
x.addRecipe('ze-cy.sc decompose', 'ogonekcomb flip_horizontal decompose')

x = ugi('zhe-cy.sc')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)
x.addRecipe('ka-cy.sc flip_horizontal flip_vertical decompose', 'ka-cy.sc')
x.addMetrics(left='=|ka-cy.sc', right='ka-cy.sc')

x = ugi('zhedescender-cy.sc')
x.addRecipe('zhe-cy.sc disable_alignment', '_part.toothright-cy enable_alignment')
x.addRecipe('zhe-cy.sc disable_alignment', 'toothright-cy enable_alignment')


#
# --------------------------------
#
#   Other
#
# --------------------------------
#


x = ugi('brevecomb-cy')
x.addRecipe('breve')

x = ugi('toothcentered-cy')
x.addRecipe('toothright-cy decompose')
x.addAnchor('_#toothcenter', position_x=xpos.outline_center, position_y=ypos.base_line)

x = ugi('Toothcenter-cy')
x.addAnchor('_#toothcenter', position_x=xpos.outline_center, position_y=ypos.base_line)

x = ugi('toothleft-cy')
x.addRecipe('toothright-cy flip_horizontal')
x.addAnchor('_#toothleft', position_x=xpos.stem_top_right, position_y=ypos.base_line)
x.addAnchor('_toothleft', suppress_auto=True)

x = ugi('toothright-cy')
x.addRecipe('quotesinglbase decompose')
x.addAnchor('_#toothright', position_x=xpos.stem_top_left, position_y=ypos.base_line)
x.addAnchor('_bottomright', position_x=xpos.outline_left, position_y=ypos.base_line)
x.addAnchor('_toothright', suppress_auto=True)

x = ugi('palatalizationcomb-cy')
x.addAnchor('_top', position_x=xpos.outline_center, position_y='ypos.xHeight')

x = ugi('pokrytiecomb-cy')
x.addAnchor('_top', position_x=xpos.outline_center, position_y='ypos.xHeight')

x = ugi('psilipneumatacomb-cy')
x.addAnchor('_top', position_x=xpos.outline_center, position_y='ypos.xHeight')

x = ugi('titlocomb-cy')
x.addAnchor('_top', position_x=xpos.outline_center, position_y='ypos.xHeight')

x = ugi('dasiapneumatacomb-cy')
x.addAnchor('_top', position_x=xpos.outline_center, position_y='ypos.xHeight')

x = ugi('pokrytiecomb-cy')
x.addRecipe('tildecomb decompose')

x = ugi('psilipneumatacomb-cy')
x.addRecipe('commaabovecomb')
x.addRecipe('commaaccentcomb')
