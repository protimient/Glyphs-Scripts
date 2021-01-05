# MenuTitle: Remove Selected Kerning Groups...
# -*- coding: utf-8 -*-
__doc__ = """
Remove Kern Groups on the left, right or both sides of the selected glyphs.
"""

import vanilla


class removeKernGroups(object):
    def __init__(self):
        # Window 'self.w':
        hMargin = 10
        vMargin = 15
        textWidth = 250
        textHeight = 14 * 2
        buttonWidth = 90
        buttonHeight = 20

        windowWidth = buttonWidth * 3 + hMargin * 4
        windowHeight = textHeight + buttonHeight + vMargin * 3
        windowWidthResize = 100  # user can resize width by this value
        windowHeightResize = 0   # user can resize height by this value
        self.w = vanilla.FloatingWindow(
            (windowWidth, windowHeight),  # default window size
            "Remove Kern Groups",  # window title
            minSize=(windowWidth, windowHeight),  # minimum size (for resizing)
            maxSize=(windowWidth + windowWidthResize, windowHeight + windowHeightResize),  # maximum size (for resizing)
        )

        # UI elements:
        self.w.text_1 = vanilla.TextBox((hMargin, vMargin, textWidth, textHeight), "Remove Kern Groups on the left, right or both sides of the selected glyphs.", sizeStyle='small')
        self.w.button_1 = vanilla.SquareButton(
            (hMargin, vMargin + textHeight + vMargin, buttonWidth, buttonHeight),
            u"Left Groups",
            sizeStyle='small',
            callback=self.removeLeft
        )
        self.w.button_2 = vanilla.SquareButton(
            (hMargin + buttonWidth + hMargin, vMargin + textHeight + vMargin, buttonWidth, buttonHeight),
            u"Both Groups",
            sizeStyle='small',
            callback=self.removeBoth
        )
        self.w.button_3 = vanilla.SquareButton(
            (hMargin + buttonWidth + hMargin + buttonWidth + hMargin, vMargin + textHeight + vMargin, buttonWidth, buttonHeight),
            u"Right Groups",
            sizeStyle='small',
            callback=self.removeRight
        )

        # Open window and focus on it:
        self.w.open()
        self.w.makeKey()

    def removeLeft(self, sender):
        for g in [x.parent for x in Glyphs.font.selectedLayers]:
            g.setLeftKerningGroup_('')
        self.w.close()

    def removeBoth(self, sender):
        for g in [x.parent for x in Glyphs.font.selectedLayers]:
            g.setRightKerningGroup_('')
            g.setLeftKerningGroup_('')
        self.w.close()

    def removeRight(self, sender):
        for g in [x.parent for x in Glyphs.font.selectedLayers]:
            g.setRightKerningGroup_('')
        self.w.close()


removeKernGroups()
