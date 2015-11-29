# https://github.com/Empire-of-Code-Puzzles/checkio-empire-landing-holes

def rotr(num, mbits):
    num &= (2**mbits-1)
    bit = num & 1
    num >>= 1
    if(bit):
        num |= (1 << (mbits-1))

    return num

def rotate(state, pipe_numbers):
    z = int(''.join([str(i) for i in state]), 2)

    m = len(state)
    c = z

    r = []
    for n in range(m):

        cc = bin(c)[2:].rjust(m, "0")
        if all([int(cc[i]) for i in pipe_numbers]):
            r.append(n)

        c = rotr(c, m)

    return r
