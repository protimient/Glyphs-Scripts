# MenuTitle: Make Metrics Display
# -*- coding: utf-8 -*-
__doc__ = """
Opens a tab containing Metrics strings for the selected glyphs.
"""

import re

Glyphs.clearLog()
# Glyphs.showMacroWindow()

patterns = {}

patterns['latin'] = {}

patterns['latin']['key'] = 'nnnnn\nnnoonn\nnonon\nno\nHnnHdpd\nOnnOdpd\nHHHHH\nHHOOHH\nHOHOH'
patterns['latin']['Uppercase'] = '/{gn} nod /{gn} dni  HH/{gn} HH OO/{gn} OO /{gn}   '
patterns['latin']['Smallcaps'] = '/d.sc/h.sc/h.sc/{gn}/h.sc/h.sc/o.sc/  /h.sc/o.sc/o.sc/{gn}/o.sc/o.sc/h.sc  /{gn}  '
patterns['latin']['Lowercase'] = 'dnn/{gn} nno  hoo/{gn} ooh  /{gn}   '

patterns['greek'] = {}
patterns['greek']['key'] = '/omicron/gamma/alpha/space/mu/gamma/eta/space/eta/gamma/mu/space/gamma/gamma/gamma/space/gamma/\n/omicron/eta/alpha/space/mu/eta/eta/space/eta/eta/mu/space/gamma/eta/gamma/space/eta/\n/omicron/mu/alpha/space/mu/mu/eta/space/eta/mu/mu/space/gamma/mu/gamma/space/mu/\n/omicron/omicron/alpha/space/mu/omicron/eta/space/eta/omicron/mu/space/gamma/omicron/gamma/space/omicron'  # NoQA: E501
patterns['greek']['Uppercase'] = '/{gn}/eta/alpha/delta/space/{gn}/omicron/kappa/iota/space/Eta/Eta/{gn}/Eta/Eta/space/Omicron/Omicron/{gn}/Omicron/Omicron/space/{gn}'
patterns['greek']['Smallcaps'] = '/eta.sc/eta.sc/{gn}/eta.sc/eta.sc  /omicron.sc/omicron.sc/{gn}/omicron.sc/omicron.sc  /{gn}'
patterns['greek']['Lowercase'] = '/omicron/{gn}/alpha/space/mu/{gn}/eta/space/eta/{gn}/mu/space/gamma/{gn}/gamma/space/{gn}'

patterns['cyrillic'] = {}
patterns['cyrillic']['Uppercase'] = '/Ie-cy/En-cy/{gn}/Ie-cy/En-cy/space/Ve-cy/O-cy/{gn}/O-cy/Ve-cy/space/{gn}/en-cy/er-cy/en-cy/space/space/{gn}/a-cy/ie-cy/a-cy/space/space/{gn}'
patterns['cyrillic']['Smallcaps'] = '/ie-cy.sc/en-cy.sc/{gn}/ie-cy.sc/en-cy.sc/space/ve-cy.sc/o-cy.sc/{gn}/o-cy.sc/ve-cy.sc/space/{gn}'
patterns['cyrillic']['Lowercase'] = '/en-cy/ii-cy/en-cy/{gn}/en-cy/ii-cy/en-cy  /o-cy/a-cy/o-cy/{gn}/o-cy/a-cy/o-cy  /{gn}'

patterns['armenian'] = {}
patterns['armenian']['key'] = '/vo-arm/vo-arm/ayb-arm/vo-arm/vo-arm/space/space/ayb-arm/ayb-arm/vo-arm/ayb-arm/ayb-arm'
patterns['armenian']['Uppercase'] = '/Vo-arm/Vo-arm/{gn}/Vo-arm/Vo-arm/space/Seh-arm/Seh-arm/{gn}/Seh-arm/Seh-arm/space/{gn}/vo-arm/gim-arm/zhe-arm/space/{gn}/gim-arm/ini-arm/ayb-arm/space/{gn}  '
patterns['armenian']['Smallcaps'] = '/vo-arm.sc/vo-arm.sc/{gn}/vo-arm.sc/vo-arm.sc/space/seh-arm.sc/seh-arm.sc/{gn}/seh-arm.sc/seh-arm.sc/space/space/{gn}  '
patterns['armenian']['Lowercase'] = '/vo-arm/vo-arm/{gn}/vo-arm/vo-arm   /ayb-arm/ayb-arm/{gn}/ayb-arm/ayb-arm  /{gn}  '

patterns['arabic'] = {}
patterns['arabic']['Other'] = '/alef-ar/{gn}/alef-ar/seen-ar  /{gn}  '


patterns[None] = {}
patterns[None]['Currency'] = '0/{gn} 0 123/{gn} 678 792/{gn} 526 /{gn}  '
patterns[None]['Decimal Digit'] = '/two{suffix}/zero{suffix}/{gn} /zero{suffix}/eight{suffix} /nine{suffix}/seven{suffix}/{gn} /two{suffix}/five{suffix} /two{suffix}/eight{suffix}/{gn} /seven{suffix}/four{suffix} /{gn}/{gn}/{gn} /eight{suffix}/eight{suffix}/eight{suffix}/one{suffix}/one{suffix}/one{suffix} /{gn}  '  # NoQA: E501


def isAuto(g):
    if g:
        return all([l.hasAlignedWidth() for l in g.layers])

    return False


metricsKeys = set()
for gn in [x.parent.name for x in Glyphs.font.selectedLayers if x.parent.export]:
    g = Glyphs.font.glyphs[gn]

    lmk = g.leftMetricsKey

    if lmk:
        lmk = lmk[re.search(r'\w+', lmk).start():]
    else:
        lmk = g.name

    if isAuto(Glyphs.font.glyphs[lmk]) or re.match(r'^\d+$', lmk):
        lmk = None

    if lmk:
        metricsKeys.add(lmk)

    rmk = g.rightMetricsKey
    if rmk:
        rmk = rmk[re.search(r'\w+', rmk).start():]
    else:
        rmk = g.name

    if isAuto(Glyphs.font.glyphs[rmk]) or re.match(r'^\d+$', rmk):
        rmk = None

    if rmk:
        metricsKeys.add(rmk)

try:
    strings = [patterns[Glyphs.font.selectedLayers[0].parent.script]['key']]
except KeyError:
    strings = []

metricsKeys = list(metricsKeys)
try:
    metricsKeys.sort(key=lambda x: Glyphs.font.glyphs[x].unicode)
except AttributeError:
    pass

try:
    metricsKeys.sort(key=lambda x: Glyphs.font.glyphs[x].subCategory)
except AttributeError:
    pass

numeral_suffixes = [
    '.sups', '.superior', 'superior',
    '.subs', '.inferior', '.sinf', 'inferior',
    '.dnom', '.denominator', 'denominator',
    '.numr', '.numerator', 'numerator', '.nominator',
]


def get_subcategory(g):
    suffix = g.name.partition('.')
    g_subCategory = g.subCategory

    if suffix in numeral_suffixes:
        g_subCategory = 'Decimal Digit'

    if g.category == 'Symbol' and g.subCategory == 'Math':
        g_subCategory = 'Decimal Digit'

    return g_subCategory, suffix


for gn in metricsKeys:
    g = Glyphs.font.glyphs[gn]
    if g:
        try:
            g_subCategory, suffix = get_subcategory(g)
            pattern = patterns[g.script][g_subCategory]
        except KeyError:
            pattern = patterns['latin']['Lowercase']

        strings.append(pattern.format(gn=g.name, suffix=suffix))


Glyphs.font.newTab('\n'.join(strings))


print('Done.')
