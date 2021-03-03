# n,m = map(int,input().split())
n,m = 3,3
# graph = []

# for i in range(n):
#   data = list(map(int,input().split()))
#   graph.append(data)

# graph = [[2,0,0,0,1,1,0],[0,0,1,0,1,2,0],[0,1,1,0,1,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,1,1],[0,1,0,0,0,0,0],[0,1,0,0,0,0,0]]

graph = [[0,0,2],[0,0,0],[0,0,0]]

visited = [[False]*m for _ in range(n)]

dist = 0
minval = int(1e9)
dx = [1,0,0,-1]
dy = [0,1,-1,0]

def test(p1,p2,p3):
  res = 1
  graph[p1[0]][p1[1]] = 1
  graph[p2[0]][p2[1]] = 1
  graph[p3[0]][p3[1]] = 1
  visited[p1[0]][p1[1]] = True
  visited[p2[0]][p2[1]] = True
  visited[p3[0]][p3[1]] = True

  flg = False

  while 1:
    for i in range(n):
      for j in range(m):
        if visited[i][j] == False:
          flg = True

    if flg == False:
      break

    for q in range(n):
      for w in range(m):
        if graph[q][w] == 2 and visited[q][w] == False:
          visited[q][w] = True
          for e in range(4):
            if i+dx[e] < 0 or i+dx[e] > n-1 or j+dy[e] < 0 or j+dy[e] > m-1:
              continue
            if(graph[i+dx[e]][j+dy[e]] == 0):
              graph[i+dx[e]][j+dy[e]] = 2
              res += 1
    print(graph)
  # print(p1,p2,p3,res,end='\n')
  # print(graph,end='\n')
  
  return res

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      visited[i][j] = True
# print(visited)

for i in range(n):
  for j in range(m):
    # print(i,j,end='\t')
    for a in range(n):
      for b in range(m):
        # print(a,b,end='\t')
        for s in range(n):
          for t in range(m):
            # print(s,t,end='\n')
            # print(i,j,a,b,s,t,end='\n')
            minval = min(minval,test((i,j),(a,b),(s,t)))
            # print(visited)
            visited = [[False]*m for _ in range(n)]
            

print(minval)
      
            
