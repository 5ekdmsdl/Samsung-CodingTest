import heapq
INF = int(1e9)

# n, k = map(int,input().split())
n,k = 3,3
# graph = [[] for _ in range(n)]

# for i in range(n):
#   graph[i].append(list(map(int,input().split())))
graph = [[1,0,2],[0,0,0],[3,0,0]]
# s,x,y = map(int,input().split())
s,x,y = 2,2,2

def findshortest(start):
  q = []
  # visited = [False]*(n+1)
  heapq.heappush(q,start)
  distance = [[INF]*(n) for _ in range(n)]
  distance[start[0]][start[1]] = 0
  dx = [-1,0,0,1]
  dy = [0,1,-1,0]
  res = []
  
  while q:
    print(q,res)
    now = heapq.heappop(q)
    for i in range(4):
      nx = now[0] + dx[i]
      ny = now[1] + dy[i]
      if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
        continue
      
      if distance[now[0]][now[1]]+1 < distance[nx][ny]:
        if graph[nx][ny] != 0:
          res.append((graph[nx][ny],distance[now[0]][now[1]]+1))

        heapq.heappush(q,(nx,ny))
        distance[nx][ny] = distance[now[0]][now[1]]+1
  print(res)
  return res

data = findshortest((x-1,y-1))
data.sort(key=lambda data:(data[1],data[0]))

if data[0][1] > s:
  print('0')
else:
  print(data[0][0])


