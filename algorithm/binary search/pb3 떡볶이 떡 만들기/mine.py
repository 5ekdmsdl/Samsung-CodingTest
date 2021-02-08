# n, m = map(int,input().split())
# length = list(map(int,input().split()))

import time

n=1000000
m=100
length = [19,15,9,17]*250000

start_time = time.time()

def left_len(length, H):
  left = [0]*n
  for i in range(n):
    if length[i] > H:
      left[i] = length[i] - H
    else : left[i] = 0
  return sum(left)

def binary_search(target,start,end):
  while start <= end:
    mid = (start + end) // 2
    result = left_len(length,mid)

    if result == target:
      return mid
    elif result < target:
      end = mid - 1
    else: start = mid + 1

  if target > result :
    return mid - 1
  else: return mid

#log(N)*N^2

print(binary_search(m,0,max(length)))

end_time = time.time()
print(end_time - start_time)
