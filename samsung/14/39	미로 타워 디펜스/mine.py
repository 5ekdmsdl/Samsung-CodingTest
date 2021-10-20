def Input():
    n,m = map(int, input().split())
    mapp, dps = [], []

    for _ in range(n):
        mapp.append(list(map(int, input().split())))

    for _ in range(m):
        dps.append(list(map(int, input().split())))

    return n,m, mapp, dps

def move(d,s):
    global nxy, pos

    for i in range(1,s+1):
        nx, ny = pos[0]+dx[d]*i, pos[1]+dy[d]*i
        nxy.append([nx,ny])

    pos = [nx,ny]

    return

def setnxy():
    global nxy

    move(1,1) #down

    for i in range(2,n,2):
        move(0,i) #right
        move(3,i) #up
        move(2,i+1) #left

        if i+1 != n :
            move(1,i+1) #down

    nxy = nxy[:-1]
    return

def Attack():
    global t, scr
    d, p = dps[t]

    for s in range(1,p+1):
        nx, ny = center[0]+dx[d]*s , center[1]+dy[d]*s

        scr += mapp[nx][ny]
        mapp[nx][ny] = 0

    return

def Move():
    global nxy, start, mapp

    nmapp = [[0 for _ in range(n)] for _ in range(n)]
    dest = 0

    for i, xy in enumerate(nxy) :
        x,y = xy

        if mapp[x][y] == 0:
            continue

        nmapp[nxy[dest][0]][nxy[dest][1]] = mapp[x][y]

        dest += 1

    a = 1

    mapp = [n[:] for n in nmapp]
    return

def Same4():
    global nxy, start, mapp, scr

    end = True
    mon = 0
    cnt = 0

    nmapp = [n[:] for n in mapp]

    for i, xy in enumerate(nxy) :
        x,y = xy

        if mapp[x][y] == mon :
            cnt += 1
        else :
            if cnt >= 4:
                end = False
                for idx in range(i-cnt,i) :
                    tx, ty = nxy[idx]
                    nmapp[tx][ty] = 0
                scr += cnt * mon

            mon = mapp[x][y]
            cnt = 1

    mapp = [n[:] for n in nmapp]

    return end

def Arrange():
    global nxy, start, mapp, scr
    tmp = []
    mon = 0
    cnt = 0
    idx = 0

    for i, xy in enumerate(nxy):
        x, y = xy

        # if mapp[x][y] == 0 : break

        if mapp[x][y] == mon:
            cnt += 1
        else:
            if i != 0 :
                tmp += [cnt, mon]

            mon = mapp[x][y]
            cnt = 1

    mapp = [[0 for _ in range(n)] for _ in range(n)]

    for i, xy in enumerate(nxy[:min(len(nxy), len(tmp))]) :
        mapp[xy[0]][xy[1]] = tmp[i]

    return


dx, dy = [0,1,0,-1], [1,0,-1,0]
n,m, mapp, dps = Input()
scr = 0
center =  [n//2, n//2]
start = [center[0], center[1]-1]

pos, nxy = start, [start]
setnxy()

for t in range(m):
    Attack()

    Move()

    while 1:
        end = Same4()
        if end : break

        Move()

    Arrange()


print(scr)
