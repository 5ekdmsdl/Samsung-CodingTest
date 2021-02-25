n = int(input())
# n = 12
# data = []

# for _ in range(n):
#   line = input().split()
#   data.append([line[0],int(line[1]),int(line[2]),int(line[3])])

data = [['Junk', 50, 60, 100], ['Sangk', 80, 60, 50], ['Suny', 80, 70, 90],
        ['Soo', 80, 70, 100],['Haeb',50,60,100],['Kangs',60,80,100],['Dongh',80,60,100],['Sei',70,70,70],['Wons',70,70,90],['Sangh',70,70,80],['nsj',80,80,80],['Tae',50,60,90]]

data.sort(key=lambda data: data[1], reverse=True)

cnt = 0
for i in range(n - 1):
    if data[i][1] == data[i + 1][1]:
      cnt += 1
    else:
      if cnt >= 1:
        data[i-cnt:i+1].sort(key=lambda data: data[2])
        print(data[i-cnt:i+1])
        cnt = 0
      else:
        pass



    #     if data[i][3] == data[i + 1][3]:
    #         data[i:i + 1].sort(key=lambda data: data[0])
    #     else:
    #         data[i:i + 1].sort(key=lambda data: data[3],reverse=True)
    # else:
    #     data[i:i + 1].sort(key=lambda data: data[2])

print('\n\n')
print(data)
