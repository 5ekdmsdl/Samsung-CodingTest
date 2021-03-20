INF = int(1e9)

s1 = input()
s2 = input()

printval = 0

for i in range(len(s2)):
    if i >= len(s1):
      printval += 1
      s1 = s1[:i] + s2[i] + s1[i:]
      continue
    
    if s2[i] == s1[i]:
        continue

    insert = 1
    
    if s2[i] in s1:
      for j in range(i,len(s1)):
        if s1[j] == s2[i]:
          remove = j - i
          break
    else : remove = INF
    
    if s1[i] in s2:
        replace = INF
    else : 
      replace = 1

    res = min(remove, insert, replace)
    printval += res

    if res == replace:
        s1 = s1[:i] + s2[i] + s1[i+1:]

    elif res == insert:
        s1 = s1[:i] + s2[i] + s1[i:]
    else:
        s1 = s1[:i] + s1[bisect.bisect_left(s1,s2[i]):]

print(printval)
