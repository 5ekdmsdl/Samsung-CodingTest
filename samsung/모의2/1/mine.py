from collections import deque

def Input():
    n = int(input())
    Ws, mapp = [], []
    for i in range(n):
        l = list(input())
        a = []
        for j in range(len(l)):
            if l[j] == '.' :
                a.append(0)
            else :
                Ws.append([i,j])
                a.append(1)
        mapp.append(a)

    return n, mapp, Ws

def Connected():
    bflg = 0
    for x in range(n):
        for y in range(n):
            if mapp[x][y] == 0 :
                bflg = 1
                break
        if bflg : break

    q = deque([[x,y]])
    visited = [m[:] for m in mapp]
    visited[x][y] = 1

    while q :
        x,y = q.popleft()

        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]
            if not (0<=nx<=n-1 and 0<=ny<=n-1) : continue

            if visited[nx][ny] : continue
            visited[nx][ny] = 1

            q.append([nx, ny])

    for v in visited:
        if 0 in v :
            return False

    return True

def dfs(i):
    global chW, Wcnt, Ws, mapp

    if len(chW) >= Wcnt or i > len(Ws)-1 :
        return
    W = Ws[i]
    tmp = chW[:]
    tmapp = [m[:] for m in mapp]

    chW.append(W)
    mapp[W[0]][W[1]] = 0

    if Connected():
        if len(chW) < Wcnt :
            Wcnt = len(chW)
            return
    else :
        dfs(i+1)
    chW = tmp[:]
    mapp = [m[:] for m in tmapp]

    dfs(i + 1)
    chW = tmp[:]
    mapp = [m[:] for m in tmapp]




dx, dy = [0,0,-1,1],[-1,1,0,0]
n, mapp, Ws = Input()
chW, Wcnt = [], 7

if not Connected():
    dfs(0)
else :
    Wcnt = 0

if Wcnt == 7 :
    print(-1)
else :
    print(Wcnt)



