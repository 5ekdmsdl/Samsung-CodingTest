from collections import deque
import copy

def virus(graph):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  q = deque([])
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 2:
        q.append([i,j])
  
  while q:
    [x,y] = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = 2
        q.append([nx,ny])

  return graph


def count_zero(graph):
  cnt = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        cnt += 1
  return cnt


def solution(graph):
  answer = 0

  for i1 in range(n*m):
    w1_x = i1 // m
    w1_y = i1 % m
    if graph[w1_x][w1_y] == 1 or graph[w1_x][w1_y] == 2:
      continue
    for i2 in range(i1+1, n*m):
      w2_x = i2 // m
      w2_y = i2 % m
      if graph[w2_x][w2_y] == 1 or graph[w2_x][w2_y] == 2:
        continue
      for i3 in range(i2+1, n*m):
        w3_x = i3 // m
        w3_y = i3 % m
        if graph[w3_x][w3_y] == 1 or graph[w3_x][w3_y] == 2:
          continue
        
        temp = copy.deepcopy(graph)
        # print(graph1)

        temp[w1_x][w1_y] = 1
        temp[w2_x][w2_y] = 1
        temp[w3_x][w3_y] = 1
        # print(temp,'\n',graph1,'\n',graph,'\n')
        temp = virus(temp)
        
        answer = max(answer, count_zero(temp))

  return answer

n,m = map(int,input().split())
graph = []

for i in range(n):
  graph.append(list(map(int,input().split())))

# n, m= 4,6
# graph = ([0,0,0,0,0,0],[1,0,0,0,0,2],[1,1,1,0,0,2],[0,0,0,0,0,2])

answer = solution(graph)

print(answer)
