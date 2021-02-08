n, k = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

#N*logN + N
for i in range(k):
    A[0+i], B[0+i] = B[0+i], A[0+i]

print(sum(A))
