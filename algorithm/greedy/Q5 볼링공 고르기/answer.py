# n,m = map(int,input().split())
n,m = 8,5
w = [0]* (m+1) #무게

# balls = list(map(int, input().split()))
balls = [1,5,4,3,2,4,5,2]

for i in range(n):
  idx = i
  weight = balls[i]
  w[weight] += 1

answer = 0
for i in range(1,m+1):
  n -= w[i]
  answer += w[i]*n

print(answer)

#시간복잡도 : n+m
