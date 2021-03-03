# n = int(input())
n = 7
# a = list(map(int,input().split()))
a = [-15,-4,2,8,9,13,15]
# a = [-15,-4,3,8,9,13,15]

res = -1
start = 0
end = n-1

while start < end:
  mid = (start+end)//2

  if mid == a[mid]:
    res = a[mid]
    break
  elif start == a[start]:
    res = a[start]
    break
  elif end == a[end]:
    res = a[end]
    break

  if mid < a[mid]:
    end = mid-1
  else:
    start = mid+1

print(res)
