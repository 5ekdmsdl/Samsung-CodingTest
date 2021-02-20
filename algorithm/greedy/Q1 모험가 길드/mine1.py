#원래 푼방식
#그 뒤에 고침 (6분초과)

import time

# n = int(input())
n = 5*20000

# data = list(map(int,input().split()))
data = [2,3,1,2,2]*20000

start_time = time.time()

flag = False
team_cnt = 0
index = 0
data.sort(reverse=True)

# while index < n:
#   val = data[index]
#   index += val
#   if index > n:
#     break
#   else:
#     team_cnt += 1


# print(data)

def find_max():
  max_val=-1
  max_index=-1
  for i in range(n):
    if max_val < data[i]:
      max_val = data[i]
      max_index = i
  return max_val, max_index

while 1:
  val, index = find_max()
  if val == -1:
    break

  data[index] = -1

  for i in range(val-1):
    val2, index2 = find_max()

    if val == -1:
      flag = True
      break

    data[index2] = -1

  if flag:
    break
  else:
    team_cnt += 1

print(team_cnt)
print(time.time()-start_time)
