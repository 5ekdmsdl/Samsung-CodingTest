from collections import deque

def Input():
    n = int(input())
    mapp = []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))

    return n, mapp

def runQ(x,y,c):
    dx, dy = [0,-1,0,1],[-1,0,1,0]

    q = deque([[x,y]])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1

    while q :
        x,y = q.popleft()

        nmapp[x][y] = c

        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]
            if not (0<=nx<=n-1 and 0<=ny<=n-1 ): continue

            if visited[nx][ny] == 1 : continue

            visited[nx][ny] = 1

            if nmapp[nx][ny] == 0:

                q.append([nx,ny])

    return

def set2():
    global nmapp, ps

    p = ps[0]
    for i in range(1,n):
        if not (0<=p[0] - i<=n-1) : break
        nmapp[p[0] - i][p[1]] = 2

    p = ps[2]
    for i in range(1, n):
        if not (0 <= p[1] + i <= n - 1): break
        nmapp[p[0]][p[1] + i] = 3

    p = ps[1]
    for i in range(1, n):
        if not (0 <= p[1] - i <= n - 1): break
        nmapp[p[0]][p[1] - i] = 4

    p = ps[3]
    for i in range(1, n):
        if not (0 <= p[0] + i <= n - 1): break
        nmapp[p[0]+i][p[1]] = 5

    runQ(0,0,2)

    return

def set3():
    global nmapp, ps



    runQ(0,n-1,3)
    return

def set4():
    global nmapp, ps



    runQ(n-1,0,4)

    return

def set5():
    global nmapp, ps

    runQ(n-1,n-1,5)

    return

def setNmapp(x,y,ld,rd):
    global nmapp,ps

    nmapp = [[0 for _ in range(n)] for _ in range(n)]

    ps = [[x,y]]

    for d1 in range(rd+1):
        nx, ny = x+dx[1]*d1, y+dy[1]*d1

        if d1 == rd : ps.append([nx,ny])


        for d2 in range(ld+1):
            nnx, nny = nx + dx[0] * d2, ny + dy[0] * d2

            nmapp[nnx][nny] = 1

            if nny != ny and d1 != rd :
                nmapp[nnx][nny+1] = 1

        if d1 == 0 or d1 == rd : ps.append([nnx, nny])

    set2()
    set3()
    set4()
    set5()

    return

def getGap():
    global ans

    G = [0 for _ in range(5)]

    for x in range(n):
        for y in range(n):
            G[nmapp[x][y]-1] += mapp[x][y]

    a = max(G) - min(G)

    ans = min(a, ans)

    return

def Rec(x,y,cnt):
    global ls

    if cnt == 2:

        if x + ls[0] + ls[1] > n - 1: return

        setNmapp(x,y,ls[0], ls[1])

        getGap()

        return

    tmp = ls[:]

    for d in range(1,n):

        nx, ny = x+dx[cnt]*d, y+dy[cnt]*d

        if not (0<=nx<=n-1 and 0<=ny<=n-1) : break


        ls.append(d)

        Rec(x,y,cnt+1)

        ls = tmp[:]


    return

dx, dy = [1,1,-1,-1], [-1,1,1,-1]
n, mapp = Input()
nmapp = [[0 for _ in range(n)] for _ in range(n)]
ans = int(1e9)

for x in range(0,n-2):
    for y in range(0,n-1):
        ps, ls = [], []
        Rec(x,y,0)

print(ans)


