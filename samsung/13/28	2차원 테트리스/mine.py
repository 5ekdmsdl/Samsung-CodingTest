def makeBlk(t,x,y):
    if t == 1 :
        return [[x,y]]
    elif t == 2 :
        return [[x,y], [x,y+1]]
    elif t == 3:
        return [[x,y], [x+1, y]]

def Y2R(blk):
    nblk = []
    for b in blk :
        x,y = b
        nx,ny = y,3-x
        nblk.append([nx,ny])
    return nblk

def new(blk):
    nblk = []
    for b in blk :
        nblk.append([b[0]+1, b[1]])
    return nblk

def move(blk, m):
    stop = 0
    while not stop :
        nblk = new(blk)

        for n in nblk :
            x,y = n
            if not 0<=x<=R-1 or m[x][y] == 1 :
                stop = 1
                break

        if not stop :
            blk = nblk

    for b in blk :
        m[b[0]][b[1]] = 1

    return m

def Full(m):
    global scr
    nm = []

    for r in range(R-1,-1,-1):
        if m[r] == [1,1,1,1] :
            scr += 1
        else :
            nm = [m[r]] + nm

    for _ in range((len(m) - len(nm))):
        nm = [[0,0,0,0]] + nm

    return nm

def Light(m):
    nm = [mm[:] for mm in m]
    for r in lightzone:
        if 1 in m[r] :
            nm = [[0,0,0,0]] + nm[:-1]
    return nm

def getans():
    ans = 0
    for i in range(R):
        for j in range(4):
            ans += Ym[i][j] + Rm[i][j]
    return ans

R = 10
scr = 0
lightzone = [4,5]
k = int(input())
Ym = [[0 for _ in range(4)] for _ in range(R)]
Rm = [[0 for _ in range(4)] for _ in range(R)]

for i in range(k):
    t,x,y = map(int, input().split())
    Yblk = makeBlk(t,x,y)
    Rblk = Y2R(Yblk)

    for y in Yblk :
        Ym[y[0]][y[1]] = 1
    a = 1
    for y in Yblk :
        Ym[y[0]][y[1]] = 0

    for y in Rblk:
        Rm[y[0]][y[1]] = 1
    a = 1
    for y in Rblk:
        Rm[y[0]][y[1]] = 0

    
    Ym = move(Yblk, Ym)
    Rm = move(Rblk, Rm)

    Ym = Full(Ym)
    Rm = Full(Rm)

    Ym = Light(Ym)
    Rm = Light(Rm)

ans = getans()

print(scr)
print(ans)
