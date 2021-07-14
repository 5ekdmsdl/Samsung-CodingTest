def rotate() :
    global end
    ncurve = []
    for p in curve :
        xgap, ygap = end[0]-p[0], end[1]-p[1]
        ncurve.append((end[0]-ygap, end[1]+xgap))
    for n in ncurve :
        curve[(n[0], n[1])] = 1
    end = ncurve[0]


n = int(input())
every_curve = {}

dx, dy = [0,-1,0,1], [1,0,-1,0]

for _ in range(n):
    curve = {}
    x, y, d, g = map(int, input().split())
    curve[(x,y)] = 1
    end = (x + dx[d], y + dy[d])
    curve[end] = 1
    for i in range(g) :
        rotate()
    for k in curve.keys() :
        every_curve[k] = 1 #19
    # print()

cnt, keys = 0, list(every_curve.keys())
dx, dy = [0,0,1,1], [0,1,0,1]
for k in keys :
    failed = 0
    x, y = k[0], k[1]
    for i in range(4):
        nkx, nky = x + dx[i], y + dy[i]
        if (nkx, nky) not in keys :
            failed = 1
            break
    if not failed :
        # print(x,y)
        cnt += 1
print(cnt)
