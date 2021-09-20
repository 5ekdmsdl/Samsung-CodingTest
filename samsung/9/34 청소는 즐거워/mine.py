def Input():
    global totalDust
    mapp = []
    n = int(input())
    for _ in range(n):
        line = list(map(int, input().split()))
        mapp.append(line)
        totalDust += sum(line)
    return n,mapp

def left(xy, cnt):
    x,y = xy
    rtv = []
    for i in range(1,cnt+1):
        rtv.append((x, y - i))
    return rtv

def right(xy, cnt):
    x, y = xy
    rtv = []
    for i in range(1, cnt + 1):
        rtv.append((x, y + i))
    return rtv

def down(xy, cnt):
    x, y = xy
    rtv = []
    for i in range(1, cnt + 1):
        rtv.append((x+i, y ))
    return rtv

def up(xy, cnt):
    x, y = xy
    rtv = []
    for i in range(1, cnt + 1):
        rtv.append((x-i, y))
    return rtv

def setMove():
    move = []
    center = ((n-1)//2, (n-1)//2)
    nxy = [center]
    for i in range(1,n,2):
        nxy = left(nxy[-1],i)
        move += nxy
        nxy = down(nxy[-1], i)
        move += nxy
        nxy = right(nxy[-1], i+1)
        move += nxy
        nxy = up(nxy[-1], i+1)
        move += nxy
    nxy = left(nxy[-1], n-1)
    move += nxy
    return move

def getSpread(direction):
    S = [
    {
        (-2,0) : 0.02,
        (-1,-1) : 0.1,
        (-1,0) : 0.07,
        (-1,1) : 0.01,
        (0,-2) : 0.05,
        # (0,-1) : 0.55,
        (0,0) : 0,
        (1,-1) : 0.1,
        (1,0) : 0.07,
        (1,1) : 0.01,
        (2,0) : 0.02
    }, #left
    {
        (-1, 1): 0.1,
        (1, 1): 0.1,
        (-2, 0): 0.02,
        (2, 0): 0.02,
        (-1, 0): 0.07,
        (1, 0): 0.07,
        (-1, -1): 0.01,
        (1, -1): 0.01,
        (0, 2): 0.05,
    }, #right
    {
        (0,2): 0.02,
        (0, -2): 0.02,
        (-1, 1): 0.1,
        (-1, -1): 0.1,
        (0, 1): 0.07,
        (0, -1): 0.07,
        (1, 1): 0.01,
        (1, -1): 0.01,
        (-2, 0): 0.05,
    }, #up
    {
        (0,-2): 0.02,
        (0, 2): 0.02,
        (1, -1): 0.1,
        (1, 1): 0.1,
        (0, -1): 0.07,
        (0, 1): 0.07,
        (-1, -1): 0.01,
        (-1, 1): 0.01,
        (2, 0): 0.05,
    }, #down
    ]
    return S[direction]

def spreadDust(xy, direction):
    dxx, dyy = [0, 0, -1, 1], [-1, 1, 0, 0],
    x,y = xy
    spread = getSpread(direction)
    leftdust = mapp[x][y]
    for [dx,dy] , p in spread.items():
        nx,ny = x+dx, y+dy
        mdust = (mapp[x][y]*p)//1
        leftdust -= mdust
        if 0<=nx<=n-1 and 0<=ny<=n-1 :
            mapp[nx][ny] += mdust
    nx, ny = x+dxx[direction], y+dyy[direction]
    if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
        mapp[nx][ny] += leftdust
    mapp[x][y] = 0
    return

def swap(m,direction):
    spreadDust(m, direction)

def leftDust():
    dust = 0
    for x in range(n):
        for y in range(n):
            if mapp[x][y] :
                dust += mapp[x][y]
    return dust

def main():
    direction = {
        (0,-1) : 0,
        (0,1) : 1,
                (-1,0) : 2,
                 (1,0) : 3
    }
    prem = ((n-1)//2, (n-1)//2)
    for m in move :
        dxy = (m[0]-prem[0], m[1]-prem[1])
        swap(m, direction[dxy])
        prem = m
    answer = totalDust - leftDust()
    return answer

answer, totalDust = 0, 0
n, mapp = Input()
move = setMove()
answer = int(main())

print(answer)
