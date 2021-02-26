import bisect

# n, x = map(int,input().split())
n,x = 9,5
# data = list(map(int,input().split()))
data = [1,1,2,2,2,2,3,4,4,100]

left = bisect.bisect_left(data,x)
right = bisect.bisect(data,x)
cnt = (right-left)

if cnt == 0:
  print('-1')
else :
  print(cnt)
