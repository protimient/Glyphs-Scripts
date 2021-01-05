# MenuTitle: General Corrections
__doc__ = """
A suite of general corrections.
Tries to assign micro/mu etc.
Adds empty glyphs.
Sets standard metrics.
"""

Glyphs.clearLog()


class generalFix():
    def __init__(self):
        self.glyph_info = {}
        self.glyph_info['03BC'] = 'mu'
        self.glyph_info['03A9'] = 'Omega'
        self.glyph_info['0394'] = 'Delta'
        self.glyph_info['2206'] = 'increment'
        self.glyph_info['2126'] = 'Ohm'
        self.glyph_info['00B5'] = 'micro'

        # Glyphs.clearLog()
        Glyphs.font.disableUpdateInterface()

        # self.fixMuOmegaDelta()

        self.fixNoWidthSpaces()

        self.fixEmptyGlyph('NULL', '0000', width=0)
        self.fixEmptyGlyph('CR', '000D', width_key='space')
        self.fixEmptyGlyph('nbspace', '00A0', width_key='space')
        self.fixEmptyGlyph('uniFEFF', 'FEFF', width=0)

        # self.fixTcedilla()

        if not Glyphs.font.glyphs['napostrophe']:
            self.fixNapostrophe()

        self.fixSofthyphen()

        # for gn in ['i', 'j']:
        # 	if len(Glyphs.font.glyphs[gn].layers[0].components) > 1:
        # 		self.glyphDecompose(gn)

        if Glyphs.font.glyphs['apple']:
            Glyphs.font.removeGlyph_(Glyphs.font.glyphs['apple'])

        self.setTrueTypeCurveError()
        self.setGASPtable()

        if Glyphs.font.upm != 1000:
            print('The upm is {0}!'.format(Glyphs.font.upm))
            Glyphs.showMacroWindow()

        Glyphs.font.enableUpdateInterface()
        self.check_for_quadratic_outlines()

    def check_for_quadratic_outlines(self):
        affected_layers = []
        for g in Glyphs.font.glyphs:
            for l in g.layers:
                for p in l.paths:
                    if l in affected_layers:
                        break
                    for n in p.nodes:
                        if n.type == QCURVE:
                            l.selection = [n]
                            affected_layers.append(l)
                            break

        if affected_layers:
            if not Glyphs.font.tabs:
                Glyphs.font.newTab()

            Glyphs.font.tabs[0].layers = affected_layers
            Glyphs.showNotification('Quadratic Curves Found', 'There were Quadratic Curves found in some layers. They have been opened in a new tab.')
            print('Quadratic Curves Found', 'There were Quadratic Curves found in some layers. They have been opened in a new tab.')

    def fixMuOmegaDelta(self):
        for uni, gn in self.glyph_info.items():
            g = Glyphs.font.glyphs[uni]
            if g is None:
                g = Glyphs.font.glyphs[gn]

            if g is not None:
                g.unicode = uni
                g.name = gn
                g.export = True

        glyph_pairs = []
        glyph_pairs.append(('00B5', '03BC'))
        glyph_pairs.append(('2126', '03A9'))
        glyph_pairs.append(('2206', '0394'))

        for pair in glyph_pairs:
            target_uni, source_uni = pair
            self.addMissing(target_uni, source_uni)
            source_uni, target_uni = pair
            self.addMissing(target_uni, source_uni)

    def addMissing(self, target_uni, source_uni):
        target_g = Glyphs.font.glyphs[target_uni]
        source_g = Glyphs.font.glyphs[source_uni]
        if source_g is not None and target_g is None:
            print(source_g, target_g)
            new_g = GSGlyph(self.glyph_info[target_uni])
            Glyphs.font.glyphs.append(new_g)

            for m in Glyphs.font.masters:
                new_layer = GSLayer()
                new_layer.associatedMasterId = m.id
                new_layer.width = source_g.layers[m.id].width
                new_g.layers[m.id] = new_layer

                new_layer.components.append(GSComponent(source_g.name))

            new_g.updateGlyphInfo()

    def fixEmptyGlyph(self, gname, gunicode, **kwargs):
        gwidthkey = kwargs.get('width_key')
        gwidth = kwargs.get('width', 0)

        g = Glyphs.font.glyphs[gunicode]
        if g is not None:
            del Glyphs.font.glyphs[g.name]

        g = Glyphs.font.glyphs[gname]
        if g is not None:
            del Glyphs.font.glyphs[g.name]

        newG = GSGlyph(gname)
        newG.unicode = gunicode
        newG.updateGlyphInfo()
        Glyphs.font.glyphs.append(newG)
        if gwidthkey is not None and Glyphs.font.glyphs[gwidthkey] is not None:
            newG.widthMetricsKey = gwidthkey
            for l in newG.layers:
                l.syncMetrics()
        else:
            for l in newG.layers:
                l.width = gwidth

    def fixNoWidthSpaces(self):
        # Correct NULL name or add it if not present
        for gname in ['null', '.null']:
            gnull = Glyphs.font.glyphs[gname]
            if gnull:
                del Glyphs.font.glyphs[gname]

        for g in [Glyphs.font.glyphs[gu] for gu in ['200B', '200C', '200D']]:
            if g is not None:
                for l in g.layers:
                    l.width = 0

    def fixSofthyphen(self):
        keyGlyph = Glyphs.font.glyphForUnicode_('002D')
        others = {
            'softhyphen': '00AD',
            'nonbreakinghyphen': '2011',
        }

        if keyGlyph:
            for gn, gu in others.iteritems():
                g = Glyphs.font.glyphForUnicode_(gu)
                if not g:
                    g = Glyphs.font.glyphForName_(gn)

                if g:
                    g.setUnicode_(gu)
                    for l in g.layers:
                        if not l.paths and l.components:
                            for c in l.components:
                                c.disableAlignment = False
                        else:
                            l.LSB = keyGlyph.layers[l.layerId].LSB
                            l.width = keyGlyph.layers[l.layerId].width
                else:
                    newG = GSGlyph(gn)
                    newG.leftKerningGroup = keyGlyph.leftKerningGroup
                    newG.rightKerningGroup = keyGlyph.rightKerningGroup
                    Glyphs.font.glyphs.append(newG)

                    for m in Glyphs.font.masters:
                        new_layer = GSLayer()
                        new_layer.associatedMasterId = m.id
                        newG.layers[m.id] = new_layer

                        new_component = GSComponent(keyGlyph.name)
                        new_layer.components.append(new_component)
                        new_component.automaticAlignment = True

                    newG.updateGlyphInfo()

    def fixTcedilla(self):
        # Replace all tcedilla varients with the same components as in tcommaaccent
        allTcommaaccents = [g for g in Glyphs.font.glyphs if 'tcommaaccent' in g.name.lower()]
        allTcedillas = [g for g in Glyphs.font.glyphs if 'tcedilla' in g.name.lower()]

        for gi, g in enumerate(allTcommaaccents):
            if [x.name for x in allTcommaaccents].count(g.name) > 1:
                del allTcommaaccents[gi]
                g.name = g.name + '.001'
                Glyphs.font.removeGlyph_(g)

        for gi, g in enumerate(allTcedillas):
            if [x.name for x in allTcedillas].count(g.name) > 1:
                del allTcedillas[gi]
                g.name = g.name + '.001'
                Glyphs.font.removeGlyph_(g)
            else:
                if g.name.replace('cedilla', 'commaaccent') not in [x.name for x in allTcommaaccents]:
                    g.name = g.name.replace('cedilla', 'commaaccent')
                    allTcommaaccents.append(g)
                    del allTcedillas[gi]

        for g in allTcedillas:
            Glyphs.font.removeGlyph_(g)

        for g in allTcommaaccents:
            newG = GSGlyph(g.name.replace('commaaccent', 'cedilla'))
            newG.export = g.export
            for l in g.layers:
                newLayer = GSLayer()
                newLayer.associatedMasterId = l.layerId
                newLayer.width = l.width
                if l.components:
                    for c in l.components:
                        newLayer.components.append(c)
                else:
                    newLayer.components.append(GSComponent(g.name))
                newG.layers[l.layerId] = newLayer

            newG.updateGlyphInfo()
            Glyphs.font.addGlyph_(newG)

    def fixNapostrophe(self):
        # Fix napostrophe
        if Glyphs.font.glyphs['napostrophe']:
            del Glyphs.font.glyphs['napostrophe']

            newNapostrope = GSGlyph('napostrophe')
            for m in Glyphs.font.masters:
                newLayer = GSLayer()
                newLayer.associatedMasterId = m.id
                newLayer.components.append(GSComponent('n'))
                newLayer.width = Glyphs.font.glyphs['n'].layers[m.id].width

                quote = GSComponent('quoteright')
                quote.x = -(Glyphs.font.glyphs['quoteright'].layers[m.id].bounds.size.width + Glyphs.font.glyphs['quoteright'].layers[m.id].bounds.origin.x)
                newLayer.components.append(quote)

                newNapostrope.layers[m.id] = newLayer

            newNapostrope.updateGlyphInfo()
            Glyphs.font.addGlyph_(newNapostrope)

    def fix_comb_accents(self):
        for g in [x for x in Glyphs.font.glyphs if x.subCategory == 'Nonspacing']:
            self.make_zerowidth(g)

    def make_zerowidth(self, g):
        for l in g.layers:
            l.width = 0
            relocation = (l.LSB * -1) - (l.bounds.size.width / 2)
            l.applyTransform((1, 0, 0, 1, relocation, 0))

    def glyphDecompose(self, glyphName):
        g = Glyphs.font.glyphs[glyphName]
        if g:
            for l in g.layers:
                for ci in reversed(range(len(l.components))):
                    c = l.components[ci]
                    c.decompose()

    def setTrueTypeCurveError(self):
        for inst in Glyphs.font.instances:
            inst.customParameters['TrueType Curve Error'] = 0.3

    def setGASPtable(self):
        for inst in Glyphs.font.instances:
            inst.customParameters['GASP Table'] = ''


generalFix()


print('Done.')
