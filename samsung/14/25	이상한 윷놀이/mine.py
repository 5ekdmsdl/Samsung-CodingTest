def Input():
    n,k = map(int,input().split())
    mapp = []
    for _ in range(n):
        mapp.append(list(map(int,input().split())))
    kmapp = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        x,y,d = map(int,input().split())
        kmapp[x-1][y-1].append([_,d])
    return n,k,mapp,kmapp

def getxy(i):
    for x in range(n):
        for y in range(n):
            if kmapp[x][y] :
                for ii, k in enumerate(kmapp[x][y]) :
                    if k[0] == i :
                        return x,y,ii
    return

def Blue(Ml,nx,ny):
    d = opp[Ml[0][1]]
    Ml[0][1] = d

    nx,ny = x+dx[d], y+dy[d]

    if not (0<=nx<=n-1 and 0<=ny<=n-1) or mapp[nx][ny] == B :
        kmapp[x][y] += Ml
        return
    else :
        Move(Ml,x,y)

    return

def Red(Ml,nx,ny):
    # if len(Ml) >= 2 :
    #     aa= 1
    Ml.reverse()
    White(Ml,nx,ny)
    return

def White(Ml,nx,ny):
    kmapp[nx][ny] += Ml
    return

def Move(Ml, x, y):
    d = Ml[0][1]
    nx,ny = x+dx[d], y+dy[d]

    if not (0<=nx<=n-1 and 0<=ny<=n-1) or mapp[nx][ny] == B :
        Blue(Ml,nx,ny)
    elif mapp[nx][ny] == R :
        Red(Ml,nx,ny)
    else :
        White(Ml, nx, ny)
    return

def End():
    for x in range(n):
        for y in range(n):
            if kmapp[x][y] :
                if len(kmapp[x][y]) >= 4 :
                    return True
    return False

W,R,B = 0,1,2
dx, dy = [0,0,0,-1,1], [0,1,-1,0,0]
opp = [0,2,1,4,3]
n,k,mapp,kmapp = Input()
b = 0

for t in range(1000):
    for i in range(k):
        x,y,idx = getxy(i)
        Ml = kmapp[x][y][idx:]
        kmapp[x][y] = kmapp[x][y][:idx]

        Move(Ml, x, y)

        if End():
            b = 1
            break

    if b : break

if t+1 != 1000 :
    print(t+1)
else :
    print(-1)
