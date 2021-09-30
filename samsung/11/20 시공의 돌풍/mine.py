def Input():
    global W
    n,m,T = map(int, input().split())
    mapp = []
    for _ in range(n):
        l = list(map(int, input().split()))
        if -1 in l :
            W.append([_,0])
        mapp.append(l)
    return n,m,T,mapp

def setwind():
    uwind, dwind = [], []
    uW, dW = W[0], W[1]

    for i in range(1,n):
        x = uW[0] - i
        uwind.append([x,uW[1]])
        if x <= 0: break
    for j in range(1,m):
        y = uW[1] + j

        uwind.append([x,y])
        if y >= m - 1: break
    for i in range(1,n):
        x = i

        uwind.append([x,y])
        if x >= uW[0]: break
    for j in range(m-2,uW[1],-1):
        y = j

        uwind.append([x,y])
        if y <= uW[1]: break

    #dWind
    for i in range(1,n):
        x = dW[0] + i
        dwind.append([x, uW[1]])
        if x >= n-1 : break


    for j in range(1,m):
        y = dW[1] + j
        dwind.append([x, y])
        if y >= m-1 : break

    for i in range(1,n):
        x = (n-1) - i
        dwind.append([x, y])
        if x <= dW[0] : break

    for j in range(m-2,uW[1],-1):
        y = j
        if y <= uW[1] : break
        dwind.append([x,y])

    return uwind, dwind

def spread():
    global mapp

    pmapp = [[0 for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if mapp[x][y] == -1 : continue
            s = mapp[x][y] // 5

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if (not (0<=nx<=n-1 and 0<=ny<=m-1)) : continue
                elif mapp[nx][ny] == -1 : continue
                pmapp[nx][ny] += s
                pmapp[x][y] -= s

    for x in range(n):
        for y in range(m):
            mapp[x][y] += pmapp[x][y]

def clean():
    #uclean
    for i in range(1,len(uwind)):
        x,y = uwind[i]
        px,py = uwind[i-1]
        mapp[px][py] = mapp[x][y]
    mapp[x][y] = 0

    # dclean
    for i in range(1, len(dwind)):
        x, y = dwind[i]
        px, py = dwind[i - 1]
        mapp[px][py] = mapp[x][y]
    mapp[x][y] = 0

def answer():
    s = 0
    for x in range(n):
        for y in range(m):
            if mapp[x][y] == -1 : continue
            s += mapp[x][y]
    return s

dx, dy = [0,0,-1,1],[-1,1,0,0]
W = []
n,m,T,mapp = Input()
uwind, dwind = setwind()

for t in range(T):
    spread()
    clean()

print(answer())



