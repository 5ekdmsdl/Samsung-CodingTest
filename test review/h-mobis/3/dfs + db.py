def func(i, costs,graph):
  global db

  if db[i] != 0:
    return db[i]

  if len(graph[i]) == 0: #원자재인 경우
    sup = costs[i-1]
    hum = 0
  else: #부품인 경우
    sup = 0
    hum = costs[i-1]

  for a in graph[i]: #dfs로 graph로 뒤에 연결되어 있는 부품/원자재 값 계산
    [n_sup, n_hum] = func(a[0], costs,graph)
    sup += (n_sup)*a[1]
    hum += (n_hum)*a[1]

  return [sup, hum]


def solution(n,costs,edges):

  answer = [0,0]
  
  graph = [[] for _ in range(n+1)]

  for e in edges: #그래프 형성
    [a,b,c] = e
    graph[b].append([a,c])
  
  for i in range(1,n+1):
    result = func(i, costs,graph)
    db[i] = result
    #print(db)
    answer = max(result, answer)

  return answer

n = 8
costs = [1,2,3,4,5,6,7,8]
edges = [[2,4,2],[3,4,1],[2,5,1],[3,5,2],[6,7,1],[1,7,3],[4,7,1],[5,7,2],[7,8,2]]

db = [0]*(n+1) #노드 반복 방지
a = solution(n,costs,edges)
print(a)
