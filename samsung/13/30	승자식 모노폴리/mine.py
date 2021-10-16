def Input():
    n,m,k = map(int, input().split())
    k += 1

    ps = [0 for _ in range(m)]
    for i in range(n):
        l = list(map(int, input().split()))
        for j in range(n):
            if l[j] :
                ps[l[j]-1] = [i,j]

    ds = list(map(int, input().split()))
    for i,d in enumerate(ds):
        ps[i].append(d-1)

    pds = [[[] for _ in range(4)] for _ in range(m)]
    for i in range(m):
        for j in range(4):
            l = list(map(int, input().split()))
            for a in range(4) :
                l[a] -= 1
            pds[i][j] = l

    return n,m,k,ps,pds

def contact():
    global ps
    for i, p in enumerate(ps):
        if not p : continue
        own(i, p[0], p[1])
    return

def own(i,x,y):
    global k
    mapp[x][y] = [i,k]

def countdown():
    for i in range(n):
        for j in range(n):
            if mapp[i][j] :
                mapp[i][j][1] -= 1
                if mapp[i][j][1] == 0:
                    mapp[i][j] = []
    return

def moveTo(i,x,y,d):
    global ps
    ps[i] = [x,y,d]

def move():
    for i in range(m):
        if not ps[i] : continue
        x,y,d = ps[i]
        moved = 0

        for nd in pds[i][d] :
            nx, ny = x+dx[nd], y+dy[nd]
            if not (0<=nx<=n-1 and 0<=ny<=n-1) : continue
            if not mapp[nx][ny] :
                moveTo(i,nx,ny,nd)
                # own(i,nx,ny)
                moved = 1
                break

        if not moved :
            for nd in pds[i][d]:
                nx, ny = x + dx[nd], y + dy[nd]
                if not (0 <= nx <= n - 1 and 0 <= ny <= n - 1): continue
                if mapp[nx][ny] and mapp[nx][ny][0] == i:
                    moveTo(i, nx, ny, nd)
                    # own(i, nx, ny)
                    break
    return

def remove():
    cnts = {}

    for i in range(m):
        if not ps[i] : continue
        x,y,d = ps[i]
        if (x,y) in cnts.keys() :
            cnts[(x,y)].append(i)
        else :
            cnts[(x,y)] = [i]

    for (x,y), p in cnts.items():
        if len(p) >= 2 :
            p.sort(reverse = True)

            for a in p[:-1] :
                ps[a] = []

    return

def ended():
    if ps[1:] == [[] for _ in range(m-1)]:
        return True
    return False

dx, dy = [-1,1,0,0], [0,0,-1,1]
n,m,k,ps,pds = Input()
mapp = [[[] for _ in range(n)] for _ in range(n)]

contact()
countdown()

for t in range(1000):
    move()
    remove()
    contact()
    countdown()

    if ended() :
        break

if t == 999 :
    print(-1)
else :
    print(t+1)

