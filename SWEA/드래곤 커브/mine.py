dx, dy = [0,-1,0,1],[1,0,-1,0]

def rotate(target, pivot):
    xg, yg = pivot[0]-target[0], pivot[1]-target[1]
    return (pivot[0]-yg, pivot[1]+xg)

def func(d,g):
    points = [(0,0)]
    x,y = dx[d], dy[d]
    points.append((x,y))
    for _ in range(g-1):
        end = points[-1]
        for i in range(len(points)-1, -1, -1):
            p = points[i]
            if end == p:
                continue
            points.append(rotate(p,end))
    return points

gen = []
for i in range(1,11):
    line = []
    for j in range(4):
        line.append(func(j,i))
    #print(line)
    gen.append(line)

# for i in range(len(gen)):
#     print(gen[i])

points = [(0,0),(1,0),(0,1),(1,1)]
result = 0
xys = []
ds = []
gs = []

def draw(xy,d,g):
    global mapp
    x,y = xy
    for nxy in gen[g][d]:
        nx, ny = x + nxy[0], y+nxy[1]
        mapp[nx][ny] = 1

n = int(input())
for _ in range(n):
    a,b,c,d = map(int,input().split())
    xys.append([a,b])
    ds.append(c)
    gs.append(d)

mapp = [[0]*100 for _ in range(100)]

for i in range(n):
    draw(xys[i], ds[i], gs[i])

for x in range(100):
    for y in range(100):
        flg = True
        for a in range(4):
            nx, ny = x + points[a][0], y+points[a][1]
            if not mapp[nx][ny] :
                flg = False
                break
        if flg :
            result += 1

for i in range(100):
    print(mapp[i])
print(result)

