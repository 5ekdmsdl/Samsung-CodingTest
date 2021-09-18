def catch(x,y,_mapp,t):
    score = 0
    if _mapp[x][y] :
        score += _mapp[x][y][0]
        td = _mapp[x][y][1]
        _mapp[t[0]][t[1]] = 0
        _mapp[x][y] = 99
        t = [x,y]
    return t, td, score

def rotate(d,i):
    d = d + i
    if d < 0 :
        d += 8
    elif d > 7 : d -= 8
    return d

def runner():
    for num in range(1,17):
        bflg = 0
        for x in range(4):
            for y in range(4):
                if mapp[x][y] == 99 or mapp[x][y] == 0 : continue
                if mapp[x][y][0] == num :
                    d = mapp[x][y][1]
                    for i in range(8):
                        nx, ny = x+dx[d], y+dy[d]
                        if (not (0<=nx<=3 and 0<=ny<=3)) or mapp[nx][ny] == 99 :
                            d = rotate(d, 1)
                            continue
                        else :
                            if mapp[x][y]:
                                tmp = mapp[x][y]
                                mapp[x][y] = mapp[nx][ny]
                                mapp[nx][ny] = tmp
                            else :
                                mapp[nx][ny] = mapp[x][y]
                                mapp[x][y] = 0
                            bflg = 1
                            break
                if bflg :
                    break
            if bflg : break
    return

def game(mapp, result,cnt,t,td):
    global answer
    runner()
    end = 1
    for i in range(1,4):
        cx,cy = t[0]+dx[td]*i, t[1]+dy[td]*i
        if not (0<=cx<=3 and 0<=cy<=3):
            break
        if mapp[cx][cy] :
            _mapp = [[[] for _ in range(4)] for _ in range(4)]
            for x in range(4) :
                for y in range(4):
                    _mapp[x][y] = mapp[x][y]
            cresult = catch(cx,cy,_mapp,t)
            _t , _td = cresult[0], cresult[1]
            _result = cresult[2] + result
            game(_mapp, _result,cnt+1,_t,_td)
            end = 0
    if end :
        if result > answer :
            answer = result
        return

dx, dy = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
mapp = [[] for _ in range(4)]
answer = 0
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        mapp[i].append([line[j*2], line[j*2+1]-1])

t = [0,0]
t, td, score = catch(0,0,mapp,t)
game(mapp, score,0,t, td)

print(answer)
