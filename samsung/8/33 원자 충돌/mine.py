def alldirsame(ms):
    ds1 = [0, 2, 4, 6]
    ds2 = [1, 3, 5, 7]
    if ms[0][2] in ds1 :
        default = ds1
    else : default = ds2
    for m in ms[1:] :
        if m[2] in default :
            continue
        else : return False
    return True

dx, dy = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]
def moveAtoms():
    global mapp
    done = []
    for x in range(n):
        for y in range(n):
            if mapp[x][y] :
                for m in mapp[x][y] :
                    if m in done : continue
                    else : done.append(m)
                    ms, s, d = m
                    nx, ny = x+dx[d]*s, y+dy[d]*s
                    if not (0<=nx<=n-1 and 0<=ny<=n-1):
                        nx = nx % n
                        ny = ny % n
                    mapp[x][y].remove([ms, s, d])
                    mapp[nx][ny].append([ms, s, d])
    return

def mergeAtoms():
    global mapp
    tomerge = []
    for x in range(n):
        for y in range(n):
            if len(mapp[x][y]) >= 2 :
                tomerge.append([x,y])
    for [x,y] in tomerge:
        ms = mapp[x][y]
        tms, tv = 0,0
        for m in ms :
            tms += m[0]
            tv += m[1]
        if alldirsame(ms):
            nds =[0,2,4,6]
        else : nds = [1,3,5,7]
        nms, nv = tms//5, tv//len(ms)
        mapp[x][y] = []
        if nms == 0:
            continue
        for i in range(4):
            mapp[x][y].append([nms, nv, nds[i]])
    return

n,m,k = map(int, input().split())
mapp = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y, ms, s, d = map(int, input().split())
    mapp[x-1][y-1].append([ms, s, d])

for _ in range(k):
    moveAtoms()
    mergeAtoms()

answer = 0
for m in mapp :
    for mm in m :
        for mmm in mm :
             answer += mmm[0]
print(answer)
