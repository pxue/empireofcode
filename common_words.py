# https://github.com/Empire-of-Code-Puzzles/checkio-empire-common-words
def common_words(first, second):
    f = set(first.split(","))
    s = set(second.split(","))

    i = list(sorted(f.intersection(s)))

    return ",".join(i)
