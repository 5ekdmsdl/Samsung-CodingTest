# n,c = map(int,input().split())
n,c = 5,3

# graph = []
# for i in range(n):
#   graph.append(int(input()))
graph = [1,2,8,4,9]

graph.sort()

maxval = 0

for i in range(1,n-1):
  dist = min(graph[i] - graph[0], graph[n-1] - graph[i])
  if maxval < dist:
    maxval = dist

print(maxval)

