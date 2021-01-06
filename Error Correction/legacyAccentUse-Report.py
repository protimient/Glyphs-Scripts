# MenuTitle: Report Legacy Accent Usage

__doc__ = """
Shows glyphs that are using the old, legacy accents instead of combining marks.
"""

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

unicodes = [
    '00B4', 	# acute
    '02D8', 	# breve
    '02C7', 	# caron
    '00B8', 	# cedilla
    '02C6', 	# circumflex
    '00A8', 	# dieresis
    '02D9', 	# dotaccent
    '02DD', 	# hungarumlaut
    '00AF', 	# macron
    '02DB', 	# ogonek
    '02DA', 	# ring
    '02DC', 	# tilde
]

legacy_glyphs = [Glyphs.font.glyphs[gu] for gu in unicodes if Glyphs.font.glyphs[gu]]

affected_layers = []
for g in Glyphs.font.glyphs:
    for l in g.layers:
        for c in l.components:
            if c.component in legacy_glyphs:
                affected_layers.append(l)

if affected_layers:
    Glyphs.font.newTab()
    Glyphs.font.tabs[-1].layers = affected_layers
else:
    Glyphs.showNotification('Legacy Accents', 'All good. No legacy accents are being used.')
    print('Legacy Accents', 'All good. No legacy accents are being used.')
