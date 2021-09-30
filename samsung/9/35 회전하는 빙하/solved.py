from collections import deque

def Input():
    n,q = map(int, input().split())
    mapp = []
    for _ in range(exp2(n)):
        mapp.append(list(map(int, input().split())))
    ls = list(map(int, input().split()))
    return n,q,mapp,ls

def exp2(a):
    b= 1
    for i in range(a):
        b *= 2
    return b

def copy(x1,x2,y1,y2):
    global mapp
    rtv = []
    for i in range(x1,x2):
        rtv.append(mapp[i][y1:y2])
    return rtv

def cat(tmp,x1,x2,y1,y2 ):
    global mapp
    for a,i in enumerate(list(range(x1, x2))):
        mapp[i][y1:y2] = tmp[a]

def rotateLevel(x,y,m):
    global mapp
    d = m // 2
    if m == 1:
        return
    tmp1 = copy(x,x+d, y,y+d)
    tmp2 = copy(x,x+d, y+d,y+2*d)
    tmp3 = copy(x+d,x+2*d, y,y+d)
    tmp4 = copy(x+d,x+2*d, y+d,y+2*d)

    cat(tmp1, x,x+d, y+d,y+2*d)
    cat(tmp2, x+d,x+2*d, y+d,y+2*d)
    cat(tmp4, x+d,x+2*d, y,y+d)
    cat(tmp3, x,x+d, y,y+d)

    return

def rotate(L):
    if L == 0:
        return
    d = exp2(L)

    for x in range(0,exp2(n),d):
        for y in range(0, exp2(n), d):
            rotateLevel(x,y,d)

def melt():
    global mapp
    dx, dy = [0,0,-1,1],[-1,1,0,0]
    nmapp = [m[:] for m in mapp]
    for x in range(exp2(n)):
        for y in range(exp2(n)):
            if mapp[x][y] == 0 : continue
            cnt = 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if not (0<=nx<=exp2(n)-1 and 0<=ny<=exp2(n)-1):
                    continue
                if mapp[nx][ny] :
                    cnt += 1
            if cnt < 3 :
                nmapp[x][y] -= 1
    mapp = [n[:] for n in nmapp]
    return

def getsum():
    global mapp
    rtv = 0
    for x in range(2**n):
        for y in range(2**n):
            if mapp[x][y] :
                rtv += mapp[x][y]
    return rtv

def runQ(x,y):
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    q = deque([[x,y]])
    rtl = [[x,y]]
    visited = [[0 for _ in range(2**n)] for _ in range(2**n)]
    visited[x][y] = 1

    while(q):
        x,y = q.popleft()
        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]
            if not (0<=nx<=2**n-1 and 0<=ny<=2**n-1) : continue
            if visited[nx][ny] : continue

            if mapp[nx][ny] :
                rtl.append([nx,ny])
                visited[nx][ny] = 1
                q.append([nx, ny])

    return rtl


def getbiggest():
    rtv = 0
    visited = [[0 for _ in range(2**n)] for _ in range(2**n)]

    for x in range(2**n):
        for y in range(2**n):
            if mapp[x][y] and not visited[x][y] :
                Is = runQ(x,y)

                if Is :
                    rtv = max(rtv, len(Is))
                    for i in Is :
                        visited[i[0]][i[1]] = 1

    return rtv


n,q,mapp,ls = Input()
for l in ls :
    rotate(l)
    melt()

a = getsum()
b = getbiggest()

print(a)
print(b)
