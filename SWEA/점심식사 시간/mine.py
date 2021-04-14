import math

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    on_board = {}
    on_stair = []
    people = []
    stair = []
    n = int(input())
    s_len = []
    
    for i in range(n):
        line = list(map(int,input().split()))
        for j in range(n):
            if line[j] == 1:
                people.append([i,j])
            elif line[j] > 1:
                stair.append([[i,j], line[j]])
                s_len.append(line[j])
    #print(people, stair)
	
    for i, p in enumerate(people):
        x,y = p
        dist = []
        for s in stair:
            sx, sy = s[0]
            dist.append(abs(x-sx) + abs(y-sy))
        on_board[i+1] = dist
    print(on_board)
    while 1:
        for i in on_board.keys():
            for e, j in enumerate(on_board[i]):
                if j  > 0:
                    on_board[i][e] -= 1
                else :
                    on_stair.append([i, s_len[e]])
        print(on_board)
        break
