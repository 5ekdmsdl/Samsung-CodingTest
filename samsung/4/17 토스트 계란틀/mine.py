def func(x,y) :
    global finished
    included.append((x,y))
    # print(included)
    for i in range(4) :
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1 :
            now, next = mapp[x][y], mapp[nx][ny]
            # print(abs(now - next), l, r)
            if (nx, ny) not in included and (l <= abs(now - next) <= r) :
                finished = 0
                func(nx,ny)
    return


included, Included = [], []
dx, dy = [0,0,-1,1], [-1,1,0,0]
n,l,r = map(int, input().split())
mapp = []
for _ in range(n):
    mapp.append(list(map(int, input().split())))

cnt = 0
while(1) :
    finished, done = 1, []
    for x in range(n) :
        for y in range(n) :
            if (x,y) not in done :
                func(x,y) #dfs -> incldued
            if included.__len__() > 1:
                Included.append(included)
                done += included
            included = []

    if finished :
        break
    else :
        for I in Included :
            total = 0
            for i in I :
                total += mapp[i[0]][i[1]]
            avg = total // I.__len__()
            for i in I :
                mapp[i[0]][i[1]] = avg
        Included = []
        cnt += 1

print(cnt)
