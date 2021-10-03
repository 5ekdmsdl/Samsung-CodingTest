def Input():
    r,c,k = map(int, input().split())

    mapp = []
    for _ in range(3):
        mapp.append(list(map(int, input().split())))


    return r,c,k, mapp

def sortR():
    global mapp
    rlen, clen = len(mapp), len(mapp[0])
    maxc = 0

    nmapp = [[] for _ in range(rlen)]

    for x in range(rlen):
        num = {}
        l = mapp[x]
        for i in l :
            if i :
                if i in num :
                    num[i] += 1
                else : num[i] = 1
            # else : break

        nnum = []

        for n, cnt in num.items():
            nnum.append([n,cnt])

        nnum.sort(key=lambda a:[a[1], a[0]])

        tmp = []
        for n in nnum :
            tmp += n
        nnum = tmp

        if len(nnum) > 100 : nnum = nnum[:100]
        nmapp[x] = nnum
        maxc = max(maxc, len(nnum))

        for i,n in enumerate(nmapp):
            if len(n) < maxc :
                nmapp[i] += [0 for _ in range(maxc - len(n))]


    mapp = [n[:] for n in nmapp]

    return

def Flip():
    global mapp

    rlen, clen = len(mapp), len(mapp[0])

    nmapp = [[0 for _ in range(rlen)] for _ in range(clen)]

    for x in range(rlen):
        for y in range(clen):
            nmapp[y][x] = mapp[x][y]

    mapp = [n[:] for n in nmapp]

    return


r,c,k,mapp = Input()

for t in range(100):

    rlen, clen = len(mapp), len(mapp[0])

    if rlen >= r and clen >= c and mapp[r-1][c-1] == k :
        print(t)
        break

    if rlen >= clen :
        sortR()

    else :
        Flip()
        sortR()
        Flip()

    rlen, clen = len(mapp), len(mapp[0])


if t == 99 :
    print(-1)
