#myself
import math

def solution(n):
    sqt = math.sqrt(n)
    if n % sqt == 0:
        return (sqt+1)**2
    else:
        return -1

#https://programmers.co.kr/learn/courses/30/lessons/12934
#----------------------------------------------------------
#with other solution - Not Importing math
def solution1(n):
    sqrt = n ** (0.5)   # **(0.5): float, **(1/2): 1, 1/2: 0
    print(n **(0.5), n **(1/2), 1/2)
    if sqrt%1 == 0: #정수인지 아닌 지 판별. 소수는 1로 나누면 소수점이 나온다.
        return (sqrt+1)**2
    return -1
