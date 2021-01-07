# MenuTitle: Make Character Set Plist...
# -*- coding: utf-8 -*-
__doc__ = """
Adds the selected glyphs to a custom external plist.
"""

import os
import re
from collections import OrderedDict
from vanilla import (
    Window,
    TextBox,
    Button,
    EditText,
    CheckBox,
)

Glyphs.clearLog()
Glyphs.showMacroWindow()


class makePlist(object):
    def __init__(self):
        self.file_name = 'CustomFilter Project Glyph Sets.plist'
        folder_path = os.path.dirname(Glyphs.font.filepath)
        self.file_path = os.path.join(folder_path, self.file_name)

        self.charsets = OrderedDict()
        self.parse_plist()

        self.basic_xml = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.08">
<array>
{charsets}
</array>
</plist>"""

        item_height = 24.0
        w_width = 350.0
        w_height = item_height * 7
        margin = 10
        next_y = margin
        col_1_width = w_width - (margin * 2)
        item_height = 24

        self.w = Window((w_width, w_height), "Insert a font as brace layers")

        next_y = margin
        self.w.charset_name_label = TextBox((margin, next_y + 2, col_1_width, item_height), "Character Set Name:", sizeStyle='regular')
        next_y += item_height
        self.w.charset_name = EditText((margin, next_y, col_1_width, item_height), callback=self.check_extant_charsets)
        next_y += item_height + 2
        self.w.extant_warning = TextBox((margin, next_y + 2, col_1_width, item_height), "The Character Set already exists and will be overwritten!", sizeStyle='small')
        self.w.extant_warning.show(False)
        next_y += (item_height * 0.7) + margin

        self.w.reopen = CheckBox((margin, next_y, col_1_width, item_height), "Close and Reopen current file", value=True)
        next_y += item_height + margin

        self.w.gobutton = Button((margin + (col_1_width / 4), next_y, col_1_width / 2, item_height), 'Make Character Set', callback=self.makeitso)

        self.w.setDefaultButton(self.w.gobutton)

        self.w.open()

    class charset:
        def __init__(self, xml_string=None):
            self.name = None
            self.glyph_names = None

            self.charset_template = """
\t<dict>
\t\t<key>list</key>
\t\t<array>
\t\t\t{glyphnames}
\t\t</array>
\t\t<key>name</key>
\t\t<string>{charset_name}</string>
\t</dict>"""

            if xml_string:
                self.parse_xml_string(xml_string)

        def parse_xml_string(self, xml_string):
            xml_string = re.sub('<!--.+?-->', '', xml_string)
            try:
                self.name = re.search(r'<key>name<\/key>\s+<string>(.+)<\/string>', xml_string).group(1)

                glyph_names_string = re.search(r'<array>(.+?)<\/array>', xml_string, re.DOTALL).group(1)
                self.glyph_names = re.findall(r'<string>(.+?)<\/string>', glyph_names_string)
            except AttributeError:
                pass

        def make_xml_string(self):
            glyph_strings = '\n'.join(['\t\t\t<string>{gn}</string>'.format(gn=gn) for gn in self.glyph_names])
            return self.charset_template.format(glyphnames=glyph_strings, charset_name=self.name)

    def parse_plist(self):
        if not os.path.exists(self.file_path):
            self.make_file()

        with open(self.file_path, 'r') as f:
            file_contents = f.read()

        all_charsets = re.findall(r'<dict>.*?<\/dict>', file_contents, re.DOTALL)
        for cs in all_charsets:
            csObj = self.charset(cs)
            self.charsets[csObj.name] = csObj

    def check_extant_charsets(self, sender):
        self.w.extant_warning.show(sender.get() in self.charsets.keys())

    def make_file(self):
        with open(self.file_path, 'w') as f:
            f.write(self.basic_xml.format(charsets=''))

    def check_file(self):
        with open(self.file_path, 'r') as f:
            file_contents = f.read()
        return file_contents.startswith('<?xml version="1.0" encoding="UTF-8"?>')

    def replace_charset(self, charset_name, charset_entry):
        with open(self.file_path, 'r') as f:
            file_contents = f.read()
        all_char_sets = re.findall(r'<dict>.*?<\/dict>', file_contents, re.DOTALL)
        try:
            this_char_set = [x for x in all_char_sets if '<string>{}</string>'.format(charset_name) in x][0]
        except IndexError:
            return None

        file_contents.replace(this_char_set, charset_entry)
        with open(self.file_path, 'w') as f:
            f.write(file_contents)

        return True

    def append_charset(self, full_entry):
        with open(self.file_path, 'r') as f:
            file_contents = f.read()

        full_entry = full_entry + '\n</array>'
        file_contents = full_entry.join(file_contents.rsplit('</array>', 1))
        with open(self.file_path, 'w') as f:
            f.write(file_contents)

    def makeitso(self, sender):
        self.w.close()
        charset_name = self.w.charset_name.get()
        if not charset_name:
            return

        if not os.path.exists(self.file_path):
            self.make_file()

        if not self.check_file():
            self.make_file()

        glyph_names = [l.parent.name for l in Glyphs.font.selectedLayers]

        this_charset = self.charsets.get(charset_name) or self.charset
        this_charset.name = charset_name
        this_charset.glyph_names = glyph_names
        self.charsets[charset_name] = this_charset

        all_charset_string = '\n'.join([cs.make_xml_string() for cs in self.charsets.values()])
        full_text = self.basic_xml.format(charsets=all_charset_string)

        with open(self.file_path, 'w') as f:
            f.write(full_text)

        if self.w.reopen.get():
            this_filepath = str(Glyphs.font.filepath)
            Glyphs.font.close()
            Glyphs.open(this_filepath)


makePlist()
