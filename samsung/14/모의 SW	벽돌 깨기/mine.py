from collections import deque

def Input():
    n,w,h = map(int, input().split())
    mapp = []
    for _ in range(h):
        mapp.append(list(map(int, input().split())))
    return n,w,h,mapp

def Count():
    global ans, mapp

    ccnt = 0
    for x in range(h):
        for y in range(w):
            if mapp[x][y] :
                ccnt += 1
    if ccnt < ans :
        ans = ccnt

    return

def Remove():
    global Bs

    for B in Bs.keys() :
        x,y = B
        mapp[x][y] = 0
    Bs = {}

    return

def Grav():
    global mapp, h,w
    tmp = [[0 for _ in range(w)] for _ in range(h)]

    for y in range(w):
        last = h - 1

        for x in range(h-1, -1, -1):
            if mapp[x][y] == 0 : continue

            tmp[last][y] = mapp[x][y]

            last -= 1

    mapp = [t[:] for t in tmp]

    return

def Explode(x,y):
    global Bs, mapp

    q = deque([[x,y]])
    visited  = [[0 for _ in range(w)] for _ in range(h)]
    visited[x][y] = 1

    while q :
        x,y = q.popleft()
        Bs[x,y] = 1
        S = mapp[x][y]

        if S == 1 :
            continue

        for d in range(4):
            for s in range(1, S):
                nx, ny = x+dx[d]*s, y+dy[d]*s
                if not (0<=nx<=h-1 and 0<=ny<=w-1) : break

                if mapp[nx][ny] and (nx,ny) not in list(Bs.keys()) :
                    q.append([nx,ny])
                    visited[nx][ny] = 1

    return

def Shoot(j):
    global mapp, Bs

    for i in range(h):
        if mapp[i][j] :
            Explode(i,j)
            break
    return

def dfs(cnt):
    global mapp

    if cnt == n :
        Count()
        return

    tmapp = [m[:] for m in mapp]

    for j in range(w):
        Shoot(j)
        Remove()
        Grav()

        dfs(cnt+1)

        mapp = [m[:] for m in tmapp]

    return


INF = int(1e9)
dx, dy = [0,0,-1,1], [-1,1,0,0]

T = int(input())
for t in range(T) :
    ans = INF
    Bs = {}

    n, w, h, mapp = Input()

    dfs(0)

    print('#'+str(t+1)+' '+str(ans))
