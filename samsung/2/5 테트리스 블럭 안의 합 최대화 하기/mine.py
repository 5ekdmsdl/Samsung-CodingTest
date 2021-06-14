def func(x,y,cnt,included):
    global max_val
    if cnt == 4:
        result = 0
        # print(included)
        for inc in included:
            result += mapp[inc[0]][inc[1]]
        if result > max_val :
            max_val = result
            # print(max_val)
    else :
        dx, dy = [-1,1,0,0], [0,0,-1,1]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<=n-1 and 0<=ny<=m-1 and (nx,ny) not in included:
                func(nx,ny,cnt+1,included+[(nx,ny)])

def func2(x,y):
    global max_val
    dx,dy = [0,0,0,-1,1], [0,-1,1,0,0]
    comb = [[1,2,3],[1,3,4],[1,2,4],[2,3,4]]

    for c in comb:
        friends = []
        for i in range(3):
            nx, ny = x+dx[c[i]],y+dy[c[i]]
            if (0 <= nx <= n-1 and 0 <= ny <= m-1) :
                friends.append((nx, ny))
        if len(friends) < 3 :
            continue
        else :
            result = mapp[x][y]
            for f in friends :
                result += mapp[f[0]][f[1]]
                if result > max_val :
                    max_val = result


    return 0


n,m = map(int, input().split())
mapp = []
for _ in range(n):
    mapp.append(list(map(int,input().split())))

max_val = -1

for i in range(n):
    for j in range(m):
        func(i,j,1,[(i,j)])
        func2(i,j)

print(max_val)

