def setting(data):
    return (data[0],-data[1])

def solution(N, stages):
    total = len(stages)
    perc = [[0,i] for i in range(N+1)]
    answer = []
    
    for i in range(1,N+1):
        cnt = stages.count(i)
        if total > 0:
            perc[i][0] = cnt / total
        else : perc[i][0] = 0
        total -= cnt
        
    perc = perc[1:][:]
    perc.sort(key = setting, reverse = True)
    
    for i in range(N):
        answer.append(perc[i][1])
    return answer
