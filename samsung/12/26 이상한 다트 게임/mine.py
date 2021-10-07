def Input():
    n,m,q = map(int, input().split())
    mapp = []
    for i in range(n):
        mapp.append(list(map(int, input().split())))
    return n,m,q,mapp

def turn(i):
    global mapp,d,k
    if d :
        tmp = mapp[i][k:] + mapp[i][:k]
    else :
        tmp = mapp[i][m-k:] + mapp[i][:m-k]
    mapp[i] = tmp
    return

def erase():
    global mapp, erased, dx, dy, m

    nmapp = [m[:] for m in mapp]

    for x in range(n):
        for y in range(m):
            if mapp[x][y] == 0 : continue
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if not 0 <= nx <= n - 1:
                    continue
                elif ny < 0:
                    ny += m
                elif m - 1 < ny:
                    ny -= m

                if mapp[x][y] == mapp[nx][ny]:
                    nmapp[x][y] = 0
                    nmapp[nx][ny] = 0
                    erased = 1

    mapp = [n[:] for n in nmapp]
    return

def Normalize():
    global mapp, tot, cnt, avg
    for x in range(n):
        for y in range(m):
            if mapp[x][y]:
                cnt += 1
                tot += mapp[x][y]
    a = 1

    if cnt:
        avg = tot // cnt

        for i in range(n):
            for j in range(m):
                if mapp[i][j]:
                    if mapp[i][j] > avg:
                        mapp[i][j] -= 1
                    elif mapp[i][j] < avg:
                        mapp[i][j] += 1
    return

def answer():
    global ans
    for x in range(n):
        for y in range(m):
            if mapp[x][y]:
                ans += mapp[x][y]
    return

dx, dy = [0,0,-1,1], [-1,1,0,0]
n,m,q,mapp = Input()

for t in range(q):
    erased = 0
    tot, cnt, avg = 0, 0, 0

    x,d,k = map(int, input().split())

    for i in range(n):
        if (i+1) % x == 0:
            turn(i)

    erase()

    if not erased :
        Normalize()

ans = 0
answer()

print(ans)
