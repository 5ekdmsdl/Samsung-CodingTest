def Input():
    n = int(input())
    pds = [[]]
    for _ in range(8):
        pds.append(list(map(int, input().split())))
    kcs = []
    for _ in range(n):
        kcs.append(list(map(int, input().split())))

    return n, pds, kcs

def Blk(col,k):
    for i in range(R):
        if mapp[i][col] : continue
        mapp[i][col] = k
        break
    return

def Up():
    global mapp, scr, ans
    a = 1
    nmapp = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):

            if mapp[i][j] :
                if i == 0 :
                    nmapp[i][j] = mapp[i][j]
                    continue

                ci = i
                while 1:

                    ni = ci - 1

                    if ni == 0 :
                        if nmapp[ni][j] == 0:
                            nmapp[ni][j] = mapp[i][j]
                            # nmapp[i][j] = 0
                            break
                        else :
                            nmapp[ci][j] = mapp[i][j]
                            # mapp[i][j] = 0
                            break

                    if nmapp[ni][j] == 0 :
                        ci = ni

                    else :
                        nmapp[ci][j] = mapp[i][j]
                        # mapp[i][j] = 0
                        break

    mapp = [n[:] for n in nmapp]
    return

def Score():
    global mapp, scr, ans
    while 1 :
        if not 0 in mapp[0] :
            scr += 1
            mapp = mapp[1:] + [[0,0,0,0]]
            Up(mapp)
        else : break

def Rearrange():
    global mapp, scr, ans
    nmapp = [[[] for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if mapp[i][j] :
                pd = pds[mapp[i][j]]
                for d in pd :
                    nx, ny = i+dx[d], j+dy[d]
                    if not (0<=nx<=R-1 and 0<=ny<=C-1): continue
                    else :
                        nmapp[nx][ny].append(mapp[i][j])
                        break
    for i in range(R):
        for j in range(C):
            if len(nmapp[i][j]) >= 2 :
                nmapp[i][j].sort()
                nmapp[i][j] = nmapp[i][j][0]
            elif nmapp[i][j] == []:
                nmapp[i][j] = 0
            else :
                nmapp[i][j] = nmapp[i][j][0]

    mapp = [n[:] for n in nmapp]
    Up()

    return

def Run(col,k):
    Blk(col, k)
    Score()
    Rearrange()
    Score()

    return

def dfs(i):
    global ans, scr, mapp
    if i == n :
        if ans < scr : scr = ans
        return

    k, c = kcs[i]

    if c == 0:
        mtmp = [m[:] for m in mapp]
        tmp = scr

        for col in range(4):
            Run(col,k)

            mapp = [t[:] for t in mtmp]
            scr = tmp

    else :
        Run(c-1, k)

    dfs(i+1)
    return

R, C = 100,4
dx, dy = [0,-1,-1,0,1,1,1,0,-1], [0,0,-1,-1,-1,0,1,1,1]
n, pds, kcs = Input()
ans, scr = 0, 0
mapp = [[0 for _ in range(C)] for _ in range(R)]

dfs(0)



print(ans)
