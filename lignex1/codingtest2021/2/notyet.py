import sys

def InputData():
	readl = sys.stdin.readline
	N, M, C, D = map(int, readl().split())
	T = list(map(int, readl().split()))

	return N, M, C, D, T

ans = 0

# 입력 받는 부분
# N: CPU 수
# M: 테스크 수
# C: 연속작업 수
# D: 준비시간
# T: 태스크 수행사이클
N, M, C, D, T = InputData()
# 총시간, 갯수
cs = [[0,0] for _ in range(N)]
for i in range(N):
	cs[i] = [T[i],1]
# print(cs)

for task in T[N:]:
	# print(task)
	mc, mi = int(1e9),-1
	for i, c in enumerate(cs):
		rest = 0
		cycle, cnt = c
		if cnt % C == 0:
			rest += D
		if cycle + task + rest < mc :
			mc = cycle + task + rest
			mi = i
		elif cycle + task + rest == mc :
			
	cs[mi][1] += 1
	cs[mi][0] += task + rest
# 	print(task+rest, mi, cs)
# print(cs)

lcycle = 0
for c in cs :
	if c[0] > lcycle :
		lcycle = c[0]
print(lcycle)
