n,m,x,y,k = map(int,input().split())

mapp = []
for i in range(n):
    mapp.append(list(map(int,input().split())))

move = list(map(int,input().split()))
# move = [1,4,2,3,2,4,1,]

bottom = 5
dx, dy = [0,0,0,-1,1], [0,1,-1,0,0]

top = 0
dice = [0,0,0,0,0,0,]
n_idx = [[],
         [1,5,2,0,4,3],
         [3,0,2,5,4,1],
         [4,1,0,3,5,2],
         [2,1,5,3,0,4]]

def func(dice,mv):
    n_dice = [-1]*6
    for i,v in enumerate(n_idx[mv]):
        n_dice[i] = dice[v]
    return n_dice

for mv in move:

    nx, ny = x+dx[mv], y+dy[mv]
    # print(x, y, nx, ny,m,(0 <= nx <= n-1 and 0 <= ny <= m-1) )
    if not (0 <= nx <= n-1 and 0 <= ny <= m-1) :
        continue
    x,y = nx, ny
    dice = func(dice, mv)
    # print(mv,bottom)

    if mapp[x][y] == 0 :
        mapp[x][y] = dice[bottom]
    else :
        dice[bottom] = mapp[x][y]
        mapp[x][y] = 0

    print(dice[top])
    # print(dice, mapp)
