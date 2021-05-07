def solution(s):
    s= list(s)
    stack=[]
    for i in s:
        if len(stack)==0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        print(i, stack)
    
    answer = 1 if len(stack) == 0 else 0
    return answer

print(solution('cdcd'))
print(solution('baabaa'))

'''
https://programmers.co.kr/learn/courses/30/lessons/12973
'''
