#O(M)
#가장 간결한 방법

n = int(input())
array = set(map(int,input().split()))

m = int(input())
requested = list(map(int,input().split()))

for i in requested:
  if i in array:
    print("yes",end = ' ')
  else:
    print("no",end = ' ')
