def import_scripts(font):
    font_scripts = set([g.script for g in font.glyphs])

    unified_infos = dict()
    if 'armenian' in font_scripts:
        from UGI.UGInfos_Armenian import collect_infos  # NoQA F401
        collect_infos(unified_infos)

    if 'cyrillic' in font_scripts:
        from UGI.UGInfos_Cyrillic import collect_infos  # NoQA F401
        collect_infos(unified_infos)

    if 'latin' in font_scripts:
        from UGI.UGInfos_Latin import collect_infos  # NoQA F401
        collect_infos(unified_infos)

    if 'greek' in font_scripts:
        from UGI.UGInfos_Greek import collect_infos  # NoQA F401
        collect_infos(unified_infos)

    if 'bengali' in font_scripts:
        from UGI.UGInfos_Bengali import collect_infos  # NoQA F401
        collect_infos(unified_infos)

    if 'devanagari' in font_scripts:
        from UGI.UGInfos_Devanagari import collect_infos  # NoQA F401
        collect_infos(unified_infos)

    from UGI.UGInfos_Other import collect_infos  # NoQA F401
    collect_infos(unified_infos)

    return unified_infos
