n = int(input())
data = []

for i in range(n):
  data.append(input().split())

data = sorted(data,key=lambda data:data[1])

for person in data:
  print(person[0],end=' ')
  
