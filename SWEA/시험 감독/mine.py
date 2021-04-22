n = int(input())
ass = list(map(int,input().split()))
b,c = map(int,input().split())

# n = 5
# ass = [10,9,10,9,10]
# b,c = 7,2

total = 0

for a in ass :
  st = a-b
  if st < 0 :
    total += 1
  elif st%c :
    total += st//c + 2
  else :
    total += st//c+1

print(total)    
