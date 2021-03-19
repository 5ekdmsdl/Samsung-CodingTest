import heapq

n = int(input())
q = []

for i in range(n):
  a = int(input())
  heapq.heappush(q,a)

res = 0

while len(q) > 1 :
  one = heapq.heappop(q)
  two = heapq.heappop(q)
  sum = one + two
  res += sum
  heapq.heappush(q,sum)

print(res)
