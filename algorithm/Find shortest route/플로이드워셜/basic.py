INF = int(1e9)

# n = int(input())
# m = int(input())
n = 4
m = 7

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b] = 0

# for _ in range(m):
#   a,b,c = map(int, input().split())
#   graph[a][b] = c

graph[1][2] = 4
graph[1][4] = 6
graph[2][1] = 3
graph[2][3] = 7
graph[3][1] = 5
graph[3][4] = 4
graph[4][3] = 2

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b] == INF:
      print("INFF",end=' ')
    else:
      print(graph[a][b],end=' ')
  print()

