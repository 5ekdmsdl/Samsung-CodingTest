def MaxMin(A,B,C,D):
    At, Bt, Ct, Dt, Et = 0, 0, 0, 0, 0
    for a1 in range(A[0]+1):
        for a2 in range(A[1]+1):
            At += mapp[a1][a2]
    At -= mapp[A[0]][A[1]]
    tmp = [A[0]+1, A[1]-1]
    while (tmp[0] != B[0]):
        for i in range(tmp[1]):
            At += mapp[tmp[0]][i]
        tmp[0] += 1
        tmp[1] += -1

    for b1 in range(B[0],n):
        for b2 in range(0,B[1]+1) :
            Bt += mapp[b1][b2]
    Bt -= mapp[B[0]][B[1]]
    tmp = [B[0] + 1, B[1] + 1]
    while (tmp[0] != C[0]):
        for i in range(tmp[0]+1,n):
            Bt += mapp[i][tmp[1]]
        tmp[0] += 1
        tmp[1] += 1

    for c1 in range(C[0],n):
        for c2 in range(C[1],n):
            Ct += mapp[c1][c2]
    Ct -= mapp[C[0]][C[1]]
    tmp = [C[0]-1 , C[1] + 1]
    while (tmp[0] != D[0]):
        for i in range(tmp[1]+1,n):
            Ct += mapp[tmp[0]][i]
        tmp[0] += -1
        tmp[1] += 1

    for d1 in range(D[0]+1):
        for d2 in range(D[1],n):
            Dt += mapp[d1][d2]
    Dt -= mapp[D[0]][D[1]]
    tmp = [D[0] - 1, D[1] - 1]
    while (tmp[0] != A[0]):
        for i in range(0,tmp[0]):
            Dt += mapp[i][tmp[1]]
        tmp[0] += -1
        tmp[1] += -1

    Et = total - (At+Bt+Ct+Dt)

    # if max(At,Bt,Ct,Dt,Et) - min(At,Bt,Ct,Dt,Et) == 8 :
    #     print()
    return max(At,Bt,Ct,Dt,Et) - min(At,Bt,Ct,Dt,Et)

def findB(A, d):
    return (A[0]+d, A[1]-d)

def findCD(A,B,d1,d2):
    C = (B[0]+d2, B[1]+d2)
    D = (A[0]+d2, A[1]+d2)
    return C, D

def inmapp(p):
    if 0<=p[0]<=n-1 and 0<=p[1]<=n-1 :
        return 1
    else : return 0
    
n = int(input())
mapp = []
total, answer = 0, int(1e9)
for _ in range(n) :
    line = list(map(int, input().split()))
    mapp.append(line)
    total += sum(line)

for Ax in range(n-2):
    for Ay in range(n-1) :
        A = (Ax, Ay)
        for d1 in range(1,n) :
            B = findB(A, d1)
            if not inmapp(B):
                break
            for d2 in range(1,n):
                C,D = findCD(A,B,d1,d2)
                if not inmapp(C) or not inmapp(D) :
                    break
                # if d1 == 2 and d2 == 2 :
                #     print()
                result = MaxMin(A,B,C,D)
                if result < answer :
                    answer = result

print(answer)

