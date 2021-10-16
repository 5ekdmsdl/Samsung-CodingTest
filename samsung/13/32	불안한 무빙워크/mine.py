def Input():
    n,k = map(int, input().split())
    Rs = list(map(int, input().split()))
    return n,k , Rs

def working():
    global Rs
    if Rs.count(0) >= k : return False
    return True

def rotate():
    global Rs, Ps
    Rs = [Rs[-1]] + Rs[0:-1]
    Ps = [0] + Ps[0:-1]
    removeP()
    return

def move():
    for i in range(n-1, -1, -1):
        if Ps[i] :
            if Ps[i+1] or Rs[i+1] <= 0 : continue
            Ps[i] = 0
            Ps[i+1] = 1
            PonR(i+1)
    return

def addP():
    if Ps[0] == 0 and Rs[0] != 0 :
        PonR(0)
        Ps[0] = 1
    return

def removeP():
    Ps[n-1] = 0

def PonR(i):
    Rs[i] -= 1
    return

n,k,Rs = Input()
Ps = [0 for _ in range(n)]
N = 2*n
cnt = 0

while(working()):
    cnt += 1
    rotate()
    move()
    addP()
    removeP()

print(cnt)
