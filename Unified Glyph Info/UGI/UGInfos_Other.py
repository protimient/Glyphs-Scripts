# -*- coding: utf-8 -*-

from .unifiedglyphinfo import CollectedGlyphInfos, xpos, ypos


def collect_infos(infos_dict):
    return infos_dict.update(ugi.unified_infos)


ugi = CollectedGlyphInfos()

x = ugi('dottedCircle')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addAnchor('bottom', position_x=xpos.outline_center, position_y=ypos.base_line)

x = ugi('underscore')
x.addRecipe('endash disable_alignment')

x = ugi('endash')
x.addKerning(left='hyphen', right='hyphen')

x = ugi('emdash')
x.addKerning(left='hyphen', right='hyphen')

x = ugi('overline')
x.addRecipe('endash disable_alignment')
x.addBuildString('/d/overline/h')
x.addMetrics(left='endash', right='endash')

x = ugi('underscoredbl')
x.addRecipe('underscore', 'underscore disable_alignment')
x.addBuildString('/n/underscoredbl/h')
x.addMetrics(left='endash', right='endash')

x = ugi('exclamdouble')
x.addMetrics(left='exclam', right='exclam')

x = ugi('apple')
x.addRecipe('.notdef')

x = ugi('micro')
x.addRecipe('u decompose', '_part.stem')

x = ugi('mu')
x.addRecipe('micro')

x = ugi('percent')
x.addRecipe('zero.numr', 'fraction', 'zero.dnom')

x = ugi('perthousand')
x.addRecipe('zero.numr', 'fraction', 'zero.dnom', 'zero.dnom')

x = ugi('onehalf')
x.addRecipe('one.numerator', 'fraction', 'two.denominator')

x = ugi('onequarter')
x.addRecipe('one.numerator', 'fraction', 'four.denominator')

x = ugi('threequarters')
x.addRecipe('three.numerator', 'fraction', 'four.denominator')

x = ugi('integral')
x.addRecipe('f decompose')

x = ugi('approxequal')
x.addRecipe('asciitilde', 'asciitilde')

x = ugi('minute')
x.addRecipe('quotesingle')

x = ugi('second')
x.addRecipe('minute', 'minute')

x = ugi('pi')
x.addRecipe('n', 't decompose', 't decompose')

x = ugi('increment')
x.addRecipe('A decompose')

x = ugi('Ohm')
x.addRecipe('O', 'two decompose')

x = ugi('lessequal')
x.addRecipe('less', 'minus')

x = ugi('summation')
x.addRecipe('Z decompose')

x = ugi('greaterequal')
x.addRecipe('greater', 'minus')

x = ugi('lozenge')
x.addRecipe('asciicircum decompose', 'asciicircum decompose')

x = ugi('product')
x.addRecipe('H decompose')

x = ugi('partialdiff')
x.addRecipe('eth decompose')

x = ugi('radical')
x.addRecipe('v decompose', 'slash decompose', 'macroncomb decompose')

x = ugi('exclam')
x.addRecipe('period', '_part.stem')

x = ugi('interrobang')
x.addRecipe('exclam decompose', 'question decompose')

x = ugi('at')
x.addRecipe('a', 'copyright decompose')

x = ugi('divisionslash')
x.addRecipe('slash')

x = ugi('firsttonechinese')
x.addRecipe('macron')

x = ugi('periodcentered')
x.addRecipe('period')

x = ugi('periodcentered.loclCAT')
x.addRecipe('periodcentered')

x = ugi('exclamdown')
x.addRecipe('exclam flip_vertical')

x = ugi('quotedbl')
x.addRecipe('quotesingle', 'quotesingle')

x = ugi('backslash')
x.addRecipe('slash flip_horizontal')

x = ugi('backslash.sc')
x.addRecipe('slash.sc flip_horizontal')

x = ugi('braceright')
x.addRecipe('braceleft flip_horizontal')
x.addKerning(left='parenright', right='parenright')

x = ugi('braceleft')
x.addKerning(left='parenleft', right='parenleft')

x = ugi('braceright.sc')
x.addRecipe('braceleft.sc flip_horizontal flip_vertical')

x = ugi('bracketright')
x.addRecipe('bracketleft flip_horizontal flip_vertical')
x.addKerning(left='parenright', right='parenright')

x = ugi('bracketleft')
x.addKerning(left='parenleft', right='parenleft')

x = ugi('bracketright.sc')
x.addRecipe('bracketleft.sc flip_horizontal flip_vertical')

x = ugi('quoteleft')
x.addRecipe('quoteright flip_horizontal flip_vertical')
x.addKerning(left='quotedblright', right='quotedblleft')

x = ugi('quoteright')
x.addKerning(left='quotedblright', right='quotedblleft')

x = ugi('quotedblright')
x.addRecipe('quoteright', 'quoteright')
x.addKerning(left='quotedblright', right='quotedblleft')

x = ugi('quotedblleft')
x.addRecipe('quotedblright flip_horizontal flip_vertical')
x.addKerning(left='quotedblright', right='quotedblleft')

x = ugi('quotedblbase')
x.addRecipe('quotedblright')
x.addKerning(left='quotedblbase', right='quotedblbase')

x = ugi('quotesinglbase')
x.addRecipe('quoteright')
x.addKerning(left='quotedblbase', right='quotedblbase')

x = ugi('quotereversed')
x.addRecipe('quoteright flip_horizontal')
x.addKerning(left='quotedblright', right='quotedblleft')

x = ugi('quotedblrightreversed')
x.addRecipe('quotedblright flip_horizontal decompose', italic=True)
x.addRecipe('quotedblright flip_horizontal')
x.addKerning(left='quotedblright', right='quotedblleft')

x = ugi('guillemetleft')
x.addKerning(left='guillemetleft', right='guillemetleft')
x.addMetrics(left='guillemetleft', right='guillemetleft')

x = ugi('guillemetright')
x.addKerning(left='guillemetright', right='guillemetright')
x.addMetrics(left='=|guillemetleft', right='=|guillemetleft')

x = ugi('guilsinglleft')
x.addKerning(left='guillemetleft', right='guillemetleft')
x.addMetrics(left='guillemetleft', right='guillemetleft')

x = ugi('guilsinglright')
x.addKerning(left='guillemetright', right='guillemetright')
x.addMetrics(left='=|guillemetleft', right='=|guillemetleft')

x = ugi('question')
x.addRecipe('period', 'two decompose')

x = ugi('ellipsis')
x.addKerning(left='period', right='period')

x = ugi('questiondown')
x.addRecipe('question flip_vertical flip_horizontal')

x = ugi('dagger')
x.addRecipe('plus decompose')

x = ugi('daggerdbl')
x.addRecipe('dagger decompose')

x = ugi('plusminus')
x.addRecipe('plus', 'minus')

x = ugi('logicalnot')
x.addRecipe('plus decompose')

x = ugi('asciitilde')
x.addRecipe('tilde decompose')

x = ugi('parenright')
x.addRecipe('parenleft flip_horizontal flip_vertical')
x.addKerning(left='parenright', right='parenright')

x = ugi('parenleft')
x.addKerning(left='parenleft', right='parenleft')

x = ugi('parenright.sc')
x.addRecipe('parenleft.sc flip_horizontal flip_vertical')

x = ugi('parenright.tf')
x.addRecipe('parenleft.tf flip_horizontal')

x = ugi('parenright.numr')
x.addRecipe('parenleft.numr flip_horizontal')

x = ugi('parenright.dnom')
x.addRecipe('parenleft.dnom flip_horizontal')

x = ugi('parenleft.sups')
x.addRecipe('parenleft.subs')

x = ugi('parenright.sups')
x.addRecipe('parenleft.sups flip_horizontal flip_vertical')

x = ugi('parenright-ar')
x.addRecipe('parenleft-ar flip_horizontal')

x = ugi('greater')
x.addRecipe('less flip_horizontal')

x = ugi('plus.subs')
x.addRecipe('plus.sups')

x = ugi('minus.subs')
x.addRecipe('minus.sups')

x = ugi('equal.subs')
x.addRecipe('equal.sups')

x = ugi('parenleft.subs')
x.addRecipe('parenleft.sups')

x = ugi('parenright.subs')
x.addRecipe('parenleft.subs flip_horizontal flip_vertical')

x = ugi('parenright.subs')
x.addRecipe('parenright.sups')

x = ugi('hyphen')
x.addKerning(left='hyphen', right='hyphen')  # hyphen

x = ugi('nonbreakinghyphen')
x.addRecipe('hyphen')
x.addKerning(left='hyphen', right='hyphen')  # nonbreakinghyphen

x = ugi('softhyphen')
x.addRecipe('hyphen')
x.addKerning(left='hyphen', right='hyphen')  # nonbreakinghyphen

x = ugi('hyphentwo')
x.addRecipe('hyphen')
x.addKerning(left='hyphen', right='hyphen')  # nonbreakinghyphen

x = ugi('published')
x.addRecipe('copyright decompose', 'p.sc decompose')

x = ugi('overline')
x.addRecipe('underscore')

x = ugi('underscoredbl')
x.addRecipe('underscore', 'underscore')

x = ugi('apostrophemod')
x.addRecipe('quoteright')

x = ugi('quotereversed')
x.addRecipe('quoteright flip_horizontal')

x = ugi('colon')
x.addRecipe('period', 'period')

x = ugi('semicolon')
x.addRecipe('period', 'comma')

x = ugi('upArrow')
x.addRecipe('rightArrow rotate_270')

x = ugi('downArrow')
x.addRecipe('upArrow flip_vertical')

x = ugi('leftArrow')
x.addRecipe('rightArrow flip_horizontal')

x = ugi('southEastArrow')
x.addRecipe('northEastArrow flip_vertical')

x = ugi('northWestArrow')
x.addRecipe('northEastArrow flip_horizontal')

x = ugi('southWestArrow')
x.addRecipe('northEastArrow flip_horizontal flip_vertical')

x = ugi('leftRightArrow')
x.addRecipe('rightArrow disable_alignment', 'leftArrow disable_alignment')

x = ugi('upDownArrow')
x.addRecipe('upArrow disable_alignment', 'downArrow disable_alignment')

#
# --------------------------------
#
#   Currency
#
# --------------------------------
#

x = ugi('baht')
x.addRecipe('B', '_part.stem')
x.addRecipe('B', 'bar')
x.addRecipe('B', 'dollar decompose')

x = ugi('bitcoin')
x.addRecipe('B', 'dollar decompose')

x = ugi('cedi')
x.addRecipe('C', '_part.stem')
x.addRecipe('C', 'bar')
x.addRecipe('C', 'dollar decompose')

x = ugi('cent')
x.addRecipe('c', '_part.stem')
x.addRecipe('c', 'bar')

x = ugi('colonsign')
x.addRecipe('C', 'slash', 'slash')

x = ugi('currency')
x.addRecipe('o decompose', 'multiply decompose')

x = ugi('dollar')
x.addRecipe('S', '_part.stem')
x.addRecipe('S', 'bar')

x = ugi('dong')
x.addRecipe('dcroat', '_part.bar')
x.addRecipe('dcroat', 'underscore')

x = ugi('euro')
x.addRecipe('C decompose', 'equal decompose')

x = ugi('florin')
x.addRecipe('_part.bar disable_alignment', 'integral')
x.addRecipe('integral', 'f decompose')

x = ugi('franc')
x.addRecipe('F', '_part.bar')
x.addRecipe('F', 'minus')

x = ugi('guarani')
x.addRecipe('G', '_part.stem')
x.addRecipe('G', 'bar')
x.addRecipe('G', 'dollar decompose')

x = ugi('hryvnia')
x.addRecipe('S flip_horizontal decompose', 'lira decompose')
x.addBuildString('/dollar/euro/hryvnia/lira')

x = ugi('kip')
x.addRecipe('C', '_part.stem')
x.addRecipe('K', '_part.bar')

x = ugi('lira')
x.addRecipe('sterling decompose')

x = ugi('liraTurkish')
x.addRecipe('Ech-arm decompose', 'I decompose', 'euro decompose')
x.addRecipe('L decompose', 'equal decompose')
x.addRecipe('L decompose', 'euro decompose')

x = ugi('manat')
x.addRecipe('I decompose', 'Germandbls decompose')
x.addRecipe('I', 'sterling decompose')

x = ugi('naira')
x.addRecipe('N', 'lira decompose')

x = ugi('peseta')
x.addRecipe('P', 't', 's')

x = ugi('peso')
x.addRecipe('P', 'lira decompose')

x = ugi('ruble')
x.addRecipe('_part.bar disable_alignment', 'P decompose')
x.addRecipe('macroncomb decompose', 'P decompose')

x = ugi('rupeeIndian')
x.addRecipe('R decompose', 'sterling decompose')

x = ugi('tenge')
x.addRecipe('equal decompose', 'T decompose')
x.addRecipe('T decompose', '_part.bar')

x = ugi('tugrik')
x.addRecipe('T', 'liraTurkish decompose')

x = ugi('won')
x.addRecipe('W', '_part.bar')

x = ugi('yen')
x.addRecipe('Y decompose', 'equal decompose')
