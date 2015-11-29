# description: https://github.com/Empire-of-Code-Puzzles/checkio-empire-stair-steps

def golf(numbers):
    dist = {}
    for i in range(len(numbers)+1):
        dist[chr(65+i)] = numbers[i-1]

    ret = [0] * (len(numbers)+1)
    dist["A"] = 0
    for i in range(1, len(numbers)+1):
        m = chr(65+i)
        n = dist[m]
        
        dist[m] = max(n+dist[chr(65+i-1)], n+dist.get(chr(65+i-2), 0))

        ret[i] = dist[m]

    return max(ret[-2:])

def golf2(n):
    dist = {0:0}

    ret = []
    for i in range(1, len(n)+1):
        dist[i] = max(n[i-1]+dist[i-1], n[i-1]+dist.get(i-2, 0))
        ret.append(dist[i])

    return max(ret[-2:])

def golf3(n):
    d = {0:0,1:n[0]}

    for i in range(1,len(n)):
        d[i+1] = n[i]+max(d[i],d[i-1])

    return max(d.values()[-2:])

def golf4(n):
    v = [0,n[0]]

    for i in range(1, len(n)):
        v += [n[i] + max(v[i-1:i+1])]

    return max(v[-2:])

def golf5(n):
 v=[0]
 for i in range(len(n)):
  v += [n[i] + max(v[i-1],v[i])]
  return max(v[-2:])
