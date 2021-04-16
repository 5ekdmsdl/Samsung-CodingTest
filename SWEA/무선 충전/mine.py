import math

def Inarea(xy, bcxy, bcc,a):
    x,y = xy
    data = [-1]
    for i in range(a):     
        dist = abs(x-bcxy[i][0]) + abs(y-bcxy[i][1])
        #print(i, bcxy[i], xy, dist ,bcc[i])
        if dist <= bcc[i]:
            data.append(i)
    return data

def move(x,y,d):
    dx, dy = [0,0,1,0,-1], [0,-1,0,1,0]
    return x + dx[d], y + dy[d]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    am, bm, bcxy, bcc, bcp = [0],[0],[], [], []
    m, a = map(int, input().split())
    #print('a',a)
    am += list(map(int, input().split()))
    bm += list(map(int, input().split()))
    for _ in range(a):
        q, b,c,d = map(int,input().split())
        bcxy.append([q,b])
        bcc.append(c)
        bcp.append(d)
    #print(am, bm)
    result = 0
    ax, ay, bx, by = 1,1,10,10
    ain, bin = [False]*a, [False]*a
    for i in range(m+1): #움직이는 횟수
        ax, ay = move(ax, ay,am[i])
        bx, by = move(bx, by,bm[i])
        #print(i, ax, ay, bx,by)
        ain = Inarea([ax, ay], bcxy, bcc,a)
        bin = Inarea([bx, by], bcxy, bcc,a)
        #print(i,ain, bin)
        
        answer = 0
        for aa in ain:
            for bb in bin:
                xx = []
                total = 0
                if aa >= 0 and aa == bb :
                    xx.append(bcp[aa])
                    total += bcp[aa]
                else:
                    if aa >= 0 : 
                        xx.append(bcp[aa])
                        total += bcp[aa]
                    if bb >= 0 : 
                        xx.append(bcp[bb])
                        total += bcp[bb]
                answer = max(answer, total)
        
        
        result += answer
        #print(i,[ax,ay],[bx,by],answer,xx)
    print('#{} {}'.format(test_case, result))
                    
                    
                    
                    
