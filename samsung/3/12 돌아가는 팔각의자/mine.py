def rotate(n,d):
    # print(n,d)
    global tables
    if d == 1 :
        tables[n] = [tables[n][7]] + tables[n][:7]
    elif d == -1 :
        tables[n] = tables[n][1:] + [tables[n][0]]

def func(n, d, rotated) :
    # print(n,d,rotated)
    to_be_rotated.append((n,d))
    rotated += [n]
    if (1 <= n-1 <= 4) and (tables[n-1][2] != tables[n][6]) and (n-1 not in rotated) :
        # to_be_rotated.append(n-1)
        func(n-1, -d, rotated)
    if (1 <= n+1 <= 4) and (tables[n+1][6] != tables[n][2]) and (n+1 not in rotated) :
        # to_be_rotated.append(n+1)
        func(n+1, -d, rotated)
    return

tables = [[0]*8]
to_be_rotated = []

for _ in range(4):
    tables.append(list(map(int, input())))
#
# for t in tables :
#     print(t)

k = int(input())
for _ in range(k) :
    n,d = map(int, input().split())
    func(n,d,[])
    for tn, td in to_be_rotated :
        rotate(tn, td)
    to_be_rotated = []
    # rotate(n,-d)

# for t in tables :
#     print(t)

result = 0
for i in range(4) :
    twos = 1
    for j in range(i):
        twos *= 2
    # print(twos, tables[i+1][0])
    result += twos*tables[i+1][0]
print(result)
