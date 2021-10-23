def setmapp():
    mapp = [i for i in range(0,41,2)]
    mapp += [
        99,
        13,16,19,
        22,24,
        28,27,26,
        25,30,35,
    ]
    return mapp

def is_start(idx):
    if mapp[idx] == start :
        return True
    return False

def is_end(idx):
    if mapp[idx] == end:
        return True
    return False

def moveTo(idx):
    global npos
    npos = idx
    return

def next(idx):
    return idx + 1

def move(i, step):
    global npos, scr

    npos = ps[i]

    for s in range(step):
        if s == 0 and npos in Bs.keys():
            moveTo(Bs[npos])

        elif npos in Int.keys():
            moveTo(Int[npos])

        else :
            moveTo(next(npos))

        if is_end(npos) :
            ps[i] = npos
            break

    if not is_start(npos) and not is_end(npos) and npos in ps :
        return

    elif not is_end(npos) :
        scr += mapp[npos]
        ps[i] = npos

    return

def dfs(i):
    global ans, scr, steps, ps, mapp, end, fp, cnt

    if i >= 10 :
        cnt += 1
        if scr > ans :
            ans = scr
            fp = []
        return

    step = steps[i]

    tmp, ptmp, ftmp = scr, ps[:], fp[:]

    for idx in range(4):
        if is_end(ps[idx]) == False :
            move(idx, step)
            fp.append([idx, mapp[ps[idx]]])
            dfs(i+1)

            scr, ps, fp = tmp, ptmp[:], ftmp[:]
    return

ans, scr = 0,0
start, end = 0, 99
npos = 0
ps = [start] * 4
cnt = 0

fp = []

steps = list(map(int, input().split()))

mapp = setmapp()
Bs = {
    5 : 22, 10:25, 15:27,
}
Int = {
    24:30,
    26:30,
    29 : 30,
    32 : 20
}
dfs(0)

print(ans)
