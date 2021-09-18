def Input():
    global n,m,k,mapp, Ps, Pdir
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j]:
                Ps[line[j]-1] = [i, j]
                contact(line[j]-1,i,j)
                Pmapp[i][j].append(line[j]-1)

    line = list(map(int, input().split()))
    for i, l in enumerate(line):
        Ps[i].append(l-1)

    for i in range(m):
        for j in range(4):
            line = list(map(int, input().split()))
            for a in range(len(line)):
                line[a] -= 1
            Pdir[i].append(line)
    return

def main():
    # print()
    for i in alive:
        move(i)
    removePlayer()
    for i,P in enumerate(Ps):
        if i in alive :
            contact(i,P[0],P[1])
    decreaseContactCnt()
    return checkEnd()

def contact(i,x,y):
    global k
    mapp[x][y] = [i,k+1]

def move(i):
    global Ps
    x,y,d = Ps[i]
    d_list = Pdir[i][d]
    for j in d_list:
        nx,ny = x+dx[j], y+dy[j]
        if not (0<=nx<=n-1 and 0<=ny<=n-1): continue
        if mapp[nx][ny] == [] :
            Ps[i] = [nx,ny,j]
            # contact(i,nx,ny)
            Pmapp[x][y].remove(i)
            Pmapp[nx][ny].append(i)
            return
    for j in d_list:
        nx,ny = x+dx[j], y+dy[j]
        if not (0<=nx<=n-1 and 0<=ny<=n-1): continue
        if mapp[nx][ny] and mapp[nx][ny][0] == i :
            Ps[i] = [nx,ny,j]
            # contact(i,nx,ny)
            Pmapp[x][y].remove(i)
            Pmapp[nx][ny].append(i)
            return

def removePlayer():
    global alive
    for x in range(n):
        for y in range(n):
            if len(Pmapp[x][y]) >= 2:
                dead = []
                for P in Pmapp[x][y] :
                    dead.append(P)
                dead.remove(min(Pmapp[x][y]))
                Pmapp[x][y] = [min(Pmapp[x][y])]
                if dead :
                    for d in dead :
                        alive.remove(d)

    return

def decreaseContactCnt():
    for x in range(n):
        for y in range(n):
            if mapp[x][y] :
                mapp[x][y][1] -= 1
                if mapp[x][y][1] <= 0 :
                    mapp[x][y] = []
    return

def checkEnd():
    maxv = 0
    for P in Pmapp :
        if max(P) and max(P)[0] > maxv :
            maxv = max(P)[0]
    if maxv == 0 :
        return True
    else : return False

dx, dy = [-1,1,0,0], [0,0,-1,1]
n,m,k = map(int, input().split())
mapp = [[[] for _ in range(n)] for _ in range(n)]
Pmapp = [[[] for _ in range(n)] for _ in range(n)]
Ps = [[] for _ in range(m)]
Pdir = [[] for _ in range(m)]
answer = 1
Input()
alive = list(range(m))

aflg = 0
decreaseContactCnt()
for turn in range(1000):
    if main():
        answer += turn
        aflg = 1
        break

if aflg :
    print(answer)
else : print(-1)




