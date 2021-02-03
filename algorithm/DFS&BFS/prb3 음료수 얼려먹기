def dfs(graph,i,j,visited):

  dx = [-1,0,0,+1]
  dy = [0,-1,+1,0]

  visited[i][j] = True
  # print(i,j,end  = '\n')

  for a in range(4):
    ni = i + dx[a]
    nj = j + dy[a]
    if ni < 0 or ni > n-1 or nj < 0 or nj > m-1:
      continue
    else :
      if graph[ni][nj] == 0:
        if not visited[ni][nj]:
          dfs(graph,ni,nj,visited)


n,m = map(int,input().split())

array = []

for i in range(n):
  array.append(list(map(int,input())))

visited = [[False]*m for _ in range(n)]

result = 0

for row in range(len(array)):
  for col in range(len(array[0])):
    if array[row][col] == 0:
      if visited[row][col] == True:
        continue
      else : 
        dfs(array,row,col,visited)
        result += 1
        # print(visited,end = '\n')

print(result)
