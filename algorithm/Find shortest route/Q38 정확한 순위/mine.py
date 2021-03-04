import heapq

# n,m = map(int,input().split())
n,m = 5,5
graph = [[] for _ in range(n+1)]

# for _ in range(m):
#   a,b = map(int,input().split())
#   graph[a].append(b)

# graph=[[],[5],[],[4],[2,6],[2,4],[]]
graph = [[],[2],[],[1,2],[3],[1]]

start = 1
q = []
heapq.heappush(q,start)
cnt = 0
res = 0

while q:
  flg = 0
  now = heapq.heappop(q)
  cnt += 1
  if len(graph[now]) + cnt == n:
    res += 1
  for next in graph[now]:
    flg = 1
    heapq.heappush(q,next)
  if flg == 0:
    cnt -= 1
    # heapq.heappush(q,now+1)
  print(now,cnt,flg,res,end='\n')
    

print(res)
