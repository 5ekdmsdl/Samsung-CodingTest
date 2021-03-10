def solution(key, lock):
    il = []
    ik = []
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                il.append((i,j))
    for a in range(M):
        for b in range(M):
            if key[a][b] == 1:
                ik.append((a,b))
                
    for i in range(4):
        il, ik = turn(il,ik)
        if fit(il,ik) == True:
            return True          
    return False

def turn(key,M,N):
    graph1 = [[0]*M for _ in range(M)]
    graph2 = key
    for i in range(M):
        graph1[i] = graph2[M-i-1]
    for i in range(M):
        for j in range(M):
            graph2[j][i] = graph1[i][j]
    return graph2

def fit(key,lock,M,N):
    
    xgap = il[0][0] - ik[0][0]
    ygap = il[0][1] - ik[0][1]
    
    flg = True
    for i in il:
        if key[i[0]-xgap][i[1]-ygap] == 0:
            flg = False
            break
    return flg
   
