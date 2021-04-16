def move(location, style):
    if style == 0:
        return location
    elif style == 1:
        location[0] -= 1
        return location
    elif style == 2:
        location[1] += 1
        return location
    elif style == 3:
        location[0] += 1
        return location
    elif style == 4:
        location[1] -= 1
        return location
 
 
def score(location):
    score = [0] * A
    for tt in range(A):
        if abs(location[0] - AP[tt][1]+1) + abs(location[1] - AP[tt][0]+1) <= AP[tt][2]:
            score[tt] = AP[tt][3]
    return score
 
 
def cal(score1, score2):
    result = 0
    if A ==1:
        return max(score1[0], score2[0])
    for i in range(A):
        for j in range(A):
            if i == j:
                pass
            else:
                if score1[i] + score2[j] > result:
                    result = score1[i] + score2[j]
    return result
 
 
T = int(input())
for _ in range(T):
    M, A = map(int, input().split())
    move1 = list(map(int, input().split()))
    move2 = list(map(int, input().split()))
    AP = []
    for t in range(A):
        AP.append(list(map(int, input().split())))
    user1 = [0,0]
    user2 = [9,9]
    result = 0
    result += cal(score(user1),score(user2))
 
    for __ in range(M):
        user1 = move(user1, move1[__])
        user2 = move(user2, move2[__])
        result += cal(score(user1), score(user2))
    print("#%d %d" % (_ + 1, result))
