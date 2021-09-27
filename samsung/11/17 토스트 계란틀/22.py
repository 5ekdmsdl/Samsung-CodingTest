from collections import deque

def Input():
    n,L,R = map(int, input().split())
    mapp = []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))
    return n,L,R,mapp

def runQ(x,y):
    global done
    dx,dy = [0,0,-1,1],[-1,1,0,0]
    q = deque([[x,y]])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    sssflg, total = 1, 0
    es = [[x,y]]
    visited[x][y] = 1

    while(q):
        x,y = q.popleft()
        total += mapp[x][y]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<=n-1 and 0<=ny<=n-1):
                continue
            if visited[nx][ny] == 1 or done[nx][ny] == 1 : continue
            visited[nx][ny] = 1

            if L <= abs(mapp[nx][ny] - mapp[x][y]) <= R :
                es.append([nx,ny])
                q.append([nx,ny])

    if len(es) >= 2 :
        sssflg = 0
        a = total // len(es)
        for e in es :
            x,y = e
            nmapp[x][y] = a
            done[x][y] = 1

    return sssflg

def Egg():
    global done
    ssflg = 1
    rtv = 0
    for x in range(n):
        for y in range(n):
            if done[x][y] : continue
            done[x][y] = 1

            rtv = runQ(x,y)
            if rtv == 0 :
                ssflg = 0

    return ssflg




n,L,R,mapp = Input()

cnt = 0

while(1):
    nmapp = [n[:] for n in mapp]
    done = [[0 for _ in range(n)] for _ in range(n)]

    sflg = Egg()
    if sflg :
        break
    cnt += 1

    mapp = [n[:] for n in nmapp]


print(cnt)





