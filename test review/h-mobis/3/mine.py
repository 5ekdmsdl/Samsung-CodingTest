def func(i, costs,graph):
  if len(graph[i]) == 0:
    sup = costs[i-1]
    hum = 0
  else:
    sup = 0
    hum = costs[i-1]

  for a in graph[i]:
    [n_sup, n_hum] = func(a[0], costs,graph)
    sup += (n_sup)*a[1]
    hum += (n_hum)*a[1]

  return [sup, hum]


def solution(n,costs,edges):
  answer = [0,0]
  db = [0]*(n+1)
  graph = [[] for _ in range(n+1)]

  for e in edges:
    [a,b,c] = e
    graph[b].append([a,c])
  
  for i in range(1,n+1):
    result = func(i, costs,graph)
    print(result)
    answer = max(result, answer)

  return answer

n = 8
costs = [1,2,3,4,5,6,7,8]
edges = [[2,4,2],[3,4,1],[2,5,1],[3,5,2],[6,7,1],[1,7,3],[4,7,1],[5,7,2],[7,8,2]]

a = solution(n,costs,edges)
print(a)
