def delete(data,frame):
    [a, x, y] = data
    frame[a].remove([x,y,a])
    return frame

def add(data,frame):
    [a, x, y] = data
    frame[a].append([x,y,a])
    return frame

def check(xya, frame):
    [x,y,a] = xya
    if [x,y,a] in frame[a] and IsCorrect_Add(frame, [a,x,y]) == False:
        return False
    return True

def IsCorrect_Delete(frame,axy):
    [a,x,y] = axy
    
    if a == 0:
        if check([x,y+1,0],frame) == False:
            return False
        elif check([x,y+1,1],frame) == False:
            return False
        elif check([x-1,y+1,1],frame) == False:
            return False
    elif a == 1:
        if check([x,y,0],frame) == False:
            return False
        elif check([x+1,y,0],frame) == False:
            return False
        elif check([x-1,y,1],frame) == False:
            return False
        elif check([x+1,y,1],frame) == False:
            return False
    return True


def IsCorrect_Add(frame,axy):
    [a,x,y] = axy
    
    if a == 0:
        if y == 0:
            return True
        elif [x,y,1] in frame[1] or [x-1,y,1] in frame[1]:
            return True
        elif [x,y-1,0] in frame[0]:
            return True
    elif a == 1:
        if [x,y-1,0] in frame[0] or [x+1,y-1,0] in frame[0]:
            return True
        elif [x-1,y,1] in frame[1] and [x+1,y,1] in frame[1]:
            return True
    return False
    

def solution(n, build_frame):
    frame = [[],[]]
    
    for i in range(len(build_frame)):
        [x,y,a,b] = build_frame[i]
        if b == 0:
            new_frame = delete([a,x,y],frame)
            if IsCorrect_Delete(new_frame,[a,x,y]):
                frame = new_frame
        elif b == 1:
            new_frame = add([a,x,y],frame)
            if IsCorrect_Add(new_frame,[a,x,y]):
                frame = new_frame
            
    frame = frame[0] + frame[1]
    frame.sort(key = lambda frame: (frame[0],frame[1],frame[2]))
    return frame





#     for i in frame[0]:
#         x,y = i[0], i[1]
#         if y == 0:
#             continue
#         elif [x,y,1] in frame[1]:
#             continue
#         elif [x,y-1,0] in frame[0]:
#             continue
#         else : 
#             return False
    
#     for i in frame[1]:
#         x,y = i[0], i[1]
#         if [x,y-1,0] in frame[0] or [x+1,y-1,0] in frame[0]:
#             continue
#         elif [x-1,y,1] in frame[1] and [x+1,y,1] in frame[1]:
#             continue
#         else : return False
        
#     return True
