from itertools import product

def run(p, step):
    global ps, nodes
    point = 0
    pos = ps[p]
    if pos == 5 or pos == 10 or pos == 15 :
        pos = nodes[pos][1][1]
        if pos == 99 :
            return point
        point += nodes[pos][0]
        print(nodes[pos][0])
        step -= 1
    for s in range(step) :

        if pos == 5 or pos == 10 or pos == 15 :
            pos = nodes[pos][1][0]
        else:
            pos = nodes[pos][1]
        if pos == 99 :
            return point
        point += nodes[pos][0]
        print(nodes[pos][0])

    ps[p] = pos
    return point

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


ps = [0,0,0,0]
nodes = setnodes()
turns = list(product(list(range(1,5)),repeat=10))
answer = 0
steps = list(map(int, input().split()))
onEnd = []

for turn in turns :
    total = 0
    for i in range(10):
        total += run(turn[i], steps[i])
    if total > answer :
        answer = total

# idx =
# for i in range(9):
#     n = nodes[idx]
#     print(n[0])
#     idx = n[1]
