import heapq
INF = int(1e9)

def dist(xy, target) :
    return abs(xy[0] - target[0]) + abs(xy[1] - target[1])

def distance(xy, target,level):
    d_mapp = [[INF]*n for _ in range(n)]
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    q = []
    heapq.heappush(q, [0,xy])

    while q :
        step, xy = heapq.heappop(q)
        if xy == target :
            return step
        x,y = xy
        # print(x,y)
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1 and mapp[nx][ny] <= level :
                if d_mapp[nx][ny] > step+1 :
                    heapq.heappush(q, [step+1,(nx, ny)])
                    d_mapp[nx][ny] = step+1

    return INF


def findenemy() :
    global now
    min_d, min_xy = INF, (-1, -1)
    enemys = []
    global level
    if level > 6 :
        llevel = 6
    else : llevel = level
    for i in range(1,llevel) :
        lm = ms[i]
        if not lm :
            continue
        for m in lm :
            d = distance(now, m, llevel)
            if d == INF : continue
            if min_d > d :
                enemys = []
                min_d = d
                min_xy = now
                enemys.append([m,i,d])
            elif min_d == d :
                enemys.append([m,i,d])
    if enemys.__len__() > 1 :
        enemys.sort(key = lambda a : a[0])
        return enemys[0]
    elif enemys.__len__() == 1 :
        return enemys[0]
    else :
        return []


ms = [[] for _ in range(7)]

mapp = []
n = int(input())
for i in range(n):
    line = list(map(int, input().split()))
    mapp.append(line)
    for j, l in enumerate(line) :
        if l == 9 :
            now = (i,j)
        elif l :
            ms[l].append((i,j))

for m in ms :
    m.sort()

endgame, time, level = 0, 0, 2
kill = 0
mapp[now[0]][now[1]] = 0
# a = distance(now, (0,0),3)
# a = findenemy()
# print(a)
while(1) :
    if endgame :
        print(time)
        break
    else :
        enemy = findenemy()
        if not enemy :
            endgame = 1
            continue
        else :
            time += enemy[2]
            mapp[now[0]][now[1]] = 0
            now = enemy[0]
            mapp[now[0]][now[1]] = 9
            ms[enemy[1]].remove(now)

            kill += 1
            if kill == level :
                kill = 0
                level += 1

