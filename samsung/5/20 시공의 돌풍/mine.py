def create_upwind() :
    x,y = wind[0]
    x -= 1
    while 1 :
        upwind.append([x, y])
        x -= 1
        if not (0 <= x <= n-1 and 0 <= y <= m-1) :
            x += 1
            break
    y += 1
    while 1 :
        upwind.append([x, y])
        y += 1
        if not (0 <= x <= n-1 and 0 <= y <= m-1) :
            y -= 1
            break
    x += 1
    while 1:
        upwind.append([x, y])
        x += 1
        if x == wind[0][0]:
            upwind.append([x, y])
            break
    y -= 1
    while 1:
        upwind.append([x, y])
        y -= 1
        if y == wind[0][1]:
            break

def create_downwind() :
    x,y = wind[1]
    x += 1
    while 1 :
        downwind.append([x, y])
        x += 1
        if not (0 <= x <= n-1 and 0 <= y <= m-1) :
            x -= 1
            break
    y += 1
    while 1 :
        downwind.append([x, y])
        y += 1
        if not (0 <= x <= n-1 and 0 <= y <= m-1) :
            y -= 1
            break
    x -= 1
    while 1:
        downwind.append([x, y])
        x -= 1
        if x == wind[1][0]:
            downwind.append([x, y])
            break
    y -= 1
    while 1:
        downwind.append([x, y])
        y -= 1
        if y == wind[1][1]:
            break

def dust() :
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    d_mapp = [[0]*m for _ in range(n)]
    for i in range(n) :
        for j in range(m) :
            if [i,j] in wind : continue
            moving_dust = mapp[i][j] // 5
            for d in range(4) :
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and [nx, ny] not in wind :
                    d_mapp[nx][ny] += moving_dust
                    d_mapp[i][j] -= moving_dust

    return d_mapp

def sum_dust(d_mapp) :
    for i in range(n) :
        for j in range(m) :
            mapp[i][j] += d_mapp[i][j]
    return

def blow() :
    pre = 0
    for now in range(1, upwind.__len__()) :
        px, py = upwind[pre]
        nx, ny = upwind[now]
        mapp[px][py] = mapp[nx][ny]
        pre = now
    mapp[nx][ny] = 0

    pre = 0
    for now in range(1, downwind.__len__()):
        px, py = downwind[pre]
        nx, ny = downwind[now]
        mapp[px][py] = mapp[nx][ny]
        pre = now
    mapp[nx][ny] = 0
    return

n,m,time = map(int, input().split())
mapp = []
wind = []
upwind, downwind = [], []

for i in range(n) :
    line = list(map(int, input().split()))
    if -1 in line :
        wind.append([i,0])
    mapp.append(line)

create_upwind()
create_downwind()

for t in range(time) :
    sum_dust(dust())
    blow()

total = 0
for i in range(n) :
    for j in range(m) :
        if [i,j] in wind :
            continue
        total += mapp[i][j]

print(total)

