def func(aline):
    global cnt
    print("start",aline)

    now = 0
    line_flg = 1

    while now < n-1 :
        next = now + 1
        # print(now, next)
        if aline[now] == aline[next] :
            now += 1
            continue

        elif 0.5 < (aline[now] - aline[next]) < 2 :
            floor = aline[next]
            if next + l > n-1 :
                line_flg = 0
                break
            flg = 0
            for i in range(l):
                if aline[next+i] != floor :
                    line_flg = 0
                    flg = 1
                    break
            if flg :
                break
            now = now + l
            for i in range(l) :
                aline[next + i] += 0.5

                # print(aline)

        elif 0.5 < (aline[next] - aline[now]) < 2 :
            floor = aline[now]
            flg = 0
            for i in range(l):
                if aline[now-i] != floor :
                    line_flg = 0
                    flg = 1
                    break
            if flg :
                break
            for i in range(l) :
                aline[now - i] += 0.5
                # print(aline)
            now += 1
        else :
            line_flg = 0
            break

    print(aline)
    if line_flg :
        cnt += 1
        print("yeahh")


n, l = map(int,input().split())
mapp = []
cnt = 0
for _ in range(n) :
    mapp.append(list(map(int, input().split())))

for i in range(n):
    aline = []
    func(mapp[i][:])
    for j in range(n):
        aline.append(mapp[j][i])
    func(aline)

# func([1,3,1,1,2,1])
print(cnt)
