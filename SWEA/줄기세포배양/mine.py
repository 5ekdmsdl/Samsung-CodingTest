dx = [0,0,-1,1]
dy = [-1,1,0,0]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m,k = map(int, input().split())
    cell = []
    done, using = {}, {}
    for i in range(n):
        line = list(map(int,input().split()))
        for j in range(m):
            if line[j] > 0 :
            	cell.append([i,j,line[j], 0, line[j]])
    #print(cell)
    for t in range(k):
        #print('cell',cell,done)
        using = {}
        for c in cell :
            
            if c[3] == 0 :
                c[4] -= 1
                if c[4] == 0 :
                    c[3] = 1
                    c[4] = c[2]
                    
            elif c[3] == 1 :
                if c[4] == c[2] :
                    for i in range(4) :
                        nx = c[0] + dx[i]
                        ny = c[1] + dy[i]
                        if (nx, ny) not in done.keys() :
                            if (nx, ny) not in using.keys() :
                                using[(nx,ny)] = [nx, ny, c[2], 0, c[2]]
                            else :
                                if c[2] > using[(nx, ny)][2] :
                                    using[(nx,ny)] = [nx, ny, c[2], 0, c[2]]
                                    #print('using',using)
                c[4] -= 1
                if c[4] == 0 :
                    c[3] = 2
        #print(cell)
		
        for i in using.keys() :
            cell.append(using[i])
            done[i] = 1
        
        for c in cell :    
            if c[3] == 2 :
                cell.remove(c)
    
    for c in cell :    
        if c[3] == 2 :
            cell.remove(c)
                
        #print(len(cell),cell,'\nu',using)
    print(len(cell),cell)      
    
    
    
    
    
    
    
    
    
    
    
