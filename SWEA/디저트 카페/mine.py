# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

#import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

T = int(input())
'''
def get_right(now, l):
    [x,y] = now
    ret = []
    for i in range(l):
        if x < 0 or x > n-1 or y < 0 or y > n-1:
            return -1
    return 1
    '''
def get_right(now, l):
    [x,y] = [now[0]+1, now[1]+1]
    ret = []
    for i in range(l-1):
        if x<0 or x > n-1 or y < 0 or y > n-1:
            return -1
        ret.append(array[x][y])
        x += 1
        y += 1
    return ret

def get_left(now, l):
    [x,y] = [now[0]+1, now[1]-1]
    ret = []
    for i in range(l-1):
        if x<0 or x > n-1 or y < 0 or y > n-1:
            return -1
        ret.append(array[x][y])
        x += 1
        y -= 1
    return ret

def func(start, a, b):
    desserts = [array[start[0]][start[1]]]
    r1 = get_right(start, b)
    l1 = get_left(start, a)
    if r1 == -1 or l1 == -1:
        return -1
    desserts += r1+l1
    left, right = [start[0]+a-1, start[1]-a+1], [start[0]+b-1, start[1]+b-1]
    #print(array[start[0]][start[1]], a,b, left, right)
    r2 = get_right(left, b)
    l2 = get_left(right, a)
    if r2 == -1 or l2 == -1:
        return -1
    desserts += r2+l2[:-1]
    
    #print(desserts)
    for d in desserts:
        if desserts.count(d) > 1:
            #print(d)
            return -1
    return len(desserts)

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    array = []
    n = int(input())
    max_val = -1  
    for i in range(n):
        line = list(map(int,input().split()))
        array.append(line)
    for i in range(n):
        for j in range(n):
            start = [i,j]
            for a in range(n-1, 1, -1):
                for b in range(n-1, 1, -1):
                    if a == n-1 and b == n-1:
                        continue
                    res = func(start, a, b)
                    #print(res)
                    max_val = max(max_val, res)
    #print(array)
    print("#"+str(test_case),max_val)
    # ///////////////////////////////////////////////////////////////////////////////////
