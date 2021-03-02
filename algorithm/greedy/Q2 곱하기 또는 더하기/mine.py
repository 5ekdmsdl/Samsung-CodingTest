nums = list(map(int,input()))
result = 0

for num in nums:
  if num == 0 or result == 0:
    result += num
  else:
    result = num*result
  print(num,result,end='\n')

print(result)
