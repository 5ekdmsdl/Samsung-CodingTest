from collections import deque

def Input():
    n,m = map(int,input().split())
    mapp = []
    for _ in range(n):
        l = list(map(int,input().split()))
        for j in range(n):
            if l[j] == HO :
                Hs.append([_,j])
        mapp.append(l)
    return n,m,mapp,Hs

def update(H):
    x,y = H
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    q = deque([[x,y]])

    while q :
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if not (0<=nx<=n-1 and 0<=ny<=n-1) : continue
            if visited[nx][ny] == 1 : continue
            if mapp[nx][ny] == WA : continue

            if dmapp[x][y] + 1 < dmapp[nx][ny] :
                dmapp[nx][ny] = dmapp[x][y] + 1
                q.append([nx,ny])
                visited[nx][ny] = 1

    return

def dist():
    global dmapp, ans

    dmapp = [[INF for _ in range(n)] for _ in range(n)]
    maxd = 0

    for cH in cHs :
        dmapp[cH[0]][cH[1]] = 0
        update(cH)

    for x in range(n):
        for y in range(n):
            if mapp[x][y] == VI :
                maxd = max(maxd, dmapp[x][y])

    if maxd < ans :
        ans = maxd

    return

def dfs(i):
    global cHs

    if len(cHs) == m:
        dist()
        return

    if i == len(Hs):
        return

    tmp = cHs[:]
    cHs.append(Hs[i])
    dfs(i+1)

    cHs = tmp[:]
    dfs(i+1)

    # cHs = tmp[:]


VI, WA, HO = 0,1,2
INF = int(1e9)
ans = INF
Hs = []
cHs = []
dx, dy = [0,0,-1,1], [-1,1,0,0]


n,m,mapp,Hs = Input()
dmapp = [[INF for _ in range(n)] for _ in range(n)]

dfs(0)


if ans == INF : print(-1)
else : print(ans)
