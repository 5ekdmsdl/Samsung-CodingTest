from itertools import permutations

n = int(input())
num = list(map(int,input().split()))
line = list(map(int,input().split()))

# n = 2
# num = [5,6]
# line = [0,0,1,0]

# n = 6
# num = [1,2,3,4,5,6]
# line = [2,1,1,1]

cal = []
for i in range(4):
  cal = cal + [i]*line[i]

INF = int(1e9)
minval = INF
maxval = -INF

def func(num, cal):
  answer = num[0]
  for i in range(1,len(num)):
    next = num[i]
    n_cal = cal[i-1]
    if n_cal == 0:
      answer += next
    elif n_cal == 1:
      answer -= next
    elif n_cal == 2:
      answer *= next
    elif n_cal == 3:
      # answer = answer // next
      if answer >= 0:
        answer = answer // next
      else:
        answer = -((-answer)//next)
  return answer

per_cal = permutations(cal,n-1)

for p in per_cal:
  result = func(num,p)
  maxval = max(maxval, result)
  minval = min(minval, result)

print(maxval)
print(minval)
