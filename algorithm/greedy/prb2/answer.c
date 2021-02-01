import time

n, k = map(int, input().split())
start_time = time.time()
result = 0

while n>=k : 
  while n%k != 0:
    n -= 1
    result += 1
  n //= k
  result += 1

while n>1:
  n-=1
  result += 1

print(result)
end_time = time.time()

print("process time = ",end_time - start_time)
