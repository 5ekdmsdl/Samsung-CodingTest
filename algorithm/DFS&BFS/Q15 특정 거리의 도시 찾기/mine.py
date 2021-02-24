import heapq

n, m, k, start = map(int,input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)

INF = int(1e9)
distance = [INF]*(n+1)
print(graph)

q = []
heapq.heappush(q,start)
distance[start] = 0

while q:
  now = heapq.heappop(q)
  for i in graph[now]:
    next = i
    cost = distance[now]+1
    if cost < distance[next]:
      distance[next] = cost
      heapq.heappush(q,next)

if k in distance:
  for i in range(1,n+1):
    if distance[i] == k:
      print(i,end='\n')
else:
  print('-1')
  
 
