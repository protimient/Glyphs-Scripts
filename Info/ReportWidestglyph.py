# MenuTitle: Report Widest Selected Glyph
Glyphs.clearLog()

widest = max([l for l in Glyphs.font.selectedLayers], key=lambda l: l.width)
print(widest.parent.name)

Glyphs.showMacroWindow()

Glyphs.font.newTab([widest])
Glyphs.font.currentTab.scale = 0.2
Glyphs.font.currentTab.previewInstances = 'live'
if len(Glyphs.font.tabs) == 1:
    Glyphs.font.currentTab.previewHeight = 250
else:
    Glyphs.font.currentTab.previewHeight = Glyphs.font.tabs[0].previewHeight

