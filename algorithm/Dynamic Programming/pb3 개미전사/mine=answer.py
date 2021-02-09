n = int(input())
foods = list(map(int,input().split()))
result = [0]*n

result[0] = foods[0]
result[1] = max(foods[0],foods[1]) 

for i in range(2,n):
  result[i] = max(result[i-1],result[i-2]+foods[i])
  print(result)

print(result[n-1])
