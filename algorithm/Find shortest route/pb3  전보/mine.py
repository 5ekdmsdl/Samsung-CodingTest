import heapq

# n,m,c = map(int,input().split())
n,m,c = 3,2,1

INF = int(1e9)
start = c

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))
  graph[y].append((x,z))

# print(graph)

city_cnt = 0
time_cnt = 0

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    # print(q)
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      next = i[0]
      cost = i[1] + dist
      if cost < distance[next]:
        distance[next] = cost
        heapq.heappush(q,(cost,next))
    
dijkstra(start)

max_value = 0

for i in range(1,n+1):
  if distance[i] < INF and distance[i] > 0:
    city_cnt += 1
    if distance[i] > max_value:
      max_value = distance[i]

time_cnt = max_value  


print(city_cnt,time_cnt)
