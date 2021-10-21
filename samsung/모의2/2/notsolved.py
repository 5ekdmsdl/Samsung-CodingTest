def Input():
    n = int(input())

    mapp = []
    three = []
    for i in range(n):
        l = list(map(int, input().split()))
        mapp.append(l)
        for j in range(n):
            if l[j] == 3 :
                three.append([i,j])


    l = list(map(int, input().split()))
    Ms = []
    Mmapp = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(len(l)) :
        if 0 <= i <= n-1 :
            # Mmapp[0][i].append(i)
            Ms.append([-1, i,3])

        elif n <= i <= 2*n-1 :
            # Mmapp[i-n][n-1].append(i)
            Ms.append([i-n,n,0])

        elif 2*n <= i <= 3*n-1 :
            # Mmapp[n-1][3*n-1-i].append(i)
            Ms.append([n,3*n-1-i,2])

        elif 3*n <= i <= 4*n-1 :
            # Mmapp[4*n-1-i][0].append(i)
            Ms.append([4*n-1-i,-1,1])

    return n,mapp,Mmapp, three, Ms

def setchs(i):
    global chs, three, tmp

    if i == len(three) :
        chs.append(tmp)
        return

    ttmp = tmp[:]

    for d in range(3):
        tmp.append(d)
        setchs(i+1)

        tmp = ttmp[:]

def setmapp(ch):
    global mapp, three

    for i in range(len(ch)):
        x,y = three[i]
        mapp[x][y] = ch[i]

    for x in range(n):
        for y in range(n):
            if mapp[x][y] == 1 or mapp[x][y] == 2 :
                Mmapp[x][y] = [[], []]
    return

def Move():
    global mapp, Mmapp, cnt
    one, two = [3,2,1,0], [2,3,0,1]

    # Mmapp 복사본
    tmp = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if mapp[x][y] == 1 or mapp[x][y] == 2 :
                tmp[x][y] = [[], []]

    for i, m in enumerate(Ms):
        #이미 나간 애 처리
        if m == []:
            continue
        # 아직 살아있으면..
        x,y,d = m
        nx, ny = x+dx[d], y+dy[d]

        # 밖으로 나가면
        if not (0<=nx<=n-1 and 0<=ny<=n-1) :
            # Ms update, tmp update
            cnt += 1
            Ms[i] = []
            continue

        # 안에서 놀면
        if mapp[nx][ny] == 1 :
            if d == 1 or d==3 :
                tmp[nx][ny][0].append(i)
            else :
                tmp[nx][ny][1].append(i)

            d = one[d]
            Ms[i] = [nx, ny, d]

        elif mapp[nx][ny] == 2 :
            if d == 1 or d == 2:
                tmp[nx][ny][0].append(i)
            else:
                tmp[nx][ny][1].append(i)

            d = two[d]
            Ms[i] = [nx, ny, d]

        else :
            # Ms update, tmp update
            tmp[nx][ny].append(i)
            Ms[i] = [nx,ny,d]

    # Mmapp update
    Mmapp = [t[:] for t in tmp]

    return

def Crush():
    # # 살아남는 경우들
    # case1, case2 = [[0,1], [0,2], [1,2], [2,3]], \
    #                [[0,2], [0,3], [1,2], [1,3]]
    # Mmapp 탐색
    for x in range(n):
        for y in range(n):

            # 무조건 충돌 경우
            if mapp[x][y] == 0 and len(Mmapp[x][y]) >= 2:
                for i in Mmapp[x][y]:
                    Ms[i] = []
                Mmapp[x][y] = []

            elif mapp[x][y] == 1 or mapp[x][y] == 2 :
                for a in range(2):
                    if len(Mmapp[x][y][a]) >= 2:
                        for b in Mmapp[x][y][a]:
                            Ms[b] = []
                        Mmapp[x][y][a] = []

                # # 벽으로 두개가 올때
                # elif len(Mmapp[x][y]) == 2 :
                #     # 방향 확인
                #     ds = []
                #     for i in Mmapp[x][y] :
                #         ds.append(Ms[i][2])
                #     ds.sort()
                #
                #     # 벽두고 온 케이스면 충돌 ㄴㄴ
                #     if mapp[x][y] == 1 :
                #         if ds in case1:
                #             continue
                #     elif mapp[x][y] == 2 :
                #         if ds in case2:
                #             continue
                #     # 그렇지 않으면 충돌
                #     else :
                #         for i in Mmapp[x][y] :
                #             Ms[i] = []
                #         Mmapp[x][y] = []

    return

def End():
    for x in range(n):
        for y in range(n):
            if mapp[x][y] == 0 and Mmapp[x][y] :
                return False
            elif mapp[x][y] == 1 or mapp[x][y] == 2 :
                for a in range(2):
                    if Mmapp[x][y][a] :
                        return False
    return True

ans = 0
dx, dy = [0,0,-1,1],[-1,1,0,0]
n,o_mapp,o_Mmapp, three, o_Ms = Input()
chs, tmp = [], []
setchs(0)

for ch in chs :
    cnt = 0

    mapp = [o[:] for o in o_mapp]
    Mmapp = [o[:] for o in o_Mmapp]
    Ms = o_Ms[:]

    setmapp(ch)

    while(1):
        Move()
        Crush()
        if End():
            break

    if cnt > ans :
        ans = cnt

print(ans)
