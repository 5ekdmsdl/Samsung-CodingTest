from collections import deque

n,m = map(int,input().split())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
dist[0] = -1
dist[1] = 0
visited = [False]*(n+1)

q = deque([1])

for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

while q:
  now = q.popleft()

  if visited[now] == True:
    continue
  else:
    visited[now] = True
  
  for i in graph[now]:
    if dist[now] + 1 < dist[i]:
      dist[i] = dist[now] + 1
      q.append(i)

maxval = max(dist)
cnt = 0
flg = False

for i in range(1,n+1):
  if dist[i] == maxval:
    cnt += 1
    if flg == False:
      maxindex = i
      flg = True

print(maxindex, maxval, cnt)
