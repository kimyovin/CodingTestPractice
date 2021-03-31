#myself
def solution(a, b):
    p = -1 if a>b else 1
    answer = sum(i for i in range(a, b+p, p))
    return answer

#----------------------------------------------------------------
#####with other solution1 - Good

def solution1(a, b):
    answer = (abs(a-b)+1)*(a+b)//2  #O(1). 시간 복잡도가 더 개선됨!
    return answer

#####with other solution1
def solution2(a, b):
    return sum(range(min(a,b),max(a,b)+1))


'''
1. for i in range(10, 5): 실행 안됨. 역순으로는 step 값이 -1이 되어야 한다. (default value: 1)
    =>> in range(10, 5, -1)   

https://programmers.co.kr/learn/courses/30/lessons/12912
'''
