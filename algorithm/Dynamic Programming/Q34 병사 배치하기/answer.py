n = int(input())
data = list(map(int,input().split()))
data.reverse()

db = [0]*(n)
db[0] = 1

for i in range(1,n):
  for j in range(i-1,-1,-1):
    if data[j] < data[i]:
      db[i] = max(db[i],db[j]+1)

print(n-db[-1])
