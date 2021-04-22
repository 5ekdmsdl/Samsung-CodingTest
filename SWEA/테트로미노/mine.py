from collections import deque

n,m = map(int,input().split())
mapp = []

for i in range(n):
    mapp.append(list(map(int,input().split())))

max_val = 0
dx, dy = [-1,1,0,0],[0,0,-1,1]

def dfs(x,y,check,cnt):
    maxb = 0
    check.append([x,y])
    cnt += 1
    if cnt >= 4 :
        check.remove([x, y])
        return mapp[x][y]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue
        elif [nx, ny] in check :
            continue
        a = dfs(nx, ny, check, cnt)
        b = mapp[x][y] + a
        maxb = max(maxb, b)

    if cnt == 2 :
        nei = []
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            #print(nx, ny)
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                #print('case 1')
                continue
            elif [nx, ny] in check:
                #print('case 2',check)
                continue
            nei.append(mapp[nx][ny])
        #print('n',nei)
        if len(nei) == 2 :
            b2 = sum(nei) + mapp[x][y]
            maxb = max(maxb, b2)
        elif len(nei) == 3 :
            nei.remove(min(nei))
            b2 = sum(nei) + mapp[x][y]
            maxb = max(maxb, b2)



    #print(x,y,cnt,maxb)
    check.remove([x, y])
    return maxb

def bfs(x,y) :
    q = deque([])
    q.append([x,y,1,[[x,y]],mapp[x][y]])
    results = []

    while q :
        # if [x,y] == [0,1] :
        #     print(q)
        x,y,cnt,check, score = q.pop()
        if cnt >= 4 :
            results.append(score)

            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            elif [nx, ny] in check :
                continue
            check.append([nx, ny])
            q.append([nx, ny, cnt+1, check, score+mapp[nx][ny]])
            check.remove([nx, ny])

        if cnt == 2:
            nei = []
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                #print(nx, ny)
                if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                    # print('case 1')
                    continue
                elif [nx, ny] in check:
                    #print('case 2',check)
                    continue

                nei.append(mapp[nx][ny])
            #print(x,y,'n',nei)
            if len(nei) == 2:
                results.append(score + sum(nei))

            elif len(nei) == 3:
                nei.remove(min(nei))
                results.append(score + sum(nei))



    return max(results)





for i in range(n):
    for j in range(m):
        #val = dfs(i,j,[],0)
        val = bfs(i,j)
        max_val = max(val, max_val)
        #print('##',i, j, val)

print(max_val)
