import time

n = int(input())
start_time = time.time()
array = []

while n > 0:
  array.append(n%10)
  n = n//10

a = len(array)

if sum(array[:a//2]) == sum(array[a//2:]):
  print("LUCKY")
else:
  print("READY")
print(time.time()-start_time)
