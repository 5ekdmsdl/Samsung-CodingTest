def plus(a,b) :
    return a+b
def minus(a,b) :
    return a-b
def multiply(a,b) : return a*b

calculate = [plus, minus, multiply]

def func(result, abc, cnt):

    global max_val, min_val
    if cnt > n-1 :
        if result > max_val :
            max_val = result
        if result < min_val : min_val = result
        return
    for i in range(3) :
        if abc[i] :
            abc[i] -= 1
            #다음 연산을 위해 초기값을 변형하면 안되지!!!
            # print(calculate[i](result, nums[cnt]), abc, cnt)
            func(calculate[i](result, nums[cnt]), abc, cnt+1)
            abc[i] += 1


n = int(input())
nums = list(map(int, input().split()))
abc = list(map(int, input().split()))

min_val, max_val = int(1e9), -int(1e9)

func(nums[0], abc, 1)

print(min_val, max_val)
