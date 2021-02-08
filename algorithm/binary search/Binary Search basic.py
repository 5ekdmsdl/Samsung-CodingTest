def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = start + end // 2
  if mid == target : 
    return mid
  elif array[mid] > target:
    return binary_search(array,target,start,mid-1)
  else :
    return binary_search(array,target,mid+1,end)

n, target = map(int,input().split())

array = list(map(int,input().split()))

result = binary_search(array, target, 0, len(array))

if result == None:
  print("Can not find it")
else:
  print(result+1)
