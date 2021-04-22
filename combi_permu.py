data = [_ for _ in range(4)]

def comb(array, r): #조합
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in comb(array[i+1:], r-1):
                yield [array[i]] + next

def combwithsame(array, r): #중복 조합
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else :
            for next in comb(array[i:], r-1):
                yield [array[i]] + next

def permu(array, r): #순열
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else :
            for next in permu(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next

def permuwithsame(array, r): #중복 순열
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else :
            for next in permuwithsame(array, r-1):
                yield [array[i]] + next


a = permuwithsame(data,2)
print(list(a))
