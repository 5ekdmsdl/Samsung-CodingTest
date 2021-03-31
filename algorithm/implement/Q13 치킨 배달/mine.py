import itertools
import math

house = []
chicken = []
chick_dist = []
true_chicken = []
answer = int(1e9)

def chicken_distance(h,chicken_list):
  dist = int(1e9)
  for c in chicken_list:
    d = abs(h[0] - c[0]) + abs(h[1] - c[1])
    if d < dist:
      dist = d
      [x,y] = c
  return dist, [x,y]

n,m = map(int,input().split())

for i in range(n):
  line = list(map(int,input().split()))
  for j in range(n):
    if line[j] == 1:
      house.append((i,j))
    elif line[j] == 2:
      chicken.append((i,j))

# n,m = 5,3d
# house = [(0,2),(1,4),(2,1),(3,2)]
# chicken = [(1,2),(2,2),(4,4)]

# n,m = 5,2
# house = [(0,3),(1,0),(1,2),(3,3),(3,4),(4,3)]
# chicken = [(0,1),(3,0),(4,0),(4,1),(4,4)]

# n,m = 5,1
# house = [(0,0),(1,0),(2,0),(3,0),(4,0)]
# chicken = [(0,1),(1,1),(2,1),(3,1),(4,1)]

# n,m = 5,1
# house = [(0,0),(1,0),(2,0),(3,0),(4,0),(0,4),(1,4),(2,4),(3,4),(4,4)]
# chicken = [(0,1),(1,1),(2,1),(3,1),(4,1),(0,3),(1,3),(2,3),(3,3),(4,3)]

def chicken_distance_all(h,chicken_list):
  dist = []
  for c in chicken_list:
    d = abs(h[0] - c[0]) + abs(h[1] - c[1])
    dist.append(d)
  return dist


for h in house:
  dist, xy = chicken_distance(h, chicken)
  chick_dist.append([dist,xy])
  true_chicken.append(xy)

a = len(true_chicken)
if a <= m:
  answer = 0
  for i in chick_dist:
    answer += i[0]
  print(answer)
else:
  chick_map = []
  for h in house:
    chick_map.append(chicken_distance_all(h,true_chicken))
  
  per_idx = list(itertools.permutations(list(range(len(true_chicken))),m))
  per_idx_dist = [0]*len(per_idx)

  for a, idx in enumerate(per_idx):
    for i in range(len(house)):
      minval = int(1e9)
      for j in idx:
        minval = min(minval, chick_map[i][j])
      per_idx_dist[a] += minval
  answer = min(per_idx_dist)

  print(answer)
