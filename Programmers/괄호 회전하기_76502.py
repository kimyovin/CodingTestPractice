def check(v):
    stack = []
    for i in v:
        # print(stack, i)
        if i == "]":
            if not stack or stack.pop() != "[":
                return False
        elif i == ")":
            if not stack or stack.pop() != "(":
                return False
        elif i == "}":
            if not stack or stack.pop() != "{":
                return False
        else: stack.append(i)
    return not stack

def solution(s):
    answer = 0
    l= len(s)
    for i in range(l):
        a=list(s[i:])+list(s[:i])
        if check(a):
            answer += 1
    
    return answer

'''
https://programmers.co.kr/learn/courses/30/lessons/76502
'''
