# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

#import sys
from collections import deque
import copy

'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")


def BFS(a,n,array):
    temp = [[0]*n for _ in range(n)]
    [i,j] = a
    q = deque([a])
    temp[i][j] = 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    max_val = 1

    while q:
        [x,y] = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            if array[nx][ny] < array[x][y]:
                cost = temp[x][y] + 1
                if cost > temp[nx][ny]:
                    temp[nx][ny] = cost
                    if cost > max_val:
                        max_val = cost
                    q.append([nx, ny])
    return max_val

dx = [0,0,-1,1]
dy = [-1,1,0,0]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    array = []
    n, k  = map(int, input().split())
    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        line = list(map(int,input().split()))
        array.append(line)
    #print(array)
    #입력 다 받음
	
    array_max = max(map(max, array))
    top_indexs = []
    
    for i in range(n):
        for j in range(n):
            dist[i][j] = BFS([i,j],n,array)
            if array[i][j] == array_max :
                top_indexs.append([i,j])
    #print(top_indexs)
    #print("dist:",dist,'\n\n')
    
    
    max_val = max(map(max, dist))
    
    for t in top_indexs:
        q = deque([t])
        [x,y] = t
        start_val = array[x][y] 
        
        while q:
            [x,y] = q.popleft()
            
            if dist[x][y] == 1:
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                            continue
                        if (dist[nx][ny] - k) < dist[x][y]:
                            max_val = max(max_val, start_val + 1)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                    continue
                if dist[nx][ny] == dist[x][y] - 1:
                    q.append([nx,ny])


                if dist[nx][ny] >= dist[x][y]:
                    for j in range(4):
                        nnx = nx + dx[i]
                        nny = ny + dy[i]
                        if nnx < 0 or nnx > n-1 or nny < 0 or nny > n-1:
                            continue
                        if dist[nnx][nny] == dist[nx][ny]-1:
                            if array[x][y] - array[nnx][nny] <= k:
                                max_val = max(max_val, dist[nx][ny] + (start_val - array[x][y] + 1))

                                
    print("#",test_case,max_val) 
    #print("\n\n\n")
    
    # ///////////////////////////////////////////////////////////////////////////////////

