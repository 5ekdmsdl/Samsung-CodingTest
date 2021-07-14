def funcA():
    for (r,c) in vs.keys():
        for i, v in enumerate(vs[(r,c)]):
            if mapp[r][c] < v :
                vs[(r,c)].remove(v)
                dead.append([r,c,v])
            else :
                mapp[r][c] -= v
                vs[(r, c)][i] += 1
                if vs[(r, c)][i]%5 == 0 :
                    produce.append((r,c))
def funcB():
    global dead
    for (r,c,v) in dead :
        mapp[r][c] += (v//2)
    dead = []

def funcC():
    global produce
    dr, dc = [0,0,-1,-1,-1,1,1,1], [-1,1,0,-1,1,0,-1,1]
    for (r,c) in produce :
        for i in range(8) :
            nr, nc = r+dr[i], c+dc[i]
            if 1 <= nr <= n and 1 <= nc <= n :
                if (nr, nc) in vs.keys():
                    vs[(nr, nc)].append(1)
                    vs[(nr, nc)].sort()
                else:
                    vs[(nr, nc)] = [1]
    produce = []



n,m,k = map(int, input().split())
mapp = [[5]*(n+1) for _ in range(n+1)]
addmapp = []
vs = {}
dead = []
produce = []

for _ in range(n):
    addmapp.append(list(map(int, input().split())))

for _ in range(m):
    r,c,v = map(int, input().split())
    if (r,c) in vs.keys() :
        vs[(r,c)].append(v)
    else :
        vs[(r,c)] = [v]

# print(vs)

# for a in range(1,n+1) :
#     for b in range(1,n+1) :
#         if (a,b) in vs.keys() :
#             if vs[(a,b)] == [] :
#                 print("-", end = " ")
#             else :
#                 print(vs[(a,b)],end=" ")
#         else : print("-",end=" ")
#     print()
# print("ori","======================")


for i in range(k):
    funcA()
    funcB()
    funcC()
    for a in range(1,n+1) :
        for b in range(1,n+1) :
            mapp[a][b] += addmapp[a-1][b-1]

    # for a in range(1, n + 1):
    #     for b in range(1, n + 1):
    #         if (a,b) in vs.keys() :
    #             if vs[(a,b)] == [] :
    #                 print("-", end = " ")
    #             else :
    #                 print(vs[(a,b)],end=" ")
    #         else : print("-",end=" ")
    #     print()
    # print(i,"======================")

cnt = 0

for vv in vs.values() :
    for v in vv :
        if v :
            cnt += 1

print(cnt)
