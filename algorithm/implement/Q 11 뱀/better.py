n = int(input())  #보드 크기
k = int(input())  #사과 갯수
apple = []
for i in range(k):
  x, y = map(int, input().split())
  apple.append((x,y))

# n,k = 10,4
# apple = [(1,2),(1,3),(1,4),(1,5)]
# n,k = 10,5
# apple = [(1,5),(1,3),(1,2),(1,6),(1,7)]

dir = []
l = int(input())
for i in range(l):
  line = input()
  idx = line.find(' ')
  t = int(line[:idx])
  d = line[idx+1:]
  dir.append((t,d))
# l = 4
# dir = [(8,'D'),(10,'D'),(11,'D'),(13,'L')]
########################################################
body = [(1,1)]
answer = 0
cnt = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

direction = 0
xt = 0

def head_move(direction):
  global body
  hx = body[0][0] + dx[direction]
  hy = body[0][1] + dy[direction]
  body = [(hx,hy)] + body[:]

def Isapple():
  head = body[0]
  return head in apple

def apple_T():
  apple.remove(body[0])

def apple_F():
  global body
  body = body[:len(body)-1]

def Isgameover():
  head = body[0]
  hx = head[0]
  hy = head[1]
  if head in body[1:]:
    # print('head bumped body')
    return True
  if hx < 1 or hx > n or hy < 1 or hy > n:
    # print('head out of board')
    return True
  return False

def move(t,direction):
  global cnt
  for i in range(t):
    # print('cnt:',cnt)
    head_move(direction)
    # print(body)

    if Isapple():
      apple_T()
    else : apple_F()

    cnt += 1

    if Isgameover():
      return 'gameover'

def update_dir(direction, d):
  if d == 'L':
    direction -= 1
    if direction < 0:
      direction = 4
  else : 
    direction += 1
    if direction > 3:
      direction = 0
  return direction

for i, d in enumerate(dir):

  t = d[0] - xt
  rt = move(t,direction)
  direction = update_dir(direction, d[1])

  if rt == 'gameover':
    answer += cnt
    # print(rt,answer)
    break
  else : 
    answer += t
    cnt = 0
  
  xt = d[0]

  # print('chage dir:',rt,answer)

if rt != 'gameover':
  rt = move(int(1e9),direction)
  if rt == 'gameover':
    answer += cnt

print(answer)
