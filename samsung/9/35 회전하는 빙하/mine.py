from collections import deque

def exp2(n):
    nn = 2
    for _ in range(n-1):
        nn *= 2
    return nn

def Input():
    n,q = map(int, input().split())
    nn = exp2(n)
    mapp = []
    for i in range(nn):
        mapp.append(list(map(int, input().split())))
    Ls = list(map(int, input().split()))
    return n,q,mapp,Ls,nn

def getpoints(_L,sp1,ep1,sp2, ep2):
    L = exp2(_L)
    ps = []
    for x in range(sp1,ep1,L):
        for y in range(sp2,ep2,L):
            ps.append((x,y))
    return ps

def rotateBlk(p,L):
    global mapp
    l = exp2(L)
    nBlk = []
    Blk = mapp[p[0]:p[0]+l]
    for i in range(len(Blk)):
        Blk[i] = Blk[i][p[1]:p[1]+l]

    for j in range(0, l, 1):
        line = []
        for i in range(l - 1, -1, -1):
            line.append(Blk[i][j])
        nBlk.append(line)
    # mapp[p[0]:p[0] + l][p[1]:p[1] + l] = nBlk
    # print()
    for x, i in enumerate(list(range(p[0], p[0]+l))):
        for y, j in enumerate(list(range(p[1], p[1]+l))):
            mapp[i][j] = nBlk[x][y]
    return

def rotate(L):
    ps = getpoints(L,0,nn,0,nn)
    for p in ps :
        pps = getpoints(L-1,p[0],p[0]+exp2(L),p[1],p[1]+exp2(L))
        for pp in pps :
            rotateBlk(pp,L-1)
    return

def melt():
    global mapp, nn
    _mapp = [[[] for _ in range(nn)] for _ in range(nn)]
    for i in range(nn) :
        for j in range(nn):
            _mapp[i][j] = mapp[i][j]
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    for x in range(nn):
        for y in range(nn):
            if not mapp[x][y] :
                continue
            cnt = 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if not (0<=nx<=nn-1 and 0<=ny<=nn-1) :
                    continue
                if mapp[nx][ny] :
                    cnt += 1
            if cnt < 3 :
                _mapp[x][y] -= 1
    mapp = _mapp
    return

def sumofIce():
    rtv = 0
    for x in range(nn):
        for y in range(nn):
            if mapp[x][y] :
                rtv += mapp[x][y]
    return rtv

def runQ(x,y,done):
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    q = deque([[x, y]])
    size = 0
    while q:
        x, y = q.popleft()
        size += 1
        done[x][y] = 1
        for i in range(4):
            nx , ny = x+dx[i], y+dy[i]
            if not (0<=nx<=nn-1 and 0<=ny<=nn-1):
                continue
            if done[nx][ny] : continue
            if mapp[nx][ny] :
                q.append([nx, ny])
    return size

def biggestIce():
    maxv = 0
    done = [[0 for _ in range(nn)] for _ in range(nn)]
    for x in range(nn):
        for y in range(nn):
            if mapp[x][y] == 0 or done[x][y] :
                done[x][y] = 1
                continue
            done[x][y] = 1

            rtv = runQ(x,y,done)
            if rtv > maxv :
                maxv = rtv
    return maxv


def main():
    global Ls
    for L in Ls :
        if L > 0 :
            rotate(L)
        melt()
    print(sumofIce())
    print(biggestIce())
    return

n,q,mapp,Ls, nn = Input()
answer = 0
main()

# print()
