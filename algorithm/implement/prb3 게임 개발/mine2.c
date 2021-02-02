import time

n,m = map(int,input().split())
x,y,dir = map(int,input().split())

map_data = []

for i in range(n):
  map_data.append(list(map(int, input().split())))

start_time = time.time()
flg_back = 0
result = 1

dx = [-1,0,+1,0]
dy = [0,+1,0,-1]

def turn_left():
  global dir
  if dir == 0:
      dir=3
  else : dir = dir - 1

while(1):
  #발자국 찍기
  map_data[x][y] = 2
  
  for i in range(4):
    #방향 돌기
    turn_left()

    #갈수있나 확인
    if map_data[x + dx[dir]][y + dy[dir]] == 0:
      x = x + dx[dir]
      y = y + dy[dir]
      result += 1
      break

    if i == 3:
      print("no place to move")
      flg_back = 1

      x = x - dx[dir]
      y = y - dy[dir]
      
      if map_data[x][y] == 1:
        break

      turn_left()
  if flg_back == 1:
    break

print(map_data)
print(result)
  
end_time = time.time()

print(end_time - start_time)

