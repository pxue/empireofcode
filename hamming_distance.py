# https://github.com/Empire-of-Code-Puzzles/checkio-empire-hamming-distance

def hamming(n, m):
    return str(bin(n ^ m)).count("1")
