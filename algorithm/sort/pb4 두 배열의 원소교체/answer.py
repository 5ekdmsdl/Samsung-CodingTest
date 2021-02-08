# n=5
# k=3

# A = [1,2,5,4,3]
# B = [5,5,6,6,5]

n, k = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

#N*logN + N
for i in range(k):
  if A[0+i] < B[0+i]:
    A[0+i], B[0+i] = B[0+i], A[0+i]
  else: break

print(sum(A))
