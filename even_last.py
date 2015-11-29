#https://github.com/Empire-of-Code-Puzzles/checkio-empire-even-last

def even_last(array):
    if len(array) == 0:
        return 0
        
    return sum([z for (i, z) in enumerate(array) if i % 2 == 0]) * array[-1]
