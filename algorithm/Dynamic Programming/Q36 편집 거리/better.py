s1 = input()
s2 = input()

n = len(s1)
m = len(s2)

db = [[0]*(n+1) for _ in range(m+1)]

for j in range(m+1):
  db[j][0] = j
for i in range(n+1):
  db[0][i] = i

for i in range(1,m+1): #s2
  for j in range(1,n+1): #s1 
    if s1[j-1] == s2[i-1]:
      db[i][j] = db[i-1][j-1]
    else:
      db[i][j] = min(db[i-1][j-1]+1, db[i-1][j]+1, db[i][j-1]+1)

print(db[m][n])
