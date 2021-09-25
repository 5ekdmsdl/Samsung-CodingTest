def Input():
    n = int(input())
    xs, ys, ds, gs = [],[],[],[]
    for _ in range(n):
        x,y,d,g = map(int, input().split())
        if d == 1 : d = 3
        elif d == 3 : d = 1
        xs.append(x)
        ys.append(y)
        ds.append(d)
        gs.append(g)
    return n, xs, ys, ds, gs

def rotate(tmp, pivot):
    tmp2 = []
    px,py = pivot

    # tmpp =
    for t in tmp :
        x,y = t
        nx, ny = x-px, y-py
        nx, ny = ny, -nx
        nx, ny = nx + px, ny+py
        # if [nx,ny] not in tmp2 and [nx,ny] not in tmp :
        tmp2.append([nx, ny])

    return tmp2

def setgxy():
    global gs
    gxys = [0 for _ in range(max(gs)+1)]
    tmp = [[0,0], [0,1]]
    if 0 in gs :
        gxys[0] = tmp
    for i in range(1,max(gs)+1):
        tmp2 = rotate(reversed(tmp), tmp[-1])
        for t in tmp2 :
            if t in tmp :
                tmp2.remove(t)
        tmp = tmp + tmp2
        if i in gs :
            gxys[i] = tmp
    return gxys

def shift(gxy, xy):
    tmp = []
    x,y = xy

    for g in gxy :
        gx, gy = g
        tmp.append([gx+x, gy+y])

    return tmp

def DC(x,y,d,g):
    global mapp
    gxy = gxys[g]

    for _ in range(d):
        gxy = rotate(gxy, gxy[0])

    gxy = shift(gxy, [x,y])


    for xy in gxy :
        x,y = xy
        mapp[x][y] = 1

def getanswer():
    global mapp
    rtv = 0
    dx, dy = [0,1,1], [1,0,1]
    for x in range(99):
        for y in range(99):
            if mapp[x][y] :
                fail = 0
                for _ in range(3):
                    nx,ny = x+dx[_], y+dy[_]
                    if not mapp[nx][ny]:
                        fail = 1
                        break
                if not fail:
                    rtv += 1
    return rtv



mapp = [[0 for _ in range(100)] for _ in range(100)]
n, xs, ys, ds, gs = Input()
gxys = setgxy()

for i in range(n):
    x,y,d,g = xs[i], ys[i], ds[i], gs[i]
    DC(x,y,d,g)

answer = getanswer()

print(answer)
