n, m = map(int,input().split())

coins = []
INF = 9999
d = [INF]*(m+1)
f_found = 0

#N
for i in range(n):
  coins.append(int(input()))
  
#NlogN
coins.sort()

#M*N
for num in range(1,m+1):
  f_found = 0

  if num in coins:
    d[num] = 1
    f_found = 1
    
  else :
    for coin in coins:
      check = num - coin
      if check < 1 or check > m:
        continue
      if d[check] == -1:
        continue
      else : 
        d[num] = min(d[num],d[check] + 1)
        f_found = 1

  if f_found == 0:
    d[num] = -1
  

print(d[m])
