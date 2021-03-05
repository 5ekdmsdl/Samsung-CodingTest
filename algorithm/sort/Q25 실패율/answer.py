def solution(N, stages):
    perc = []
    total = len(stages)
    
    for i in range(1,N+1):
        count = stages.count(i)
        
        if total == 0:
            fail = 0
        else:
            fail = count/total
        perc.append((i,fail))
        total -= count

    
    perc.sort(key=lambda a:(a[1]),reverse=True)
    
    perc = [i[0] for i in perc]
                   
    return perc
