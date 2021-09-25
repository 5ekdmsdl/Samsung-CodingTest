def Input():
    ps, hs = [],[]
    n,m = map(int, input().split())
    for i in range(n):
        line = list(map(int, input().split()))
        for j,l in enumerate(line):
            if l == 1 :
                ps.append([i,j])
            elif l == 2:
                hs.append([i, j])
    return n,m,ps,hs

def dist(ch, p):
    return abs(ch[0] - p[0]) + abs(ch[1] - p[1])

def distance(chs):
    pds = [INF for _ in range(len(ps))]
    for ch in chs :
        for i,p in enumerate(ps):
            pds[i] = min(pds[i], dist(ch, p))
    return sum(pds)

def dfs(cnt):
    global chs,m, minv

    if cnt == len(hs)  :
        if len(chs) == m :
            d = distance(chs)
            minv = min(minv, d)
        return

    tchs = [c[:] for c in chs]

    chs.append(hs[cnt])
    dfs(cnt+1)

    chs = [c[:] for c in tchs]

    dfs(cnt + 1)

    chs = [c[:] for c in tchs]



INF = int(1e9)
chs = []
n,m,ps,hs = Input()
minv = INF
dfs(0)

print(minv)




# print()

