def funcA():
    for (r,c) in vs.keys():
        n_vs = vs[(r,c)]
        for i, v in enumerate(vs[(r,c)]):
            if mapp[r][c] < v :
                n_vs.remove(v) #느리다
                dead.append([r,c,v])
            else :
                mapp[r][c] -= v
                n_vs[i] += 1
                if n_vs[i] % 5 == 0 :
                    produce.append([r,c])
        vs[(r,c)] = n_vs

def funcB():
    global dead
    for (r,c,v) in dead :
        mapp[r][c] += (v//2)
    dead = []

def funcC(): #번식
    global produce
    dr, dc = [0,0,-1,-1,-1,1,1,1], [-1,1,0,-1,1,0,-1,1]
    for (r,c) in produce :
        for i in range(8) :
            nr, nc = r+dr[i], c+dc[i]
            if 1 <= nr <= n and 1 <= nc <= n :
                if (nr, nc) in vs.keys():
                    vs[(nr, nc)].append(1)
                    vs[(nr, nc)].sort()
                else:
                    vs[(nr, nc)] = [1]
    produce = []



n,m,k = map(int, input().split())
mapp = [[5]*(n+1) for _ in range(n+1)]
addmapp = []
vs = {}
dead = []
produce = []

for _ in range(n):
    addmapp.append(list(map(int, input().split())))

for _ in range(m):
    r,c,v = map(int, input().split())
    if (r,c) in vs.keys() :
        vs[(r,c)].append(v)
    else :
        vs[(r,c)] = [v]


for i in range(k):
    funcA()
    funcB()
    funcC()
    for a in range(1,n+1) :
        for b in range(1,n+1) :
            mapp[a][b] += addmapp[a-1][b-1]

cnt = 0

for vv in vs.values() :
    for v in vv :
        if v :
            cnt += 1

print(cnt)
