def Input():
    n,m,k = map(int, input().split())

    As = []
    for _ in range(m):
        l = list(map(int, input().split()))
        l[0] -= 1
        l[1] -= 1
        As.append(l)

    mapp = [[[] for _ in range(n)] for _ in range(n)]
    for i, A in enumerate(As) :
        mapp[A[0]][A[1]] = [i]

    return n,m,k, As, mapp

def move():
    for i, A in enumerate(As):
        if not A : continue
        x,y,m,s,d = A
        nx, ny = x+dx[d]*s, y+dy[d]*s
        if not (0<=nx<=n-1 and 0<=ny<=n-1) :
            nx = nx % n
            ny = ny % n
        As[i] = [nx,ny,m,s,d]
        mapp[nx][ny].append(i)
        mapp[x][y].remove(i)
    return

def merge():
    for i in range(n):
        for j in range(n):
            if len(mapp[i][j]) >= 2 :
                tm, ts, cnt = 0,0,len(mapp[i][j])
                dlist = [] #방향 종류 모음

                for a in mapp[i][j] : # a : 겹치는 index
                    dlist.append(As[a][4]%2)
                    tm += As[a][2]
                    ts += As[a][3]
                    As[a] = [] # A update
                mapp[i][j] = [] # mapp update

                # nd set
                if dlist == [0 for _ in range(len(dlist))] \
                        or dlist == [1 for _ in range(len(dlist))] :
                    nds = [0,2,4,6]
                else : nds = [1,3,5,7]

                # m = 0 : erase
                if tm // 5 == 0 : continue

                # Atom 추가
                for _ in range(4):
                    nA = [i,j,tm//5,ts//cnt,nds[_]]
                    As.append(nA) # A update
                    mapp[i][j].append(len(As)-1) # mapp update

    return

def getans():
    global As
    ans = 0
    for i in range(len(As)):
        if As[i]:
            ans += As[i][2]
    return ans

dx, dy = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]
n,m,k, As, mapp = Input()

for t in range(k):
    move()
    merge()

print(getans())
