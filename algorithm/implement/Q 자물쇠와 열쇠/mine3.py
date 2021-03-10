def solution(key, lock):
    N = len(lock)
    M = len(key)
    il = []
    ik = []
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                il.append([i,j])
    for a in range(M):
        for b in range(M):
            if key[a][b] == 1:
                ik.append([a,b])
                
    for i in range(4):
        ik = turn(ik,M)
        if fit(il,ik) == True:
            return True          
    return False

def turn(ik,M):
    for i in ik:
        i[0] = (M-1)-i[0]
        i[0],i[1] = i[1],i[0]
    return ik

def fit(il,ik):
    xgap = il[0][0] - ik[0][0]
    ygap = il[0][1] - ik[0][1]
    
    flg = True
    for i in il:
        if [i[0]-xgap,i[1]-ygap] not in ik:
            flg = False
            break
    return flg
