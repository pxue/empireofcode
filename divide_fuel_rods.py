# https://github.com/Empire-of-Code-Puzzles/checkio-empire-divide-fuel-rod

import math
def disjoint(m):
    t = lambda n: n*(n+1)/2
    s = int(math.sqrt(m * 2))

    max_l = 0
    max_x = []
    for i in range(1, s):
        #x = [t(i), t(i+1), t(i+2)]
        j = 0
        x = []
        while sum(x) < m:
            x.append(t(i+j))
            j += 1
        if sum(x) == m and max_l < len(x):
            max_x = x
            max_l = len(x)

    #z = map(lambda (x,y): x+y, list(zip(*[iter(x)] * 2))) # WOAH
    return max_x
