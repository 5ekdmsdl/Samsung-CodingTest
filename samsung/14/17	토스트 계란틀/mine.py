from collections import deque

def Func():
    global Es, mapp

    for es in Es :
        if len(es) == 1: continue
        tot = 0

        for e in es :
            x,y = e
            tot += mapp[x][y]

        avg = tot // len(es)

        for e in es :
            x, y = e
            mapp[x][y] = avg
    Es = []

    return

def RunQ(x,y):
    es = [[x,y]]
    q = deque([[x,y]])

    # for es in Es :
    #     if [x,y] in es :
    #         tt = 1

    while q :
        x,y = q.popleft()

        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]

            if not (0<=nx<=n-1 and 0<=ny<=n-1) : continue

            if [nx,ny] not in es and L <= abs(mapp[nx][ny] - mapp[x][y]) <= R :
                es.append([nx, ny])
                q.append([nx,ny])

    return es

# 2000 * (2500 + 2500 * (4+) + 2500)

def Arrange():
    global visited, tmp, mapp

    end = 1
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if visited[x][y] : continue

            es = RunQ(x,y)
            Es.append(es)

            for e in es :
                visited[e[0]][e[1]] = 1

            if len(es) != 1 :
                end = 0

    Func()

    return end


dx, dy = [0,0,-1,1], [-1,1,0,0]
n, L, R = map(int, input().split())

mapp = []
for _ in range(n):
    mapp.append(list(map(int, input().split())))

visited, tmp = [], []
Es = []


for t in range(2000):
    end = Arrange()
    if end :
        break

print(t)
