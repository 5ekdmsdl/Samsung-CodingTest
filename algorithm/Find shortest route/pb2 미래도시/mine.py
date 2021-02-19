import heapq

# n, m = map(int,input().split())
n=5
m=7
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

# for i in range(m):
#   a,b = map(int,input().split())
#   graph[a].append(b)
#   graph[b].append(a)

graph = [[],[2,3,4],[1,4],[1,4,5],[1,2,3,5],[3,4]]

# x, k = map(int,input().split())
x,k = 4,5

if x in graph[k]:
  xtok = True
else:
  xtok = False
  print(-1)

if xtok :
  q = []
  start = 1
  distance[start] = 0
  heapq.heappush(q,(distance[start],start))
  while q:
    print(q,end='\n')
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for next in graph[now] :
      cost = dist + 1
      if cost < distance[next]:
        distance[next] = cost
        heapq.heappush(q,(cost, next))

  total = distance[k] + 1
  print(total)


print(graph)


