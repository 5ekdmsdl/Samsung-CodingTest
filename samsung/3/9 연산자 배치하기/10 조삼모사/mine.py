def mainfunc(chosen):
    global min_val
    result1 = 0
    result2 = 0
    unchosen = []
    for i in list(range(n)):
        if i not in chosen :
            unchosen.append(i)

    for i, v in enumerate(chosen) :
        for j in chosen[i+1:] :
            # print(v,j,mapp[v][j],)
            result1 += (mapp[v][j] + mapp[j][v])

    for i, v in enumerate(unchosen) :
        for j in unchosen[i+1:] :
            result2 += (mapp[v][j] + mapp[j][v])

    if result1 > result2 :
        gap = result1 - result2
    else : gap = result2 - result1
    if gap < min_val :
        # print(chosen, unchosen, result1, result2, gap)
        min_val = gap
    return


def func(now, vec, len):
    # print(now, vec, len)
    if len == n//2 :
        mainfunc(vec)
        return
    elif now > n-1 :
        # print("out")
        return
    else :
        func(now+1, vec, len)
        func(now+1, vec+[now], len+1)

n = int(input())
mapp = []
# sumall = 0
min_val = int(1e9)

for _ in range(n):
    line = list(map(int,input().split()))
    # sumall += sum(line)
    mapp.append(line)

func(0,[],0)

print(min_val)
