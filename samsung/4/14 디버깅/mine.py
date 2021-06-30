from itertools import combinations
import copy

def run() :
    global mapp
    success = 0
    for col in range(1,n+1):
        now = [1,col]
        went = []
        while now[0] <= h :
            # print(now , went)
            for row in range(now[0], h+1) :
                if mapp[row][now[1]] and  [row,now[1]] not in went:
                    went.append([row,now[1]])
                    now[1] += 1
                    break
                elif mapp[row][now[1]-1] and [row,now[1]-1] not in went:
                    went.append([row,now[1]-1])
                    now[1] -= 1
                    break
                else :
                    now[0] += 1
        # print(col, "final", now)
        if col != now[1] :
            return 0
    return 1

        #

def addline(places):
    # print(places)
    global mapp
    mmapp = copy.deepcopy(mapp)
    for p in places :
        x,y = p[0], p[1]
        if 0 <= y-1 <= n :
            if mmapp[x][y-1] :
                # print("cant draw")
                return 1
        if 0 <= y+1 <= n :
            if mmapp[x][y+1] or mmapp[x][y] :
                # print("cant draw")
                return 1
        mmapp[x][y] = 1
    mapp = mmapp
    return 0

def eraseline(places) :
    for p in places :
        x,y = p[0], p[1]
        mapp[x][y] = 0
    return

def func(num) :
    cases = list(combinations(empty,num))
    # print(num,cases)

    for places in cases :
        error = 0
        error = addline(places)
        # print(places)
        # for m in mapp[1:] :
        #     print(m[1:])
        # print()
        if error :
            continue
        success = run()
        if success :
            # print(places)
            return 1
        eraseline(places)


n,m,h = map(int, input().split())
filled, empty = [], []
for _ in range(m):
    filled.append(list(map(int,input().split())))
mapp = [[0]*(n+1) for _ in range(h+1)]
for f in filled :
    mapp[f[0]][f[1]] = 1
for i in range(1,h+1) :
    for j in range(1,n) :
        if (i,j) not in filled :
            empty.append([i,j])

# for m in mapp[1:] :
#     print(m[1:])

for i in range(4) :
    success = func(i)
    if success :
        print(i)
        break
if not success :
    print(-1)
