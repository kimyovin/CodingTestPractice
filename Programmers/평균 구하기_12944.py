#myself
def solution(arr):
    return sum(arr)/len(arr) if len(arr) != 0 else 0

  
#---------------------------------
#with other solution - Using reduce()

from functools import reduce
def average(list):
    return reduce(lambda x, y : x + y, list) / len(list)

  
'''
1. reduce()
    :인자를 누적적으로 적용하여 결과를 반환
    ex) from functools import reduce    
        reduce(lambda x, y: x+y, [1,2,3,4])
        => ( ( ( 1+2 )+3 )+4 ) = 10

https://programmers.co.kr/learn/courses/30/lessons/12944
'''
