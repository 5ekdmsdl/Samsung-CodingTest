def catch(_mapp, cxy, xy):
    global catcher
    rtv = 0
    cx, cy = cxy
    x,y = xy
    rtv = _mapp[x][y][0]
    _mapp[x][y] = [99,_mapp[x][y][1]]
    if cxy != xy :
        _mapp[cx][cy] = 0
    catcher = [x,y]
    xys[rtv] = 0
    return rtv

def rotate(d):
    d += 1
    if d == -1 : d = 7
    elif d == 8 : d = 0
    return d

def runner(_mapp):
    for xy in (xys[1:]) :
        if xy == 0:
            continue
        x,y = xy
        d = _mapp[x][y][1]
        for _ in range(7):
            nx, ny = x+dx[d], y+dy[d]
            if not (0<=nx<=3 and 0<=ny<=3) or _mapp[nx][ny][0] == 99:
                d = rotate(d)
                continue
            else :
                if _mapp[nx][ny] == 0 :
                    _mapp[nx][ny] = _mapp[x][y]
                    _mapp[x][y] = 0
                    xys[_mapp[nx][ny][0]] = [nx,ny]
                else :
                    tmp = _mapp[nx][ny]
                    _mapp[nx][ny] = mapp[x][y]
                    mapp[x][y] = tmp
                    xys[_mapp[x][y][0]] = [x, y]
                    xys[_mapp[nx][ny][0]] = [nx, ny]
                break
    return _mapp

dx, dy = [0,-1,-1,0,1,1,1,0,-1], [0,0,-1,-1,-1,0,1,1,1]
xys = [0 for _ in range(17)]
mapp = [[] for _ in range(4)]
score = 0
answer = 0
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        mapp[i].append([line[j*2], line[j*2+1]])
        xys[line[j*2]] = [i,j]

catcher = [0,0]
score += catch(mapp,catcher, [0,0])
mapp = runner(mapp)
print()
