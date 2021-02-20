import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# n,m,c = map(int,input().split())
n,m,c = 3,2,1
start = c

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))
  # graph[y].append((x,z))

# print(graph)

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

city_cnt = 0
time_cnt = 0

for i in range(1,n+1):
  if distance[i] < INF:
    city_cnt += 1
    time_cnt = max(time_cnt, distance[i])

print(city_cnt-1, time_cnt)
