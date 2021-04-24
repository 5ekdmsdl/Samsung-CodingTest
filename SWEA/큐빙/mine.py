T = int(input())
sets = [
    [[4,[(i,2) for i in range(3)]],[3,[(2,i) for i in range(2,-1,-1)]],[5,[(i,0) for i in range(2,-1,-1)]],[2,[(0,i) for i in range(3)]]],
    [[2,[(2,i) for i in range(3)]],[5,[(i,2) for i in range(2,-1,-1)]],[3,[(0,i) for i in range(2,-1,-1)]],[4,[(i,0) for i in range(3)]]],
    [[4,[(2,i) for i in range(3)]],[0,[(2,i) for i in range(3)]],[5,[(2,i) for i in range(3)]],[1,[(0,i) for i in range(2,-1,-1)]]],
    [[4,[(0,i) for i in range(3)]],[1,[(2,i) for i in range(3)]],[5,[(0,i) for i in range(3)]], [0,[(0,i) for i in range(3)]]],
    [[3,[(i,0) for i in range(3)]],[0,[(i,0) for i in range(3)]],[2,[(i,0) for i in range(3)]],[1,[(i,0) for i in range(3)]]],
    [[1,[(i,2) for i in range(3)]],[2,[(i,2) for i in range(3)]],[0,[(i,2) for i in range(3)]],[3,[(i,2) for i in range(3)]]],
]

for t in range(1,T+1):
    ds,pls = [], []
    cube = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w'], ],
            [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y'], ],
            [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r'], ],
            [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o'], ],
            [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g'], ],
            [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b'], ]]
    n= int(input())
    line = list(input().split())
    for i in range(n):
        a,b = line[i]
        if b == '-':
            ds.append(0)
        else : ds.append(1)
        if a == 'U':
            pls.append(0)
        elif a == 'D' :
            pls.append(1)
        elif a == 'F':
            pls.append(2)
        elif a == 'B':
            pls.append(3)
        elif a == 'L':
            pls.append(4)
        else :
            pls.append(5)
    # print(pls, ds)




    for i in range(n):
        pl, d = pls[i], ds[i]
        # print(i,pl,d)
        s1,s2,s3,s4 = sets[pl]
        # print(s1,s2,s3,s4)
        for j in range(3):
            s1b, s1x, s1y = s1[0], s1[1][j][0], s1[1][j][1]
            s2b, s2x, s2y = s2[0], s2[1][j][0], s2[1][j][1]
            s3b, s3x, s3y = s3[0], s3[1][j][0], s3[1][j][1]
            s4b, s4x, s4y = s4[0], s4[1][j][0], s4[1][j][1]
            if d == 1:
                cube[s1b][s1x][s1y], cube[s2b][s2x][s2y], cube[s3b][s3x][s3y], cube[s4b][s4x][s4y] = cube[s4b][s4x][s4y], \
                                                                                                     cube[s1b][s1x][s1y], \
                                                                                                     cube[s2b][s2x][s2y], \
                                                                                                     cube[s3b][s3x][s3y]
            else :
                cube[s1b][s1x][s1y], cube[s2b][s2x][s2y], cube[s3b][s3x][s3y], cube[s4b][s4x][s4y] = cube[s2b][s2x][s2y], \
                                                                                                     cube[s3b][s3x][s3y], \
                                                                                                     cube[s4b][s4x][s4y], \
                                                                                                     cube[s1b][s1x][s1y]
        print(i)
        for c in cube[3]:
            print('   ',end='')
            for a in range(3):
                print(c[a], end='')
            print()
        # print()
        for a in range(3):
            for z in [4, 0, 5]:
                for b in range(3):
                    print(cube[z][a][b], end='')
            print()
        # print()

        for c in cube[2]:
            print('   ', end='')
            for a in range(3):
                print(c[a], end='')
            print()
        # print()
        for c in cube[1]:
            print('   ', end='')
            for a in range(3):
                print(c[a], end='')
            print()
        # print()
        print('===============')

    for c in cube[0]:
        for a in range(3):
            print('   ',c[a],end='')
        print()
