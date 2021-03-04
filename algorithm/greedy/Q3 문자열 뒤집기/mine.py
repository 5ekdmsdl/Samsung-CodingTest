# s = list(map(int,input()))
s = [0,0,0,1,1,0,0,1]
pre = s[0]
cnt0 = 0
cnt1 = 0

for i in range(1,len(s)):
  now = s[i]
  if now != pre:
    if pre == 0:
      cnt0 += 1
    else :
      cnt1 += 1
  pre = s[i]

if pre == 0:
  cnt0 += 1
else :
  cnt1 += 1

print(min(cnt0,cnt1))
