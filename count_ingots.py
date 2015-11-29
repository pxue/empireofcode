# https://github.com/Empire-of-Code-Puzzles/checkio-empire-count-ingots

def count_ingots(report):
    import string

    m = []
    for x in string.ascii_uppercase:
        for y in range(1,10):
            m.append("%s%d" % (x, y))

    c = 0
    for i in report.split(","):
        c += (m.index(i)+1)

    return c


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_ingots("A2,B1") == 12, "Two and ten"
    assert count_ingots("A1,A1,A1") == 3, "One, two, three"
    assert count_ingots("Z9,X8,Y7") == 672, "XYZ"
    assert count_ingots("C1,D1,B1,E1,F1") == 140, "Daily normal"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

