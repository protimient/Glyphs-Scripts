# -*- coding: utf-8 -*-

from unifiedglyphinfo import CollectedGlyphInfos, xpos, ypos


def collect_infos(infos_dict):
    return infos_dict.update(ugi.unified_infos)


ugi = CollectedGlyphInfos()

x = ugi('A')
x.addAnchor('ogonek', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.capHeight)
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('V flip_horizontal flip_vertical')

x = ugi('AE')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.capHeight)
x.addKerning(left='AE', right='E')
x.addMetrics(left='AE', right='E')
x.addRecipe('A decompose', 'E decompose')

x = ugi('AEacute')
x.addKerning(left='AE', right='E')
x.addMetrics(left='AE', right='E')

x = ugi('Aacute')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Abreve')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Abreveacute')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('A', 'brevecomb_acutecomb')

x = ugi('Abrevedotbelow')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('A', 'brevecomb', 'dotbelowcomb')

x = ugi('Abrevegrave')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('A', 'brevecomb_gravecomb')

x = ugi('Abrevehookabove')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('A', 'brevecomb_hookabovecomb')

x = ugi('Abrevetilde')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('A', 'brevecomb_tildecomb')

x = ugi('Acaron')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Acircumflex')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Acircumflexacute')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('A', 'circumflexcomb_acutecomb')

x = ugi('Acircumflexdotbelow')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('A', 'circumflexcomb', 'dotbelowcomb')

x = ugi('Acircumflexgrave')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('A', 'circumflexcomb_gravecomb')

x = ugi('Acircumflexhookabove')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('A', 'circumflexcomb_hookabovecomb')

x = ugi('Acircumflextilde')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('A', 'circumflexcomb_tildecomb')

x = ugi('Adieresis')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Adotbelow')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Agrave')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Ahookabove')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Alpha')
x.addKerning(left='O', right='H')

x = ugi('Alpha-latin')
x.addRecipe('D flip_vertical flip_horizontal decompose', 'I decompose')

x = ugi('Alphaturned-latin')
x.addRecipe('Alpha-latin flip_vertical flip_horizontal')

x = ugi('Amacron')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Aogonek')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Aring')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Aringacute')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')
x.addRecipe('A', 'ringcomb', 'acutecomb')

x = ugi('Atilde')
x.addKerning(left='A', right='A')
x.addMetrics(left='A', right='A')

x = ugi('Aturned')
x.addKerning(left='V', right='V')
x.addRecipe('A flip_horizontal flip_vertical')

x = ugi('B')
x.addKerning(left='H', right='B')
x.addMetrics(left='H', right='B')

x = ugi('Bhook')
x.addKerning(left='Bhook', right='O')
x.addRecipe('B', '_part.Hookleft')

x = ugi('Bsmall')
x.addKerning(left='n', right='Bsmall')
x.addRecipe('ve-cy')

x = ugi('C')
x.addAnchor('bottom', position_x=xpos.apex_bottom)
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)
x.addKerning(left='O', right='C')
x.addMetrics(left='O', right='C')

x = ugi('Cacute')
x.addKerning(left='O', right='C')
x.addMetrics(left='C', right='C')

x = ugi('Ccaron')
x.addKerning(left='O', right='C')
x.addMetrics(left='C', right='C')

x = ugi('Ccedilla')
x.addKerning(left='O', right='C')
x.addMetrics(left='C', right='C')

x = ugi('Ccircumflex')
x.addKerning(left='O', right='C')
x.addMetrics(left='C', right='C')

x = ugi('Cdotaccent')
x.addKerning(left='O', right='C')
x.addMetrics(left='C', right='C')

x = ugi('Chook')
x.addKerning(left='O', right='C')
x.addRecipe('C', '_part.Hook')

x = ugi('D')
x.addKerning(left='H', right='O')
x.addMetrics(left='H', right='O')

x = ugi('Dafrican')
x.addKerning(left='H', right='O')
x.addRecipe('Eth')

x = ugi('Dcaron')
x.addKerning(left='H', right='O')
x.addMetrics(left='D', right='D')

x = ugi('Dcroat')
x.addKerning(left='Eth', right='O')
x.addMetrics(left='Eth', right='D')
x.addRecipe('Eth')

x = ugi('Dhook')
x.addKerning(left='Bhook', right='O')
x.addRecipe('D', '_part.Hookleft')

x = ugi('Dsmall')
x.addKerning(left='n', right='o')
x.addMetrics(left='n', right='o')

x = ugi('E')
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addKerning(left='H', right='E')
x.addMetrics(left='H', right='E')
x.addRecipe('_part.stem', '_part.bar', '_part.bar', '_part.bar')

x = ugi('Eacute')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', right='E')

x = ugi('Ebreve')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', right='E')

x = ugi('Ecaron')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', right='E')

x = ugi('Ecircumflex')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')

x = ugi('Ecircumflexacute')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')
x.addRecipe('E', 'circumflexcomb_acutecomb')

x = ugi('Ecircumflexdotbelow')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')
x.addRecipe('E', 'circumflexcomb', 'dotbelowcomb')

x = ugi('Ecircumflexgrave')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')
x.addRecipe('E', 'circumflexcomb_gravecomb')

x = ugi('Ecircumflexhookabove')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')
x.addRecipe('E', 'circumflexcomb_hookabovecomb')

x = ugi('Ecircumflextilde')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')
x.addRecipe('E', 'circumflexcomb_tildecomb')

x = ugi('Edieresis')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')

x = ugi('Edotaccent')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')

x = ugi('Edotbelow')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')

x = ugi('Egrave')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')

x = ugi('Ehookabove')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')

x = ugi('Emacron')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', width='E')

x = ugi('Eng')
x.addKerning(left='H', right='N')
x.addMetrics(left='H', right='N')
x.addRecipe('jdotless decompose', 'N decompose')

x = ugi('Eogonek')
x.addKerning(left='H', right='E')
x.addMetrics(left='E', right='E')

x = ugi('Eopen')
x.addKerning(left='S', right='C')
x.addRecipe('Ze-cy flip_horizontal decompose')

x = ugi('EreversedOpen')
x.addKerning(left='S', right='B')
x.addRecipe('Ze-cy')

x = ugi('Esh')
x.addKerning(left='X', right='E')
x.addRecipe('Sigma')

x = ugi('Eth')
x.addBuildString(u'önghljóðuðust')
x.addKerning(left='Eth', right='O')
x.addMetrics(left='Eth', right='D')
x.addRecipe('D', '_part.bar')
x.addRecipe('D', 'macroncomb decompose')

x = ugi('Etilde')
x.addKerning(left='H', right='E')
x.addMetrics(left='H', right='E')

x = ugi('Ezh')
x.addKerning(left='Ezh', right='Germandbls')
x.addRecipe('ezh decompose')

x = ugi('F')
x.addAnchor('#bar', position_x=xpos.stem_bottom_center, position_y=ypos.height_25)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addKerning(left='H', right='F')
x.addMetrics(left='H', right='F')
x.addRecipe('E decompose')

x = ugi('G')
x.addAnchor('bottom', position_x=xpos.apex_bottom)
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)
x.addKerning(left='O', right='G')
x.addMetrics(left='O', right='G')

x = ugi('Gacute')
x.addKerning(left='O', right='G')

x = ugi('Gammaafrican')
x.addKerning(left='V', right='V')
x.addRecipe('gamma-latin decompose')

x = ugi('Gbreve')
x.addKerning(left='O', right='G')
x.addMetrics(left='G', right='G')

x = ugi('Gcircumflex')
x.addKerning(left='O', right='G')
x.addMetrics(left='G', right='G')

x = ugi('Gcommaaccent')
x.addKerning(left='O', right='G')
x.addMetrics(left='G', right='G')

x = ugi('Gdotaccent')
x.addKerning(left='O', right='G')
x.addMetrics(left='G', right='G')

x = ugi('Germandbls')
x.addKerning(left='Germandbls', right='Germandbls')
x.addMetrics(left='Germandbls', right='Germandbls')
x.addRecipe('I decompose', 'S decompose')

x = ugi('Ghook')
x.addKerning(left='O', right='G')
x.addRecipe('G', '_part.hook')

x = ugi('Glottalstop')
x.addRecipe('glottalstop decompose')

x = ugi('Gscript')
x.addKerning(left='O', right='H')
x.addRecipe('Alpha-latin decompose', 'gsingle decompose')

x = ugi('Gsmall')
x.addKerning(left='o', right='Gsmall')

x = ugi('Gsmallhook')
x.addKerning(left='o', right='dhook')
x.addMetrics(left='Gsmall', right='dhook')

x = ugi('H')
x.addAnchor('#bar', position_x=xpos.outline_center, position_y=ypos.height_75)
x.addKerning(left='H', right='H')
x.addMetrics(left='H', right='H')
x.addRecipe('_part.stem', '_part.bar', '_part.stem')

x = ugi('Hbar')
x.addKerning(left='H', right='H')
x.addMetrics(left='H', right='H')
x.addRecipe('H', '_part.bar')
x.addRecipe('H', 'macroncomb decompose')

x = ugi('Hcircumflex')
x.addKerning(left='H', right='H')
x.addMetrics(left='H', right='H')

x = ugi('Hhook')
x.addKerning(left='Bhook', right='H')
x.addRecipe('H', '_part.Hookleft')

x = ugi('Hsmall')
x.addKerning(left='n', right='u')
x.addRecipe('en-cy')

x = ugi('Hturned')
x.addKerning(left='Hturned', right='H')

x = ugi('I')
x.addAnchor('ogonek', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addAnchor('topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addKerning(left='H', right='H')
x.addMetrics(left='H', right='H')
x.addRecipe('_part.stem')

x = ugi('IJ')
x.addKerning(left='H', right='J')
x.addMetrics(left='H', right='J')

x = ugi('Iacute')
x.addKerning(left='H', right='H')
x.addMetrics(left='I', width='I')

x = ugi('Ibreve')
x.addKerning(left='H', right='H')
x.addMetrics(left='I', right='I')

x = ugi('Icaron')
x.addKerning(left='H', right='H')
x.addMetrics(left='I', right='I')

x = ugi('Icircumflex')
x.addKerning(left='H', right='H')
x.addMetrics(left='I', right='I')

x = ugi('Idieresis')
x.addKerning(left='H', right='H')
x.addMetrics(left='I', right='I')

x = ugi('Idotaccent')
x.addKerning(left='H', right='H')
x.addMetrics(left='I', right='I')

x = ugi('Idotbelow')
x.addKerning(left='H', right='H')
x.addMetrics(left='I', right='I')

x = ugi('Igrave')
x.addKerning(left='H', right='H')
x.addMetrics(width='I', right='I')

x = ugi('Ihookabove')
x.addKerning(left='H', right='H')
x.addMetrics(left='I', right='I')

x = ugi('Imacron')
x.addKerning(left='H', right='H')
x.addMetrics(left='I', right='I')

x = ugi('Iogonek')
x.addKerning(left='H', right='H')
x.addMetrics(left='I', right='I')

x = ugi('Iotaafrican')
x.addKerning(left='H', right='Iotaafrican')
x.addRecipe('iota decompose')

x = ugi('Ismall')
x.addKerning(left='Ismall', right='Ismall')

x = ugi('Istroke')
x.addKerning(left='Eth', right='Istroke')
x.addRecipe('I', '_part.bar')

x = ugi('Itilde')
x.addKerning(left='H', right='H')
x.addMetrics(left='I', right='I')

x = ugi('J')
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.capHeight)
x.addKerning(left='J', right='J')
x.addMetrics(left='J', right='J')

x = ugi('Jcircumflex')
x.addKerning(left='J', right='J')
x.addMetrics(left='J', right='J')

x = ugi('Jcrossedtail')
x.addKerning(left='J', right='Jcrossedtail')
x.addRecipe('J decompose', 'jcrossedtail decompose')

x = ugi('K')
x.addAnchor('bottom', position_x=xpos.outline_center, position_y=ypos.base_line)
x.addKerning(left='H', right='K')
x.addMetrics(left='H', right='K')

x = ugi('Kcommaaccent')
x.addKerning(left='H', right='K')
x.addMetrics(left='K', right='K')

x = ugi('Khook')
x.addRecipe('K decompose', '_part.Hook decompose')

x = ugi('Kturned')
x.addKerning(left='X', right='H')
x.addRecipe('K flip_horizontal flip_vertical')
x.addRecipe('K flip_vertical flip_horizontal')

x = ugi('L')
x.addAnchor('#dot', position_x=xpos.width_75, position_y=ypos.outline_middle)
x.addAnchor('bottom', position_x=xpos.outline_center, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.capHeight)
x.addAnchor('topright', position_x=xpos.stem_top_right, position_y=ypos.capHeight)
x.addKerning(left='H', right='L')
x.addMetrics(left='H', right='L')
x.addRecipe('E decompose')

x = ugi('Lacute')
x.addKerning(left='H', right='L')
x.addMetrics(left='L', right='L')

x = ugi('Lbelt')
x.addKerning(left='Lbelt', right='L')
x.addRecipe('L', 'lbelt decompose')

x = ugi('Lcaron')
x.addKerning(left='H', right='L')
x.addMetrics(left='L', right='L')

x = ugi('Lcommaaccent')
x.addKerning(left='H', right='L')
x.addMetrics(left='L', right='L')

x = ugi('Ldot')
x.addKerning(left='H', right='L')
x.addMetrics(left='L', right='L')
x.addRecipe('L', 'dotaccent')
x.addRecipe('L', 'periodcentered.loclCAT')

x = ugi('Lmiddletilde')
x.addKerning(left='Eth', right='L')
x.addRecipe('L', '_part.tilde')

x = ugi('Lslash')
x.addKerning(left='H', right='L')
x.addMetrics(left='Lslash', right='L')
x.addRecipe('macroncomb decompose', 'L')

x = ugi('Lsmall')
x.addKerning(left='n', right='Lsmall')

x = ugi('M')
x.addKerning(left='H', right='H')
x.addMetrics(left='H', right='H')

x = ugi('Mhook')
x.addKerning(left='H', right='H')
x.addRecipe('M', '_part.hook flip_horizontal flip_vertical')

x = ugi('Mturned')
x.addKerning(left='U', right='H')
x.addRecipe('u decompose', 'I decompose')

x = ugi('N')
x.addAnchor('bottom', position_x=xpos.outline_center)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addKerning(left='H', right='N')
x.addMetrics(left='H', right='N')

x = ugi('Nacute')
x.addKerning(left='H', right='N')
x.addMetrics(left='N', right='N')

x = ugi('Napostrophe')
x.addMetrics(left='quoteright', right='N')

x = ugi('Ncaron')
x.addKerning(left='H', right='N')
x.addMetrics(left='N', right='N')

x = ugi('Ncommaaccent')
x.addKerning(left='H', right='N')
x.addMetrics(left='N', right='N')

x = ugi('Nhookleft')
x.addKerning(left='H', right='H')
x.addRecipe('N', '_part.hook flip_horizontal flip_vertical')

x = ugi('Nlongrightleg')
x.addKerning(left='H', right='H')
x.addRecipe('Shha-cy decompose')

x = ugi('Nsmall')
x.addKerning(left='n', right='u')

x = ugi('Ntilde')
x.addKerning(left='H', right='N')
x.addMetrics(left='N', right='N')

x = ugi('O')
x.addAnchor('#center', position_x=xpos.outline_center, position_y=ypos.outline_middle)
x.addAnchor('#topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addAnchor('#topright', position_x=xpos.outline_right, position_y=ypos.capHeight)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.base_line)
x.addAnchor('center', suppress_auto=True)
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)
x.addAnchor('topleft', suppress_auto=True)
x.addAnchor('topright', suppress_auto=True)
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('OE')
x.addKerning(left='O', right='E')
x.addMetrics(left='O', right='E')
x.addRecipe('O decompose', 'E')

x = ugi('OEsmall')
x.addKerning(left='o', right='OEsmall')

x = ugi('Oacute')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Obreve')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Ocaron')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Ocenteredtilde')
x.addKerning(left='O', right='O')
x.addRecipe('Obarred-cy')

x = ugi('Ocircumflex')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Ocircumflexacute')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')
x.addRecipe('O', 'circumflexcomb_acutecomb')

x = ugi('Ocircumflexdotbelow')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')
x.addRecipe('O', 'circumflexcomb', 'dotbelowcomb')

x = ugi('Ocircumflexgrave')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')
x.addRecipe('O', 'circumflexcomb_gravecomb')

x = ugi('Ocircumflexhookabove')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', width='O')
x.addRecipe('O', 'circumflexcomb_hookabovecomb')

x = ugi('Ocircumflextilde')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')
x.addRecipe('O', 'circumflexcomb_tildecomb')

x = ugi('Odieresis')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Odotbelow')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Ograve')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Ohookabove')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Ohorn')
x.addKerning(left='O', right='Ohorn')
x.addMetrics(left='O', right='Ohorn')

x = ugi('Ohornacute')
x.addKerning(left='O', right='Ohorn')
x.addMetrics(left='O', right='Ohorn')
x.addRecipe('Ohorn', 'acutecomb')
x.addRecipe('Ohorn', 'acutecomb.case')

x = ugi('Ohorndotbelow')
x.addKerning(left='O', right='Ohorn')
x.addMetrics(left='O', right='Ohorn')
x.addRecipe('Ohorn', 'dotbelowcomb')
x.addRecipe('Ohorn', 'dotbelowcomb.case')

x = ugi('Ohorngrave')
x.addKerning(left='O', right='Ohorn')
x.addMetrics(left='O', right='Ohorn')
x.addRecipe('Ohorn', 'gravecomb')
x.addRecipe('Ohorn', 'gravecomb.case')

x = ugi('Ohornhookabove')
x.addKerning(left='O', right='Ohorn')
x.addMetrics(left='O', right='Ohorn')
x.addRecipe('Ohorn', 'hookabovecomb')
x.addRecipe('Ohorn', 'hookabovecomb.case')

x = ugi('Ohorntilde')
x.addKerning(left='O', right='Ohorn')
x.addMetrics(left='O', right='Ohorn')
x.addRecipe('Ohorn', 'tildecomb')
x.addRecipe('Ohorn', 'tildecomb.case')

x = ugi('Ohungarumlaut')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Omacron')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Oopen')
x.addKerning(left='Oopen', right='O')
x.addRecipe('C flip_horizontal flip_vertical')

x = ugi('Oslash')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')
x.addRecipe('O', 'slash decompose')

x = ugi('Oslashacute')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Otilde')
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('P')
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addKerning(left='H', right='P')
x.addMetrics(left='H', right='P')

x = ugi('Phook')
x.addKerning(left='Bhook', right='P')
x.addRecipe('P', '_part.Hookleft')

x = ugi('Q')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)
x.addKerning(left='O', right='O')
x.addMetrics(left='O', right='O')

x = ugi('Qhooktail')
x.addKerning(left='O', right='H')
x.addRecipe('Alpha-latin', '_part.Hook flip_vertical')

x = ugi('R')
x.addKerning(left='H', right='R')
x.addMetrics(left='H', right='R')

x = ugi('Racute')
x.addKerning(left='H', right='R')
x.addMetrics(left='R', right='R')

x = ugi('Rcaron')
x.addKerning(left='H', right='R')
x.addMetrics(left='R', right='R')

x = ugi('Rcommaaccent')
x.addKerning(left='H', right='R')
x.addMetrics(left='R', right='R')

x = ugi('Rsmall')
x.addKerning(left='n', right='Rsmall')

x = ugi('Rsmallinverted')
x.addKerning(left='n', right='Rsmallinverted')
x.addRecipe('Rsmall')

x = ugi('Rtail')
x.addKerning(left='H', right='R')
x.addRecipe('R', '_part.Hook flip_vertical')

x = ugi('S')
x.addAnchor('#center', position_x=xpos.outline_center, position_y=ypos.outline_middle)
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.capHeight)
x.addKerning(left='S', right='S')
x.addMetrics(left='S', right='S')

x = ugi('Sacute')
x.addKerning(left='S', right='S')
x.addMetrics(left='S', right='S')

x = ugi('Scaron')
x.addKerning(left='S', right='S')
x.addMetrics(left='S', right='S')

x = ugi('Scedilla')
x.addKerning(left='S', right='S')
x.addMetrics(left='S', right='S')

x = ugi('Schwa')
x.addKerning(left='O', right='O')
x.addMetrics(left='Schwa', right='O')
x.addRecipe('G decompose flip_horizontal')
x.addRecipe('O decompose', 'two decompose', 'H decompose', italic=True)
x.addRecipe('Schwa-cy')
x.addRecipe('schwa decompose')

x = ugi('Scircumflex')
x.addKerning(left='S', right='S')
x.addMetrics(left='S', right='S')

x = ugi('Scommaaccent')
x.addKerning(left='S', right='S')
x.addMetrics(left='S', right='S')

x = ugi('T')
x.addAnchor('#center', position_x=xpos.stem_bottom_center, position_y=ypos.outline_middle)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center)
x.addKerning(left='T', right='T')
x.addMetrics(left='T', right='T')
x.addRecipe('_part.stem', '_part.bar')

x = ugi('Tbar')
x.addKerning(left='T', right='F')
x.addMetrics(left='T', right='T')
x.addRecipe('T', '_part.bar')

x = ugi('Tcaron')
x.addKerning(left='T', right='T')
x.addMetrics(left='T', right='T')

x = ugi('Tcedilla')
x.addKerning(left='T', right='T')
x.addMetrics(left='T', right='T')
x.addRecipe('T', 'cedillacomb')

x = ugi('Tcommaaccent')
x.addKerning(left='T', right='T')
x.addMetrics(left='T', right='T')

x = ugi('Thook')
x.addKerning(left='Bhook', right='T')
x.addRecipe('T decompose', '_part.Hookleft decompose')

x = ugi('Thorn')
x.addKerning(left='H', right='Thorn')
x.addMetrics(left='H', right='Thorn')
x.addRecipe('P decompose', 'I decompose')

x = ugi('Tretroflexhook')
x.addKerning(left='T', right='T')
x.addRecipe('T', '_part.Hook flip_vertical')

x = ugi('Tturned')
x.addKerning(left='Tturned', right='L')
x.addRecipe('T flip_vertical flip_horizontal')

x = ugi('U')
x.addAnchor('bottom', position_x=xpos.apex_bottom, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Uacute')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Ubar')
x.addKerning(left='U', right='U')
x.addRecipe('U', '_part.bar')

x = ugi('Ubreve')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Ucaron')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Ucircumflex')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Udieresis')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Udieresisacute')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Udieresiscaron')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Udieresisgrave')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Udieresismacron')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Udotbelow')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Ugrave')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Uhookabove')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Uhorn')
x.addKerning(left='U', right='Uhorn')
x.addMetrics(left='U', right='Uhorn')

x = ugi('Uhornacute')
x.addKerning(left='U', right='Uhorn')
x.addMetrics(left='U', right='Uhorn')
x.addRecipe('Uhorn', 'acutecomb')
x.addRecipe('Uhorn', 'acutecomb.case')

x = ugi('Uhorndotbelow')
x.addKerning(left='U', right='Uhorn')
x.addMetrics(left='U', right='Uhorn')
x.addRecipe('Uhorn', 'dotbelowcomb')
x.addRecipe('Uhorn', 'dotbelowcomb.case')

x = ugi('Uhorngrave')
x.addKerning(left='U', right='Uhorn')
x.addMetrics(left='U', right='Uhorn')
x.addRecipe('Uhorn', 'gravecomb')
x.addRecipe('Uhorn', 'gravecomb.case')

x = ugi('Uhornhookabove')
x.addKerning(left='U', right='Uhorn')
x.addMetrics(left='U', right='Uhorn')
x.addRecipe('Uhorn', 'hookabovecomb')
x.addRecipe('Uhorn', 'hookabovecomb.case')

x = ugi('Uhorntilde')
x.addKerning(left='U', right='Uhorn')
x.addMetrics(left='U', right='Uhorn')
x.addRecipe('Uhorn', 'tildecomb')
x.addRecipe('Uhorn', 'tildecomb.case')

x = ugi('Uhungarumlaut')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Umacron')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Uogonek')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Upsilonafrican')
x.addKerning(left='O', right='O')
x.addRecipe('Omega flip_vertical flip_horizontal')

x = ugi('Uring')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('Usmall')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='=|u')
x.addRecipe('u decompose')

x = ugi('Utilde')
x.addKerning(left='U', right='U')
x.addMetrics(left='U', right='U')

x = ugi('V')
x.addKerning(left='V', right='V')
x.addMetrics(left='V', right='V')

x = ugi('Vhook')
x.addKerning(left='U', right='U')
x.addRecipe('vhook decompose', 'U decompose')

x = ugi('Vturned')
x.addKerning(left='A', right='A')
x.addRecipe('V flip_vertical flip_horizontal')

x = ugi('W')
x.addAnchor('bottom', position_x=xpos.outline_center)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addKerning(left='V', right='V')
x.addMetrics(left='V', right='V')

x = ugi('Wacute')
x.addKerning(left='V', right='V')
x.addMetrics(left='W', right='W')

x = ugi('Wcircumflex')
x.addKerning(left='V', right='V')
x.addMetrics(left='W', right='W')

x = ugi('Wdieresis')
x.addKerning(left='V', right='V')
x.addMetrics(left='W', right='W')

x = ugi('Wgrave')
x.addKerning(left='V', right='V')
x.addMetrics(left='W', right='W')

x = ugi('Whook')
x.addKerning(left='V', right='V')
x.addRecipe('W decompose', 'Khook decompose')

x = ugi('X')
x.addKerning(left='X', right='K')
x.addMetrics(left='=|X', right='=K*1.05')

x = ugi('Y')
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addKerning(left='Y', right='Y')
x.addMetrics(left='V', right='V')

x = ugi('Yacute')
x.addKerning(left='Y', right='Y')
x.addMetrics(left='Y', right='Y')

x = ugi('Ycircumflex')
x.addKerning(left='Y', right='Y')
x.addMetrics(left='Y', right='Y')

x = ugi('Ydieresis')
x.addKerning(left='Y', right='Y')
x.addMetrics(left='Y', right='Y')

x = ugi('Ydotbelow')
x.addKerning(left='Y', right='Y')
x.addMetrics(left='Y', right='Y')

x = ugi('Ygrave')
x.addKerning(left='Y', right='Y')
x.addMetrics(left='Y', right='Y')

x = ugi('Yhookabove')
x.addKerning(left='Y', right='Y')
x.addMetrics(left='Y', right='Y')

x = ugi('Ysmall')
x.addKerning(left='v', right='v')

x = ugi('Ytilde')
x.addKerning(left='Y', right='Y')
x.addMetrics(left='Y', right='Y')

x = ugi('Z')
x.addKerning(left='Z', right='Z')
x.addMetrics(left='Z', right='Z')

x = ugi('Zacute')
x.addKerning(left='Z', right='Z')
x.addMetrics(left='Z', right='Z')

x = ugi('Zcaron')
x.addKerning(left='Z', right='Z')
x.addMetrics(left='Z', right='Z')

x = ugi('Zdotaccent')
x.addKerning(left='Z', right='Z')
x.addMetrics(left='Z', right='Z')

x = ugi('Zstroke')
x.addMetrics(left='Z', right='Z')

#
# --------------------------------
#
#   Lowercase
#
# --------------------------------
#

x = ugi('a')
x.addAnchor('ogonek', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addKerning(left='a', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', right='a', italic_left='o', italic_right='u')

x = ugi('aacute')
x.addKerning(left='a', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('abreve')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('abreveacute')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')
x.addRecipe('a', 'brevecomb_acutecomb')

x = ugi('abrevedotbelow')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')
x.addRecipe('a', 'brevecomb', 'dotbelowcomb')

x = ugi('abrevegrave')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')
x.addRecipe('a', 'brevecomb_gravecomb')

x = ugi('abrevehookabove')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')
x.addRecipe('a', 'brevecomb_hookabovecomb')

x = ugi('abrevetilde')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')
x.addRecipe('a', 'brevecomb_tildecomb')

x = ugi('acaron')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('acircumflex')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('acircumflexacute')
x.addKerning(left='abreve', right=None, italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')
x.addRecipe('a', 'circumflexcomb_acutecomb')

x = ugi('acircumflexdotbelow')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')
x.addRecipe('a', 'circumflexcomb', 'dotbelowcomb')

x = ugi('acircumflexgrave')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')
x.addRecipe('a', 'circumflexcomb_gravecomb')

x = ugi('acircumflexhookabove')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')
x.addRecipe('a', 'circumflexcomb_hookabovecomb')

x = ugi('acircumflextilde')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')
x.addRecipe('a', 'circumflexcomb_tildecomb')

x = ugi('acutegraveacutecomb')
x.addMetrics(left='=50', right='=50')
x.addRecipe('graveacutegravecomb flip_horizontal')

x = ugi('acutemacroncomb')
x.addMetrics(left='=50', right='=50')
x.addRecipe('macrongravecomb flip_horizontal')

x = ugi('adieresis')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('adotbelow')
x.addKerning(left='a', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('ae')
x.addKerning(left='a', right='e', italic_left='o')
x.addMetrics(left='a', right='e', italic_left='o')
x.addRecipe('a decompose', 'e decompose')

x = ugi('aeacute')
x.addKerning(left='a', right='e', italic_left='o')
x.addMetrics(left='ae', width='ae', italic_left='o')

x = ugi('agrave')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('ahookabove')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('alpha')
x.addKerning(left='o', right='u')

x = ugi('alpha-latin')
x.addRecipe('alpha')

x = ugi('alphaturned')
x.addKerning(left='n', right='o')

x = ugi('alphaturned-latin')
x.addRecipe('alpha')

x = ugi('amacron')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('aogonek')
x.addKerning(left='a', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('aring')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('aringacute')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('atilde')
x.addKerning(left='abreve', right='a', italic_left='o', italic_right='u')
x.addMetrics(left='a', width='a')

x = ugi('aturned')
x.addKerning(left='u', right='e')
x.addRecipe('a flip_vertical')

x = ugi('b')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.ascender)
x.addKerning(left='b', right='o')
x.addMetrics(left='b', right='o')

x = ugi('bhook')
x.addKerning(left='b', right='o')

x = ugi('bilabialclick')
x.addKerning(left='bilabialclick', right='O')
x.addRecipe('O', 'dotaccentcomb')

x = ugi('brevebelowcomb')
x.addMetrics(left='brevecomb', right='brevecomb')

x = ugi('bridgebelowcomb')
x.addRecipe('minusbelowcomb decompose')

x = ugi('bridgeinvertedbelowcomb')
x.addRecipe('bridgebelowcomb flip_vertical')

x = ugi('c')
x.addAnchor('bottom', position_x=xpos.apex_bottom)
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.xHeight)
x.addKerning(left='o', right='c')
x.addMetrics(left='o', right='c')

x = ugi('cacute')
x.addKerning(left='o', right='c')
x.addMetrics(left='c', width='c')

x = ugi('ccaron')
x.addKerning(left='o', right='c')
x.addMetrics(left='c', width='c')

x = ugi('ccedilla')
x.addKerning(left='o', right='c')
x.addMetrics(left='c', width='c')

x = ugi('ccircumflex')
x.addKerning(left='o', right='c')
x.addMetrics(left='c', width='c')

x = ugi('ccurl')
x.addKerning(left='o', right='c')

x = ugi('cdotaccent')
x.addKerning(left='o', right='c')
x.addMetrics(left='c', width='c')

x = ugi('chook')
x.addKerning(left='o', right='dhook')
x.addMetrics(left='c', right='dhook')
x.addRecipe('c', '_part.hook')

x = ugi('clickalveolar')
x.addKerning(left='clickalveolar', right='clickalveolar')
x.addRecipe('clickdental', '_part.bar', '_part.bar')

x = ugi('clickdental')
x.addKerning(left='clickdental', right='clickdental')
x.addRecipe('bar decompose')

x = ugi('clicklateral')
x.addKerning(left='clickdental', right='clickdental')
x.addRecipe('clickdental', 'clickdental')

x = ugi('clickretroflex')
x.addKerning(left='h', right='d')
x.addRecipe('exclam')

x = ugi('closeup')
x.addMetrics(left='undertie', right='undertie')
x.addRecipe('undertie', 'breveinverteddoublecomb')

x = ugi('colontriangularhalfmod')
x.addRecipe('periodcentered decompose')

x = ugi('colontriangularmod')
x.addRecipe('colontriangularhalfmod', 'colontriangularhalfmod flip_vertical')

x = ugi('d')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.ascender)
x.addAnchor('topright', position_x=xpos.stem_top_right, position_y=ypos.ascender)
x.addKerning(left='o', right='d')
x.addMetrics(left='d', right='d')

x = ugi('dblarchinvertedbelowcomb')
x.addMetrics(left='seagullbelowcomb', right='seagullbelowcomb')
x.addRecipe('seagullbelowcomb flip_vertical flip_horizontal')

x = ugi('dblverticalbar')
x.addRecipe('bar', 'bar')

x = ugi('dcaron')
x.addKerning(left='o', right='dcaron')
x.addMetrics(left='d', width='d')

x = ugi('dcroat')
x.addKerning(left='o', right='d')
x.addMetrics(left='d', right='d')
x.addRecipe('d', '_part.bar')
x.addRecipe('d', 'macroncomb decompose')

x = ugi('dezh')
x.addKerning(left='o', right='ezh')
x.addRecipe('d', 'ezh')

x = ugi('dhook')
x.addKerning(left='o', right='dhook')
x.addMetrics(left='d')
x.addRecipe('d decompose', '_part.hook')

x = ugi('dhookandtail')
x.addKerning(left='o', right='dhook')
x.addMetrics(left='d', right='dhook')
x.addRecipe('dhook', '_part.hook')

x = ugi('downtackbelowcomb')
x.addRecipe('uptackbelowcomb flip_vertical flip_horizontal')

x = ugi('downtackmod')
x.addRecipe('uptackmod flip_vertical')

x = ugi('dtail')
x.addKerning(left='o', right='dtail')
x.addRecipe('d', '_part.hook')

x = ugi('dzaltone')
x.addKerning(left='o', right='z')
x.addMetrics(left='d', right='z')
x.addRecipe('d', 'z')

x = ugi('dzcurl')
x.addKerning(left='d', right='zcurl')
x.addMetrics(left='d', right='zcurl')
x.addRecipe('d', 'zcurl')

x = ugi('e')
x.addAnchor('bottom', position_x=xpos.apex_bottom)
x.addAnchor('ogonek', position_x=xpos.width_75, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.apex_top)
x.addKerning(left='o', right='e')
x.addMetrics(left='o', right='e')

x = ugi('eacute')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')

x = ugi('ebreve')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')

x = ugi('ecaron')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')

x = ugi('ecircumflex')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')

x = ugi('ecircumflexacute')
x.addKerning(left='o', right=None)
x.addMetrics(left='e', width='e')
x.addRecipe('e', 'circumflexcomb_acutecomb')

x = ugi('ecircumflexdotbelow')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')
x.addRecipe('e', 'circumflexcomb', 'dotbelowcomb')

x = ugi('ecircumflexgrave')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')
x.addRecipe('e', 'circumflexcomb_gravecomb')

x = ugi('ecircumflexhookabove')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')
x.addRecipe('e', 'circumflexcomb_hookabovecomb')

x = ugi('ecircumflextilde')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')
x.addRecipe('e', 'circumflexcomb_tildecomb')

x = ugi('edieresis')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')

x = ugi('edotaccent')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')

x = ugi('edotbelow')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')

x = ugi('egrave')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')

x = ugi('ehookabove')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')

x = ugi('emacron')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', width='e')

x = ugi('eng')
x.addKerning(left='n', right='j')
x.addMetrics(left='n', right='j')
x.addRecipe('jdotless decompose', 'n decompose')

x = ugi('eogonek')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', right='e')

x = ugi('eopen')
x.addKerning(left='s', right='c')
x.addRecipe('ze-cy decompose')

x = ugi('eopenreversed')
x.addKerning(left='eopenreversed', right='Bsmall')
x.addRecipe('ze-cy')

x = ugi('eopenreversedclosed')
x.addKerning(left='o', right='Bsmall')
x.addRecipe('ze-cy decompose')

x = ugi('eopenreversedhook')
x.addKerning(left='eopenreversed', right='eopenreversedhook')
x.addRecipe('eopenreversed', '_part.hook')

x = ugi('ereversed')
x.addKerning(left='o', right='o')
x.addRecipe('e decompose')

x = ugi('esh')
x.addKerning(left='j', right='dhook')
x.addMetrics(right='dhook')
x.addRecipe('f decompose')

x = ugi('eth')
x.addKerning(left='eth', right='eth')
x.addMetrics(left='eth', right='eth')

x = ugi('etilde')
x.addKerning(left='o', right='e')
x.addMetrics(left='e', right='e')

x = ugi('ezh')
x.addKerning(left='ezh', right='ezh')

x = ugi('f')
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.ascender)
x.addKerning(left='f', right='f')
x.addMetrics(left='f', right='f')

x = ugi('f_f')
x.addKerning(left='f', right='f')
x.addRecipe('f', 'f')

x = ugi('f_f_i')
x.addKerning(left='f', right='i')
x.addRecipe('f', 'f', 'i')

x = ugi('f_f_l')
x.addKerning(left='f', right='d')
x.addRecipe('f', 'f', 'l')

x = ugi('f_i')
x.addKerning(left='f', right='i')
x.addRecipe('fi')

x = ugi('f_l')
x.addKerning(left='f', right='d')
x.addRecipe('fl')

x = ugi('fi')
x.addKerning(left='f', right='i')
x.addRecipe('f_i')

x = ugi('fl')
x.addKerning(left='f', right='d')
x.addRecipe('f_l')

x = ugi('g')
x.addKerning(left='g', right='g')
x.addMetrics(left='g', right='g')

x = ugi('gacute')
x.addKerning(left='g', right='g')

x = ugi('gamma')
x.addKerning(left='v', right='v')

x = ugi('gamma-latin')
x.addRecipe('v decompose')

x = ugi('gbreve')
x.addKerning(left='g', right='g')
x.addMetrics(left='g', right='g')

x = ugi('gcircumflex')
x.addKerning(left='g', right='g')
x.addMetrics(left='g', right='g')

x = ugi('gcommaaccent')
x.addKerning(left='g', right='g')
x.addMetrics(left='g', right='g')
x.addRecipe('g', 'commaturnedabovecomb')

x = ugi('gdotaccent')
x.addKerning(left='g', right='g')
x.addMetrics(left='g', right='g')

x = ugi('germandbls')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.ascender)
x.addKerning(left='f', right='germandbls')
x.addMetrics(left='f', right='germandbls')
x.addRecipe('f decompose', 's decompose')

x = ugi('ghook')
x.addKerning(left='o', right='dhook')
x.addMetrics(left='g', right='dhook')
x.addRecipe('gsingle', '_part.hook')

x = ugi('glottalstop')
x.addKerning(left='glottalstop', right='glottalstop')
x.addRecipe('question decompose')

x = ugi('glottalstopreversed')
x.addKerning(left='glottalstopreversed', right='glottalstopreversed')
x.addRecipe('glottalstop flip_horizontal')

x = ugi('glottalstopsmall')
x.addRecipe('glottalstop decompose')

x = ugi('glottalstopstroke')
x.addKerning(left='glottalstopstroke', right='glottalstopstroke')
x.addRecipe('glottalstop', '_part.bar')

x = ugi('glottalstopstrokereversed')
x.addKerning(left='glottalstopstrokereversed', right='glottalstopstrokereversed')
x.addRecipe('glottalstopreversed', '_part.bar')

x = ugi('graveacutegravecomb')
x.addMetrics(left='=50', right='=50')
x.addRecipe('caron decompose', 'circumflex decompose')

x = ugi('gravemacroncomb')
x.addMetrics(left='=50', right='=50')
x.addRecipe('macronacutecomb flip_horizontal')

x = ugi('gsingle')
x.addKerning(left='o', right='u')
x.addRecipe('q decompose', 'y decompose')

x = ugi('h')
x.addKerning(left='h', right='n')
x.addMetrics(left='h', right='n')

x = ugi('hbar')
x.addKerning(left='h', right='n')
x.addMetrics(width='h', right='h')
x.addRecipe('h', '_part.bar')
x.addRecipe('h', 'macroncomb decompose')

x = ugi('hcircumflex')
x.addKerning(left='h', right='n')
x.addMetrics(width='h', right='h')

x = ugi('henghook')
x.addKerning(left='j', right='n')
x.addRecipe('hhook', '_part.hook')

x = ugi('hhook')
x.addKerning(left='h', right='n')
x.addRecipe('n', '_part.hook')

x = ugi('hturned')
x.addKerning(left='u', right='q')
x.addRecipe('h flip_horizontal flip_vertical')

x = ugi('hv')
x.addKerning(left='h', right='vhook')
x.addMetrics(left='h', right='vhook')
x.addRecipe('h decompose', 'vhook decompose')

x = ugi('i')
x.addAnchor('bottom', position_x=xpos.stem_bottom_center)
x.addAnchor('ogonek', position_x='xpos.stem_bottom_right')
x.addKerning(left='i', right='i')
x.addMetrics(left='i', right='i')

x = ugi('iacute')
x.addKerning(left='i', right='i')
x.addMetrics(left='i', right='i')

x = ugi('ibreve')
x.addKerning(left='idieresis', right='i')
x.addMetrics(left='idieresis', right='i')

x = ugi('icaron')
x.addKerning(left='idieresis', right='i')
x.addMetrics(left='idieresis', right='i')

x = ugi('icircumflex')
x.addKerning(left='idieresis', right='i')
x.addMetrics(left='idieresis', right='i')

x = ugi('idieresis')
x.addKerning(left='idieresis', right='i')
x.addMetrics(left='idieresis', right='i')

x = ugi('idotaccent')
x.addKerning(left='i', right='i')
x.addMetrics(left='i', right='i')

x = ugi('idotbelow')
x.addKerning(left='i', right='i')
x.addMetrics(left='i', width='i')

x = ugi('idotless')
x.addAnchor('bottom', position_x=xpos.outline_center)
x.addAnchor('ogonek', suppress_auto=True)
x.addAnchor('top', position_x=xpos.outline_center)
x.addKerning(left='n', right='u')
x.addMetrics(left='i', width='i')
x.addRecipe('i decompose')

x = ugi('igrave')
x.addKerning(left='idieresis', right='i')
x.addMetrics(left='idieresis', right='i')

x = ugi('ihookabove')
x.addKerning(left='i', right='i')
x.addMetrics(left='i', width='i')

x = ugi('ij')
x.addKerning(left='i', right='j')
x.addMetrics(left='i', right='j')

x = ugi('imacron')
x.addKerning(left='idieresis', right='i')
x.addMetrics(left='idieresis', right='i')

x = ugi('iogonek')
x.addKerning(left='i', right='i')
x.addMetrics(width='i')
x.addRecipe('i', 'ogonekcomb')

x = ugi('istroke')
x.addKerning(left='i', right='i')
x.addRecipe('i', '_part.bar')

x = ugi('itilde')
x.addKerning(left='idieresis', right='i')
x.addMetrics(left='idieresis', right='i')

x = ugi('j')
x.addKerning(left='j', right='j')
x.addMetrics(left='j', right='j')

x = ugi('jcircumflex')
x.addKerning(left='jcircumflex', right='j')
x.addMetrics(left='jcircumflex', right='j')

x = ugi('jcrossedtail')
x.addKerning(left='jcrossedtail', right='jcrossedtail')
x.addRecipe('j decompose')

x = ugi('jdotless')
x.addAnchor('bottom', position_x=xpos.outline_center, position_y=ypos.outline_bottom)
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.xHeight)
x.addKerning(left='j', right='j')
x.addKerning(left='p', right='q')
x.addMetrics(left='j', width='j')
x.addRecipe('j decompose')

x = ugi('jdotlessstroke')
x.addKerning(left='jdotlessstroke', right='istroke')
x.addRecipe('jdotless', '_part.bar')

x = ugi('jdotlessstrokehook')
x.addKerning(left='jdotlessstroke', right='dhook')
x.addRecipe('jdotlessstroke', '_part.hook')

x = ugi('k')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.ascender)
x.addKerning(left='h', right='k')
x.addMetrics(left='h', right='k')

x = ugi('kcommaaccent')
x.addKerning(left='h', right='k')
x.addMetrics(left='k', right='k')

x = ugi('kgreenlandic')
x.addKerning(left='n', right='k')
x.addMetrics(left='n', right='k')
x.addRecipe('k decompose')

x = ugi('khook')
x.addKerning(left='h', right='k')
x.addRecipe('kgreenlandic', '_part.hook')

x = ugi('kturned')
x.addKerning(left='x', right='q')
x.addRecipe('k flip_horizontal flip_vertical')

x = ugi('l')
x.addAnchor('#dot', position_x='xpos.RSB', position_y=ypos.outline_middle)
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.stem_top_center)
x.addAnchor('topright', position_x=xpos.stem_top_right)
x.addKerning(left='h', right='d')
x.addMetrics(left='h', right='d')

x = ugi('lacute')
x.addKerning(left='h', right='d')
x.addMetrics(left='l', right='l')

x = ugi('lambdastroke')
x.addKerning(left='vturned', right='vturned')
x.addMetrics(left='lambda', right='lambda')
x.addRecipe('lambda', 'eth decompose')

x = ugi('lbar')
x.addKerning(left='lslash', right='lslash')
x.addMetrics(left='lslash', right='lslash')
x.addRecipe('l', '_part.bar')

x = ugi('lbelt')
x.addKerning(left='lslash', right='lslash')
x.addRecipe('l', 'zcurl decompose')

x = ugi('lcaron')
x.addKerning(left='h', right='dcaron')
x.addMetrics(left='l', right='dcaron')

x = ugi('lcommaaccent')
x.addKerning(left='h', right='d')
x.addMetrics(left='l', right='l')

x = ugi('ldot')
x.addKerning(left='h', right='ldot')
x.addMetrics(left='l', right='ldot')
x.addRecipe('l', 'dotaccent')
x.addRecipe('l', 'periodcentered.loclCAT')

x = ugi('leftangleabovecomb')
x.addRecipe('lefttackbelowcomb decompose')

x = ugi('lefttackbelowcomb')
x.addRecipe('uptackmod decompose')

x = ugi('lezh')
x.addKerning(left='h', right='ezh')
x.addRecipe('l', 'ezh')

x = ugi('lhookretroflex')
x.addKerning(left='h', right='dtail')
x.addRecipe('l', '_part.hook')

x = ugi('lmiddletilde')
x.addKerning(left='lslash', right='lslash')
x.addRecipe('l', '_part.tilde')

x = ugi('longs')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.ascender)
x.addKerning(left='f', right='f')
x.addMetrics(left='f', right='f')
x.addRecipe('f decompose')

x = ugi('lslash')
x.addKerning(left='lslash', right='lslash')
x.addMetrics(left='lslash', right='lslash')
x.addRecipe('macroncomb decompose', 'l')

x = ugi('m')
x.addAnchor('bottom', position_x=xpos.outline_center)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)
x.addKerning(left='n', right='n')
x.addMetrics(left='n', right='n')

x = ugi('macronacutecomb')
x.addMetrics(left='=50', right='=50')
x.addRecipe('macron decompose', 'acute decompose')

x = ugi('macronbelowcomb')
x.addMetrics(left='macroncomb', right='macroncomb')

x = ugi('macrongravecomb')
x.addMetrics(left='=50', right='=50')
x.addRecipe('macroncomb decompose', 'gravecomb decompose')

x = ugi('mhook')
x.addKerning(left='n', right='j')
x.addRecipe('m', '_part.hook flip_horizontal flip_vertical')

x = ugi('minusbelowcomb')
x.addRecipe('lefttackbelowcomb', 'lefttackbelowcomb flip_horizontal')

x = ugi('minusmod')
x.addMetrics(left='plus', right='plus')
x.addRecipe('macron')

x = ugi('mlonglegturned')
x.addKerning(left='u', right='q')
x.addRecipe('m flip_horizontal flip_vertical', '_part.stem flip_horizontal flip_vertical')

x = ugi('mpalatalhook')
x.addKerning(left='n', right='n')
x.addRecipe('m', '_part.hook flip_vertical flip_horizontal')

x = ugi('mturned')
x.addKerning(left='u', right='u')
x.addRecipe('m flip_horizontal flip_vertical')

x = ugi('n')
x.addAnchor('bottom', position_x=xpos.outline_center)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)
x.addKerning(left='n', right='n')
x.addMetrics(left='n', right='n')

x = ugi('n.subs')
x.addRecipe('nmod')

x = ugi('nacute')
x.addKerning(left='n', right='n')
x.addMetrics(left='n', right='n')

x = ugi('napostrophe')
x.addKerning(left=None, right='n')
x.addMetrics(left=None, right='n')
x.addRecipe('quoteright', 'n')

x = ugi('ncaron')
x.addKerning(left='n', right='n')
x.addMetrics(left='n', right='n')

x = ugi('ncommaaccent')
x.addKerning(left='n', right='n')
x.addMetrics(left='n', right='n')

x = ugi('nhookleft')
x.addKerning(left='j', right='n')
x.addRecipe('n', '_part.hook flip_horizontal flip_vertical')

x = ugi('nhookretroflex')
x.addKerning(left='n', right='nhookretroflex')
x.addRecipe('n', '_part.hook flip_vertical')

x = ugi('nmod')
x.addRecipe('n.sups')

x = ugi('ntilde')
x.addKerning(left='n', right='n')
x.addMetrics(left='n', right='n')

x = ugi('o')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', right='o')

x = ugi('oacute')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')

x = ugi('obarred')
x.addKerning(left='o', right='o')
x.addRecipe('obarred-cy')

x = ugi('obreve')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')

x = ugi('ocaron')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')

x = ugi('ocircumflex')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')

x = ugi('ocircumflexacute')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')
x.addRecipe('o', 'circumflexcomb_acutecomb')

x = ugi('ocircumflexdotbelow')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')
x.addRecipe('o', 'circumflexcomb', 'dotbelowcomb')

x = ugi('ocircumflexgrave')
x.addKerning(left=None, right='o')
x.addMetrics(right='o', width='o')
x.addRecipe('o', 'circumflexcomb_gravecomb')

x = ugi('ocircumflexhookabove')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')
x.addRecipe('o', 'circumflexcomb_hookabovecomb')

x = ugi('ocircumflextilde')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')
x.addRecipe('o', 'circumflexcomb_tildecomb')

x = ugi('odieresis')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')

x = ugi('odotbelow')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')

x = ugi('oe')
x.addAnchor('bottom', position_x=xpos.outline_center)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)
x.addKerning(left='o', right='e')
x.addMetrics(left='o', right='e')
x.addRecipe('o', 'e')

x = ugi('ograve')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')

x = ugi('ohookabove')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')

x = ugi('ohorn')
x.addKerning(left='o', right='ohorn')
x.addMetrics(left='o', width='ohorn')

x = ugi('ohornacute')
x.addKerning(left='o', right='ohorn')
x.addMetrics(left='o', width='ohorn')
x.addRecipe('ohorn', 'acutecomb')

x = ugi('ohorndotbelow')
x.addKerning(left='o', right='ohorn')
x.addMetrics(left='o', width='ohorn')
x.addRecipe('ohorn', 'dotbelowcomb')

x = ugi('ohorngrave')
x.addKerning(left='o', right='ohorn')
x.addMetrics(left='o', width='ohorn')
x.addRecipe('ohorn', 'gravecomb')

x = ugi('ohornhookabove')
x.addKerning(left='o', right='ohorn')
x.addMetrics(left='o', width='ohorn')
x.addRecipe('ohorn', 'hookabovecomb')

x = ugi('ohorntilde')
x.addKerning(left='o', right='ohorn')
x.addMetrics(left='o', width='ohorn')
x.addRecipe('ohorn', 'tildecomb')

x = ugi('ohungarumlaut')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')

x = ugi('omacron')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', width='o')

x = ugi('oopen')
x.addKerning(left='eopenreversed', right='o')
x.addRecipe('c flip_horizontal flip_vertical')

x = ugi('oslash')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', right='o')
x.addRecipe('o', 'slash decompose')

x = ugi('oslashacute')
x.addKerning(left='o', right='o')
x.addMetrics(left='oslash', right='oslash')

x = ugi('otilde')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', right='o')

x = ugi('p')
x.addKerning(left='p', right='o')
x.addMetrics(left='p', right='o')

x = ugi('phi')
x.addKerning(left='o', right='o')

x = ugi('phi-latin')
x.addRecipe('phi')

x = ugi('plusbelowcomb')
x.addRecipe('lefttackbelowcomb decompose', 'lefttackbelowcomb flip_vertical')

x = ugi('plusmod')
x.addMetrics(left='plus', right='plus')
x.addRecipe('plusbelowcomb')

x = ugi('q')
x.addKerning(left='o', right='q')
x.addMetrics(left='o', right='q')

x = ugi('r')
x.addAnchor('bottom', position_x=xpos.stem_bottom_center, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)
x.addKerning(left='n', right='r')
x.addMetrics(left='n', right='r')

x = ugi('racute')
x.addKerning(left='n', right='r')
x.addMetrics(left='r', right='r')

x = ugi('ramshorn')
x.addKerning(left='ramshorn', right='ramshorn')
x.addRecipe('gamma-latin decompose')

x = ugi('rcaron')
x.addKerning(left='rcaron', right='r')
x.addMetrics(left='r', right='r')

x = ugi('rcommaaccent')
x.addKerning(left='n', right='r')
x.addMetrics(left='r', right='r')

x = ugi('rfishhook')
x.addKerning(left='s', right='r')
x.addRecipe('_part.stem', '_part.hook')

x = ugi('rhook')
x.addKerning(left='n', right='r')
x.addRecipe('r', '_part.hook flip_vertical')

x = ugi('rhookturned')
x.addKerning(left='rturned', right='rhookturned')
x.addRecipe('rturned', '_part.hook flip_vertical')

x = ugi('rhotichookmod')
x.addRecipe('eopenreversedhook decompose')

x = ugi('righttackbelowcomb')
x.addRecipe('lefttackbelowcomb flip_horizontal')

x = ugi('ringhalfleftbelowcomb')
x.addRecipe('ringhalfrightbelowcomb flip_horizontal')

x = ugi('ringhalfrightbelowcomb')
x.addRecipe('brevecomb')

x = ugi('rlonglegturned')
x.addKerning(left='rturned', right='d')
x.addRecipe('rturned', '_part.stem flip_horizontal flip_vertical')

x = ugi('rturned')
x.addKerning(left='rturned', right='u')
x.addRecipe('r flip_horizontal flip_vertical')

x = ugi('s')
x.addAnchor('bottom', position_x=xpos.apex_bottom)
x.addAnchor('top', position_x=xpos.apex_top)
x.addKerning(left='s', right='s')
x.addMetrics(left='s', right='s')

x = ugi('s_t')
x.addRecipe('s', 't')

x = ugi('sacute')
x.addKerning(left='s', right='s')
x.addMetrics(left='s', right='s')

x = ugi('scaron')
x.addKerning(left='s', right='s')
x.addMetrics(left='scaron', right='s')

x = ugi('scedilla')
x.addKerning(left='s', right='s')
x.addMetrics(left='s', right='s')

x = ugi('schwa')
x.addKerning(left='o', right='o')
x.addMetrics(left='o', right='o')
x.addRecipe('e flip_vertical flip_horizontal')

x = ugi('schwahook')
x.addKerning(left='o', right='eopenreversedhook')
x.addRecipe('schwa decompose', 'eopenreversedhook decompose')

x = ugi('scircumflex')
x.addKerning(left='s', right='s')
x.addMetrics(left='s', right='s')

x = ugi('scommaaccent')
x.addKerning(left='s', right='s')
x.addMetrics(left='s', right='s')

x = ugi('seagullbelowcomb')
x.addRecipe('brevecomb decompose', 'brevecomb decompose')

x = ugi('shook')
x.addKerning(left='s', right='s')
x.addRecipe('s', '_part.hook flip_vertical')

x = ugi('squarebelowcomb')
x.addRecipe('bridgebelowcomb', 'bridgebelowcomb flip_vertical')

x = ugi('t')
x.addAnchor('bottom', position_x=xpos.outline_center, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.outline_top)
x.addAnchor('topright', position_x=xpos.stem_top_right, position_y=ypos.ascender)
x.addKerning(left='t', right='t')
x.addMetrics(left='t', right='t')

x = ugi('tbar')
x.addKerning(left='t', right='t')
x.addMetrics(left='t', right='t')
x.addRecipe('t', '_part.bar')
x.addRecipe('t', 'macroncomb decompose')

x = ugi('tcaron')
x.addKerning(left='t', right='tcaron')
x.addMetrics(left='t', right='t')

x = ugi('tccurl')
x.addKerning(left='t', right='c')
x.addMetrics(left='t', right='ccurl')
x.addRecipe('t decompose', 'ccurl decompose')

x = ugi('tcedilla')
x.addKerning(left='t', right='t')
x.addMetrics(left='t', right='t')
x.addRecipe('t', 'cedillacomb')

x = ugi('tcommaaccent')
x.addKerning(left='t', right='t')
x.addMetrics(left='t', right='t')

x = ugi('tesh')
x.addKerning(left='t', right='dhook')
x.addMetrics(left='t', right='esh')
x.addRecipe('t', 'esh')

x = ugi('thorn')
x.addKerning(left='b', right='o')
x.addMetrics(left='b', right='o')
x.addRecipe('p decompose', 'l decompose')

x = ugi('tildeoverlaycomb')
x.addRecipe('asciitilde decompose', 'z')

x = ugi('tonebarextrahighmod')
x.addRecipe('plus decompose')

x = ugi('tonebarextralowmod')
x.addRecipe('tonebarextrahighmod flip_vertical')

x = ugi('tonebarhighmod')
x.addRecipe('tonebarextrahighmod decompose')

x = ugi('tonebarlowmod')
x.addRecipe('tonebarhighmod flip_vertical')

x = ugi('tonebarmidmod')
x.addRecipe('tonebarextrahighmod decompose')

x = ugi('tretroflexhook')
x.addKerning(left='t', right='tretroflexhook')
x.addRecipe('t decompose')

x = ugi('ts')
x.addKerning(left='t', right='s')
x.addMetrics(left='t', right='s')
x.addRecipe('t', 's')

x = ugi('u')
x.addAnchor('bottom', position_x=xpos.outline_center)
x.addAnchor('ogonek', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.xHeight)
x.addAnchor('topright', position_x=xpos.stem_top_right, position_y=ypos.xHeight)
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('uacute')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('ubar')
x.addKerning(left='istroke', right='istroke')
x.addRecipe('u', '_part.bar')

x = ugi('ubreve')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('ucaron')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('ucircumflex')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('udieresis')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('udieresisacute')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('udieresiscaron')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('udieresisgrave')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('udieresismacron')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('udotbelow')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('ugrave')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('uhookabove')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('uhorn')
x.addKerning(left='u', right='ohorn')
x.addMetrics(left='u', right='ohorn')

x = ugi('uhornacute')
x.addKerning(left='u', right='ohorn')
x.addMetrics(left='u', right='uhorn')
x.addRecipe('uhorn', 'acutecomb')

x = ugi('uhorndotbelow')
x.addKerning(left='u', right='ohorn')
x.addMetrics(left='u', right='uhorn')
x.addRecipe('uhorn', 'dotbelowcomb')

x = ugi('uhorngrave')
x.addKerning(left='u', right='ohorn')
x.addMetrics(left='u', right='uhorn')
x.addRecipe('uhorn', 'gravecomb')

x = ugi('uhornhookabove')
x.addKerning(left='u', right='ohorn')
x.addMetrics(left='u', right='uhorn')
x.addRecipe('uhorn', 'hookabovecomb')

x = ugi('uhorntilde')
x.addKerning(left='u', right='ohorn')
x.addMetrics(left='u', right='uhorn')
x.addRecipe('uhorn', 'tildecomb')

x = ugi('uhungarumlaut')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('umacron')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('undertie')
x.addRecipe('parenleft')

x = ugi('uni2C70')
x.addKerning(left='H', right='O')

x = ugi('uogonek')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('upsilon')
x.addKerning(left='upsilon-latin', right='upsilon-latin')

x = ugi('uptackbelowcomb')
x.addRecipe('lefttackbelowcomb decompose')

x = ugi('uptackmod')
x.addMetrics(left='plus', right='plus')
x.addRecipe('plus decompose')

x = ugi('uring')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('utilde')
x.addKerning(left='u', right='u')
x.addMetrics(left='u', right='u')

x = ugi('v')
x.addKerning(left='v', right='v')
x.addMetrics(left='v', right='v')

x = ugi('verticallinebelowcomb')
x.addRecipe('macroncomb decompose')

x = ugi('verticallinelowmod')
x.addRecipe('verticallinemod')

x = ugi('verticallinemod')
x.addRecipe('verticallinebelowcomb')

x = ugi('vhook')
x.addKerning(left='u', right='vhook')
x.addRecipe('u decompose', '_part.hook flip_horizontal')

x = ugi('vrighthook')
x.addKerning(left='v', right='r')
x.addMetrics(left='v', right='r')
x.addRecipe('v decompose', '_part.hook decompose')

x = ugi('vturned')
x.addKerning(left='vturned', right='vturned')
x.addRecipe('v flip_horizontal flip_vertical')
x.addRecipe('v')

x = ugi('w')
x.addKerning(left='v', right='v')
x.addMetrics(left='v', right='v')

x = ugi('wacute')
x.addKerning(left='v', right='v')
x.addMetrics(left='w', right='w')

x = ugi('wcircumflex')
x.addKerning(left='v', right='v')
x.addMetrics(left='w', right='w')

x = ugi('wdieresis')
x.addKerning(left='v', right='v')
x.addMetrics(left='w', right='w')

x = ugi('wgrave')
x.addKerning(left='v', right='v')
x.addMetrics(left='w', right='w')

x = ugi('wturned')
x.addKerning(left='vturned', right='vturned')
x.addRecipe('w flip_horizontal flip_vertical')

x = ugi('x')
x.addKerning(left='x', right='k')
x.addMetrics(left='x', right='x')

x = ugi('xdotaccent')
x.addMetrics(left='x', right='x')

x = ugi('y')
x.addAnchor('bottom', position_x=xpos.width_75, position_y=ypos.base_line)
x.addKerning(left='v', right='v', italic_left='y', italic_right='y')
x.addMetrics(left='v', right='v', italic_left='y', italic_right='y')

x = ugi('yacute')
x.addKerning(left='v', right='v', italic_left='y', italic_right='y')
x.addMetrics(left='y', right='y', italic_left='y', italic_right='y')

x = ugi('ycircumflex')
x.addKerning(left='v', right='v', italic_left='y', italic_right='y')
x.addMetrics(left='y', right='y', italic_left='y', italic_right='y')

x = ugi('ydieresis')
x.addKerning(left='v', right='v', italic_left='y', italic_right='y')
x.addMetrics(left='y', right='y', italic_left='y', italic_right='y')

x = ugi('ydotbelow')
x.addKerning(left='v', right='v', italic_left='y', italic_right='y')
x.addMetrics(left='y', width='y')

x = ugi('ygrave')
x.addKerning(left='v', right='v', italic_left='y', italic_right='y')
x.addMetrics(left='y', right='y', italic_left='y', italic_right='y')

x = ugi('yhookabove')
x.addKerning(left='v', right='v', italic_left='y', italic_right='y')
x.addMetrics(left='y', right='y', italic_left='y', italic_right='y')

x = ugi('ytilde')
x.addKerning(left='v', right='v', italic_left='y', italic_right='y')
x.addMetrics(left='y', right='y', italic_left='y', italic_right='y')

x = ugi('yturned')
x.addKerning(left='vturned', right='vturned')
x.addRecipe('y flip_horizontal flip_vertical')

x = ugi('z')
x.addKerning(left='z', right='z')
x.addMetrics(left='z', right='z')

x = ugi('zacute')
x.addKerning(left='z', right='z')
x.addMetrics(left='z', right='z')

x = ugi('zcaron')
x.addKerning(left='z', right='z')
x.addMetrics(left='z', right='z')

x = ugi('zcurl')
x.addKerning(left='z', right='zcurl')
x.addRecipe('z decompose', 'ccurl decompose')

x = ugi('zdotaccent')
x.addKerning(left='z', right='z')
x.addMetrics(left='z', right='z')

x = ugi('zretroflexhook')
x.addKerning(left='z', right='rhookturned')
x.addRecipe('z', '_part.hook flip_vertical')

x = ugi('zstroke')
x.addMetrics(left='z', right='z')

x = ugi('a.sc')
x.addAnchor('ogonek', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.smallcapHeight)

x = ugi('ae.sc')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.smallcapHeight)
x.addRecipe('a.sc decompose', 'e.sc decompose')
x.addBuildString('/A/AE/E/a.sc/ae.sc/e.sc')

x = ugi('dcroat.sc')
x.addRecipe('eth.sc')

x = ugi('e.sc')
x.addAnchor('bottom', position_x=xpos.outline_center, position_y=ypos.base_line)
x.addAnchor('ogonek', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)

x = ugi('eng.sc')
x.addRecipe('jdotless decompose', 'n.sc decompose')
x.addBuildString('/N/Eng/J/n.sc/eng.sc/j.sc')

x = ugi('f.sc')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)

x = ugi('g.salt.sc')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.outline_top)

x = ugi('g.sc')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.smallcapHeight)

x = ugi('germandbls.sc')
x.addRecipe('s.sc', 's.sc')

x = ugi('h.sc')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('#topleft', position_x=xpos.outline_left, position_y=ypos.smallcapHeight)
x.addAnchor('#topright', position_x=xpos.outline_right, position_y=ypos.smallcapHeight)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)
x.addAnchor('topleft', suppress_auto=True)

x = ugi('i.sc')
x.addAnchor('ogonek', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.smallcapHeight)

x = ugi('k.sc')
x.addAnchor('#bottomright', position_x=xpos.outline_right, position_y=ypos.base_line)
x.addAnchor('#topleft', position_x=xpos.outline_left, position_y=ypos.smallcapHeight)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)
x.addAnchor('topleft', suppress_auto=True)

x = ugi('napostrophe.sc')
x.addMetrics(left='quoteright', right='n.sc')

x = ugi('o.sc')
x.addAnchor('#center', position_x=xpos.outline_center, position_y=ypos.outline_middle)
x.addAnchor('center', suppress_auto=True)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)

x = ugi('oe.sc')
x.addRecipe('o.sc decompose', 'e.sc')
x.addBuildString('/O/OE/E/o.sc/oe.sc/e.sc')

x = ugi('t.sc')
x.addAnchor('bottom', position_x=xpos.outline_center, position_y=ypos.outline_bottom)
x.addAnchor('center', position_x=xpos.outline_center, position_y=ypos.outline_middle)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.outline_top)

x = ugi('tcedilla.sc')
x.addRecipe('t.sc', 'cedillacomb')

x = ugi('thorn.sc')
x.addRecipe('p.sc decompose', 'i.sc decompose')
x.addBuildString('/P/Thorn/thorn.sc/p.sc')

x = ugi('u.sc')
x.addAnchor('bottom', position_x=xpos.outline_center, position_y=ypos.base_line)
x.addAnchor('center', position_x=xpos.outline_center, position_y=ypos.outline_middle)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.outline_top)

x = ugi('y.sc')
x.addAnchor('#center', position_x=xpos.outline_center, position_y=ypos.outline_middle)
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.smallcapHeight)
x.addAnchor('topleft', position_x=xpos.outline_left, position_y=ypos.smallcapHeight)


#
# --------------------------------
#
#   Accents Marks
#
# --------------------------------
#

x = ugi('dotaccentcomb')
x.addRecipe('dieresiscomb decompose')

x = ugi('dieresisbelowcomb')
x.addRecipe('dieresiscomb accent_bottom')

x = ugi('brevebelowcomb')
x.addRecipe('brevecomb accent_bottom')

x = ugi('macronbelowcomb')
x.addRecipe('macroncomb accent_bottom')
