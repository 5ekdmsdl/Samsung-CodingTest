from collections import deque
dx, dy = [-1,1,0,0], [0,0,-1,1]
def bfs(x,y):
    q = deque()
    q.append([x,y,0,mapp[x][y]])

    while q :
        # print(q)
        x,y,cnt,st = q.popleft()
        if cnt >= 5:
            nums[st] = 1
        else :
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx > 4 or ny < 0 or ny > 4 :
                    continue
                q.append([nx,ny,cnt+1, st+mapp[nx][ny]])


mapp = [list(input().split()) for _ in range(5)]

nums = {}

for i in range(5):
    for j in range(5):
        bfs(i,j)
print(len(list(nums.keys())))
