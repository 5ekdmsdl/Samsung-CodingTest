def Input():
    n, k = map(int, input().split())

    cmapp = []
    for _ in range(n):
        cmapp.append(list(map(int, input().split())))

    ds = []

    mapp = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(k):
        x,y,d = map(int, input().split())
        mapp[x-1][y-1].append(i)
        ds.append(d)

    return n,k,cmapp,ds,mapp

def Blue():
    global nx,ny
    global i
    opp = [0,2,1,4,3]

    ds[i] = opp[ds[i]]
    d = ds[i]

    nx,ny = x+dx[d], y+dy[d]

    if not (0 <= nx <= n - 1 and 0 <= ny <= n - 1) or cmapp[nx][ny] == B :
        ds[i] = opp[ds[i]]
        return
    elif cmapp[nx][ny] == W:
        White()
    elif cmapp[nx][ny] == R:
        Red()

    return

def White():
    global x,y,i

    idx = mapp[x][y].index(i)

    mapp[nx][ny] += mapp[x][y][idx:]
    mapp[x][y] = mapp[x][y][:idx]

    return

def Red():
    idx = mapp[x][y].index(i)

    tmp = mapp[x][y][idx:]
    mapp[x][y] = mapp[x][y][:idx]
    # if mapp[nx][ny] :
    #     print()
    mapp[nx][ny] += reversed(tmp)

    return

def getxy(i):
    for a in range(n):
        for b in range(n):
            if i in mapp[a][b]:
                # idx = mapp[a][b].index(i)
                return a, b
    return

def checklen():
    for a in range(n):
        for b in range(n):
            if len(mapp[a][b]) >= 4:
                return True
    return False


n,k,cmapp,ds,mapp = Input()
W, R, B = 0,1,2
dx, dy = [0,0,0,-1,1], [0,1,-1,0,0]
bflg = 0

for t in range(1,1001):

    for i in range(k):
        x,y = getxy(i)
        d = ds[i]
        # x,y,d
        nx,ny = x+dx[d], y+dy[d]

        if not (0<=nx<=n-1 and 0<=ny<=n-1) or cmapp[nx][ny] == B :
            Blue()

        elif cmapp[nx][ny] == W :
            White()

        elif cmapp[nx][ny] == R :
            Red()


        if checklen() :
            print(t)
            bflg = 1
            break

    if bflg : break


if t == 1000 :
    print(-1)
