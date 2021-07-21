def get(c) :
    global total
    for x in range(n) :
        if (x,c) in gs.keys() :
            total += gs[(x,c)][0]
            gs.pop((x,c))
            break
    return

def move():
    global gs
    n_gs = {}
    for xy in gs.keys() :
        ox,oy = xy
        x,y = xy
        b,s,d = gs[xy]

        for i in range(s) :
            nx, ny = x+dx[d], y+dy[d]
            if not (0 <= nx <= n-1 and 0 <= ny <= m-1) :
                d = rev[d]
                nx, ny = x + dx[d], y + dy[d]
            x,y = nx, ny

        if (x,y) in n_gs.keys() :
            if n_gs[(x,y)][0] < b :
                n_gs[(x,y)] = [b,s,d]
        else : n_gs[(x,y)] = [b,s,d]

    gs = n_gs
    return




n,m, k = map(int, input().split())
gs = {}

for _ in range(k) :
    x,y,s,d,b = map(int, input().split())
    gs[(x-1,y-1)] = [b,s,d]

dx, dy = [0,-1,1,0,0], [0,0,0,1,-1]
rev = [0,2,1,4,3]
total = 0

if k != 0 :
    for i in range(m) :
        get(i)
        move()

print(total)
