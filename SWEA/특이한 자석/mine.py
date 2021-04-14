#import sys
#sys.stdin = open("input.txt", "r")
from collections import deque 

def check(n,d):
    if d == 1:
        d = -1
    else :
        d = 1
    answer = []
    check = [[],[2], [2,6],[2,6],[6]]
    
    for i in check[n]:
        if i == 2:
            side = 6
            if data[n][i] != data[n+1][side]:
                answer.append([n+1, d])
        else : 
            side = 2
            if data[n][i] != data[n-1][side]:
                answer.append([n-1, d])

    #print(answer)
    return answer

def move_clk(line):
    #print('before mc:', line)
    line.reverse()
    line.append(line[0])
    line.reverse()
    line = line[:-1]
    #print(line)
    return line

def move_anti_clk(line):
    #print('before anti mc:', line)
    line.append(line[0])
    line = line[1:]
    #print(line)
    return line

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = [[]]
    k = int(input())
    for i in range(4):
        data.append(list(map(int,input().split())))
        
    for i in range(k):
        n,d = map(int,input().split())
        print(n,d)
        q = deque([[n, d]])
        #print(q)
        while q:
            #print(q)
            n, d = q.popleft()
            #print(n, d)
            arr = check(n, d)
            #print(arr)
            for a in arr:
                q.append(a)
            if d == 1:
                #print(n, move_clk(data[n]))
                data[n] = move_clk(data[n])
                #print(data[n])
            else:
                data[n] = move_anti_clk(data[n])
            print(q, data)
    answer = 0
    for i in range(1,n+1):
        if data[i][0] == 1:
            answer += i*2
    
    print('#'+str(test_case),answer)
    
    
