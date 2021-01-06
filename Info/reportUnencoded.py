# MenuTitle: Report Unencoded, Unfeatured glyphs
# -*- coding: utf-8 -*-
__doc__ = """
Colours red and opens a tab with any unencoded glyph not used as a component or included in an Opentype feature.
"""
Glyphs.clearLog()
Glyphs.showMacroWindow()


def get_removable_glyphs():
    removeable_glyphs = set()
    for inst in Glyphs.font.instances:
        if inst.customParameters['Remove Glyphs']:
            removeable_glyphs |= set(inst.customParameters['Remove Glyphs'])

    return removeable_glyphs


def get_feature_code():
    all_feature_code_lines = '\n'.join([f.code for f in Glyphs.font.features]).split('\n')
    for li in reversed(range(len(all_feature_code_lines))):
        line = all_feature_code_lines[li].strip()

        if not line:
            del all_feature_code_lines[li]

        else:
            verboten = [
                '#',
                '}',
                'lookup',
                'script',
                'feature',
            ]
            for v in verboten:
                if line.startswith(v):
                    del all_feature_code_lines[li]

    return '\n'.join(all_feature_code_lines)


def get_is_component():
    is_component = set()
    for g in Glyphs.font.glyphs:
        for l in g.layers:
            for c in l.components:
                is_component.add(c.name)

    return is_component


feature_code = get_feature_code()
removeable_glyphs = get_removable_glyphs()
is_a_component = get_is_component()


def is_eligable(g):
    if g.name in feature_code:
        return False

    if g.name in removeable_glyphs:
        return False

    if not g.export:
        return False

    if g.unicode is not None:
        return False

    if g.name in is_a_component:
        return False

    return True


def get_unencoded_unfeatured():
    return [g for g in Glyphs.font.glyphs if is_eligable(g)]


affected_glyphs = get_unencoded_unfeatured()
for g in affected_glyphs:
    g.color = 0
string = '  '.join(['/' + g.name for g in affected_glyphs])
Glyphs.font.newTab(string)
