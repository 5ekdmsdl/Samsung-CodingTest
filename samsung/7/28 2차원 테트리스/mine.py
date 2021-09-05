def down(mapp, block):
    bflag = 0
    while(1):
        nb = []
        for b in block :
            nb.append([b[0]+1, b[1]])

        for b in nb :
            if mapp[b[0]][b[1]] == 1 :
                for b in block:
                    mapp[b[0]][b[1]] = 1
                return
        for b in nb :
            if b[0] == 9 :
                for b in nb:
                    mapp[b[0]][b[1]] = 1
                return
        block = nb

def makeblock(x,y,t):
    if t == 1 :
        return [[x,y]]
    elif t == 2 :
        return [[x,y],[x,y+1]]
    elif t == 3:
        return [[x,y],[x+1,y]]
    return

def changeaxis(block):
    nb = []
    for b in block:
        x,y = b[1],abs(b[0]-3)
        nb.append([x,y])
    return nb

def linefull(mapp):
    global score
    rtlist = []
    for i in range(10) :
        if 0 in mapp[i] :
            continue
        else :
            score += 1
            rtlist.append(i)
    return rtlist

def eraseline(mapp,i):
    tmp = [[0] * 4]
    tmp += mapp[0:i]
    tmp += mapp[i+1:]

    return tmp

def blockinZone(mapp):
    rtv = 0
    if 1 in mapp[4] :
        rtv += 1
    if 1 in mapp[5]:
        rtv += 1
    return rtv

ymapp, rmapp = [[0]*4 for _ in range(10)], [[0]*4 for _ in range(10)]
score = 0
n = int(input())
for _ in range(n):
    t, x,y = map(int, input().split())
    yblock = makeblock(x,y,t)
    rblock = changeaxis(yblock)
    # for y in yblock:
    #     ymapp[y[0]][y[1]] = 1
    # print()
    # for y in yblock:
    #     ymapp[y[0]][y[1]] = 0
    for y in rblock:
        rmapp[y[0]][y[1]] = 2
    # print()
    for y in rblock:
        rmapp[y[0]][y[1]] = 0
    down(ymapp, yblock)
    down(rmapp, rblock)
    # print()

    rtlist = linefull(ymapp)
    for rtv in rtlist :
        ymapp = eraseline(ymapp,rtv)

    rtlist = linefull(rmapp)
    for rtv in rtlist :
        rmapp = eraseline(rmapp,rtv)

    rtv = blockinZone(ymapp)
    if rtv :
        for _ in range(rtv):
            ymapp = eraseline(ymapp,9)
    rtv = blockinZone(rmapp)
    if rtv:
        for _ in range(rtv):
            rmapp = eraseline(rmapp,9)

cnt = 0
for x in ymapp :
    for y in x :
        if y == 1 :
            cnt += 1
for x in rmapp :
    for y in x :
        if y == 1 :
            cnt += 1

print(score)
print(cnt)






# score = 0
# ymapp = [[0]*4 for _ in range(10)]
# rtv = linefull(ymapp)
# print(rtv)
