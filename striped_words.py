# https://github.com/Empire-of-Code-Puzzles/checkio-empire-striped-words

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

import re
W = re.compile(r"[\[0-9A-za-z]+")

def striped_words(text):
    c = 0
    for w in W.findall(text):
        w = w.upper()
        if len(w) < 2:
            continue

        last_c = -1
        s = True
        for ch in w:
            n = 1 if ch in CONSONANTS else 0
            if last_c == n:
                s = False # don't strip
                break
            last_c = n

        if s:
            c += 1

    return c
