# n = int(input())
n = 5*20000

# data = list(map(int,input().split()))
data = [2,3,1,2,2]*20000

team_cnt = 0
index = 0
data.sort(reverse=True)

while index < n:
  val = data[index]
  index += val
  team_cnt += 1

if index > n:
   team_cnt -= 1
    
print(team_cnt)
