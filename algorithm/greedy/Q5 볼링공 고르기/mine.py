# n,m = map(int,input().split())
n,m = 8,5
w = [[] for _ in range(m+1)] #무게

# balls = list(map(int, input().split()))
balls = [1,5,4,3,2,4,5,2]

for i in range(n):
  idx = i
  weight = balls[i]
  w[weight].append(idx+1)
# 1
# 3 5
# 2 4
answer = 0
for i in range(1,m+1):
  for j in range(i+1,m+1):
    answer += len(w[i])*len(w[j])

print(answer)

#시간복잡도 : n+m^2




