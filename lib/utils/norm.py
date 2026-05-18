import unicodedata

TRANSLATION_TABLE = str.maketrans({
    "․": ".",
    "。": ".",
    "｡": ".",
    "﹒": ".",
    "．": ".",
})

def normalize_host(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.translate(TRANSLATION_TABLE)
    s = s.casefold()
    return s