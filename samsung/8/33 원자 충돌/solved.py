def Input():
    global n,m,k
    n,m,k = map(int, input().split())
    mapp = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(m):
        line = list(map(int, input().split()))
        x,y,m,s,d = line
        mapp[x-1][y-1].append([m,s,d,0])
    return mapp

def nextxy(x,y,s,d):
    dx,dy = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]
    nx, ny = x+dx[d]*s, y+dy[d]*s
    if not (0<=nx<=n-1 and 0<=ny<=n-1):
        nx, ny = nx%n, ny%n
    return nx,ny

def move():
    for x in range(n):
        for y in range(n):
            if mapp[x][y]:
                tmp = []
                tmp += mapp[x][y]
                for ma in mapp[x][y] :
                    m,s,d,done = ma
                    if done or not m : continue
                    nx, ny = nextxy(x,y,s,d)
                    if [x,y] == [nx,ny] :
                        idx = tmp.index(ma)
                        tmp[idx][3] = 1
                        continue
                    ma[3] = 1
                    mapp[nx][ny].append(ma)
                    tmp.remove(ma)
                # if tmp :
                #     print()
                mapp[x][y] = tmp
    return

def direction(d):
    if d % 2 == 0 :
        return 0
    return 1

def mergeAtom(x,y):
    tm, ts, td, dflg = 0,0,direction(mapp[x][y][0][2]),0
    for ma in mapp[x][y] :
        tm += ma[0]
        ts += ma[1]
        if direction(ma[2]) != td :
            dflg = 1
    tm = tm // 5
    if tm == 0 :
        mapp[x][y] = []
        return False
    ts = ts // len(mapp[x][y])
    return [tm, ts, dflg]

def splitAtom(x,y,rtv):
    [m, s, dflg] = rtv
    if dflg :
        d = [1,3,5,7]
    else : d = [0,2,4,6,]
    mapp[x][y] = []
    for _ in range(4):
        mapp[x][y].append([m,s,d[_],1])
    return

def mergeNsplit():
    for x in range(n):
        for y in range(n):
            if len(mapp[x][y]) >= 2 :
                rtv = mergeAtom(x,y)
                if rtv :
                    splitAtom(x,y,rtv)
    return

def resetdone():
    for x in range(n):
        for y in range(n):
            if mapp[x][y] :
                for i in range(len(mapp[x][y])) :
                    mapp[x][y][i][3] = 0

def sumofAtoms():
    result = 0
    for x in range(n):
        for y in range(n):
            if mapp[x][y] :
                for i in range(len(mapp[x][y])) :
                    result += mapp[x][y][i][0]
    return result

def main():
    for i in range(k):
        move()
        mergeNsplit()
        resetdone()
        # print()
    return sumofAtoms()

n,m,k = 0,0,0
mapp = Input()
rtv = main()

print(rtv)
