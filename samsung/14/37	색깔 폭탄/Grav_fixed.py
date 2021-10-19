from collections import deque

def Input():
    n, m = map(int, input().split())
    mapp = []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))
    return n,m,mapp

def RunQ(x,y):
    blks = [[x,y]]
    c = mapp[x][y]
    q = deque([[x,y]])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    Rcnt = 0

    while q :
        x,y = q.popleft()

        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if not (0<=nx<=n-1 and 0<=ny<=n-1) : continue

            if visited[nx][ny] : continue

            if mapp[nx][ny] == 0 or mapp[nx][ny] == c :
                if mapp[nx][ny] == 0 : Rcnt += 1
                blks.append([nx,ny])
                q.append([nx,ny])
                visited[nx][ny] = 1

    return Rcnt, blks

def getGroup():
    done = [[0 for _ in range(n)] for _ in range(n)]
    tmp = []

    for x in range(n):
        for y in range(n):
            if not done[x][y] and mapp[x][y] > 0:
                done[x][y] = 1
                Rcnt, blks = RunQ(x,y)

                for b in blks :
                    bx, by = b
                    done[bx][by] = 1

                if Rcnt == len(blks) or len(blks) < 2 : continue

                blks.sort(key = lambda a : [-a[0], a[1]])

                for b in blks :
                    bx, by = b
                    if mapp[bx][by] != 0 :
                        ax, ay = bx, by
                        break

                tmp.append([len(blks), Rcnt, ax, ay, blks])

    if not tmp :
        return False

    tmp.sort(key = lambda a : [-a[0], a[1], -a[2], a[3]])

    return tmp[0][4]

def Bomb(blks):
    global scr
    for b in blks :
        mapp[b[0]][b[1]] = -2
    scr += len(blks)**2

#Again@@@@!!!!
def Grav():
    global m, mapp

    tmp = [[-2 for _ in range(n)] for _ in range(n)]

    for y in range(n):

        dx = n-1

        for x in range(n-1, -1, -1):
            if mapp[x][y] == -2 :
                continue
            elif mapp[x][y] == -1 :
                tmp[x][y] = mapp[x][y]
                dx = x-1
            else :
                tmp[dx][y] = mapp[x][y]
                dx = dx-1

    mapp = [t[:] for t in tmp]

    return

def Rotate():
    global mapp

    tmp = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            tmp[n-1-y][x] = mapp[x][y]

    mapp = [t[:] for t in tmp]
    return


scr = 0
dx, dy = [0,0,-1,1], [-1,1,0,0]
n,m,mapp = Input()
done = [[0 for _ in range(n)] for _ in range(n)]


while(1):
    Gp = getGroup()
    if not Gp :
        break

    Bomb(Gp)

    Grav()

    Rotate()

    Grav()

    # break

print(scr)
