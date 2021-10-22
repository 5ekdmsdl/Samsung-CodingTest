def Input():
    n, m, k = map(int, input().split())

    mapp = [[[] for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x,y,s,d,b = map(int, input().split())
        mapp[x-1][y-1].append([s,d,b])

    return n,m,k,mapp

def getV(y):
    global ans
    for x in range(n):
        if mapp[x][y] :
            ans += mapp[x][y][0][2]
            mapp[x][y] = []
            return
    return

def next(x,y,s,d):
    N, M = 2*n-2, 2*m-2

    nx, ny = x+dx[d]*s, y+dy[d]*s
    nd = d


    if not 0<=nx<=n-1 :
        nx1 = nx % N
        if n <= nx1 <= N - 1:
            nx1 = N - nx1

        nx2 = nx % N // n
        if nx2 == 0 : nd = d
        else : nd = opp[d]

        nx = nx1


    if not 0 <= ny <= m - 1:
        ny1 = ny % M
        if m <= ny1 <= M-1 :
            ny1 = M - ny1

        ny2 = ny % M // m
        if ny2 == 0:
            nd = d
        else:
            nd = opp[d]

        ny = ny1

    return nx,ny,nd

def Move():
    global mapp,n,m

    tmp = [[[] for _ in range(m)] for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if mapp[x][y] :
                s,d,b = mapp[x][y][0]
                nx,ny,nd = next(x,y,s,d)
                tmp[nx][ny].append([s,nd,b])

    mapp = [t[:] for t in tmp]

    return

def Eat():
    for x in range(n):
        for y in range(m):
            if len(mapp[x][y]) >= 2:
                # Vs = mapp[x][y]
                mapp[x][y].sort(key = lambda a : -a[2])
                mapp[x][y] = [mapp[x][y][0]]
    return



dx, dy = [0,-1,1,0,0], [0,0,0,1,-1]
opp = [0,2,1,4,3]
n,m,k,mapp = Input()
ans = 0

for j in range(m):
    getV(j)
    Move()
    Eat()

print(ans)








