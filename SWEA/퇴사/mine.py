n = int(input())
ts = [0]
ps = [0]
dp = [0]

for i in range(1,n+1):
    a,b = map(int, input().split())
    ts.append(a)
    ps.append(b)
    if i + a > n+1 :
        dp.append([i + a, -1])
    else : dp.append([i+a, b])

for i in range(2,n+1):
    t, p = ts[i], ps[i]
    for j in range(1,i) :
        pt, pp = dp[j]
        if pt <= i :
            temp = pp + p
            if temp > dp[i][1] :
                if i + t > n+1 :
                    continue
                dp[i][1] = temp
                dp[i][0] = i+t

max_val = 0
for i in range(1, n+1) :
    if max_val < dp[i][1]:
        max_val = dp[i][1]
print(max_val)
