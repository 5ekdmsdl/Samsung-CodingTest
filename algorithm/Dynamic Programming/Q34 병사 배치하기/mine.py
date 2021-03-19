n = int(input())
data = list(map(int,input().split()))
db = [0]*(n)

for i in range(1,n):
  pre = data[i-1]
  now = data[i]

  if pre < now :
    db[i] = db[i-1] + 1
  else:
    db[i] = db[i-1]
  
print(db[-1])
