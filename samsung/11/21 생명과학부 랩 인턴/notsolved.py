def Input():
    n,m,k = map(int, input().split())
    mapp = [[[] for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y,d,s,b = map(int, input().split())
        mapp[x-1][y-1].append([d,s,b])
    return n,m,k ,mapp

def nxy(tmp,x,y) :
    dx, dy = [0,-1,1,0,0], [0,0,0,1,-1]
    opp = [0,2,1,4,3]
    s,d,b = tmp
    nd = d

    nx, ny = x+dx[d]*s, y+dy[d]*s

    if not (0<=nx<=n-1):
        if nx > n-1 :
            g = nx % (2*n)
            if 0<=g<=n-1 :
                nx = g
                nd = opp[d]
            else :
                nx = (n-1) - g

        elif nx < 0 :
            g = nx % (2 * n)
            if 0<=g<=n-1 :
                nx = g
            else :
                nx = (n-1) - g
                nd = opp[d]


    if not (0 <= ny <= m - 1):
        if ny > m-1 :
            g = ny % (2 * m)
            if 0 <= g <= n - 1:
                ny = g
                nd = opp[d]
            else:
                ny = (m - 1) - g

        elif ny < 0 :
            g = ny % (2 * m)
            if 0 <= g <= m - 1:
                ny = g
            else:
                ny = (m - 1) - g
                nd = opp[d]




    return nx,ny,nd

def remove(j):
    a = 0
    for i in range(n):
        if mapp[i][j] :
            a = mapp[i][j][0]
            mapp[i][j] = []
            return a[2]
    return a

def move():
    global mapp
    nmapp = [[[] for _ in range(m)] for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if mapp[x][y] :
                nx, ny, nd = nxy(mapp[x][y][0],x,y)
                l = [mapp[x][y][0][0],nd,mapp[x][y][0][2]]
                nmapp[nx][ny].append(l)

    mapp = [n[:] for n in nmapp]


    return

def eat():
    for x in range(n):
        for y in range(m):
            if len(mapp[x][y]) >= 2 :
                tmp = mapp[x][y]
                tmp.sort(key=lambda a : -a[2])
                mapp[x][y] = [tmp]
    return

n,m,k ,mapp = Input()
ans = 0

for j in range(m):
    ans += remove(j)
    move()
    eat()

