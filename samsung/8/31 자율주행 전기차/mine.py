from collections import deque
INF = int(1e9)

def getdist(p1, p2):
    global mapp
    dx, dy = [0,0,-1,1],[-1,1,0,0]
    tmp = [[INF]*n for _ in range(n)]
    q = deque([[p1,0]])
    tmp[p1[0]][p1[1]] = 0
    while q:
        p,d = q.popleft()
        for i in range(4):
            np = p[0]+dx[i], p[1]+dy[i]
            if 0<=np[0]<=n-1 and 0<=np[1]<=n-1 :
                if mapp[np[0]][np[1]] == 0 :
                    if tmp[np[0]][np[1]] > d+1 :
                        tmp[np[0]][np[1]] = d+1
                        q.append([np, d+1])
    return tmp[p2[0]][p2[1]]

def chooserider():
    mind, minr = INF, 0
    for r in riders:
        start = [r[0],r[1]]
        dst = [r[2],r[3]]
        sd = abs(taxi[0]-start[0]) + abs(taxi[1]-start[1])
        if sd > mind : continue
        d = getdist(taxi, start)
        if d <= mind :
            if minr == 0 :
                mind, minr = d,r
            if sorted([[mind, minr],[d,r]])[0] == [d,r] :
                mind, minr = d, r
    return [mind, minr]

mapp = []
n,m,c = map(int, input().split())
for _ in range(n):
    mapp.append(list(map(int, input().split())))
taxi = list(map(int, input().split()))
taxi[0] -= 1
taxi[1] -= 1
riders = []
for _ in range(m):
    riders.append(list(map(int, input().split())))
for i in range(len(riders)):
    for j in range(len(riders[i])):
        riders[i][j] -= 1

result = 1
for t in range(m):
    distA, r = chooserider()
    if distA > c :
        result = 0
        break
    taxi = [r[0],r[1]]
    c -= distA
    riders.remove(r)
    distB = getdist(taxi, [r[2],r[3]])
    if distB > c :
        result = 0
        break
    taxi = [r[2],r[3]]
    c -= distB
    c += distB*2

if result :
    print(c)
else :
    print(-1)
