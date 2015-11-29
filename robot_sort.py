# https://github.com/Checkio-Game-Missions/checkio-empire-robot-sort.git

def swap_sort(array):
    a = list(array)

    r = []
    while a != sorted(a):
        for i in range(len(a)):
            cur = a[i]
            j = i

            while j < len(a)-1 and cur > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                j += 1

            if i == j:
                continue

            for x in range(i, j):
                r.append("%d%d" % (x, x+1))

    return ",".join(r)
