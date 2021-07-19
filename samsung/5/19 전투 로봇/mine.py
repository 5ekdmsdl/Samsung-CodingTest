import heapq
INF = int(1e9)

def distance(now, target, level) :
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    d_mapp = [[INF]*n for _ in range(n)]
    d_mapp[now[0]][now[1]] = 0
    q = []
    heapq.heappush(q, [d_mapp[now[0]][now[1]], now])

    while q :
        dist, now = heapq.heappop(q)

        if now[0] == target[0] and now[1] == target[1]  :
            return dist
        if d_mapp[now[0]][now[1]] < dist :
            continue

        for i in range(4) :
            n_dist = dist+1
            nx, ny = now[0] + dx[i], now[1] + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1 and mapp[nx][ny] <= level:
                if n_dist < d_mapp[nx][ny] :
                    d_mapp[nx][ny] = n_dist
                    heapq.heappush(q, [n_dist, [nx,ny]])
    return INF


def findenemy() :
    min_d, min_xy = INF, (-1, -1)
    enemys = []

    for i in range(1,min(level, 7)) :
        for m in ms[i] :
            d = abs(m[0] - now[0]) + abs(m[1] - now[1])
            if d > min_d :
                continue
            d = distance(now, m, level)
            if d == INF : continue
            if min_d > d :
                enemys = [[m,i,d]]
                min_d = d
            elif min_d == d :
                enemys.append([m,i,d])

    enemys.sort()
    if enemys.__len__() > 1 :
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

while(1) :
    enemy = findenemy()
    if not enemy :
        print(time)
        break
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
