def check_crct(v):
    if v == "": return v
    stack=[]
    for idx, i in enumerate(v):
        if i==")":
            if not stack or stack.pop() != "(":
                return False
        else: stack.append(i)
    return True
    

def make_crct(p):   # 균형잡힌 괄호 문자열
    answer=[]
    #1
    if not p : return list(p)
    #2
    l, r = 0, 0
    for idx, i in enumerate(list(p)):
        if i=="(":
            l += 1
        elif i==")":
            r += 1
        
        if l==r:
            u = list(p)[:idx+1]
            v = list(p)[idx+1:] if idx != len(p)-1 else []
            if check_crct(u):   # u가 올바르다면
                new_v = make_crct(v)
                return u+new_v
            else:   # u가 올바르지 않다면
                new_u = ["("]
                new_v = make_crct(v)
                new_u.extend(new_v)
                new_u.append(")")
                return new_u+list(["(" if i==")" else ")" for i in u[1:-1] ])

def solution(p):
    answer = ''
    answer = ''.join(make_crct(p))
    return answer
  
#######################################################
def check(p): # stack 대신 개수로 check 가능
    l = 0
    for i in p:
        if i == '(':
            l += 1
        else:
            l -= 1
            if l < 0:
                return False
    return l == 0

def seperate(p):
    l = r = 0
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1
        if l > 0 and l == r:
            return p[:i+1], p[i+1:]

def solution(p):
    if p == '':
        return p
    u, v = seperate(p)
    if check(u):
        return u + solution(v)
    return f"({solution(v)}){''.join([i == ')' and '(' or ')' for i in u[1:-1]])}"

    
'''
https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
'''
