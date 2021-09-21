# 00
def setnode():
    global node
    node += [_ for _ in range(2,41,2)]
    node += [
        13,16,19,
        22,24,
        28,27,26,
        25,30,35,0
    ]

# 00
def onsameNode(p):
    global ps
    if ps[p] == END or ps[p] == START:
        return False
    if ps.count(ps[p]) >= 2 :
        return True
    return False
# 00
def on_blue(p):
    if ps[p] == 5 or ps[p] == 10 or ps[p] == 15 :
        return True
    else : return False
# 00
def on_4way(p):
    if ps[p] in INTS :
        return True
    else : return False

# 00
def move_4way_onestep(p):
    global score
    if ps[p] in INTS[:3] :
        ps[p] = NODE_25
    elif ps[p] == INTS[3] :
        ps[p] = 20
    elif ps[p] == INTS[4] :
        ps[p] = END
    # score += node[ps[p]]
    return

# 00
def moveForward_onestep(p):
    global score
    ps[p] += 1
    # score += node[ps[p]]
# 00
def movefromBlue(p, step):
    global score
    if ps[p] == 5 :
        ps[p] = 21
    elif ps[p] == 10 :
        ps[p] = 24
    elif ps[p] == 15 :
        ps[p] = 26
    # score += node[ps[p]]
    step -= 1
    for s in range(step):
        if ps[p] == END :
            return
        if on_4way(p):
            move_4way_onestep(p)
        else :
            moveForward_onestep(p)
    return
# 001 2 3 4 5 1 2 3 4 5
def movefromWhite(p, step):
    for s in range(step):
        if ps[p] == END :
            return
        if on_4way(p):
            move_4way_onestep(p)
        else :
            moveForward_onestep(p)
    return

def move(p, step):
    global score
    if on_blue(p):
        movefromBlue(p, step)
        score += node[ps[p]]
    else :
        movefromWhite(p, step)
        score += node[ps[p]]
    return

def dfs(i):
    global ps, maxv, score
    if i == 10 :
        maxv = max(score, maxv)
        return
    elif ps == [END,END,END,END,] :
        maxv = max(score, maxv)
        return
    else :
        step = steps[i]
        tmpscore = score
        tmpps = []
        for pp in ps :
            tmpps.append(pp)
        for p in range(4):
            if ps[p] == END : continue
            move(p,step)
            if not onsameNode(p):
                dfs(i+1)
            score = tmpscore
            ps = []
            for pp in tmpps:
                ps.append(pp)
            # a = 1
    return

def main():
    global maxv
    setnode()
    dfs(0)
    # maxv = max(score, maxv)
    return


steps = list(map(int, input().split()))
node = [0]
START = 0
END = 32
INTS = [23,25,28,31,20]
NODE_25 = 29

ps = [START, START,START ,START]
maxv = 0
score= 0

main()
print(maxv)
