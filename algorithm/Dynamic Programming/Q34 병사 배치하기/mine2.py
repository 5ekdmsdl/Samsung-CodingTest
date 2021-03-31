n = int(input())
arr = list(map(int,input().split()))
db = [0]*(n)
db[0] = 1

for i in range(1,n):
    for j in range(0,i):
        if arr[j] > arr[i]:
            db[i] = max(db[i], db[j]+1)
    if db[i] == 0:
        db[i] += 1

print(n-max(db))
            
