def solution(s):
    answer = True
    s = list(s)
    stack = []
    for bracket in s:
        if bracket=="(":
            stack.append(bracket)
        else:   # bracket ==")"
            if not stack:
                return False
            elif stack[-1] == "(":
                del stack[-1]
            else:   #stack[-1] == ")"
                stack.append[bracket]

    if stack:
        answer = False    
    
    return answer

def other_solution(s):
    open_cnt = 0
    for c in s:
        if c == '(':
            open_cnt += 1
        elif c == ')':
            open_cnt -= 1
            if open_cnt < 0:
                return False
                
    return open_cnt == 0

print(solution("(()())()")
print(solution("(()("))
'''
https://programmers.co.kr/learn/courses/30/lessons/12909
'''
