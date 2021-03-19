import heapq
import bisect

n = int(input())

graph = [1]
q = []
heapq.heappush(q,1)

while 1:
  num = heapq.heappop(q)

  index = bisect.bisect_left(graph,num)
  if index == n-1:
    print(graph[index])
    break

  add = [num*2,num*3,num*5]

  for a in add:
    if a not in graph:
      graph.append(a)
      heapq.heappush(q,a)
  graph.sort()
    

