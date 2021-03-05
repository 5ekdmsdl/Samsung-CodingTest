def solution(N, stages):
    total = len(stages)
    stages.sort()
    pre = stages[0]
    perc = [[-1,i] for i in range(N)]
    cnt = 1

    for i in range(1,total):
        now = stages[i]
        if pre != now:
            perc[pre][0] = (cnt/(total))
            total -= cnt
            cnt = 1
        else : 
            cnt += 1
        pre = now
        
    perc.sort(key=lambda perc:perc[0])
    
    answer = []
    for i in range(N):
        answer.append(perc[i][1])
        
    return answer
