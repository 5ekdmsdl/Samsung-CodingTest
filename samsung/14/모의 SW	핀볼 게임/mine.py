def Input():
    n,m,k = map(int, input().split())
    xys = {}
    for i in range(n):
        l = list(map(int, input().split()))

        for j in range(m):
            if l[j] :
                xys[(i,j)] = [l[j],0]
    return n,m,k,xys

def Produce(x,y,X):
    global dead, xys, baby

    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if (nx,ny) in dead or (nx,ny) in xys.keys():
            continue
        if (nx,ny) in baby.keys():
            baby[(nx,ny)].append([X,0])
        else :
            baby[(nx, ny)] = [[X,0]]
    return

def Dead(x,y):
    global n_dead
    n_dead.add((x,y))
    return

def Grow():
    global xys

    for (x,y), [X,l] in xys.items() :
        if l == X :
            Produce(x,y,X)

        l += 1

        if l == 2*X :
            Dead(x,y)
            continue
        else :
            xys[(x,y)] = [X,l]

    return

def Babys():
    for (x,y), B in baby.items():
        if len(B) >= 2 :
            B.sort(key = lambda a : -a[1])
            B = [B[0]]
        xys[(x,y)] = B[0]
    return

def Deads():
    global dead, n_dead
    for (x,y) in n_dead :
        xys.pop((x,y))
    dead.update(list(n_dead))
    return

dx, dy = [0,0,-1,1], [-1,1,0,0]
T = int(input())

for tt in range(T):
    n,m,k,xys = Input()
    dead = set()

    for t in range(k):
        baby = {}
        n_dead = set()

        Grow()
        Babys()
        if n_dead :
            Deads()

    print('#'+str(tt+1)+' '+str(len(list(xys.keys()))))
