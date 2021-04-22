blocks = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

mapp = []
n,m = map(int, input().split())
for _ in range(n):
    mapp.append(list(map(int, input().split())))

max_val = 0

for i in range(n):
    for j in range(m):
        for idx in range(19) :
            result = 0
            for b in range(4) :
                # nx = i + blocks[idx][b][0]
                # ny = j + blocks[idx][b][1]
                # if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 :
                #     break
                # result += mapp[nx][ny]
                try :
                    nx = i + blocks[idx][b][0]
                    ny = j + blocks[idx][b][1]
                    result += mapp[nx][ny]
                except IndexError :
                    continue
            max_val = max(max_val, result)

print(max_val)


