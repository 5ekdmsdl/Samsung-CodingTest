import bisect

# n = int(input())
n = 5

# coin = list(map(int,input().split()))
coin = [3,2,1,1,9]
coin.sort()

num = 1
flg = False

while 1:
  c = coin
  res = num
  
  while 1:
    index = bisect.bisect_left(c,num)
    val = c[index]
    c[index] = 0
    c.sort()
    
    if val < res:
      res -= val
    elif val == res:
      num += 1
      break
    elif val < 1:
      flg = True
      break
  
  if flg == True:
    print(num)
    break

