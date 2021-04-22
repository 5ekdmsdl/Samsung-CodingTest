from itertools import product

dx, dy = [-1,1,0,0],[0,0,-1,1]
def move(r,b,d):
  rx, ry = r
  bx, by = b
  cnt, rflg, bflg = 1, False, False

  while(1):
    nrx, nry = rx + dx[d]*cnt, ry + dy[d]*cnt
    nbx, nby = bx + dx[d]*cnt, by + dy[d]*cnt
    
    
    
    if [nrx, nry] == hole or [nbx, nby] == hole :
      return [nrx, nry], [nbx, nby]
    
    print([rx, ry],[bx, by],d,[nrx, nry], [nbx, nby],rflg,bflg)
    
    if not rflg and mapp[nrx][nry] == '#':
      rflg = True
      arx, ary = rx, ry
    if not bflg and mapp[nbx][nby] == '#':
      bflg = True
      abx, aby = bx, by
    if rflg and bflg :
      return [arx, ary], [abx, aby]
      
    cnt += 1
  


#n,m = map(int, input().split())
n,m =5,5
mapp = []
r,b,hole = 0,0,0
# for i in range(n):
#   line = list(input())
#   mapp.append(line)
#   for j in range(m):
#     if line[j] == 'R' :
#       r = [i,j]
#     elif line[j] == 'B':
#       b = [i,j]
#     elif line[j] == 'O':
#       hole = [i,j]
mapp = [['#','#','#','#','#',],['#','.','.','B''#',],['#','.','#','.','#',],['#','R','O','.','#',]]
r,b,hole = [3,1],[1,3],[3,2]
nums = [0,1,2,3]
dp = []
flg = False
failed = {}


for t in range(1,2):
  cases = product(nums, repeat = t)
  for case in cases :
    for d in case :
      r,b = move(r,b,d)

      if r == hole or b == hole :
        if b == hole :
          failed[c] = 1
          continue
        elif r == hole :
          print(len(case))
          flg = True
          break
    if flg :
      break




  



