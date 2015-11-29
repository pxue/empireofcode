# https://github.com/Empire-of-Code-Puzzles/checkio-empire-median

def median(data):
    if len(data) % 2 != 0:
        
        return sorted(data)[int(len(data)/2)]

    a = sorted(data)[int(len(data)/2)]
    b = sorted(data)[int(len(data)/2 - 1)]

    return float(a+b)/2.0
