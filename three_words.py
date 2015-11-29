# https://github.com/Checkio-Game-Missions/checkio-empire-three-words.git

def three_words(words):
    w = words.split()
    c = 0
    max_c = 0
    for x in w:
        if x.isdigit():
            c = 0
        else:
            c += 1
        max_c = max(c, max_c)
    return max_c >= 3
