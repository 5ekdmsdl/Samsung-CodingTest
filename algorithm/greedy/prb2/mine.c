import time

n, k = map(int, input().split())
start_time = time.time()
cnt = 0

while(n != 1):
  if(n%k == 0):
    n = n//k
  else :
    n = n-1
  cnt = cnt + 1

print(cnt)
end_time = time.time()

print("process time = ",end_time - start_time)
