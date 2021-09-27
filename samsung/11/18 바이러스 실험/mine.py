def Input():
    n,m,k = map(int, input().split())
    pmapp = []
    for _ in range(n):
        pmapp.append(list(map(int, input().split())))
    mapp = [[[] for _ in range(n) ] for _ in range(n)]
    for _ in range(m):
        x,y,v = map(int, input().split())
        mapp[x-1][y-1].append(v)
    return n,m,k,pmapp,mapp

def eat():
    for x in range(n):
        for y in range(n):
            if mapp[x][y] :
                if len(mapp[x][y]) >= 2 :
                    mapp[x][y].sort()

                nm = []

                for i,v in enumerate(mapp[x][y]):
                    if fmapp[x][y] >= v :
                        fmapp[x][y] -= v
                        nm.append(v+1)
                        # mapp[x][y][i] += 1
                    else:
                        dead[(x,y)] = mapp[x][y][i:]
                        break
                        # mapp[x][y] = mapp[x][y][0:i]
                mapp[x][y] = nm

def die():
    for xy, vs in dead.items():
        x,y = xy
        for v in vs :
            fmapp[x][y] += (v // 2)

def birth():
    global mapp

    dx, dy = [0,0,-1,1,-1,1,-1,1], [-1,1,0,0,-1,1,1,-1]

    tmp = [m[:] for m in mapp]

    for x in range(n):
        for y in range(n):
            if mapp[x][y] :
                for v in mapp[x][y] :
                    if v % 5 == 0 :
                        for i in range(8):
                            nx, ny = x+dx[i], y+dy[i]

                            if not (0<=nx<=n-1 and 0<=ny<=n-1):
                                continue

                            tmp[nx][ny].append(1)

    mapp = [t[:] for t in tmp]

def plus():
    for x in range(n):
        for y in range(n):
            fmapp[x][y] += pmapp[x][y]

def answer():
    a = 0
    for x in range(n):
        for y in range(n):
            if mapp[x][y] :
                a += len(mapp[x][y])
    return a

n,m,k,pmapp,mapp = Input()
fmapp = [[5 for _ in range(n)] for _ in range(n)]

for i in range(k):
    dead = {}
    eat()
    die()
    birth()
    plus()

print(answer())











