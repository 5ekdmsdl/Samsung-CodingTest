n,m = map(int, input().split())
x,y,d = map(int, input().split())

mapp = []
for _ in range(n):
    mapp.append(list(map(int,input().split())))

dx, dy = [-1,0,1,0], [0,1,0,-1]

BeenHere = [(x,y)]
while(1):
    flg = 0
    for i in range(4):
        d -= 1
        if d < 0 : d = 3
        nx, ny = x + dx[d], y + dy[d]
        if mapp[nx][ny] == 0 and (nx, ny) not in BeenHere :
            x,y = nx, ny
            BeenHere.append((x,y))
            flg = 1
            break
    if flg == 0 :
        nx,ny = x-dx[d], y-dy[d]
        if mapp[nx][ny] :
            break
        x,y = nx, ny

print(len(BeenHere))
