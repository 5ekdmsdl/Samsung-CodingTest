def flip() :
    global mapp
    if flipped :
        nr, nc = mc, mr
    else : nr, nc = mr, mc
    n_mapp = [[] for _ in range(nr)]
    for a in range(nr) :
        for b in range(nc) :
            n_mapp[a].append(mapp[b][a])
    mapp = n_mapp


def assort():
    global mapp, mr, mc
    if flipped : longer = mc
    else : longer = mr
    n_mapp = []
    for l in mapp :
        d = {}
        for s in l :
            if not s  : continue
            if s in d.keys():
                d[s] += 1
            else : d[s] = 1
        nd = [[] for _ in range(100)]
        for k, v in d.items():
            nd[v].append(k)
        nl = []
        for i,v in enumerate(nd):
            if not v : continue
            v.sort()
            for vv in v :
                nl.append(vv)
                nl.append(i)
        if len(nl) > longer :
            longer = len(nl)
        n_mapp.append(nl)

    for n in n_mapp :
        if len(n) < longer :
            n += [0]*(longer-len(n))

    mapp = n_mapp
    if not flipped :
        mr = longer
    else : mc = longer
    return 0

def kropmap() :
    global mr, mc, mapp
    if mr > 100 :
        for m in mapp :
            m = m[:100]
    elif mc > 100 :
        mapp = mapp[:100][:]
    return 0


mapp = []
r,c,k = map(int, input().split())
for i in range(3):
    mapp.append(list(map(int, input().split())))

flipped = 0
mr, mc = 3,3
t = 0

while(t < 100) :
    if flipped :
        if r <= mc and c <= mr and mapp[c-1][r-1] == k : break
    else :
        if r <= mc and c <= mr and mapp[r-1][c-1] == k : break

    if mc >= mr :
        if flipped :
            flip()
            flipped =0
    else :
        if flipped :
            pass
        else :
            flip()
            flipped = 1
    assort()

    kropmap()
    t += 1

# mapp = [[3,1,2],[1,1,2],[5,5,5]]
# flip()
# flipped = 1
# assort()
# kropmap()
# if flipped :
#     flip()
if t == 100 :  t = -1
print(t)
