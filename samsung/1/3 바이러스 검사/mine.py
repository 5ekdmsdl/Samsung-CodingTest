n = int(input())
arr = list(map(int, input().split()))
l , t = map(int, input().split())

answer = 0
result = 0

for i, a in enumerate(arr):
    if a < 1:
        continue
    result = a - l
    if result < 0:
        answer += 1
    else :
        answer += 1
        if result % t > 0:
            answer += (result//t)+1
        else :
            answer+= (result//t)

print(answer)
