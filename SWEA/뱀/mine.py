# n = int(input())
# k = int(input())
# apples = []
# dirs = []

# for i in range(k):
#   apples.append(list(map(int,input().split())))

# l = int(input())
# for _ in range(l):
#   a,b = input().split()
#   dirs.append([int(a),b])

n,k = 10,4
apples = [[1,2],[1,3],[1,4],[1,5]]
l = 4
dirs = [[8,'D'],[10,'D'],[11,'D'],[13,'L'],[10000,'X']]

nt, flg = 0, False
head, body, d = [1,1], [], 0
dx, dy = [0,1,0,-1], [1,0,-1,0]

for tttime, dl in dirs:
  ttime = tttime - nt

  for t in range(ttime):
    nt += 1
    new_head = [head[0]+dx[d], head[1]+dy[d]]
    #print(nt, new_head,head,body)
    print('time:',nt)
    for i in range(1,n+1):
      for j in range(1,n+1):
        if [i,j] == new_head :
          print('n',end='')
        elif [i,j] == head :
          print('h',end='')
        elif [i,j] in apples :
          print('a',end='')
        elif [i,j] in body :
          print('b',end='')
        else : print('.',end='')

      print()
    
    if (new_head[0]<1 or new_head[0]>n or new_head[1]<1 or new_head[1]>n) or new_head in body :
      print(nt)
      flg = True
      break
    if new_head in apples:
      body.append(head)
      head = new_head
      apples.remove(new_head)
      continue
    else :
      if len(body) > 0:
        body.remove(body[0])
        body.append(head)
        head = new_head
        continue
      else :
        head = new_head

  if flg :
    break
  
  if dl == 'D':
    d += 1
    if d > 3:
      d = 0
  elif dl == 'L' :
    d -= 1
    if d < 0 :
      d = 3    
  else :
    break

