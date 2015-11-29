# https://github.com/Checkio-Game-Missions/checkio-empire-pearl-box.git

from collections import defaultdict
def probability(marbles, step):
    # unbalanced binary tree of height = step-1
    binary_tree = defaultdict(list)
    binary_tree[0] = [marbles]

    m = float(len(marbles))
    for h in range(step-1):
        for n in binary_tree[h]:
            # count "b" and "w" marbles
            b = n.split(",")[-1].count("b")
            w = n.split(",")[-1].count("w")

            if b == 0: #www
                binary_tree[h+1].append(n+",1,"+"w"*(w-1)+"b")
            elif w == 0: #bbb
                binary_tree[h+1].append(n+",1,"+"b"*(b-1)+"w")
            else:
                # pick a black -> b-1, w+1
                binary_tree[h+1].append((n + ",%.2f," + "b"*(b-1) + "w"*(w+1)) % float(b/m))
                # pick a white -> w-1, b+1
                binary_tree[h+1].append((n + ",%.2f," + "b"*(b+1) + "w"*(w-1)) % float(w/m))

    p = 0
    for path in binary_tree[max(binary_tree)]:
        sub_p = 1
        for n in path.split(","):
            try:
                sub_p *= float(n)
            except:
                pass
        # leaf nodes only grab white chances
        leaf = path.split(",")[-1]
        sub_p *= float(leaf.count("w")/m)

        p += sub_p

    return p
