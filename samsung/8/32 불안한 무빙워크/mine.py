def rotate():
    global rail, people
    rail = [rail[-1]] + rail[0:len(rail)-1]
    people = [people[n - 1]] + people[0:n-1]
    # if people[n-1] :
    #     people[n-1] = 0
    return

def move():
    if people[n-1] :
        people[n-1] = 0
    for i in range(n-2, -1, -1):
        if people[i]:
            if people[i+1] or rail[i+1] == 0:
                continue
            else :
                people[i+1] = people[i]
                people[i] = 0
                rail[i+1] -= 1
    return

def addperson():
    # global num
    if people[0] == 0 and rail[0] != 0  :
        people[0] = 1
        # num += 1
        rail[0] -= 1
    if people[n-1] :
        people[n-1] = 0
    return

def checkK():
    if rail.count(0) >= k :
        return False
    return True

num = 0
n,k = map(int, input().split())
rail = list(map(int, input().split()))
people = [0 for _ in range(n)]

while(checkK()):
    num += 1
    rotate()
    move()
    addperson()

print(num)
