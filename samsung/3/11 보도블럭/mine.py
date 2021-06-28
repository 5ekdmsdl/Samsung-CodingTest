def func(aline):
    global cnt
    # print(aline)
    now = 0
    success = 1
    while(now < n-1) :
        next = now + 1
        # print(now, next)
        if aline[now] == aline[next] :
            now += 1
            continue

        elif aline[now] > aline[next] :
            if aline[now] - aline[next] > 1 :
                success = 0
                break
            else :
                floor = aline[next]
                for i in range(l):
                    if next+i > n-1 or aline[next+i] != floor :
                        line_succ = 0
                        success = 0
                        break
                if line_succ :
                    for i in range(l) :
                        print(next+i)
                        aline[next+i] += 0.5

        else :
            if aline[next] - aline[now] > 1 :
                success = 0
                break
            else :
                floor = aline[now]
                for i in range(l) :
                    if now-i < 0 or aline[now-i] != floor :
                        success = 0
                        break
                if line_succ :
                    for i in range(l) :
                        print(next+i)
                        aline[next+i] += 0.5


    # print(aline)
    if success :
        cnt += 1
        # print("yeahh")


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
print(cnt)
