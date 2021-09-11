import sys

def input_data() :
	readl = sys.stdin.readline
	N = int(readl())#협찬 물품의 수
	D = list(map(int, readl().split()))#선호도 
	return N, D


def Solve():
	sol = -30001#첫번째 방법의 최대 선호도
	for i in range(0,N-2) :
		t = sum(D[i:i+3])
		if(t > sol) : sol = t
	return sol

def Solve2():
	dp = [0 for _ in range(N)]
	dp[0] = D[0]
	for i in range(1,len(D)) :
		if dp[i-1] + D[i] < D[i]:
			dp[i] = D[i]
		else :
			dp[i] = dp[i-1] + D[i]
	return max(dp)

#입력받는 부분
N, D = input_data()
answer = Solve2()
# answer = 0
# N = 100000
# for i in range(1,N+1):
# 	answer += i
print(answer)#출력하는 부분

# total = 0
# for i in range(1,100001):
# 	total += 1/i
# print(total)	

