import bisect

# n = int(input())
n = 5
# data_in = list(map(int,input().split()))
data_in = [3,2,1,1,9]
data_in.sort()
num = 1
print(data_in)

while 1:
  data = data_in
  print(data_in,data)
  res = num
  flg = False
  while 1:
    a = bisect.bisect_left(data, num)
    b = data[a]
    data[a] = 0
    data.sort()

    if b < res:
      res = res - b
    elif b == res:
      flg = True
      break
    elif b == 0:
      flg = False
      break
    else :
      flg = False
      break
  
  if flg == False:
    # print(data_in)
    # print(data)
    print(num)
    break
  else:
    num += 1
