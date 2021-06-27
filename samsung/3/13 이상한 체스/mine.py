import copy

def up(x,y,mapp) :
    for i in range(x,-1,-1) :
        if mapp[i][y] == 6 :
            break
        mapp[i][y] = 99
def down(x,y,mapp) :
    for i in range(x,n) :
        if mapp[i][y] == 6 :
            break
        mapp[i][y] = 99
def left(x,y,mapp) :
    for i in range(y,-1,-1) :
        if mapp[x][i] == 6 :
            break
        mapp[x][i] = 99
def right(x,y,mapp) :
    for i in range(y,m) :
        if mapp[x][i] == 6 : break
        mapp[x][i] = 99

line = [[],
        [[up],[down],[left],[right]],
        [[up,down], [left, right]],
        [[up,left],[up,right],[down,left],[down,right]],
        [[up,down,left],[up,down,right],[up,left,right],[down,left,right]],
        [[up,down,left,right]]
        ]

def drawline(num,x,y,style,mapp) :
    # print(line)
    for draw in line[num][style] :
        draw(x,y,mapp)

cases = [
    [0],[0,1,2,3],[0,1],[0,1,2,3],[0,1,2,3]
]
def func(cnt, mapp) :
    global min_val
    # print("cnt",cnt)
    # for m in mapp:
    #     print(m)
    # print()
    if cnt > clen - 1:
        result = 0
        for m in mapp :
            result += m.count(0)
        if min_val > result :
            min_val = result
            # print("min val")
            # for m in mapp:
            #     print(m)
            # print()
        return

    else :
        num, x, y = chess[cnt]
        mmapp = copy.deepcopy(mapp)
        # print(num)
        for c in cases[num] :
            drawline(num, x,y,c,mmapp)
            func(cnt+1, mmapp)
            mmapp = copy.deepcopy(mapp)


min_val = int(1e9)
n,m = map(int, input().split())
mapp, chess, fives = [], [], []
for i in range(n) :
    aline = list(map(int, input().split()))
    mapp.append(aline)
    for j,l in enumerate(aline) :
        if l :
            if l < 5 :
                chess.append((l,i,j))
            elif l == 5 :
                fives.append((i,j))

clen = chess.__len__()
# print(clen,chess)
if fives :
    for x,y in fives :
        drawline(5,x,y,0,mapp)

func(0,mapp)



print(min_val)
