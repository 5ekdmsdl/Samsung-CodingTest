from collections import deque

def  bfs(i,j):
  global data
  global cnt_array
  global n
  global m

  queue = deque([i-1])
  queue.append(j-1)
  queue.append(0)

  dx = [-1,0,+1,0]
  dy = [0,-1,0,+1]

  cnt_array = [0]

  while queue:
    founded = 0
    print(queue)

    x = queue.popleft()
    y = queue.popleft()
    cnt = queue.popleft()

    print(x,y,cnt,'\n')

    cnt_array[cnt] += 1

    data[x][y] = 0

    if x == n-1 and y == m-1:
      return cnt_array[cnt]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx>n-1 or ny<0 or ny>m-1:
        continue
      else:
        if data[nx][ny] == 1:
          founded += 1
          queue.append(nx)
          queue.append(ny)
          if founded > 1:
            queue.append(cnt+founded-1)
            cnt_array.append(cnt_array[cnt])
          else : queue.append(cnt)


n, m = map(int, input().split())

for i in range(n):
  data.append(list(map(int,input())))

# n=5
# m=6
# data = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]

cnt_array = []

print('\n\n',bfs(1,1))

