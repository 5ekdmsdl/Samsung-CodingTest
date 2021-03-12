def solution(p):
    #1
    if p == '':
        return ''
    #2
    answer = again(p)
    return answer

def again(p):
    if p == '':
        return ''
    u,v = split(p)
    if right(u) == True:
        return ifright(u,v)
    else:
        return ifnotright(u,v)
    
def split(p):
    if p == '':
        return '' , ''
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        elif p[i] == ')':
            cnt -= 1
        if cnt == 0:
            u,v = p[:i+1], p[i+1:]
            return u , v

def ifright(u,v):
    res = u + again(v)
    return res

def ifnotright(u,v):
    string = '('
    a,b = again(v)
    string = string + a + b 
    string += ')'
    u = u[1:len(u)-1]
    new_u = []
    for i in range(len(u)):
        if u[i] == '(':
            new_u.append(')')
        else:
            new_u.append('(')
    string += (u)
    return string


def right(p):
    cnt = 0
    for i in range(len(p)//2):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True
