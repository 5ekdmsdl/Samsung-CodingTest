import sys
from collections import deque

def InputData():
	global Hs
	H = []
	readl = sys.stdin.readline
	N = int(readl())
	for r in range(N) :
		l = list(map(int,readl().split()))
		for ll in l:
			Hs[ll] = None
		H.append(l)
	return N, H

def aHill(x,y,h):
	global done
	dx, dy = [0,0,-1,1], [-1,1,0,0]
	visited = {}
	q = deque([[x,y]])
	done[x][y] = 1
	while q :
		x,y = q.popleft()
		if (x,y) in visited: continue
		visited[(x,y)] = 1
		for i in range(4):
			nx, ny = x+dx[i], y+dy[i]
			if 0<=nx<=N-1 and 0<=ny<=N-1 :
				if H[nx][ny] > h :
					# print(nx, ny)
					q.append([nx, ny])
					done[nx][ny] = 1
	
	return

def countHills(n,h):
	rtv = 0
	for x in range(n):
		for y in range(n):
			if done[x][y] : continue
			if H[x][y] > h :
				aHill(x,y,h)
				rtv += 1
	return rtv


ans = -1
Hs = {
	1 : None,
	100000 : None
}
# 입력 함수
N, H = InputData()
# print(N,H)
# hs = sorted(Hs.keys())
for i in list(Hs.keys()): #운무 높이
	done = [[0]*N for _ in range(N)]
	rtv = countHills(N,i)
	if rtv > ans :
		ans = rtv
# 출력
print(ans)
