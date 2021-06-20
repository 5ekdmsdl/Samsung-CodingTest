def up(xy, Rxy,Bxy) :
    x, y = xy[0] - 1, xy[1]
    while(0 <= x <= n-1):
        if (x, y) == Rxy or (x, y) == Bxy:
            return (x + 1, y)
        if mapp[x][y] == '.' or mapp[x][y] == 'O' :
            x -= 1
        else : break
    return (x + 1, y)

def down(xy, Rxy,Bxy) :
    x, y = xy[0] + 1, xy[1]
    while(0 <= x <= n-1):
        if (x, y) == Rxy or (x, y) == Bxy:
            return (x - 1, y)
        if mapp[x][y] == '.' or mapp[x][y] == 'O' :
            x += 1
        else : break
    # print('2',nx, y)
    return (x-1, y)

def left(xy, Rxy,Bxy) :
    x, y = xy[0], xy[1] - 1
    while(0 <= y <= n-1):
        if (x, y) == Rxy or (x, y) == Bxy:
            return (x , y+1)
        if mapp[x][y] == '.' or mapp[x][y] == 'O' :
            y -= 1
        else : break
    return (x, y+1)

def right(xy, Rxy,Bxy) :
    x, y = xy[0], xy[1] + 1
    while(0 <= y <= n-1):
        if (x, y) == Rxy or (x, y) == Bxy:
            return (x , y-1)
        if mapp[x][y] == '.' or mapp[x][y] == 'O' :
            y += 1
        else : break
    return (x, y-1)

move = [up, down, left, right]

def func(Rxy, Bxy, dir, cnt, history) :
    global min_val


    cnt += 1
    Rxy, Bxy = move[dir](Rxy,Rxy,Bxy), move[dir](Bxy,Rxy,Bxy)
    Rxy, Bxy = move[dir](Rxy, Rxy, Bxy), move[dir](Bxy, Rxy, Bxy)
    # history.append(dir)
    # print(Rxy, Bxy)
    # print(Rxy, Bxy, Out, cnt, min_val, history+[dir])
    if Bxy == Out :
        return
    if Rxy == Out :
        print('bingo',Rxy, Bxy, Out, cnt,min_val,history+[dir])
        if cnt < min_val :
            min_val = cnt
            return
    if cnt == 10 :
        return
    else :
        for d in range(4):
            if d != dir :
                func(Rxy, Bxy, d, cnt,history+[dir])

n,m = map(int, input().split())
mapp = []
oBxy, oRxy, Out = 0, 0 , 0


for i in range(6):
    line = list(input())
    if 'B' in line :
        idx = line.index('B')
        oBxy = (i,idx)
        line = line[:idx] + ['.'] + line[idx+1:]
    if 'R' in line :
        idx = line.index('R')
        oRxy = (i, idx)
        line = line[:idx] + ['.'] + line[idx + 1:]
    if 'O' in line :
        idx = line.index('O')
        Out = (i, idx)
        line = line[:idx] + ['.'] + line[idx + 1:]
    mapp.append(line)

print(mapp)
min_val = int(1e9)

for dir in range(4):
    # print(oRxy, oBxy)
    func(oRxy, oBxy, dir, 0,[])
    # print(move[dir](oRxy,oRxy, oBxy))


if min_val == int(1e9):
    print('-1')
else :
    print(min_val)
