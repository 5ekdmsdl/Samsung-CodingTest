import sys
input = sys.stdin.readline
INF = int(1e9)

# n,m = map(int,input().split())
n, m = 6, 11

# start = int(input())
start = 1

graph = [[] for _ in range(n+1)]


visited = [False] * (n+1)

distance = [INF] * (n+1)

# for _ in range(m):
#   a, b, c = map(int,input().split())
#   graph[a].append((b,c))
graph = [[],[(2,2),(3,5),(4,1)],[(3,3),(4,2)],[(2,3),(6,5)],[(3,3),(5,1)],[(3,1),(6,2)],[]]

def get_smallest_node():
  min_index = 0
  for i in range(1,n+1):
    if not visited[i] and distance[min_index] > distance[i]:
      min_index = i
  return min_index

def dijkstra(start):
  distance[start] = 0
  now = start
  
  for i in graph[start]:
    distance[i[0]] = i[1]

  for _ in range(n-1):
    now = get_smallest_node()
    visited[now] = True
    for route in graph[now]:
      if distance[now] + route[1] < distance[route[0]]:
        distance[route[0]] = distance[now] + route[1]

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INF")
  else :
    print(distance[i])
