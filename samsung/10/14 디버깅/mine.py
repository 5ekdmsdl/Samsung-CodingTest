def Input():
    n,m,h = map(int, input().split())
    mapp = [[0 for _ in range(n)] for _ in range(h)]
    for _ in range(m):
        a,b = map(int, input().split())
        mapp[a-1][b-1] = 1
        mapp[a-1][b+1-1] = 2
    return n,h,m,mapp

def run():
    global mapp
    fflg = 0
    for py in range(n):
        y = py
        for x in range(h):
            if mapp[x][y] == 1:
                y += 1
            elif mapp[x][y] == 2:
                y -= 1
        if y != py :
            # a = 1
            return 0
    return 1

def dfs(i, cnt):
    global ms, mapp, answer
    if cnt == 4 : return
    if i == len(ms) : return

    x,y = ms[i]

    if mapp[x][y] :
        dfs(i+1, cnt)
        return
    elif mapp[x][y+1] :
        dfs(i + 1, cnt)
        return
    else :
        tmapp = [m[:] for m in mapp]

        mapp[x][y] = 1
        mapp[x][y+1] = 2
        if run():
            answer = min(answer, cnt)
            return
        dfs(i+1, cnt+1)

        mapp = [m[:] for m in tmapp]

        dfs(i + 1, cnt)

        mapp = [m[:] for m in tmapp]


answer = int(1e9)
n,h,m,mapp = Input()
ms = [ ]
for x in range(h):
    for y in range(n-1):
        ms += [[x,y] ]

if not run():
    dfs(0,1)
else :
    answer = 0


print(answer)






