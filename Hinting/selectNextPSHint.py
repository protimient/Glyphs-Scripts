# MenuTitle: Select Next PS Hint

Glyphs.clearLog()
# Glyphs.showMacroWindow()


def is_PS_hint(thisHint):
    return thisHint.type in [TOPGHOST, STEM, BOTTOMGHOST]


l = Glyphs.font.selectedLayers[0]
h = None
for o in l.selection:
    if is_PS_hint(o):
        h = o

l.selection = []

if h is not None:
    seen = False
    for this_h in Glyphs.font.selectedLayers[0].hints:
        if this_h == h:
            seen = True
            continue

        if seen:
            if is_PS_hint(h):
                h = this_h
                h.selected = True
                break

if h is None:
    for h in Glyphs.font.selectedLayers[0].hints:
        if is_PS_hint(h):
            h.selected = True
            break
