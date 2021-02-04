from collections import deque

# n,m = map(int,input().split())

# graph = []

# for i in range(n):
#   graph.append(list(map(int,input())))

n=5
m=6

graph = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  print(queue)
  while queue:
    x, y = queue.popleft()
    print(x,'&',y)

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      print(dx[i],dy[i])
      print(nx,ny)
      if nx<0 or nx>n-1 or ny<0 or ny > m-1:
        continue
      if graph[nx][ny] == 0:
        print('0',nx,ny)
        continue
      if graph[nx][ny] == 1:
        print('1',nx,ny)
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
  
  print(graph)
  return graph[n-1][m-1]

print(bfs(0,0))
