import time

n,m = map(int,input().split())
x,y,dir = map(int,input().split())

map_data = []

for i in range(n):
  map_data.append(list(map(int, input().split())))

start_time = time.time()
flg_back = 0
result = 1

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
    if dir == 0:
        if map_data[x-1][y] == 0:
          x = x-1
          result += 1
          break
    elif dir == 1:
        if map_data[x][y+1] == 0:
            y=y+1
            result += 1
            break
    elif dir == 2:
      if map_data[x+1][y] == 0:
          x = x+1
          result += 1
          break
    elif dir == 3:
      if map_data[x][y-1] == 0:
          y=y-1
          result += 1
          break
    
    if i == 3:
      flg_back = 1
      turn_left()

  if flg_back == 1:
    print("no place to move")

    if dir == 0:
      x = x+1
    elif dir == 1:
      y = y-1
    elif dir ==2:
      x=x-1
    elif dir ==3:
      y=y+1
    flg_back = 0
    
    if map_data[x][y] == 1:
      print(map_data)
      print(result)
      break

end_time = time.time()

print(end_time - start_time)


