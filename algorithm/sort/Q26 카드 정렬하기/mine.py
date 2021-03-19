n = int(input())
graph = []

for i in range(n):
  graph.append(int(input()))

graph.sort()

if len(graph) == 1:
  res = 0
else:
  res = graph[0] + graph[1]

  for i in range(2,n):
    res += (res + graph[i])

print(res)
