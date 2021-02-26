# n = int(input())
n=5
# graph = []

# for i in range(n):
#   graph.append(list(map(int,input().split())))
graph = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]

for i in range(n-1,0,-1):
  for j in range(i):
    up = graph[i-1][j]
    down1 = graph[i][j]
    down2 = graph[i][j+1]
    graph[i-1][j] = max(up + down1, up + down2)
    # print(i,j,up,down1,down2,graph[i-1][j],end='\n')

print(graph[0][0])

