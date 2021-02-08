
import time

# n, m = map(int,input().split())
# length = list(map(int,input().split()))

n=4
m=6
length = [19,15,10,17]

start_time = time.time()

def binary_search(target,start,end):
  while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for i in length:
      if i > mid:
        total += (i-mid)

    if total < target:
      end = mid - 1
    else:
      result = mid
      start = mid + 1
  return result

#log(N)*N^2

print(binary_search(m,0,max(length)))

end_time = time.time()
print(end_time - start_time)
