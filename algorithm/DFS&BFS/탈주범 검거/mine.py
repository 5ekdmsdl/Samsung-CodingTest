#import sys
from collections import deque

#sys.stdin = open("input.txt", "r")
dx = [0,0,-1,1]
dy = [-1,1,0,0]

dir = [[], [0,1,2,3], [2,3], [0,1], [2,1], [1,3], [0,3], [0,2]]

def bfs(start, l):
    cnt = 0
    visited = {start : 1}
    q = deque()
    q.append([start, 1])
    while q:
        #print(q)
        [(x,y),t] = q.popleft()
        if t > l :
            continue
        else : cnt += 1
        for d in dir[arr[x][y]]:
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 : 
                continue
            if (nx, ny) in visited:
                continue
            if d == 1 and 0 in dir[arr[nx][ny]]:
                visited[(nx,ny)] = 1
                q.append([(nx, ny), t+1])
            elif d == 2 and 3 in dir[arr[nx][ny]]:
                visited[(nx,ny)] = 1
                q.append([(nx, ny), t+1])
            elif d == 3 and 2 in dir[arr[nx][ny]]:
                visited[(nx,ny)] = 1
                q.append([(nx, ny), t+1])
            elif d == 0 and 1 in dir[arr[nx][ny]]:
                visited[(nx,ny)] = 1
                q.append([(nx, ny), t+1])
            #print(0 in dir[arr[nx][ny]])
        #print(cnt)
    return cnt

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    arr = []
    n,m,r,c,l = map(int,input().split())
    start = (r,c)
    for i in range(n):
        line = list(map(int, input().split()))
        arr.append(line)
    #print(arr)
    answer = bfs(start, l)
    print("#"+str(test_case),answer)
    # ///////////////////////////////////////////////////////////////////////////////////
