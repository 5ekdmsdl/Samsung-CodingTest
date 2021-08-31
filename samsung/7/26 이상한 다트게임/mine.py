def rotate(x,d,k):
    global mapp
    if d == 0 :
        p = mapp[x]
        np = p[m-k:m] + p[0:m-k]
    else :
        p = mapp[x]
        np = p[k:] + p[0:k]
    mapp[x] = np
    return

dx, dy = [0,0,-1,1], [-1,1,0,0]
def erase():
    global mapp
    eraselist = []
    for x in range(n):
        for y in range(m):
            if mapp[x][y] == 0 : continue
            for dir in range(4):
                nx, ny = x + dx[dir], y+ dy[dir]
                if nx == -1 or nx == n : continue
                if ny == -1 : ny = m-1
                elif ny == m : ny = 0
                if mapp[x][y] == mapp[nx][ny] :
                    eraselist.append((x,y))
                    eraselist.append((nx,ny))
    if not eraselist :
        return 0
    else :
        for e in eraselist :
            mapp[e[0]][e[1]] = 0
        return 1
    return

def normalize():
    cnt, total = 0, 0
    for x in range(n):
        for y in range(m):
            if mapp[x][y]:
                total += mapp[x][y]
                cnt += 1
    if cnt == 0 : return 0
    total = total // cnt
    for x in range(n):
        for y in range(m):
            if mapp[x][y] :
                if mapp[x][y] > total : mapp[x][y] -= 1
                elif mapp[x][y] < total : mapp[x][y] += 1

n,m,q = map(int, input().split())
mapp = []

for _ in range(n):
    mapp.append(list(map(int, input().split())))

for time in range(q) :
    x,d,k = map(int, input().split())
    t = 1
    while(x*t <= n):
        rotate(x*t-1,d,k)
        t += 1
    erased = erase()
    if not erased :
        normalize()
    # print()

answer = 0
for m in mapp :
    answer += sum(m)

print(answer)
