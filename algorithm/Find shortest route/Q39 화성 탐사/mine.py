import heapq

# t = int(input())
t=1
res = []
INF = int(1e9)
dx = [1,0,0,-1]
dy = [0,1,-1,0]

def findmincost(graph,n):
  q = []
  flgs = [[False]*n for _ in range(n)]
  heapq.heappush(q,(graph[0][0],0,0))
  while q:
    price, x,y = heapq.heappop(q)
    for i in range(4):
      nx = dx[i]+x
      ny = dy[i]+y
      if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
        continue
      if flgs[nx][ny] == False:
        graph[nx][ny] += graph[x][y]
        heapq.heappush(q,(graph[nx][ny],nx,ny))
        flgs[nx][ny] = True
      if nx == n-1 and ny == n-1:
        return graph[nx][ny]
      


for j in range(t):
  # n = int(input())
  n=7
  graph = []
  # for i in range(n):
  #   graph.append(list(map(int,input().split())))
  graph = [[9,0,5,1,1,5,3],[4,1,2,1,6,5,3],[0,7,6,1,6,8,5],[1,1,7,8,3,2,3],[9,4,0,7,6,4,1],[5,8,3,2,4,8,3],[7,4,8,4,8,3,4]]
  res.append(findmincost(graph,n))

for j in range(t):
  print(res[j])

