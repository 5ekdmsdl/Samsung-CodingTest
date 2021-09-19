from itertools import product
def setnodes():
    ns = [[0,1]]
    for i in range(1,21):
        ns.append([2*i, i+1])
    ns.append([0,99]) #21번이 끝!, 25가 가운데
    tmp = [[13,23],[16,24],[19,25]] #22 23 24
    ns += tmp
    ns.append([25,31])
    tmp = [[22,27],[24,25]] #26 27
    ns += tmp
    tmp = [[28,29],[27,30],[26,25]] # 28 29 30
    ns += tmp
    tmp = [[30,32],[35,20]] # 31 32
    ns += tmp
    ns[5] = [10,[6,22]]
    ns[10] = [20,[11,26]]
    ns[15] = [30,[16,28]]
    return ns

def startonBlue(pos, point):
    global nodes
    pos = nodes[pos][1][1] #빨간색 라인 따라 한칸 이동
    # if pos == 99 :
    #     onEnd.append(p)
    #     return [point, ps, onEnd]
    point += nodes[pos][0] #이동한 노드의 점수 획득
    return [pos, point]

def elseMove(pos, point):
    global nodes
    # 도중에 파란 노드만나면 검은 라인 따라서 한칸 이동
    if pos == 5 or pos == 10 or pos == 15:
        pos = nodes[pos][1][0]
    else:
        pos = nodes[pos][1]
    point += nodes[pos][0]
    return pos, point

# p를 step만큼 움직여서 그때 얻는  point를 return하는 함수
def run(p, step, ps, onEnd):
    global nodes
    point = 0
    pos = ps[p]
    # 파란 노드에서 이동 시작하면 한칸만 직접 이동
    if pos == 5 or pos == 10 or pos == 15:
        pos, point = startonBlue(pos, point)
        step -= 1
    # 나머지 칸 이동
    for s in range(step) :
        pos, point = elseMove(pos, point)
        if pos == 21:
            onEnd.append(p)
            _ps = [] + ps
            _onEnd = [] + onEnd
            return [point, _ps, _onEnd]
    if pos in ps :
        return False
    else :
        ps[p] = pos
        _ps = [] + ps
        _onEnd = [] + onEnd
        return [point, _ps, _onEnd]

def dfs(cnt, point, ps, onEnd,turn):
    global answer
    if cnt == 10 :
        if point > answer :
            answer = point
            return
    else :
        for i in range(4):
            if i in onEnd :
                continue
            possible = run(i,steps[cnt],ps, onEnd)
            if not possible :
                continue
            _point, _ps, _onEnd = possible
            # _ps[0] += 1
            dfs(cnt+1, _point, _ps, _onEnd,turn+[i])
    return
# def main():
#     answer = 0
#     for turn in turns:
#         ps, onEnd = [0, 0, 0, 0], []
#         total = 0
#         alldone = 1
#         for i in range(10):
#             if turn[i] in onEnd :
#                 alldone = 0
#                 break
#             total += run(turn[i], steps[i],ps, onEnd)
#         if alldone and total > answer:
#             answer = total
#     return answer

nodes = setnodes()
steps = list(map(int, input().split()))
answer = 0

dfs(0,0,[0,0,0,0],[],[])

print(answer)
