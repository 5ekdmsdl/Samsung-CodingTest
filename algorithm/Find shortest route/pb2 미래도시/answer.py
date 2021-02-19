# n, m = map(int,input().split())
n=5
m=7
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
  graph[a][a] = 0

for i in range(m):
  a, b = map(int,input().split())
  graph[a][b] = 1
  graph[b][a] = 1

# x, k = map(int,input().split())
x,k = 4,5

for c in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][c]+graph[c][b],graph[a][b])

distance = graph[1][k] + graph[k][x]

if distance > INF:
  print(-1)
else:
  print(distance)
