n,m = map(int, input().split())
mapp = [list(map(int,input().split())) for _ in range(n)]

blocks = [[[0, 1], [0, 2], [0, 3]], # ㅡ
             [[1, 0], [2, 0], [3, 0]], # ㅣ
             [[0, 1], [1, 0], [1, 1]],
             [[1, 0], [2, 0], [2, 1]],
             [[1, 0], [2, 0], [2, -1]],
             [[0, 1], [0, 2], [1, 0]],
             [[0, 1], [0, 2], [1, 2]],
             [[0, 1], [1, 1], [2, 1]],
             [[0, 1], [1, 0], [2, 0]],
             [[0, 1], [0, 2], [-1, 2]],
             [[1, 0], [1, 1], [1, 2]],
             [[1, 0], [1, 1], [2, 1]],
             [[1, 0], [1, -1], [2, -1]],
             [[0, 1], [-1, 1], [-1, 2]],
             [[0, 1], [1, 1], [1, 2]],
             [[0, 1], [0, 2], [1, 1]],
             [[1, 0], [1, 1], [2, 0]],
             [[1, 0], [1, -1], [2, 0]],
             [[0, 1], [0, 2], [-1, 1]]]

max_val = 0
result = 0
for i in range(n):
    for j in range(m):
        for block in blocks :
            result = mapp[i][j]
            for b in range(3) :
                nx = i + block[b][0]
                ny = j + block[b][1]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 :
                    result += mapp[nx][ny]
                # if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 :
                #     break
                # result += mapp[nx][ny]

            if max_val < result :
                max_val = result

print(max_val)

# 주석 지우기
# 이미 탐색 범위 많으면 => 하드코딩으로 가자
