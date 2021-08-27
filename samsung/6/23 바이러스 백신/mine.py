from collections import deque
INF = int(1e9)
dx, dy = [0,0,-1,1],[-1,1,0,0]

def run(ch):
    global minvalue
    q = deque()
    dmapp = [[INF] * n for _ in range(n)]
    for c in ch :
        q.append(c+[0])
        dmapp[c[0]][c[1]] = 0

    while q :
        x,y,d = q.popleft()
        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<=n-1 and 0<=ny<=n-1) : continue
            if mapp[nx][ny] == 1 : continue
            nd = d+1
            if nd < dmapp[nx][ny] :
                if mapp[nx][ny] == 0 : mapp[nx][ny] = 3
                dmapp[nx][ny] = nd
                q.append([nx, ny, nd])
    cmax = 0

    for i in range(n):
        if 0 in mapp[i] :
            minvalue = -1
            break
        for j in range(n):
            if mapp[i][j] == 3 :
                if dmapp[i][j] > cmax :
                    cmax = dmapp[i][j]

    if cmax < minvalue :
        minvalue = cmax


# a = 현재 idx
def chooseh(ch,a):
    global m,h,n
    if a == len(h) :
        if len(ch) == m :
            run(ch)
        return
    ch.append(h[a])
    chooseh(ch, a+1)
    ch.pop()
    chooseh(ch, a+1)

n,m = map(int, input().split())
mapp = []
h = []
minvalue = INF
for x in range(n):
    line = list(map(int, input().split()))
    mapp.append(line)
    if 2 in line :
        for y, l in enumerate(line) :
            if l == 2:
                h.append([x,y])

chooseh([], 0)
print(minvalue)



