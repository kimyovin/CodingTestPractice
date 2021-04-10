### 
# 정수 num이 짝수일 경우 "Even"을 반환하고 
# 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
###
def solution(num):
    return "Even" if num%2 == 0 else "Odd"

print(solution(4))

#-------------------------------
#with other solution - Using bit

def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]

'''
1. 비트 연산으로 홀/짝수를 알 수 있음.
    num&1 => 0: Even (첫번째 비트가 0)
             1: Odd  (첫번째 비트가 1)
https://programmers.co.kr/learn/courses/30/lessons/12937
'''
