from collections import deque

n,m,k,start = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m+1):
  a,b = map(int,input().split())
  graph[a].append(b)

distance = [-1]*(n+1)
distance[start] = 0

q=deque([x])
while q:
  now = q.popleft()
  for next in graph[now]:
    if distance[next] == -1:
      distance[next] = distance[now]+1
      q.append(next)

check = False
for i in range(1,n+1):
  if distance[i] == k:
    check = True]
    print(distance[i],end='\n')

if not check:
  print('-1')
