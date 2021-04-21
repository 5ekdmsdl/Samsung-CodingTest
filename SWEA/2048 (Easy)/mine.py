from itertools import product
import copy


def move_up():
  global mapp
  check, dir = {}, 0
  
  for j in range(n):
    for i in range(n):
      #print(i,j)
      if mapp[i][j] == 0 :
        continue
      x,y = i, j
      while(1) :
        nx, ny = x + dx[dir], y + dy[dir]
        #print(nx,ny,x,y)
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 :
          if [i,j] != [x,y]:
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
          break
        elif mapp[nx][ny] == 0 :
          x,y = nx, ny
          continue
        elif mapp[nx][ny] > 0 and mapp[i][j] == mapp[nx][ny] :
          if (nx,ny) not in check :
            mapp[nx][ny] *= 2
            check[(nx, ny)] = 1
            mapp[i][j] = 0
            break
          else :
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
            break
        elif mapp[nx][ny] > 0 and mapp[i][j] != mapp[nx][ny]:
          if [x,y] != [i,j] :
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
          break

def move_down():
  global mapp
  check, dir = {}, 1
  
  for j in range(n):
    for i in range(n-1,-1,-1):
      #print(i,j)
      if mapp[i][j] == 0 :
        continue
      x,y = i, j
      while(1) :
        nx, ny = x + dx[dir], y + dy[dir]
        #print(nx,ny,x,y)
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 :
          if [i,j] != [x,y]:
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
          break
        elif mapp[nx][ny] == 0 :
          x,y = nx, ny
          continue
        elif mapp[nx][ny] > 0 and mapp[i][j] == mapp[nx][ny] :
          if (nx,ny) not in check :
            mapp[nx][ny] *= 2
            check[(nx, ny)] = 1
            mapp[i][j] = 0
            break
          else :
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
            break
        elif mapp[nx][ny] > 0 and mapp[i][j] != mapp[nx][ny]:
          if [x,y] != [i,j] :
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
          break
  
def move_left():
  global mapp
  check, dir = {}, 2
  
  for i in range(n):
    for j in range(n):
      #print(i,j)
      if mapp[i][j] == 0 :
        continue
      x,y = i, j
      while(1) :
        nx, ny = x + dx[dir], y + dy[dir]
        #print(nx,ny,x,y)
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 :
          if [i,j] != [x,y]:
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
          break
        elif mapp[nx][ny] == 0 :
          x,y = nx, ny
          continue
        elif mapp[nx][ny] > 0 and mapp[i][j] == mapp[nx][ny] :
          if (nx,ny) not in check :
            mapp[nx][ny] *= 2
            check[(nx, ny)] = 1
            mapp[i][j] = 0
            break
          else :
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
            break
        elif mapp[nx][ny] > 0 and mapp[i][j] != mapp[nx][ny]:
          if [x,y] != [i,j] :
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
          break


def move_right():
  global mapp
  check, dir = {}, 3
  
  for i in range(n):
    for j in range(n-1,-1,-1):
      #print(i,j)
      if mapp[i][j] == 0 :
        continue
      x,y = i, j
      while(1) :
        nx, ny = x + dx[dir], y + dy[dir]
        #print(nx,ny,x,y)
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 :
          if [i,j] != [x,y]:
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
          break
        elif mapp[nx][ny] == 0 :
          x,y = nx, ny
          continue
        elif mapp[nx][ny] > 0 and mapp[i][j] == mapp[nx][ny] :
          if (nx,ny) not in check :
            mapp[nx][ny] *= 2
            check[(nx, ny)] = 1
            mapp[i][j] = 0
            break
          else :
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
            break
        elif mapp[nx][ny] > 0 and mapp[i][j] != mapp[nx][ny]:
          if [x,y] != [i,j] :
            mapp[x][y] = mapp[i][j]
            mapp[i][j] = 0
          break
  

n = int(input())

o_mapp = []
for i in range(n):
    o_mapp.append(list(map(int,input().split())))

max_val = 0
dx, dy = [-1,1,0,0],[0,0,-1,1]
ns = [_ for _ in range(0,4)]
every_case = product(ns ,repeat = 5)
#every_case = [[0,1,2,3,3]]
mapp = []

for case in every_case :
  mapp = copy.deepcopy(o_mapp)
  for d in case :
    if d == 0 :
      move_up()
    elif d == 1:
      move_down()
    elif d == 2:
      move_left()
    elif d == 3:
      move_right()
    #if case == (2,3,3,2,2) :
    #  print(d, mapp)

  for m in mapp :
    if max(m) > max_val :
      #print(case, mapp)
      max_val = max(m)

print(max_val)
