from collections import deque

def Input():
    n,L,R = map(int, input().split())
    mapp = []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))
    return n,L,R,mapp

def shouldMerge(x,y,nx,ny):
    if L <= abs(mapp[nx][ny] - mapp[x][y]) and abs(mapp[nx][ny] - mapp[x][y]) <= R:
        return True
    return False

def getes(x,y):
    global done, mapp
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    visited = [d[:] for d in done] # deque에서 확인했음

    es = [[x, y]] # 합쳐야할 틀 목록
    q = deque([[x, y]])
    visited[x][y] = 1

    while (q):
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx <= n - 1 and 0 <= ny <= n - 1):
                continue

            if visited[nx][ny] == 1 : continue
            visited[nx][ny] = 1

            if shouldMerge(x, y, nx, ny):
                es.append([nx, ny])
                q.append([nx, ny])

    return es

def getNew(es):
    global  mapp
    total = 0

    for e in es:
        x, y = e
        total += mapp[x][y]

    a = total // len(es)

    return a

def runQ(x,y):
    global done, mapp, Es
    es = getes(x,y)

    # if len(es) >= 2 :
    #     a = getNew(es)
    #     if a in Es.keys():
    #         Es[a] += es
    #     else :
    #         Es[a] = es
    a = getNew(es)
    for e in es :
        x,y = e
        done[x][y] = a

def Egg():
    global mapp
    for x in range(n):
        for y in range(n):
            if done[x][y] : continue

            runQ(x,y)

            # done[x][y] = 1

def setNew():
    global Es, mapp

    for v, xys in Es.items():
        for xy in xys :
            x,y = xy
            mapp[x][y] = v


n,L,R,mapp = Input()
cnt = 0

while(1):
    # Es = {}
    done = [[0 for _ in range(n)] for _ in range(n)] # 어떤 그룹에 이미 속해있음

    Egg()

    changed = 0
    for i in range(n):
        if mapp[i] != done[i] :
            changed = 1
            break

    if changed :
        mapp = [d[:] for d in done]
        cnt += 1
    else :
        break

    # if Es :
    #     setNew()
    #     cnt += 1
    # else :
    #     break

print(cnt)
