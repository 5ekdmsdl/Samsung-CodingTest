#O( (N+M)*logN )

def search_item(array,target,start,end):
  while start <= end:
    mid = (start+end)//2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    elif array[mid] < target:
      start = mid + 1
  return None
#logN


n = int(input())
items = list(map(int,input().split()))
items.sort()
#NlogN


m = int(input())
requested = list(map(int,input().split()))

for item in requested:
  #M*logN
  result = search_item(items,item,0,n)
  if result == None:
    print("no",end=' ')
  else : print("yes",end=' ')
