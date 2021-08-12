#myself
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

#---------------------------------
#with other solution - Using zip()
def solution1(a, b):
    return sum([x*y for x, y in zip(a, b)])

def solution2(a, b):
    answer = 0
    for x, y in zip(a,b):
        answer += x*y
    return answer

  
  
'''
1. 리스트의 i번째 요소끼리 계산 할 땐 => zip() !!!!

https://programmers.co.kr/learn/courses/30/lessons/70128
'''
