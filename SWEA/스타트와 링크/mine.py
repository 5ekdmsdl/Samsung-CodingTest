import math


def comb(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else :
            for next in comb(array[i+1:], r-1):
                yield [array[i]] + next

n = int(input())
mapp = []
data = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    line = list(map(int, input().split()))
    mapp.append(line)
    for j in range(n):
        if not i == j:
            data[min(i,j)+1][max(i,j)+1] += mapp[i][j]

ns = [_ for _ in range(1,n+1)]
ec1 = list(comb(ns, n//2))

min_val = int(1e9)
nn = len(ec1)

for a in range(nn//2):
    c1,c2 = ec1[a], ec1[nn-a-1]
    result = 0
    for i in range(n//2):
        x11, x21= c1[i], c2[i]
        for j in range(i+1, n//2):
            x12 ,x22= c1[j],c2[j]
            result += data[x11][x12] - data[x21][x22]
    if result < 0:
        if min_val >  -result:
            min_val = -result
    else :
        if min_val >  result:
            min_val = result

print(min_val)
