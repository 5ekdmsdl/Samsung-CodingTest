import copy

def draw(xy, dir):
    global mapp
    x,y = xy
    for d in dir :
        cnt = 0
        while(1):
            nx, ny = x+dx[d]*cnt, y+dy[d]*cnt
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 :
                break
            elif mapp[nx][ny] == 6 :
                break
            else :
                mapp[nx][ny] = -1
                cnt += 1

def erase(xy, dir):
    global mapp
    x,y = xy
    for d in dir :
        cnt = 0
        while(1):
            nx, ny = x+dx[d]*cnt, y+dy[d]*cnt
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 :
                break
            elif mapp[nx][ny] == 6 :
                break
            else :
                mapp[nx][ny] = 0
                cnt += 1

dx, dy = [-1,1,0,0], [0,0,-1,1]
dirs = [[[-1]],
        [[0],[1],[2],[3]],
        [[2,3],[0,1]],
        [[0,2],[0,3],[1,2],[1,3]],
        [[1,2,3],[0,2,3],[0,1,3],[0,1,2]],
        [[0,1,2,3]]]

n,m = map(int, input().split())

cxys, cns = [[] for _ in range(8)], [0 for _ in range(8)]
mapp2 = []

cnt = 0
for i in range(n):
    line = list(map(int,input().split()))
    mapp2.append(line)
    for j in range(m):
        if 1 <= line[j] <= 5 :
            cxys[cnt] = [i,j]
            cns[cnt] = line[j]
            cnt += 1
print(cxys, cns)

min_val = int(1e9)
for c0 in dirs[cns[0]]:
    if c0 != [-1] :
        draw(cxys[0],c0)
    # for i in range(len(mapp)):
    #     print(mapp[i])
    # print('=============')

    for c1 in dirs[cns[1]]:
        if c1 != [-1] :
            draw(cxys[1], c1)
        # for i in range(len(mapp)):
        #     print(mapp[i])
        # print('=============')

        for c2 in dirs[cns[2]]:
            if c2 != [-1]:
                draw(cxys[2], c2)
            # for i in range(len(mapp)):
            #     print(mapp[i])
            # print('=============')

            for c3 in dirs[cns[3]]:
                if c3 != [-1]:
                    draw(cxys[3], c3)
                # for i in range(len(mapp)):
                #     print(mapp[i])
                # print('=============')

                for c4 in dirs[cns[4]]:
                    if c4 != [-1]:
                        draw(cxys[4], c4)
                    # for i in range(len(mapp)):
                    #     print(mapp[i])
                    # print('=============')

                    for c5 in dirs[cns[5]]:
                        if c5 != [-1]:
                            draw(cxys[5], c5)
                        # for i in range(len(mapp)):
                        #     print(mapp[i])
                        # print('=============')

                        for c6 in dirs[cns[6]]:
                            if c6 != [-1]:
                                draw(cxys[6], c6)
                            # for i in range(len(mapp)):
                            #     print(mapp[i])
                            # print('=============')

                            for c7 in dirs[cns[7]]:
                                if c7 != [-1]:
                                    draw(cxys[7], c7)

                                res = 0

                                print(c0,c1,c2,c3,c4,c5,c6,c7)
                                for i in range(len(mapp)):
                                    print(mapp[i])
                                    res += mapp[i].count(0)
                                print('r',res)
                                mapp = copy.deepcopy(mapp2)
                                # print
                                print('=============')
                                if res < min_val :
                                    min_val = res
    #                             if c7 != [-1]:
    #                                 erase(cxys[7], c7)
    #                         if c6 != [-1]:
    #                             erase(cxys[6], c6)
    #                     if c5 != [-1]:
    #                         erase(cxys[5], c5)
    #                 if c4 != [-1]:
    #                     erase(cxys[4], c4)
    #             if c3 != [-1]:
    #                 erase(cxys[3], c3)
    #
    #         if c2 != [-1]:
    #             erase(cxys[2], c2)
    #
    #     if c1 != [-1]:
    #         erase(cxys[1],c1)
    #
    # if c0 != [-1]:
    #     erase(cxys[0],c0)

# for i in range(len(mapp)):
#     print(mapp[i])
print('=============')
print(min_val)
