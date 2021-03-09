# n = int(input())
n=10
# graph = [[] for _ in range(n+1)]
t = [-1] * (n+1)
p = [-1] * (n+1)
db = [-1] * (n+1)
maxval = -1

# for i in range(1,n+1):
#   t,p = map(int,input().split())
#   graph[i].append((t,p))

graph = [[],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10]]

for i in range(1,n+1):
  end = i+graph[i][0]-1
  price = graph[i][1]
  if end < n+1:
    t[i] = end
    p[i] = price
  else:
    p[i] = 0

for i in range(n,0,-1):
  if t[i] == [-1]:
    db[i] = (0)
  else:
    if t[i]+1 <= n:
      plus = db[t[i]+1]
    else:
      plus = 0
    db[i] = (p[i] + plus)
    if maxval < db[i]:
      maxval = db[i]

print(maxval)
