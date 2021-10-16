from collections import deque

def Input():
    n,m,c = map(int, input().split())
    mapp = []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))
    tx, ty = map(int, input().split())
    Rs = []
    for _ in range(m):
        l = list(map(int, input().split()))
        for i in range(4):
            l[i] -= 1
        Rs.append([l[0:2],l[2:]])

    tx -=1
    ty -= 1

    return n,m,c,mapp,tx, ty,Rs

def working():
    fin = 1
    for R in Rs :
        if R : fin = 0
    return not fin

def getD():
    global tx,ty

    q = deque([[tx,ty]])
    dmapp = [[INF for _ in range(n)] for _ in range(n)]
    dmapp[tx][ty] = 0

    visited = [m[:] for m in mapp]
    visited[tx][ty] = 1

    while q :
        x,y = q.popleft()

        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]
            if not (0<=nx<=n-1 and 0<=ny<=n-1) : continue
            if visited[nx][ny] : continue
            visited[nx][ny] = 1

            if dmapp[x][y] + 1 < dmapp[nx][ny] :
                dmapp[nx][ny] = dmapp[x][y] + 1

                q.append([nx,ny])

    return dmapp

def chooseR():
    mini, mind = [-1], INF
    Dmapp = getD()

    for i, xy in enumerate(Rs) :
        if not xy : continue
        x,y = xy[0]
        if Dmapp[x][y] < mind :
            mind = Dmapp[x][y]
            mini = [i]
        elif Dmapp[x][y] == mind :
            mini.append(i)

    nl = []
    for i in mini :
        nl.append([Rs[i][0],i])
    nl.sort(key= lambda a : [a[0][0], a[0][1]])

    return nl[0][1], mind

def moveTo(xy,d):
    global ene, tx, ty, used
    x,y = xy
    if d == -1 :
        Dmapp = getD()
        d = Dmapp[x][y]
        used = d

    ene -= d
    tx, ty = x,y

    return

def charge(oil):
    global ene, used
    used = 0
    ene += oil
    return


INF = int(1e9)
dx, dy = [0,0,-1,1],[-1,1,0,0]
n,m,ene,mapp,tx, ty,Rs = Input()
used = 0

while(working()):
    i, dist = chooseR()

    moveTo(Rs[i][0], dist)
    if ene <= 0 :
        ene = -1
        break

    moveTo(Rs[i][1], -1)
    Rs[i] = []
    if ene < 0 :
        ene = -1
        break

    charge(used * 2)
    a = 1


print(ene)
