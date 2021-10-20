def Input():
    n,m = map(int, input().split())
    mapp = []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))
    dps = []
    for _ in range(m):
        dps.append(list(map(int, input().split())))
    return n,m,mapp,dps

def Move():
    global t, stim
    d,p = dps[t]

    tmp = []

    for s in stim :
        x,y = s
        nx, ny = x+dx[d]*p, y+dy[d]*p
        if not (0<=nx<=n-1 and 0<=ny<=n-1):
            nx = nx % n
            ny = ny % n

        tmp.append([nx,ny])

    stim = tmp[:]
    return

def Work():
    global t, stim, mapp

    for s in stim :
        x,y = s
        mapp[x][y] += 1

    nmapp = [m[:] for m in mapp]

    for s in stim:
        x, y = s
        cnt = 0

        for _ in range(2,9,2):
            nx, ny = x+dx[_], y+dy[_]
            if not (0 <= nx <= n - 1 and 0 <= ny <= n - 1): continue

            if mapp[nx][ny] :
                cnt += 1

        nmapp[x][y] += cnt

    mapp = [m[:] for m in nmapp]
    return

def Cut():
    global t, stim, mapp

    tmp = []

    for x in range(n):
        for y in range(n):
            if [x,y] not in stim and mapp[x][y] >= 2 :
                mapp[x][y] -= 2
                tmp.append([x,y])

    stim = tmp[:]

    return

def ans():
    ans = 0

    for x in range(n):
        for y in range(n):
            ans += mapp[x][y]

    return ans


dx, dy = [0,0,-1,-1,-1,0,1,1,1], [0,1,1,0,-1,-1,-1,0,1]
n,m,mapp,dps = Input()
stim = [[n-2,0],[n-1,0],[n-2,1],[n-1,1]]

for t in range(m):
    Move()
    Work()
    Cut()


print(ans())
