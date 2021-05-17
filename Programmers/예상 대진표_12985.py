import math
def solution(n,a,b):
    answer = 0

    while 1 :
        if math.ceil(a/2) == math.ceil(b/2):
            return 1 + answer
          
        if a > n//2 and b > n//2:
            a = math.ceil((a - n//2)/2)
            b = math.ceil((b - n//2)/2)
            n = n//2
        elif a <= n//2 and b <= n//2:
            a = math.ceil(a/2)
            b = math.ceil(b/2)
            n = n//2 
        else:
            return int(math.log2(n))
        answer += 1
        print(n, a, b, answer)
    
    return answer

##################################
#with other solution
def solution1(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer

print(solution(8, 7, 8))
'''
https://programmers.co.kr/learn/courses/30/lessons/12985
'''
