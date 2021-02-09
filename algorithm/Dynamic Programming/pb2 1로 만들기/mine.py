import time

n = int(input())

start = time.time()

cnt = [0]
result = [n]
index = 0

while(1):

  current_cnt = cnt[index]
  current_result = result[index]

  if n%5 == 0:
    cnt.append(current_cnt+1)
    result.append(current_result//5)

  if n%3 == 0:
    cnt.append(current_cnt+1)
    result.append(current_result//3)
  
  if n%2 == 0:
    cnt.append(current_cnt+1)
    result.append(current_result//2)
  
  cnt.append(current_cnt+1)
  result.append(current_result-1)

  if current_result <= 1:
    print(current_cnt,current_result,end=' ')
    break

  index += 1

  # print(cnt,result, end='\n')

print(time.time() - start)
