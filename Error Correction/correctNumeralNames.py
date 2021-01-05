# MenuTitle: Correct Numeral Names
# -*- coding: utf-8 -*-
__doc__ = """
Tries to make numeral suffixs into those used by Glyphs
"""

import re
Glyphs.clearLog()

num_suffixes = {}
num_suffixes['.osf'] = ['.onum', '.onumprop', '.oldstyle', '.ospnum', 'oldstyle']
num_suffixes['.tosf'] = ['.taboldstyle', '.ostnum']
num_suffixes['.tf'] = ['.tab', '.tnum']
num_suffixes['.lf'] = ['.prop', '.fitted']
num_suffixes['.sups'] = ['.superior', 'superior', '.superscript']
num_suffixes['.subs'] = ['.inferior', '.sinf', 'inferior', '.subscript']
num_suffixes['.dnom'] = ['.denominator', 'denominator']
num_suffixes['.numr'] = ['.numerator', 'numerator', '.nominator']
num_suffixes['.sc.lf'] = ['.scprop']


# Glyphs.clearLog()
# Glyphs.showMacroWindow()

Glyphs.font.disableUpdateInterface()

for g in Glyphs.font.glyphs:
    for suffix, oldsuffixes in num_suffixes.items():
        for oldsuffix in oldsuffixes:
            if re.search(re.escape(oldsuffix) + '$', g.name):
                try:
                    g.name = g.name[:-len(oldsuffix)] + suffix
                except NameError:
                    pass

Glyphs.font.enableUpdateInterface()
