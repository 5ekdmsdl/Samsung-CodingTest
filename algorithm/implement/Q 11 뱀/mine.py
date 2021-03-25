# n = int(input())  #보드 크기
# k = int(input())  #사과 갯수
n,k = 6,3
# apple = []

# for i in range(k):
#   x, y = map(int, input().split())
#   apple.append((x,y))
apple = [(3,4),(2,5),(5,3)]
#######
# dir = []
# l = int(input())

# for i in range(l):
#   line = input()
#   idx = line.find(' ')
#   t = int(line[:idx])
#   d = line[idx+1:]
#   dir.append((t,d))
l = 3
dir = [(3,'D'),(15,'L'),(17,'D')]


  
############################
answer = 0
x = 1
y = 1
head = [1,1]
body = 1
body_list = []
d_list = ['right','down','left','up'] #시계방향
direction = 0 #right
############################
def move(xy,t,dir):
  x, y = xy[0], xy[1]
  if d_list[dir] == 'right':
    dest_x = x + t
    dest_y = y
  elif d_list[dir] == 'down':
    dest_y = y - t
    dest_x = x
  elif d_list[dir] == 'left':
    dest_x = x - t
    dest_y = y
  elif d_list[dir] == 'up':
    dest_y = y + t
    dest_x = x

  if gameover([dest_x, dest_y]):
    return (-1, -1)

  if Isapple((x,y),(dest_x, dest_y)):
    f_apple()
  return (x,y)
############################
def Isapple(xy,dxy):
  x, y = xy[0], xy[1]
  dx, dy = dxy[0], dxy[1]
  mx = dx - x
  my = dy - y

  if mx != 0:
    for i in range(min(mx,x),max(mx,x)):
      if (i,y) in apple:
        return True
  elif my != 0:
    for i in range(min(dy,y),max(dy,y)):
      if (x,i) in apple:
        return True

def f_apple():
  global body
  body += 1

def gameover(xy):
  x, y = xy[0], xy[1]
  if x < 1 or x > n or y < 1 or y > n:
    return True
  if (x,y) in body_list :
    return True
  return False
############################
def changedir(direction, n_d):
  if n_d == 'L':
    direction -= 1
    if direction < 0:
      direction = 3
  else : 
    direction += 1
    if direction > 3:
      direction = 0
  return direction
############################
for i in range(l):
  x, y = head[0], head[1] #머리
  time = dir[i][0] #움직일 시간
  (x,y) = move((x,y),time,direction)
  if x == -1 or y == -1:
    break
  answer += time
  direction = changedir(direction, dir[i][1])

print(answer)
