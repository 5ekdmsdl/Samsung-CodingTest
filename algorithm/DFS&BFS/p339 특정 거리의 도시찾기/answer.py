from collections import deque

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a,b = list(map(int,input().split()))
  graph[a].append(b)

# visited = [False]*(n+1)
distance = [-1]*(n+1)
distance[x] = 0

queue = deque()
queue.append(x)

while queue:
  x = queue.popleft()

  for nx in graph[x]:

    if distance[nx] == -1:
      distance[nx] = distance[x] + 1
      queue.append(nx)

check = False

for i in range(len(distance)):
  if distance[i] == k:
    print(i)
    check = True

if check == False:
  print(-1)
