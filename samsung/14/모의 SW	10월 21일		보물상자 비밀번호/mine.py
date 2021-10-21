def rotate():
    global l

    l = l[-1] + l[:-1]

    return

HtoD = {
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
'F' : 15,
}

def Todeci(a):
    num = 0

    for i in range(len(a)-1,-1,-1):
        b = a[i]

        try : b = int(b)
        except :
            b = HtoD[b]

        num += b * 16**(len(a)-1-i)

    return num

def Slice():
    global Ns

    tmp = []
    tmp.append(l[:n//4])
    tmp.append(l[n//4:2*n // 4])
    tmp.append(l[2*n // 4:3 * n // 4])
    tmp.append(l[3*n // 4:4 * n // 4])

    for N in tmp :
        Ns[Todeci(N)] = 1

    return

T = int(input())

for t in range(T):
    n,k = map(int, input().split())
    nl = n // 4
    l = input()
    Ns = {}

    Slice()
    for i in range(nl-1) :
        rotate()
        Slice()

    Ns = list(Ns.keys())
    Ns.sort(reverse = True)

    print('#'+str(t+1)+' '+str(Ns[k-1]))
