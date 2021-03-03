# n = int(input())
n=4
# house = list(map(int,input().split()))
house = [5,1,7,9]
house.sort()

dist = [0]*(n)
# total = sum(house)
minval = int(1e9)
mini = -1

for i in range(n):
  total1 = sum(house[:i])
  total2 = sum(house[i+1:])
  dist[i] = abs(total1 - (house[i]*i)) + abs(total2 - (house[i]*(n-i-1)))
  if dist[i] < minval:
    minval = dist[i]
    mini = i
  print(minval,mini,end ='\n')

print(house[mini])
