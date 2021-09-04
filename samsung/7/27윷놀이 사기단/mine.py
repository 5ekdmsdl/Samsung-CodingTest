def catch(x,y):
    global result, mapp, t
    if mapp[x][y] :
        result += mapp[x][y][0]
        mapp[t[0]][t[1]] = 0
        mapp[x][y] = 99
        t = [x,y]
    return

def rotate(d,i):
    d = d + i
    if d < 0 :
        d += 8
    elif d > 7 : d -= 8
    return d

def runner():
    num = 1
    for x in range(4):
        for y in range(4):
            if mapp[x][y] == 99 : continue
            if mapp[x][y][0] == num :
                num += 1
                for i in range(8):
                    d = mapp[x][y][1]-1
                    nx, ny = x+dx[d], y+dy[d]
                    if (not 0<=nx<=3 and 0<=ny<=3) or mapp[nx][ny] == 99 :
                        d = rotate(d, i)
                        continue
                    else :
                        if mapp[x][y]:
                            tmp = mapp[x][y]
                            mapp[x][y] = mapp[nx][ny]
                            mapp[nx][ny] = tmp
                        else :
                            mapp[nx][ny] = num
                            mapp[x][y] = 0
                        break



    return

def catcher():
    return

def game(mapp, result):
    runner()
    # catcher()

dx, dy = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
mapp = [[] for _ in range(4)]
result, answer = 0, 0
t = [0,0]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        mapp[i].append([line[j*2], line[j*2+1]])

catch(0,0)

game(mapp, result)

# runner()
