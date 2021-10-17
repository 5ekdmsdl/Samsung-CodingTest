def Input():
    n = int(input())
    mapp = []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))
    return n, mapp

def move(d,s):
    global xys
    dx, dy = [0,1,0,-1], [-1,0,1,0]

    x, y = xys[-1]

    for _ in range(s):
        nx, ny = x+dx[d], y+dy[d]
        xys.append([nx, ny])

        x,y = nx,ny

    return

def setxys():
    global n, S, xys
    x,y = S

    for i in range(1,n,2):
        move(0,i)
        move(1,i)
        move(2,i+1)
        move(3,i+1)
    move(0,n-1)

    return

def setpms():
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    pms = {}

    pms[(0,-1)] = [
        [0, 0, 0.02, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0.05, 99, -1, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0, 0, 0.02, 0, 0],
    ]

    pms[(1,0)] = [
        [0, 0, 0, 0, 0],
        [0, 0.01, 0, 0.01, 0],
        [0.02, 0.07, -1, 0.07, 0.02],
        [0, 0.1, 99, 0.1, 0],
        [0, 0, 0.05, 0, 0],
    ]

    pms[(0,1)] = [
        [0, 0, 0.02, 0, 0],
        [0,0.01, 0.07, 0.1, 0],
        [0, 0, -1, 99, 0.05],
        [0,0.01, 0.07, 0.1, 0],
        [0, 0, 0.02, 0, 0],
    ]

    pms[(-1,0)] = [
        [0, 0, 0.05, 0, 0],
        [0, 0.1, 99, 0.1, 0],
        [0.02, 0.07, -1, 0.07, 0.02],
        [0, 0.01, 0, 0.01, 0],
        [0, 0, 0, 0, 0],
    ]

    return pms

def setdmapp(pmapp,cx,cy):
    global mapp

    dmapp = [[0 for _ in range(dsize)] for _ in range(dsize)]
    left = mapp[cx][cy]

    for i in range(dsize):
        for j in range(dsize):
            if pmapp[i][j] == 99 or pmapp[i][j] == 0 : continue

            dx, dy = i-2, j-2
            x,y = cx+dx, cy+dy

            dmapp[i][j] = int((pmapp[i][j] * mapp[cx][cy])//1)
            if dmapp[i][j] > 0 : left -= dmapp[i][j]

    for i in range(dsize):
        if 99 in pmapp[i] :
            j = pmapp[i].index(99)
            dmapp[i][j] = left

    return dmapp

def swapTo(xy):
    global total, pos
    cx, cy = xy
    px, py = pos

    dxy = (cx-px, cy-py)

    pmapp = pms[dxy]
    dmapp = setdmapp(pmapp,cx,cy)

    for i in range(dsize):
        for j in range(dsize):
            dx, dy = i-2, j-2
            x,y = cx+dx, cy+dy

            if not (0<=x<=n-1 and 0<=y<=n-1) :
                total += dmapp[i][j]
            else :
                mapp[x][y] += dmapp[i][j]

    pos = xy
    return




dsize, total = 5, 0
n, mapp = Input()
S, E = [n//2, n//2], [0,0]

xys = [S]
setxys()

pos = S
pms = setpms()

for i in range(1, len(xys)):
    swapTo(xys[i])


print(total)
