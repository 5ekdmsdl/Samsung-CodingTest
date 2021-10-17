from collections import deque

def Input():
    n, q = map(int, input().split())
    N = 2 ** n
    mapp = []
    for _ in range(N):
        mapp.append(list(map(int, input().split())))
    Ls = list(map(int, input().split()))

    return n, q, mapp, Ls

def rotateblks(x,y,s):
    global mapp
    nmapp = [m[:] for m in mapp]

    d = 0
    for i in range(x, x+s, s//2):
        for j in range(y, y + s, s // 2):
            ni, nj = i + dx[d] * s//2, j + dy[d] * s//2
            d += 1

            for a in range(0, s//2):
                for b in range(0, s//2):
                    nmapp[ni+a][nj+b] = mapp[i+a][j+b]

    mapp = [m[:] for m in nmapp]
    return

def rotate(L):
    if L == 0 : return

    for i in range(0,N,2**L):
        for j in range(0, N, 2 ** L):
            rotateblks(i,j,2**L)

def melt():
    global mapp

    nmapp = [m[:] for m in mapp]

    for x in range(N):
        for y in range(N):
            if mapp[x][y] == 0 : continue

            cnt  = 0
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if not (0<=nx<=N-1 and 0<=ny<=N-1): continue

                if mapp[nx][ny] : cnt +=1
            if cnt < 3 :
                nmapp[x][y] -= 1

    mapp = [m[:] for m in nmapp]
    return

def getsum():
    global mapp
    total = 0

    for i in range(N):
        for j in range(N):
            total += mapp[i][j]

    return total

def getsize(x,y):
    global done

    q = deque([(x,y)])
    done[x][y] = 1
    s = 0

    while q :
        x,y = q.popleft()
        s += 1

        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]
            if not (0<=nx<=N-1 and 0<=ny<=N-1) : continue
            if done[nx][ny] or mapp[nx][ny] == 0 : continue

            done[nx][ny] = 1
            q.append([nx,ny])

    return s

def getBunch():
    global done, mapp

    maxB = 0
    done = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not done[i][j] and mapp[i][j] :
                s = getsize(i,j)
                if s > maxB : maxB = s

    return maxB


dx, dy = [0,1,-1,0], [1,0,0,-1]
n, q, mapp, Ls = Input()
N = 2**n

for L in Ls :
    rotate(L)
    melt()


done = []

print(getsum())
print(getBunch())
