# https://github.com/Empire-of-Code-Puzzles/checkio-empire-bird-language

VOWELS = "aeiouy"

def translate(phrase):

    mod = ""
    last_ch = phrase[0]

    i = 0
    while True:
        if i >= len(phrase):
            break

        ch = phrase[i]
        if ch not in VOWELS:
            mod += ch
        else:
            if last_ch in VOWELS or last_ch == " ":
                if len(set(phrase[i:i+3])) == 1:
                    # skip to end of triplet
                    i += 2
                    mod += ch

        last_ch = ch
        i += 1

    return mod
