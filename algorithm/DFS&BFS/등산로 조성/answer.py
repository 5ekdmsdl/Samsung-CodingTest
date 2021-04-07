T = int(input())
def dfs(start,skill,cnt):
    x,y = start[0],start[1]
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx <=N-1 and 0 <= ny <=N-1 and mat[nx][ny] < mat[x][y] and (nx,ny) not in check:
            check[(nx,ny)] = 1
            sol = dfs((nx,ny),skill,cnt+1)
            s.append(sol)
            del check[(nx,ny)]
            
        elif 0 <= nx <=N-1 and 0 <= ny <= N-1 and mat[nx][ny] >= mat[x][y] and (nx,ny) not in check:
            r = mat[nx][ny] - mat[x][y]
            if r >= K or skill == 0:
                continue

            if skill == 1:
                for k in range(r+1,K+1): # 차이만큼 깎기
                    mat[nx][ny] -= k
                    if mat[nx][ny] < mat[x][y]:
                        check[(nx,ny)] = 1
                        sol = dfs((nx,ny),skill-1,cnt+1)
                        s.append(sol)
                        skill = 1
                        del check[(nx,ny)]
                    mat[nx][ny] += k
            else:
                return cnt

    return cnt

for test in range(T):
    N,K = map(int,input().split())
    mat = []
    M = 0
    highest = [] # max봉우리 저장소
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    s = []
    
    for i in range(N):
        a = list(map(int,input().split()))
        if M < max(a):
            highest = []
            M = max(a)
            
        for j in range(N):
            if a[j] == M:
                highest.append((i,j))
        mat.append(a)

    for h in highest:
        check = {h : 1}
        dfs(h,1,1)

    print('#%d'%(test+1), max(s))
