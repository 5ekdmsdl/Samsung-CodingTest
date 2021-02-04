from collections import deque

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
  route = list(map(int,input().split()))
  graph[route[0]].append(route[1])

visited = [False]*(n+1)
cnt = [-1]*(n+1)

def bfs(x,k):
  queue = deque()
  queue.append(x)
  cnt[x] = 0
  result = []

  while queue:
    x = queue.popleft()
    visited[x] = True
    for nx in graph[x]:
      if visited[nx] == True:
        continue
      else:
        queue.append(nx)
        if cnt[nx] == -1:
          cnt[nx] = cnt[x]+1

  for i in range(len(cnt)):
    if cnt[i] == k:
      result.append(i)

  return result


print(bfs(x,k))
