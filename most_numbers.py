# https://github.com/Empire-of-Code-Puzzles/checkio-empire-most-numbers

def most_difference(*args):
    d = 0
    if len(args) > 0:
        for i, x in enumerate(args):
            for j, y in enumerate(args[i:]):
                d = max(abs(x-y), d)
            
    return d
