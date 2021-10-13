def setmap():
    global Int, Blu, mapp
    Blu = {5 : 22,
           10 : 25,
           15 : 27}
    Int = {
        24 : 30,
        26 : 30,
        29 : 30,
        32 : 20
    }
    mapp = [_ for _ in range(0,41,2)]
    mapp += [
        99,
        13,16,19,
        22,24,
        28,27,26,
        25,30,35
    ]

    return

def getscr(pi):
    global tscr

    if mapp[ps[pi]] == Ev : return
    tscr += mapp[ps[pi]]

    return

def poss(pi):
    if ps[pi] == Sv or ps[pi] == Ev :
        return True
    else :
        if ps.count([ps[pi]]) >= 2 :
            return False
    return True

def Black(pi, s):
    global scr, tscr
    tscr = 0

    pitmp = pi

    for i in range(s):
        if ps[pi] in Int.keys() :
            ps[pi] = Int[ps[pi]]
        else :
            ps[pi] += 1

        getscr(pi)

        if mapp[ps[pi]] == Ev :
            Fs.append(pi)
            return

    if not poss(pi):
        pi = pitmp
    else :
        scr += tscr

    return

def Red(pi, s):
    tscr = 0

    s -= 1
    ps[pi] = Blu[ps[pi]]
    getscr(pi)

    Black(pi,s)

    return

def move(i, s):
    p = ps[i]

    if p in Blu :
        Red(i, s)
    else :
        Black(i, s)

    return

def dfs(i):
    global ps, scr, Fs, ans, cnt

    if i == 10 :
        # cnt += 1
        if scr > ans : ans = scr
        return

    ptmp = [p for p in ps]
    scrtmp = scr
    Ftmp = [F for F in Fs]

    n = ns[i]

    for j in range(4):
        if j in Fs : continue

        move(j,n)

        dfs(i+1)

        ps = [p for p in ptmp]
        scr = scrtmp
        Fs = [F for F in Ftmp]

    return


Si , Sv, Ev = 0,0,99
ans, scr, tscr, Fs = 0,0,0, []
Int, Blu = {}, {}
mapp = []
cnt = 0

ps = [Si] * 4
ns = list(map(int, input().split()))

setmap()
dfs(0)

print(ans)












