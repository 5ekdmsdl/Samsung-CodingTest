def move(x,y,d):
    return x + dx[d] ,y + dy[d]

dx, dy = [-1, 1, 0,0], [0,0,-1,1]
change = [[],[1,3,0,2],[3,0,1,2],[2,0,3,1],[1,2,3,0],[1,0,3,2]]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    blocks = {}
    whs = {}
    bhs = []
    n = int(input())
    sth = []
    db = [[[-1,-1,-1,-1] for _ in range(n)] for _ in range(n)]
    #print(db)
    
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j] > 0 :
                sth.append([i,j])
                if line[j] >= 1 and line[j] <= 5 : 
                    try : blocks[line[j]].append([i,j])
                    except : blocks[line[j]] = [[i,j]]
                elif line[j] >= 6 and line[j] <= 10 :
                    try : whs[line[j]].append([i,j])
                    except : whs[line[j]] = [[i,j]]
            elif line[j] == -1 :
                sth.append([i,j])
                bhs.append([i,j])
    #print(blocks, whs, bhs)
    
    max_score = 0
    for i in range(n):
        for j in range(n):
            if [i,j] in sth :
                continue
            
            for d_now in range(4):
                start, [x,y], score = [i,j], [i,j], 0
                d = d_now
                    
                while(1) :    
                    x,y = move(x,y,d)
                    #print(x,y,d)
                    
                    
                    
                    if [x,y] in bhs or [x,y] == start : 
                        break
                    
                    if x >= 0 and x <= n-1 and y >= 0 and y <= n-1 and db[x][y][d] >= 0 :
                        #print('dbsc',x,y, score)
                        score += db[x][y][d]
                        #print(x,y,db[x][y][d])
                        break
                    
                    if x < 0 or x > n-1 or y < 0 or y > n-1 :
                        #print('wsc', score)
                        score += 1
                        if d == 0 or d == 2 : d += 1
                        elif d == 1 or d == 3 : d -= 1
                    
                    elif [x,y] in whs.values() :
                        for i in whs.keys():
                            if [x, y] in whs[i] :
                                k = i
                        for wh in list(whs[k].values()) :
                            if wh != [x,y] :
                                [x,y] = wh
                    
                    for kk, v in blocks.items():
                        if [x,y] in v :
                            d = change[kk][d]
                            #print('bsc', score)
                            score += 1
                            break
				
                db[i][j][d_now] = score       
                #print('sc', score)
                max_score = max(max_score, score)
    #print(db)
    print('#{} {}'.format(test_case, max_score))
                
