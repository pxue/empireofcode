# https://github.com/Empire-of-Code-Puzzles/checkio-empire-count-inversion

def count_inversion(sequence):
    n = 0
    for i, x in enumerate(sequence):
        for j, y in enumerate(sequence[i:]):
            if x <= y:
                continue
            else:
                n += 1
    return n

