def solution(s):
    answer = 0
    minval = int(1e9)
    
    for num in range(1,len(s)+1): #분리 단위
        total = ''
        cnt = 1
        pre = s[0:num]

        for i in range(1,len(s)//num): #
            now = s[num*i:num*(i+1)]
            if pre == now:
                cnt += 1
            else:
                if cnt == 1:
                    total += pre
                else:
                    total += str(cnt)+pre
                cnt = 1
            pre = now
            
        if num*(len(s)//num) < len(s):
            total += s[num*(len(s)//num):]
        if cnt == 1:
            total += pre
        else:
            total += str(cnt)+pre
        minval = min(minval,len(total))
        
    answer = minval
    return answer
