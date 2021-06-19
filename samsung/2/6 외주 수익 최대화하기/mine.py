n = int(input())
results = [0]*n
ts, ps = [], []
for _ in range(n):
    t,p = map(int,input().split())
    ts.append(t)
    ps.append(p)

for i in range(0,n):
    if i + ts[i] > n :
        continue
    max_tmp = ps[i]
    for j in range(0,i):
        if j + ts[j] - 1 < i :
            if max_tmp < ps[i] + results[j] :
                max_tmp = ps[i] + results[j]
    results[i] = max_tmp

print(max(results))
