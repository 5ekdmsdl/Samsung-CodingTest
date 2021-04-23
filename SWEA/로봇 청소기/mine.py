n,m = map(int, input().split())
x,y,d = map(int,input().split())
s1,s2 = x,y

mapp = [list(map(int, input().split())) for _ in range(n)]
score = 0
dx, dy = [-1,0,1,0], [0,1,0,-1]
flg2 = False

while (1):
    if not flg2 :
        mapp[x][y] = 2
        score += 1
        flg = False

    else : flg2 = False

    for i in range(4):
        nd = d - 1
        if nd == -1 :
            nd = 3
        nx, ny = x + dx[nd], y + dy[nd]
        c = mapp[nx][ny]
        if c == 0:
            d = nd
            x, y = x + dx[d], y + dy[d]
            flg = True
            break
        else :
            d = nd
            continue

    if not flg :
        x,y = x - dx[d], y - dy[d]
        if mapp[x][y] == 1:
            break
        else :
            flg2 = True
            continue

print(score)
