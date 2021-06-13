def move(mapp):
    for x in range(n):
        for y in range(n):
            if mapp[x][y] :
                a,b = x,y
                na, nb = a - 1, b
                while (na + 1 and nb + 1 and mapp[na][nb] == 0):
                    # print(na,nb,a,b)
                    mapp[na][nb] = mapp[a][b]
                    mapp[a][b] = 0
                    a,b= na, nb
                    na, nb = a - 1, b
            else :
                continue
    return mapp

def summ(mapp):
    for x in range(0,n-1):
        for y in range(0,n):
            # print(x,y)
            if mapp[x][y] == mapp[x+1][y] :
                mapp[x][y] *= 2
                mapp[x+1][y] = 0
    return mapp
time = [0,2,1,3,]
time_r = [0,2,3,1,]

def func(mapp,dir):
    for i in range(time[dir]):
        mapp = rotate(mapp)
    mapp = move(mapp)
    mapp = summ(mapp)
    mapp = move(mapp)

    for i in range(time_r[dir]):
        mapp = rotate(mapp)

    return mapp

def rotate(mapp):
    n_mapp = [[0]*(n) for _ in range(n)]
    for j,y in enumerate(range(n)):
        for i,x in enumerate(range(n-1,-1,-1)):
            # print(j,i)
            n_mapp[j][i] = mapp[x][y]
    return n_mapp

def ff(mapp, cnt, dir):
    mapp = func(mapp, dir)
    cnt += 1
    max_val = -1
    if cnt == 5:
        for x in range(n):
            if max(mapp[x]) > max_val :
                max_val = max(mapp[x])
        return max_val
    else:
        for d in range(4):
            max_val = max(max_val, ff(mapp, cnt, d))
        return max_val
    return 0


n = int(input())
mapp = []
for i in range(n):
    mapp.append(list(map(int,input().split())))

max_val = -1
for d in range(4):
    max_val = max(ff(mapp,0,d),max_val)
print(max_val)

# dir = 1
# mapp = func(mapp,dir)
print(mapp)
max_val = 0

for x in range(n):
    if max(mapp[x]) > max_val:
        max_val = max(mapp[x])
print(max_val)

