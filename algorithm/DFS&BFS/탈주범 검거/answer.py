from collections import deque

tunnel = {
  0 : (),
  1 : ((1,0),(0,1),(-1,0),(0,-1)),
  2 : ((1,0), (-1,0)),
  3 : ((0,1),(0,-1)),
  4 : ((-1,0),(0,1)),
  5 : ((1,0),(0,1)),
  6 : ((1,0),(0,-1)),
  7 : ((-1,0),(0,-1))
}

T = int(input())
for tc in range(1,T+1):
  n,m,r,c,l = map(int,input().split())
  array = [list(map(int,input().split())) for _ in range(n)]
  q = deque([r,c])
  visit = [[0]*(m) for _ in range(n)]
  visit[r][c] = 1
  cnt = 1

  while q:
    x, y = q.popleft()
    for dx, dy in tunnel[array[x][y]]:
      nx, ny = x+dx, y+dy
      if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
        continue
      if (-dx, -dy) in tunnel[array[nx][ny]]:
        if visit[nx][ny] == 0 and array[nx][ny]:
          visit[nx][ny] = visit[x][y] + 1
          q.append((nx,ny))
          if visit[nx][ny] <= l:
            cnt += 1
  print(cnt)
