import heapq

# n = int(input())
# m = int(input())
n,m = 5,14

# # graph = [[] for _ in range(n+1)]
graph = [[],[(2,2),(3,3),(4,1),(5,10),(4,2)],[(4,2)],[(4,1),(5,1),(5,10),(1,8),(4,2)],[(5,3)],[(1,7),(2,4)]]

INF = int(1e9)
dist = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  # a, b, c = map(int,input().split())
  for j in graph[i]:
    a,b,c = i,j[0],j[1]
    dist[a][b] = min(dist[a][b], c)
  dist[i][i] = 0

for k in range(1, n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      # print(k,a,b,end='\n')
      dist[a][b] = min(dist[a][b], dist[a][k]+dist[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    print(dist[a][b],end=' ')
  print('\n')
    

