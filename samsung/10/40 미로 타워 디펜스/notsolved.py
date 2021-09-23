def Input():
    n,m = map(int, input().split())
    mapp, dps  = [], []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))
    for _ in range(m):
        dps.append(list(map(int, input().split())))
    return n,m,mapp, dps

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

def nxy(x,y):
    global dmapp
    d = dmapp[x][y]
    nx, ny = x+dx[d], y+dy[d]
    return nx, ny

def move():
    ox, oy = center
    while(1): #원소별
        ox, oy = nxy(ox, oy)

        if mapp[ox][oy] != 0: continue
        if [ox, oy] == [0, -1] : break
        # dd
        x,y = ox, oy
        while(1):

            nx, ny = nxy(x,y)
            if [nx, ny] == [0, -1]: break
            if mapp[nx][ny] == 0 :
                x,y = nx, ny
            else :
                x, y = nx, ny
                if [ox, oy] != [x,y]:
                    mapp[x][y] = mapp[ox][oy]
                    mapp[x][y] = 0
                    ox, oy = x,y
                break

n,m,mapp, dps = Input()
s = 0
dx, dy = [0,1,0,-1], [1,0,-1,0]
center = [n//2, n//2]
start = [n//2, n//2-1]
dmapp = setdmapp()


for r in range(m):
    d,p = dps[r]
    s += attack(d,p)
    move()


print()
