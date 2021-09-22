from collections import deque

def Input():
    global n,mapp,m
    mapp = []
    n,m = map(int, input().split())
    for _ in range(n):
        mapp.append(list(map(int, input().split())))

def bfs(x,y):
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    q = deque([[x,y]])
    c = mapp[x][y]
    done = [[0 for _ in range(n)] for _ in range(n)]
    done[x][y] = 1
    Rcnt = 0
    Blist = []
    while q :
        x,y = q.popleft()
        Blist.append([x,y])
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<=n-1 and 0<=ny<=n-1): continue
            if done[nx][ny] == 1 : continue
            done[nx][ny] = 1
            if mapp[nx][ny] == c :
                q.append([nx,ny])
            elif mapp[nx][ny] == 0 :
                q.append([nx, ny])
                Rcnt += 1
    if len(Blist) <= 1 or len(Blist) == Rcnt :
        Blist = []
    return [Rcnt, Blist]

def getGp():
    maxlen = 0
    Gp = [0,[]]
    done = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if done[x][y] :
                continue

            if mapp[x][y] in list(range(1,m+1)):
                gp = bfs(x,y)

                for g in gp[1] :
                    if mapp[g[0]][g[1]] in list(range(1, m + 1)):
                        done[g[0]][g[1]] = 1

                if maxlen == 0 :
                    Gp = gp
                    maxlen = len(gp[1])
                    continue

                if len(gp[1]) > maxlen :
                    Gp = gp
                    maxlen = len(gp[1])
                elif len(gp[1]) == maxlen :
                    if Gp[0] > gp[0] :
                        Gp = gp
                        maxlen = len(gp[1])
                    elif Gp[0] == gp[0] :
                        Gp[1].sort(key=lambda a: [-a[0], a[1]])
                        gp[1].sort(key=lambda a: [-a[0], a[1]])

                        for G in Gp[1] :
                            if mapp[G[0]][G[1]] == 0 :
                                continue
                            else :
                                a = G
                                break

                        for G in gp[1] :
                            if mapp[G[0]][G[1]] == 0 :
                                continue
                            else :
                                b = G
                                break

                        if a[0] < b[0] :
                            Gp = gp
                            maxlen = len(gp[1])
                        elif a[0] == b[0]:
                            if a[1] > b[1] :
                                Gp = gp
                                maxlen = len(gp[1])
    if Gp == [0,[]] or maxlen == 1:
        return []
    else :
        return Gp[1]

def removeGp(Gp):
    for g in Gp :
        x,y = g
        mapp[x][y] = -2
    return

def Grav():
    for xx in range(0,n-1):
        ox = n - 2 - xx
        for y in range(n):
            x = ox
            if mapp[x][y] == -1 or mapp[x][y] == -2:
                continue
            while(1):
                nx = x+1
                if nx >  n-1 :
                    break
                if mapp[nx][y] in list(range(-1,m+1)):
                    break
                x = nx
            if ox != x :
                mapp[x][y] = mapp[ox][y]
                mapp[ox][y] = -2
    return

def rotate():
    global mapp
    tmp = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            v = mapp[x][y]
            tmp[n-1-y][x] = v
    mapp = tmp
    return



n,m,mapp = 0,0,0
answer = 0
Input()

while(1):
    Gp = getGp()
    if Gp == [] :
        break
    answer += len(Gp)*len(Gp)
    removeGp(Gp)
    Grav()
    rotate()
    Grav()

print(answer)
