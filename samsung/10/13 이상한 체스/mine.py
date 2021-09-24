def Input():
    cs,enemy = [], []
    n,m = map(int, input().split())

    for i in range(n):
        line = (list(map(int, input().split())))
        for j,l in enumerate(line) :
            if l :
                if l == 6 :
                    enemy.append((i,j))
                else :
                    cs.append([l,i,j])
    return n,m, cs,enemy

def raser(x,y,d):
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    rlist = []
    for i in range(max(n,m)):
        nx, ny = x+dx[d]*i, y+dy[d]*i
        if not (0<=nx<=n-1 and 0<=ny<=m-1) : break
        if (nx, ny) in enemy :
            rlist.append((nx,ny))
            break
        else : rlist.append((nx,ny))
    return rlist

def dfs(i):
    global blk, maxv, direction

    if i == nc:
        blist = list(blk.keys())

        # tmp = [[0 for _ in range(m)] for _ in range(n)]
        # for b in blist :
        #     tmp[b[0]][b[1]] = 1


        lb = len(blist)
        # if lb == 53 :
        #     print()
        if lb > maxv :
            maxv = lb
        return
    else :
        c,x,y = cs[i]

        tmpblk = {}
        for a in blk.keys():
            tmpblk[a] = 1
        # tmpmaxv = maxv

        for ds in direction[c] :
            Blist = []
            for d in ds :
                blist = raser(x,y,d)
                Blist += blist
            for B in Blist :
                blk[B] = 1

            # tmp = [[0 for _ in range(m)] for _ in range(n)]
            # for b in Blist:
            #     tmp[b[0]][b[1]] = 1

            dfs(i+1)
            blk = {}
            for a in tmpblk.keys():
                blk[a] = 1





direction = [
    [],
    [[0],[1],[2],[3]],
    [[0,1],[2,3]],
    [[1,2],[1,3],[0,3],[0,2]],
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    [[0,1,2,3]]
]
n,m,cs,enemy = Input()

blk, maxv, nc = {}, 0, len(cs)
answer = 0

for e in enemy :
    blk[e] = 1
dfs(0)

print(n*m - maxv)
