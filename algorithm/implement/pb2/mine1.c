import time

input_data = input()

start_time = time.time()
row = int(input_data[1])
col = int(ord(input_data[0])-ord('a'))+1

# col = 1
# row = 1

result = 0

two = [-2,2]
one = [-1,1]

for i in range(2):
  m_col = col + two[i]
  for j in range(2):
    if m_col < 1 or m_col > 8:
      continue
    m_row = row + one[j]
    if m_row < 1 or m_row >8:
      continue
    else : 
      result += 1

for i in range(2):
  m_row = row + two[i]
  for j in range(2):
    m_col = col + one[j]
    if m_col < 1 or m_col > 8 or m_row < 1 or m_row >8:
      continue
    else : result += 1

print(result)

end_time = time.time()
print(end_time - start_time)
