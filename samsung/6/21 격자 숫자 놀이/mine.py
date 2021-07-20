def cntnums(line) :
    nums = [0]*100
    n_line, couples = [], []
    for l in line :
        if l == 0 :
            break
        elif l :
            nums[l] += 1
    for i , n in enumerate(nums) :
        if n : couples.append([n,i])
    couples.sort()
    for c in couples :
        n_line.append(c[1])
        n_line.append(c[0])
    return n_line

def sortRow() :
    global nr, nc
    for x in range(nr) :
        row = mapp[x][:nc]
        n_row = cntnums(row)
        if len(n_row) > 100 :
            n_row = n_row[:100]
        if len(n_row) >= nc :
            mapp[x][:len(n_row)] = n_row
            nc = len(n_row)
        else :
            mapp[x][:nc] = n_row+[0]*(abs(len(n_row) - nc))

def sortCol() :
    global nr, nc
    for y in range(nc) :
        col = []
        for i in range(nr) :
            col.append(mapp[i][y])
        n_col = cntnums(col)
        if len(n_col) > 100 :
            n_col = n_col[:100]
        if len(n_col) >= nr :
            for i in range(len(n_col)) :
                mapp[i][y] = n_col[i]
            nr = len(n_col)
        else :
            for i in range(len(n_col)) :
                mapp[i][y] = n_col[i]
            for i in range(len(n_col),nr) :
                mapp[i][y] = 0

tr, tc, tk = map(int, input().split())
mapp = [[0]*100 for _ in range(100)]
nc, nr = 3,3
t = 0
failed = 0
for i in range(3) :
    line = list(map(int, input().split()))
    for j in range(3) :
        mapp[i][j] = line[j]

while(mapp[tr-1][tc-1] != tk) :
    if t == 100 :
        failed = 1
        rtv = -1
        break
    if nr >= nc :
        sortRow()
    else : sortCol()
    t += 1

if not failed : rtv = t

print(rtv)


