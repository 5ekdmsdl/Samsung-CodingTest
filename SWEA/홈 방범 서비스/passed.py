#import sys
import math

#sys.stdin = open("input.txt", "r")
def find_max(center,n,m,h_index):
    [x,y] = center
    max_val = 0
    ks ={}
    for h in h_index:
        k = abs(x-h[0]) + abs(y-h[1]) + 1
        if k in ks.keys():
            ks[k] += 1
        else :
            ks[k] = 1
    ks_n = list(ks.keys())
    ks_n.sort(reverse=True)
    acc = 0
    for k in ks_n:
        n = ks[k]
        cost = k*k+(k-1)*(k-1)
        cnt = len(h_index) - acc
        gain = (cnt)*m
        acc += n
        result = gain-cost
        if result >= 0:
            max_val = max(max_val, cnt)
            
            #print(cnt)
        #print(k,n)
    #print(ks_n)

    return max_val

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    max_val = 0
    h_index = []
    n,m = map(int,input().split())
    for i in range(n):
        line = list(map(int,input().split()))
        if 1 in line:
            for j in range(n):
                if line[j] == 1:
                    h_index.append([i,j])
    #print('h:',len(h_index))

    answer = 0
    for i in range(n):
        for j in range(n):
            answer = find_max([i,j],n,m,h_index)
            
            if answer > max_val:
                max_val = answer
                #print('max:',[i,j],max_val)
            #max_val = max(max_val, answer)
            
            
    print("#"+str(test_case),max_val)
    
        
        
        
        
        
