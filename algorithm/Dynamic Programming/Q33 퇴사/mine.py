# n = int(input())
n=10
# graph = [[] for _ in range(n+1)]
db = [[] for _ in range(n+1)]
total = [[] for _ in range(n+1)]
maxval = -1

# for i in range(1,n+1):
#   t,p = map(int,input().split())
#   graph[i].append((t,p))

graph = [[],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10]]

for i in range(1,n+1):
  start = i
  end = i+graph[i][0]-1
  price = graph[i][1]
  if end < n+1:
    db[i] = [(start,end),price]
  else:
    db[i] = ['-1']

for i in range(n,0,-1):
  if db[i] == ['-1']:
    total[i] = 0
  else:
    start = db[i][0][0]
    end = db[i][0][1]
    price = db[i][1]
    if end+1 < n+1:
      plus = total[end+1]
    else  : plus = 0
    total[i] = price + plus
    if maxval < total[i]:
      maxval = total[i]

print(maxval)
