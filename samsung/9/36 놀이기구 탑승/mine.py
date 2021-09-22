INF = int(1e9)

def place(s,ls):
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if mapp[x][y] :
                tmp[x][y] = [-1,-1,x,y]
                continue
            a = [0,0,0,0]
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if not (0<=nx<=n-1 and 0<=ny<=n-1):
                    continue
                if mapp[nx][ny] in ls :
                    a[0] += 1
                elif mapp[nx][ny] == 0:
                    a[1] += 1
            a[2], a[3] = x, y
            tmp[x][y] = a
    tl = []
    for t in tmp :
        tl += t
    tl.sort(key= lambda a: (-a[0], -a[1]))
    nx, ny = tl[0][2], tl[0][3]
    mapp[nx][ny] = s
    return

def cntFav():
    global mapp
    Fav = [0,1,10,100,1000]
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    total = 0
    for x in range(n):
        for y in range(n):
            cnt = 0
            s = mapp[x][y]
            if not s : continue
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if not (0<=nx<=n-1 and 0<=ny<=n-1):
                    continue
                if mapp[nx][ny] in ss[s] :
                    cnt += 1
            total += Fav[cnt]
    return total

n = int(input())
m = n*n
ss = {}
mapp = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    line = list(map(int, input().split()))
    ss[line[0]] = line[1:]

for i in range(m):
    s = list(ss.keys())[i]
    ls = ss[s]
    place(s,ls)
total = cntFav()
    # print(total)


print(total)
