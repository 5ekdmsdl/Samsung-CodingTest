def Ride(i, favs):
    global mapp
    tmapp = [[[] for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            tmp = [-1, -1, x, y]

            if not mapp[x][y] :
                tmp = [0, 0, x, y]
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if not (0<=nx<=n-1 and 0<=ny<=n-1) : continue
                    if mapp[nx][ny] in favs :
                        tmp[0] += 1
                    elif mapp[nx][ny] == 0 :
                        tmp[1] += 1

            tmapp[x][y] = tmp[:]

    l = []
    for t in tmapp :
        l += t
    l.sort(key=lambda a : [-a[0], -a[1]])
    x,y = l[0][2], l[0][3]
    mapp[x][y] = i
    return


def ans():
    scr = [0,1,10,100,1000]
    ans = 0
    for x in range(n):
        for y in range(n):
            cnt = 0
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if not (0 <= nx <= n - 1 and 0 <= ny <= n - 1): continue
                if mapp[nx][ny] in ns[mapp[x][y]]:
                    cnt += 1
            ans += scr[cnt]
    return ans


dx, dy = [0,0,-1,1],[-1,1,0,0]
n = int(input())
N = n*n
mapp = [[0 for _ in range(n)] for _ in range(n)]
ns = {}

for _ in range(N):
    l = list(map(int, input().split()))
    ns[l[0]] = l[1:]

for num, favs in ns.items():
    Ride(num, favs)

print(ans())
