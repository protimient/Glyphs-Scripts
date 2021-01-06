# MenuTitle: Report Widest Selected Glyph
Glyphs.clearLog()

widest = max([l for l in Glyphs.font.selectedLayers], key=lambda l: l.width)
print(widest.parent.name)
Glyphs.showMacroWindow()
# Glyphs.font.newTab(widest.parent.name)
