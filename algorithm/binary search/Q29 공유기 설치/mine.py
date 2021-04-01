n, c = map(int,input().split())
array = []

for _ in range(n):
  a = int(input())
  array.append(a)
array.sort()

start = 0
end = array[-1] - array[0]
answer = 0

while start <= end:
  mid = (start + end)//2
  val = array[0]
  cnt = 1

  for i in range(1,n):
    if array[i] >= val + mid:
      cnt += 1
      val = array[i]

  if cnt >= c:
    answer = max(answer, mid)
    start = mid+1
  elif cnt < c:
    end = mid-1

print(answer)
