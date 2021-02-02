input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])-ord('a'))+1

result = 0
steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2),]

for step in steps:
  n_row = row+step[0]
  n_col = col+step[1]

  if n_row<1 or n_row>8 or n_col<1 or n_col>8 :
    continue
  else: result += 1

print(result)
