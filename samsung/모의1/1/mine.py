from collections import deque

def Input():
    n = int(input())
    Cs = [[] for _ in range(10)]
    mapp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        l = list(input())
        for j in range(n):
            if l[j] == '#':
                mapp[i][j] = -1
            elif l[j] == '.':
                continue
            elif l[j] == 'S':
                S = [i,j]
            elif l[j] == 'E':
                E = [i,j]
            elif 1 <= int(l[j]) <= 9 :
                mapp[i][j] = int(l[j])
                Cs[int(l[j])] = [i,j]
    return n, Cs, mapp, S, E

def getdist(xy):
    global pos
    sxy, exy = pos, xy
    q = deque([sxy])

    dmapp = [[INF for _ in range(n)] for _ in range(n)]
    dmapp[sxy[0]][sxy[1]] = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[sxy[0]][sxy[1]] = 1

    while q :
        x,y = q.popleft()

        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]

            if not (0<=nx<=n-1 and 0<=ny<=n-1) : continue
            if visited[nx][ny] or mapp[nx][ny] == -1: continue

            visited[nx][ny] = 1

            if dmapp[x][y] + 1 < dmapp[nx][ny] :
                dmapp[nx][ny] = dmapp[x][y] + 1
                q.append([nx,ny])


    return dmapp[exy[0]][exy[1]]

def getcoin(i):
    global step, coll, pos

    if not Cs[i] :
        return
    dist = getdist(Cs[i])
    if dist == INF :
        return
    step += dist
    coll += 1
    pos = Cs[i][:]
    coins.append(i)
    return

def dfs(cnt):
    global coll, step, coll, pos, ans,coins

    if coll >= 3 or cnt > 9 :
        if coll >= 3 :
            pos = Cs[coins[-1]][:]
            d = getdist(E)
            step += d
            if step < ans :
                ans = step
        coins = []
        return

    ptmp, ctmp = pos[:], coins[:]
    tmp = step, coll

    dfs(cnt+1)

    pos[:], coins[:] = ptmp, ctmp
    step, coll = tmp

    if Cs[cnt] :
        getcoin(cnt)
        dfs(cnt+1)

    return


INF = int(1e9)
dx, dy = [0,0,-1,1],[-1,1,0,0]
n, Cs, mapp, S, E = Input()
pos, step, coll = S, 0,0
ans = INF
coins = []
# Spos = []

dfs(1)

if ans == INF :
    print(-1)
else :
    print(ans)
