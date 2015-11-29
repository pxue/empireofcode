# https://github.com/Empire-of-Code-Puzzles/checkio-empire-non-unique-elements

from collections import Counter

def non_unique(data):
    c = Counter(data)

    l = []
    for n in data:
        try:
            z = int(n)
            if c[z] > 1:
                l.append(n)
        except:
            if c[n.lower()] + c[n.upper()] > 1:
                l.append(n)

    return l
