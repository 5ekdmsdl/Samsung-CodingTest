#O(N+M)

n = int(input())
array = [0] * 1000001

for i in input.split():
  array[int(i)] = 1
#N

m = int(input())
requested = list(map(int,input().split()))

#M
for i in requested:
  if array[i] == 1:
    print("yes",end = ' ')
  else:
    print("no",end = ' ')
