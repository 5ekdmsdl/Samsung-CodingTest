import math

def check(a,b):
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    xy1, xy2 = xy[a], xy[b]
    d1, d2 = d[a], d[b]
    
    xg = xy1[0] - xy2[0]
    yg = xy1[1] - xy2[1]
    #print('xy',xy1, xy2)
    #print('xg,yg',xg,yg)
    if abs(xg) == abs(yg):
        nxy1 = [xy1[0]+dx[d1]*abs(xg), xy1[1]+dy[d1]*abs(yg)]
        nxy2 = [xy2[0]+dx[d2]*abs(xg), xy2[1]+dy[d2]*abs(yg)]
        if nxy1 == nxy2 : return abs(xg)
    elif xg == 0 :
        #print('xg=0d',d1, d2)
        if (yg > 0 and d1 ==1 and d2 == 0) or (yg < 0 and d1 == 0 and d2 == 1):
            return abs(yg)/2
    elif yg == 0:
        #print('yg=0d',d1, d2)
        if (xg > 0 and d1 ==2 and d2 == 3) or (xg < 0 and d1 == 3 and d2 == 2):
            return abs(xg)/2
    
    return False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    xy, d, k =[], [], []
    n = int(input())
    
    for _ in range(n):
        q,w,e,r = map(int, input().split())
        xy.append([q,w])
        d.append(e)
        k.append(r)
    #print(xy, d, k)
    
    bump, done = [],[]
    
    for i in range(n):
        for j in range(i+1,n):
            t = check(i,j)
            if t :
                #print(i, j)
                bump.append([t,i,j])
    bump.sort()
    #print('bump',bump)
    answer = 0
    if len(bump) > 0:
        used, nt = [ ], bump[0][0]
        
        for t, a, b in bump:
            if a in done or b in done : continue
            if nt == t : 
                if a not in used:
                    used.append(a)
                    answer += k[a]
                if b not in used:
                    used.append(b)
                    answer += k[b]
            else :
                done += used
                nt = t
                if a in done or b in done : continue
                if a not in used:
                    used.append(a)
                    answer += k[a]
                if b not in used:
                    used.append(b)
                    answer += k[b]
    
    print('#{} {}'.format(test_case, answer))
    
