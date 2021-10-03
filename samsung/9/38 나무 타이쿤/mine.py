def Input():
    n,m = map(int, input().split())
    mapp, dps = [], []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))
    for _ in range(m):
        dps.append(list(map(int, input().split())))

    return n,m,dps,mapp

def moveds(t,d,p):
    x,y = t
    dx, dy = [0,0,-1,-1,-1,0,1,1,1], [0,1,1,0,-1,-1,-1,0,1]
    nx, ny = x+dx[d]*p , y+dy[d]*p
    if not 0<=nx<=n-1 :
        nx = nx%n
    if not 0<=ny<=n-1 :
        ny = ny%n
    return [nx, ny]

def move(d,p):
    global tmts, tmapp
    tmp = []
    for t in tmts :
        nt = moveds(t,d,p)
        tmp.append(nt)
    tmts = tmp

def work():
    dx, dy = [-1,-1,1,1], [-1,1,-1,1]
    global tmts, mapp

    for t in tmts :
        x,y = t
        mapp[x][y] += 1

    tmp = [m[:] for m in mapp]
    for t in tmts:
        x, y = t
        cnt = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<=n-1 and 0<=ny<=n-1):
                continue
            if tmp[nx][ny] >= 1 : cnt += 1
        mapp[x][y] += cnt

    # mapp = tmp

def cut():
    global tmts, mapp
    ntmts = []
    for x in range(n):
        for y in range(n):
            if [x,y] in tmts :
                continue
            if mapp[x][y] >= 2 :
                mapp[x][y] -= 2
                ntmts.append([x,y])
    tmts = ntmts

def getanswer():
    global mapp
    total = 0
    for x in range(n):
        for y in range(n):
            total += mapp[x][y]
    return total

n,m,dps,mapp = Input()
tmts = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]


tmapp = [[0 for _ in range(n)] for _ in range(n)]
for t in tmts:
    tmapp[t[0]][t[1]] = 1


for y in range(m):

    move(dps[y][0], dps[y][1])
    tmapp = [[0 for _ in range(n)] for _ in range(n)]
    for t in tmts:
        tmapp[t[0]][t[1]] = 1
    work()
    cut()
    tmapp = [[0 for _ in range(n)] for _ in range(n)]
    for t in tmts :
        tmapp[t[0]][t[1]] = 1

answer = getanswer()
print(answer)
