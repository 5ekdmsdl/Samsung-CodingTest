
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,x = map(int, input().split())
    passed_line = 0
    rows = []
    cols = [[] for _ in range(n)]
    for _ in range(n):
        row = list(map(int,input().split()))
        rows.append(row)
        for j in range(n):
            cols[j].append(row[j])
    lines = rows+cols
    for l in lines:
        pre, cnt, data, flg = l[0], 1, [], True
        for i in range(1,n):
            now = l[i]
            if pre == now:
                cnt += 1
            else :
                data.append([pre,cnt])
                cnt = 1
            pre = now
        data.append([pre, cnt])
        
        
        if len(data) == 1:
            flg = True
        else : 
            for now in range(1, len(data)):
                pre = now - 1
                if abs(data[pre][0] - data[now][0]) == 1:
                    if data[pre][0] < data[now][0]:
                        if data[pre][1] >= x :
                            data[pre][1] -= x
                            continue
                        else:
                            flg = False
                            break
                    else : 
                        if data[now][1] >= x :
                            data[now][1] -= x
                            continue
                        else:
                            flg = False
                            break   
                else  : flg = False
        if flg :
            #print(l)
            passed_line += 1
         
                         
        
    print('#{} {}'.format(test_case, passed_line))

        

    
    
    
