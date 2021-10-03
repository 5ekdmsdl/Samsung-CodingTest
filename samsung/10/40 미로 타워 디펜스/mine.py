def Input():
    n,m = map(int, input().split())
    mapp, dps  = [], []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))
    for _ in range(m):
        dps.append(list(map(int, input().split())))
    return n,m,mapp, dps

def down(i,xy):
    x,y = xy
    rtl = []

    for _ in range(i):
        x,y = x+dx[1], y+dy[1]
        rtl.append([x,y])

    return rtl

def right(i,xy):
    x, y = xy
    rtl = []

    for _ in range(i):
        x, y = x + dx[0], y + dy[0]
        rtl.append([x, y])

    return rtl

def up(i,xy):
    x, y = xy
    rtl = []

    for _ in range(i):
        x, y = x + dx[3], y + dy[3]
        rtl.append([x, y])

    return rtl

def left(i,xy):
    x, y = xy
    rtl = []

    for _ in range(i):
        x, y = x + dx[2], y + dy[2]
        rtl.append([x, y])

    return rtl

def setMove():
    x,y = start
    M = [[x,y]]
    M += down(1,[x,y])

    for i in range(2,n,2):
        M += right(i,M[-1])
        M += up(i,M[-1])

        if i+1 < n :
            M += left(i + 1, M[-1])
            M += down(i + 1,M[-1])
        else :
            M += left(i, M[-1])
    return M

def setdmapp():
    global center
    dm = [[4 for _ in range(n)] for _ in range(n)]
    a = center[0]
    for i in range(0,a+1):
        for j in range(i,n-i):
            dm[i][j] = 2
    for k, i in enumerate(list(range(n-1,a,-1))):
        for j in range(k,n-k-1):
            dm[i][j] = 0
    for x in range(n):
        for y in range(n):
            if dm[x][y] == 4 and y < center[1] :
                dm[x][y] = 1
            elif dm[x][y] == 4 and y > center[1] :
                dm[x][y] = 3

    return dm

def attack(d,p):
    global mapp, dx, dy

    x,y = center
    rtv = 0

    for i in range(1,p+1):
        nx, ny = x+dx[d]*i, y+dy[d]*i
        rtv += mapp[nx][ny]
        mapp[nx][ny] = 0

    return rtv

def move():
    global mapp
    sx, sy = start

    for i in range(len(Move)) :
        x,y = Move[i]

        if mapp[x][y] : continue
        else :
            for j in range(i+1,len(Move)-1):
                nx, ny = Move[j]
                if mapp[nx][ny] :
                    mapp[x][y] = mapp[nx][ny]
                    mapp[nx][ny] = 0
                    break

    return

def remove() :
    rtv, pre, cnt = 0, 0, 1

    for i in range(len(Move)) :
        x,y = Move[i]

        if mapp[x][y] == pre :
            cnt += 1
        else :
            if cnt >= 4 :
                for j in range(1,cnt+1):
                    px,py = Move[i-j]
                    rtv += mapp[px][py]
                    mapp[px][py] = 0
            cnt = 1
            pre = mapp[x][y]

    return rtv

def rearrange() :
    global mapp
    cnt, pre = 1, -1
    tmp = []

    for i in range(len(Move)) :
        x,y = Move[i]

        if mapp[x][y] == pre :
            cnt += 1
        elif pre == 0 : break
        else :
            if i != 0 :
            #     x1,y1 = Move[i-cnt]
            #     x2,y2 = Move[i-cnt+1]
                tmp += [cnt,pre]

            cnt = 1
            pre = mapp[x][y]

    mapp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(min(len(tmp),len(Move))) :
        x, y = Move[i]
        mapp[x][y] = tmp[i]


    return


s = 0
dx, dy = [0,1,0,-1], [1,0,-1,0] #-> 아래 <- 위

n,m,mapp, dps = Input()

center = [n//2, n//2]
start = [n//2, n//2-1]

Move = setMove()
dmapp = setdmapp()

for r in range(m):
    d,p = dps[r]
    s += attack(d,p)
    move()

    while 1 :
        rtv = remove()
        if rtv :
            s += rtv
            move()
        else : break

    rearrange()




print(s)
