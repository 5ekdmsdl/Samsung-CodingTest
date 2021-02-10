n = int(input())

d = [[] for i in range(n+1)]

d[0] = ['b']
d[1] = ['a','bb','c']

for x in range(n):
  #N
  for i in d[x-2]:

    for j in d[x-1]:

      str1 = i+j
      str2 = j+i
      if str1 == str2:
        d[x].append(str1)
      else :
        d[x].append(str1)
        d[x].append(str2)
  d[x-2] = []
  
  print(d)


print(len(d[n-1])%796796)
