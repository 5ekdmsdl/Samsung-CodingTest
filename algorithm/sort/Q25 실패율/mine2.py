def setting(data):
    return (data[0],-data[1])

def solution(N, stages):
    l = len(stages)
    perc = [[0,i] for i in range(N+1)]
    stages.sort()
    idx = 0
    for i in range(1,N+1):
        now = 0
        while idx < l and stages[idx] == i :
            now += 1
            idx += 1
        if l - idx + now > 0:
            perc[i][0] = now / (l - idx + now)
        else : perc[i][0] = 0
    answer = perc[1:][:]
    answer.sort(key=setting,reverse=True)
    answer2 = []
    for i in range(N):
        answer2.append(answer[i][1])
    return answer2
