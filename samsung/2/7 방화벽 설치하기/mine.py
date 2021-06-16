dx, dy = [0,0,-1,1], [-1,1,0,0]

def build_wall_and_fire(mapp, walls):
    global max_val, fires
    for x,y in walls:
        mapp[x][y] = 1
    q = deque(fires)
    while q :
        x,y = q.popleft()
        # print(x,y)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1 and mapp[nx][ny] == 0 :
                mapp[nx][ny] = 2
                q.append((nx,ny))
    result = 0
    for mm in mapp :
        result += mm.count(0)
    # for mm in mapp :
    #     print(mm)
    # print(result)
    if result > max_val :
        max_val = result
        # for mm in mapp :
        #     print(mm)
        # print(result, fires)

import copy
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
mapp = []
fires = []

for _ in range(n):
    aline = list(map(int, input().split()))
    mapp.append(aline)
    if 2 in aline :
        for iv , v in enumerate(aline):
            if v == 2 :
                fires.append((_, iv))

# print(fires)
cases = list(combinations(range(n*m), 3))
max_val = 0
flg = 0

for c in cases:
    walls = []
    for i in range(3):
        x,y = c[i]//m, c[i]%m
        if mapp[x][y] == 2 or mapp[x][y] == 1:
            flg = 1
            break
        walls.append((x,y))
    if flg:
        flg = 0
        continue
    n_mapp = copy.deepcopy(mapp)
    build_wall_and_fire(n_mapp, walls)
print(max_val)
