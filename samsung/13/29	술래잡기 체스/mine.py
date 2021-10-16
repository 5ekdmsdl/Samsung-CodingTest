def Input():
    n = [[] for _ in range(17)]
    mapp = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        l = list(map(int, input().split()))
        for j in range(0,len(l),2):
            nb, d = l[j], l[j+1]
            mapp[i][j//2] = d
            n[nb] = [i,j//2]
    return n, mapp

def catch(x,y):
    global ans, scr, cxy, cd

    cxy = [x,y]
    cd = mapp[x][y]
    idx = n.index([x,y])
    scr += idx
    n[idx] = []
    mapp[x][y] = 99

    if scr > ans : ans = scr

def next(d):
    d = d+1
    if d < 0 :
        d = 8
    elif d > 8 :
        d = 0
    return d

def printmapp():
    tmapp = [[0 for _ in range(4)] for _ in range(4)]

    for a, b in enumerate(n[1:]):
        if b:
            xx, yy = b
            tmapp[xx][yy] = a + 1
    return tmapp

def Theif():
    for i in range(1,16):
        if n[i] == [] :
            continue
        else :
            x,y = n[i]
        d = mapp[x][y]

        # i,x,y,d

        for _ in range(8):
            nx, ny = x+dx[d], y+dy[d]
            d = next(d)

            if not (0<=nx<=3 and 0<=ny<=3) or mapp[nx][ny] == 99 :
                continue
            else :
                if 1 <= mapp[nx][ny] <= 16 : #도둑이라면
                    # mapp 값 바꾸기
                    tmp = mapp[nx][ny]
                    mapp[nx][ny] = mapp[x][y]
                    mapp[x][y] = tmp

                    # n 값 바꾸기
                    idx = n.index([nx, ny])
                    tmp = n[idx]
                    n[idx] = n[i]
                    n[i] = tmp


                else : #빈칸이라면
                    # mapp 값 바꾸기
                    mapp[nx][ny] = mapp[x][y]
                    mapp[x][y] = 0

                    # n 값 바꾸기
                    n[i] = [nx, ny]
                break

        t = printmapp()
        # print()

    return

def dfs(cnt):
    global n,scr,cxy,cd

    Theif()
    t = printmapp()

    moved = 0
    tmp = n,scr,cxy,cd

    for i in range(3):
        x,y = cxy

        nx, ny = x+dx[cd]*i, y+dy[cd]*i

        if not (0<=nx<=3 and 0<=ny<=3) : break

        if 1 <= mapp[nx][ny] <= 16 :
            catch(nx,ny)
            dfs(cnt+1)
            moved = 1

        n, scr, cxy, cd = tmp

    if not moved :
        return
    return

ans, scr, cxy, cd = 0,0,0,0
dx, dy = [0,-1,-1,0,1,1,1,0,-1], [0,0,-1,-1,-1,0,1,1,1]
n, mapp = Input()

catch(0,0)
dfs(0)


print(ans)
