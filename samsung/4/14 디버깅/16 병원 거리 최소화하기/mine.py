from itertools import combinations
INF = int(1e9)

def distance(hs,ps) :
    global min_val
    ps_total = 0
    for p in ps :
        p_min = INF
        for h in hs :
            d = abs(p[0]-h[0]) + abs(p[1]-h[1])
            if d < p_min :
                p_min = d
        ps_total += p_min
    if ps_total < min_val :
        min_val = ps_total

n,m = map(int, input().split())a
peo, hos = [], []
min_val = INF
for i in range(n) :
    line = list(map(int, input().split()))
    for j,l in enumerate(line) :
        if l == 1 :
            peo.append((i,j))
        elif l == 2:
            hos.append((i,j))

cases = combinations(hos, m)

for c in cases :
    distance(c,peo)

print(min_val)
