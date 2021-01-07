# MenuTitle: Copy Anchors from Full form to Conjunct
# Author: Ben Jones
__doc__ = """
Copies the anchors from the last full form in the conjunct into the conjunct glyph.
Edit the script to control which anchors are copied.
"""

Glyphs.clearLog()
# Glyphs.showMacroWindow()


class copyAnchorsFullToConjunct:
    copyable_anchor_names = [
        'candra',
        'anusvara',
        'bottom',
        'top',
    ]

    def __init__(self):
        self.is_error = False

        for ls in Glyphs.font.selectedLayers:
            g = ls.parent

            last_conjunct_name = self.get_source_glyph_name(g.name)
            if last_conjunct_name is None:
                self.report('{} does not appear to be a conjunct.'.format(g.name))
                continue

            source_glyph = Glyphs.font.glyphs[last_conjunct_name]
            if source_glyph is None:
                self.report('Could not find the base glyph {} for {}'.format(last_conjunct_name, g.name))
                continue

            for l in g.layers:
                source_layer = source_glyph.layers[l.associatedMasterId]
                for aname in self.copyable_anchor_names:
                    source_a = source_layer.anchors[aname]
                    if source_a is None:
                        self.report('Could not find the {} anchor in the source layer {}'.format(aname, source_layer))
                        continue

                    pos_x = l.width - (source_layer.width - source_a.x)
                    pos_y = source_a.y

                    l.anchors[aname] = GSAnchor(aname, NSPoint(pos_x, pos_y))

        if self.is_error:
            Glyphs.showMacroWindow()

    def report(self, message):
        self.is_error = True
        print(message)

    @staticmethod
    def get_source_glyph_name(curent_glyph_name):
        if '_' not in curent_glyph_name:
            return

        curent_glyph_name = curent_glyph_name.partition('.')[0]
        split_names = curent_glyph_name.split('_')
        last_name = split_names[-1]
        if last_name == 'ra-deva':
            last_name = split_names[-2]
            if not last_name.endswith('a'):
                last_name += 'a'
            last_name += '-deva'

        return last_name


copyAnchorsFullToConjunct()
