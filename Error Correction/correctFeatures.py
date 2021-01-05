# MenuTitle: Correct Opentype Features
from collections import defaultdict
__doc__ = """
Corrects the frac Opentype feature. Adds the Germandbls to the calt feature. Adds Greek casing to calt.
"""
Glyphs.clearLog()
# Glyphs.showMacroWindow()


def make_Toshi_frac(font):
    frac_code = """lookup FractionBar {
    ignore sub slash @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures slash';
    ignore sub slash' @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures slash;
    ignore sub slash @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures slash';
    ignore sub slash' @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures slash;
    ignore sub slash @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures slash';
    ignore sub slash' @figures @figures @figures @figures @figures @figures @figures @figures @figures @figures slash;
    ignore sub slash @figures @figures @figures @figures @figures @figures @figures @figures @figures slash';
    ignore sub slash' @figures @figures @figures @figures @figures @figures @figures @figures @figures slash;
    ignore sub slash @figures @figures @figures @figures @figures @figures @figures @figures slash';
    ignore sub slash' @figures @figures @figures @figures @figures @figures @figures @figures slash;
    ignore sub slash @figures @figures @figures @figures @figures @figures @figures slash';
    ignore sub slash' @figures @figures @figures @figures @figures @figures @figures slash;
    ignore sub slash @figures @figures @figures @figures @figures @figures slash';
    ignore sub slash' @figures @figures @figures @figures @figures @figures slash;
    ignore sub slash @figures @figures @figures @figures @figures slash';
    ignore sub slash' @figures @figures @figures @figures @figures slash;
    ignore sub slash @figures @figures @figures @figures slash';
    ignore sub slash' @figures @figures @figures @figures slash;
    ignore sub slash @figures @figures @figures slash';
    ignore sub slash' @figures @figures @figures slash;
    ignore sub slash @figures @figures slash';
    ignore sub slash' @figures @figures slash;
    ignore sub slash @figures slash';
    ignore sub slash' @figures slash;
    sub @figures slash' @figures by fraction;
} FractionBar;

lookup Numerator1 {
    sub @figures' fraction by @numr;
} Numerator1;

lookup Numerator2 {
    sub @figures' @numr fraction by @numr;
} Numerator2;

lookup Numerator3 {
    sub @figures' @numr @numr fraction by @numr;
} Numerator3;

lookup Numerator4 {
    sub @figures' @numr @numr @numr fraction by @numr;
} Numerator4;

lookup Numerator5 {
    sub @figures' @numr @numr @numr @numr fraction by @numr;
} Numerator5;

lookup Numerator6 {
    sub @figures' @numr @numr @numr @numr @numr fraction by @numr;
} Numerator6;

lookup Numerator7 {
    sub @figures' @numr @numr @numr @numr @numr @numr fraction by @numr;
} Numerator7;

lookup Numerator8 {
    sub @figures' @numr @numr @numr @numr @numr @numr @numr fraction by @numr;
} Numerator8;

lookup Numerator9 {
    sub @figures' @numr @numr @numr @numr @numr @numr @numr @numr fraction by @numr;
} Numerator9;

lookup Numerator10 {
    sub @figures' @numr @numr @numr @numr @numr @numr @numr @numr @numr fraction by @numr;
} Numerator10;

lookup Denominator {
    sub [fraction @dnom] @figures' by @dnom;
} Denominator;

"""

    space_frac_lookup = """lookup fraction_space {
	sub @figures space' by space.frac;
} fraction_space;
"""

    # ot_classes = {
    # 	'figures': 'zero one two three four five six seven eight nine',
    # 	'numr': 'zero.numr one.numr two.numr three.numr four.numr five.numr six.numr seven.numr eight.numr nine.numr',
    # 	'dnom': 'zero.dnom one.dnom two.dnom three.dnom four.dnom five.dnom six.dnom seven.dnom eight.dnom nine.dnom',
    # }

    if not font.glyphs['fraction']:
        return

    if font.glyphs['space.frac']:
        frac_code += space_frac_lookup

    numrs = [g.name for g in Glyphs.font.glyphs if g.name.endswith('.numr')]
    if len(numrs) < 10:
        return

    numr_class = ' '.join(numrs)
    dnom_class = ' '.join([gn.replace('.numr', '.dnom') for gn in numr_class.split(' ')])
    figures_class = ' '.join([gn.replace('.numr', '') for gn in numr_class.split(' ')])

    ot_classes = {
        'figures': figures_class,
        'numr': numr_class,
        'dnom': dnom_class,
    }

    for classs in ot_classes.values():
        if not all([Glyphs.font.glyphs[gn] for gn in classs.split(' ')]):
            return

    if font.glyphs['thinspace'] is not None:
        frac_code += "sub @figures space' @numr by thinspace;"

    for class_name, class_code in ot_classes.items():
        if font.classes[class_name] is not None:
            font.classes[class_name].code = class_code
        else:
            font.classes.append(GSClass(class_name, class_code))

    if font.features['frac'] is not None:
        font.features['frac'].code = frac_code
    else:
        try:
            dnom_i = [fea.name for fea in font.features].index('dnom') + 1
        except ValueError:
            dnom_i = len(font.features)
        font.features.insert(dnom_i, GSClass('frac', frac_code))

    font.features['frac'].automatic = False


def fix_subs(font):
    features = list(font.features)
    feature_names = [x.name for x in features]
    # Make both the subs and sinf features
    new_tag = False
    old_tag = False

    if 'subs' not in feature_names and 'sinf' in feature_names:
        new_tag = 'subs'
        old_tag = 'sinf'

    elif 'subs' in feature_names and 'sinf' not in feature_names:
        new_tag = 'sinf'
        old_tag = 'subs'

    elif 'subs' in feature_names and 'sinf' in feature_names:
        subs = [x for x in features if x.name == 'subs'][0].code
        sinf = [x for x in features if x.name == 'sinf'][0].code

        if len(subs) > len(sinf):
            new_tag = 'sinf'
            old_tag = 'subs'
        elif subs != sinf:
            new_tag = 'subs'
            old_tag = 'sinf'
        else:
            return font

    position = len(font.features)
    if new_tag and old_tag:
        new_feat = GSFeature(new_tag)
        new_feat.code = [x for x in features if x.name == old_tag][0].code
        position = feature_names.index(old_tag) + 1
        try:
            del features[[f.name for f in font.features].index(new_tag)]
        except KeyError:
            pass

        features.insert(position, new_feat)

    font.features = features

    return font


def make_non_letter_class(font):
    def is_ok(g):
        if not g.export:
            return False

        if g.category == 'Letter':
            return False

        if g.name in ['NULL']:
            return False

        return True

    gns = [g.name for g in font.glyphs if is_ok(g)]

    all_codes = defaultdict(list)
    for inst in font.instances:
        keep_glyphs = inst.customParameters['Keep Glyphs']
        remove_glyphs = inst.customParameters['Remove Glyphs']
        rename_glyphs = inst.customParameters['Rename Glyphs']

        glyphs_to_remove = set()
        glyphs_to_add = set()

        if keep_glyphs is not None:
            this_gns = set(gns)
            this_gns &= set(keep_glyphs)
        else:
            this_gns = set(gns)

        if remove_glyphs is not None:
            glyphs_to_remove |= set(remove_glyphs)

        if rename_glyphs is not None:
            rename_dict = dict(x.split('=') for x in rename_glyphs)
            glyphs_renamed_away = set(rename_dict.keys()) - set(rename_dict.values())
            glyphs_to_remove |= glyphs_renamed_away
            glyphs_to_add |= set(rename_dict.values()) - set(rename_dict.keys())

        this_gns |= glyphs_to_add
        this_gns -= glyphs_to_remove

        all_codes[tuple(this_gns)].append(inst)

    primary_code = max(all_codes.items(), key=lambda x: len(x[1]))[0]

    newClass = GSClass('NonLetter')
    newClass.code = ' '.join(primary_code)
    if font.classes[newClass.name] is not None:
        font.classes[newClass.name].code = newClass.code
    else:
        font.classes.append(newClass)

    for code, insts in all_codes.items():
        if code != primary_code:
            for inst in insts:
                inst.customParameters['Replace Class'] = 'NonLetter;{}'.format(' '.join(code))


def fix_Germandbls(font):
    if font.glyphs['1E9E'] is None or font.glyphs['00DF'] is None:
        return font

    if not font.features['case']:
        font.features.append(GSFeature('case'))

    case_feature = font.features['case']
    case_feature.automatic = False

    Germandbls_name = font.glyphs['1E9E'].name
    germandbls_name = font.glyphs['00DF'].name

    case_code = '\nlookup germandbls_case {{\n\tsub {germandbls_name} by {Germandbls_name};\n}} germandbls_case;'.format(
        germandbls_name=germandbls_name,
        Germandbls_name=Germandbls_name,
    )
    if 'lookup germandbls_case {' not in case_feature.code:
        case_feature.code += case_code

    case_feature.code = case_feature.code.strip()

    if not font.features['calt']:
        font.features.append(GSFeature('calt'))

    calt_feature = font.features['calt']
    calt_feature.automatic = False
    calt_code = '\nlookup germandbls_calt {{\n\tsub @Uppercase {germandbls_name}\' @Uppercase by {Germandbls_name};' \
        '\n\tsub @Uppercase @Uppercase {germandbls_name}\' by {Germandbls_name};\n}} germandbls_calt;'.format(
            germandbls_name=germandbls_name,
            Germandbls_name=Germandbls_name
        )
    if 'lookup germandbls_calt {' not in calt_feature.code:
        calt_feature.code += calt_code
    calt_feature.code = calt_feature.code.strip()

    if font.classes['Uppercase'] is None:
        uc_class = GSClass('Uppercase')
        uc_class.automatic = True
        font.classes.append(uc_class)
        font.classes['Uppercase'].update()
    return font


def make_greek_case(font):
    greek_all_class_members = [g.name for g in font.glyphs if g.script == 'greek' and g.category == 'Letter' and g.export]
    if not greek_all_class_members:
        print('No Greek letters in the font.')
        return
    greek_all_class = GSClass('greekAll', ' '.join(greek_all_class_members))

    greek_caps_class_members = [g.name for g in font.glyphs if g.script == 'greek' and g.category == 'Letter' and g.subCategory in ['Uppercase', 'Smallcaps'] and g.export]
    if not greek_caps_class_members:
        print('No Greek Uppercase or Smallcaps in the font.')
        return
    greek_caps_class = GSClass('greekCaps', ' '.join(greek_caps_class_members))

    greek_capstonos_to_less_map = dict((gn, gn.replace('tonos', '')) for gn in greek_caps_class_members if 'tonos' in gn)

    greek_capstonos_class_members = [gn for gn, gnless in greek_capstonos_to_less_map.items() if font.glyphs[gnless]]
    if not greek_capstonos_class_members:
        print('No Greek Uppercase or Smallcaps with tonos in the font.')
        return
    greek_capstonos_class = GSClass('greekCapsTonos', ' '.join(greek_capstonos_class_members))

    greek_capstonosless_class_members = [gnless for gnless in greek_capstonos_to_less_map.values() if font.glyphs[gnless]]
    if not greek_capstonosless_class_members:
        print('No Greek Uppercase or Smallcaps without tonos in the font.')
        return
    greek_capstonosless_class = GSClass('greekCapsTonosLess', ' '.join(greek_capstonosless_class_members))

    make_non_letter_class(font)
    for new_class in [greek_all_class, greek_caps_class, greek_capstonos_class, greek_capstonosless_class]:
        if font.classes[new_class.name] is not None:
            font.classes[new_class.name].code = new_class.code
        else:
            font.classes.append(new_class)

    calt_feature = font.features['calt']
    calt_feature.automatic = False

    calt_code = """

lookup greek_dieresisCapInsertion {
	sub [Alphatonos Epsilontonos Omicrontonos Upsilontonos] Iota' by Iotadieresis;
	sub [Alphatonos Epsilontonos Etatonos Omicrontonos Omegatonos] Upsilon' by Upsilondieresis;
} greek_dieresisCapInsertion;

lookup greek_tonosCap {
	# tonos supression of single-letter word
	sub @greekCapsTonos' @NonLetter @NonLetter @NonLetter @NonLetter @NonLetter @greekCaps by @greekCapsTonosLess;
	sub @greekCapsTonos' @NonLetter @NonLetter @NonLetter @NonLetter @greekCaps by @greekCapsTonosLess;
	sub @greekCapsTonos' @NonLetter @NonLetter @NonLetter @greekCaps by @greekCapsTonosLess;
	sub @greekCapsTonos' @NonLetter @NonLetter @greekCaps by @greekCapsTonosLess;
	sub @greekCapsTonos' @NonLetter @greekCaps by @greekCapsTonosLess;
	sub @greekCaps @NonLetter @NonLetter @NonLetter @NonLetter @NonLetter @greekCapsTonos' by @greekCapsTonosLess;
	sub @greekCaps @NonLetter @NonLetter @NonLetter @NonLetter @greekCapsTonos' by @greekCapsTonosLess;
	sub @greekCaps @NonLetter @NonLetter @NonLetter @greekCapsTonos' by @greekCapsTonosLess;
	sub @greekCaps @NonLetter @NonLetter @greekCapsTonos' by @greekCapsTonosLess;
	sub @greekCaps @NonLetter @greekCapsTonos' by @greekCapsTonosLess;
	# tonos supression within a word
	sub @greekCaps @greekCapsTonos' by @greekCapsTonosLess;
	sub @greekCapsTonos' @greekCaps by @greekCapsTonosLess;
} greek_tonosCap;

lookup greek_anoteleia {
	ignore sub @greekAll periodcentered' @greekAll;
	sub @greekAll periodcentered' by anoteleia;
} greek_anoteleia;
    """

    if 'lookup greek_dieresisCapInsertion {' not in calt_feature.code:
        calt_feature.code += calt_code
    calt_feature.code = calt_feature.code.strip()

    if any([font.glyphs[gn] for gn in 'alphatonos.sc epsilontonos.sc omicrontonos.sc upsilontonos.sc'.split(' ')]):
        smcp_feature = font.features['smcp']
        if smcp_feature is None:
            smcp_feature = GSFeature('smcp')
            font.features.append(smcp_feature)
        
        smcp_feature.automatic = False
        smcp_greek_code = """sub [alphatonos.sc epsilontonos.sc omicrontonos.sc upsilontonos.sc] iota.sc' by iotadieresis.sc;
sub [alphatonos.sc epsilontonos.sc etatonos.sc omicrontonos.sc omegatonos.sc] upsilon.sc' by upsilondieresis.sc;
sub @grekCapsTonos by @grekCapsTonosless;\n
"""
        if smcp_greek_code.strip() not in smcp_feature.code:
            smcp_feature.code = smcp_greek_code + smcp_feature.code


fix_subs(Glyphs.font)
make_Toshi_frac(Glyphs.font)
fix_Germandbls(Glyphs.font)
make_greek_case(Glyphs.font)
