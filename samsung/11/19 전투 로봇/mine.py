from collections import deque

def Input():
    global R
    n = int(input())
    mapp = []
    for i in range(n):
        l = list(map(int, input().split()))
        if 9 in l :
            j = l.index(9)
            l[j] = 0
            R = [i,j]
        mapp.append(l)
    return n, mapp

def getd():
    global R
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    x,y = R
    dm = [[INF for _ in range(n)] for _ in range(n)]
    q = deque([R+[0]])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1

    while(q) :
        x,y,d = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if not (0<=nx<=n-1 and 0<=ny<=n-1): continue
            if mapp[nx][ny] > Rl : continue
            if visited[nx][ny] : continue

            if dm[nx][ny] > d+1 :
                dm[nx][ny] = d+1
                q.append([nx,ny,d+1])
                visited[nx][ny] = 1
    return dm

def getM():
    dmapp = getd()
    es = []
    for x in range(n):
        for y in range(n):
            if mapp[x][y] and mapp[x][y] < Rl and dmapp[x][y] <  INF:
                es.append([dmapp[x][y], x, y])
    if es :
        es.sort()
        return es[0]
    else :
        return False

def remove(m):
    global R
    R = m[1:]
    mapp[m[1]][m[2]] = 0
    return m[0]

INF = int(1e9)
R = [0,0]
n, mapp = Input()
t, cnt, Rl = 0, 0, 2

M = getM()

while(M):
    t += remove(M)
    cnt += 1
    if cnt == Rl :
        Rl += 1
        cnt = 0
    M = getM()

print(t)
