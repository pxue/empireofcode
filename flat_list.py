# https://github.com/Checkio-Game-Missions/checkio-empire-flatten-list.git
def flat_list(array):
    r = []
    while len(array) > 0:
        l = array.pop()
        if hasattr(l, "__iter__"):
            array.extend(l)
        else:
            r.append(l)

    return r[::-1]
