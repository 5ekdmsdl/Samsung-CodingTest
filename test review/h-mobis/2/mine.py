from itertools import combinations

def combine(a, data):
  result = [0]*m

  for i in a:
    t = data[i-1]
    for j in range(m):
      result[j] += t[j]

  if all(result):
    return True

  return False


def solution(n,m,data):
  ns = [_ for _ in range(1,n+1)]
  for i in range(1,n+1):
    cases = combinations(ns, i)
    #print(list(cases))
    for j in cases:
      result = combine(j,data)
      if result :
        return i
  return -1

n,m = 4,5
input_data = [[0,0,0,1,0],[1,0,0,0,0],[0,0,1,1,0],[0,1,1,1,0]]

a = solution(n,m,input_data)
print(a)
