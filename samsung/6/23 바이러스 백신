def move(n) :
    x,y,d = players[n]
    nx, ny = x+dx[d], y+dy[d]
    stack = mapp[x][y]
    idx = stack.index(n)
    moving = stack[idx:]
    mapp[nx][ny] += moving
    mapp[x][y] = mapp[x][y][:idx]
    for m in moving : players[m] = [nx, ny, players[m][2]]
    return 0

def reverse(n):
    x,y,d = players[n]
    idx = mapp[x][y].index(n)
    stack = mapp[x][y]
    if len(stack) == 1 : return
    stack = stack[:idx] + list(reversed(stack[idx:]))
    mapp[x][y] = stack
    return

def flipdir(n):
    now = players[n][2]
    if now == 1 : players[n][2] = 2
    elif now == 2 : players[n][2] = 1
    elif now == 3 : players[n][2] = 4
    elif now == 4 : players[n][2] = 3
    return


def white(n):
    move(n)

def red(n):
    reverse(n)
    move(n)

def blue(n):
    flipdir(n)
    x, y, d = players[n]
    nx, ny = x + dx[d], y + dy[d]
    if cmapp[nx][ny] == 2 : return
    else : move(n)

dx, dy = [0,0,0,-1,1], [0,1,-1,0,0]

nn,k = map(int, input().split())
cmapp, players = [], []
mapp = [[[] for _ in range(nn)] for _ in range(nn)]

for _ in range(nn):
    cmapp.append(list(map(int, input().split())))
for _ in range(k):
    x,y,d = map(int, input().split())
    players.append([x-1,y-1,d])
    mapp[x-1][y-1].append(_)

t = 0
done = 0
while(t < 1000) :
    t += 1
    for i, p in enumerate(players) :
        x,y,d = p
        nx, ny = x+dx[d], y+dy[d]
        if not (0<=nx<=nn-1 and 0<=ny<=nn-1) :
            flipdir(i)
            move(i)
        else :
            if cmapp[nx][ny] == 0 :
                white(i)
            elif cmapp[nx][ny] == 1:
                red(i)
            else : blue(i)
        for m1 in mapp :
            for m2 in m1 :
                if len(m2) >= 4 : done = 1
    if done :
        break

if t >= 1000 : print(-1)
else : print(t)



