#myself
def solution(arr1, arr2):
    count = len(arr1)
    sumSize = len(arr1[0])
    answer = [[0]*sumSize for _ in range(count)]

    for i in range(count):
        for j in range(sumSize):
            answer[i][j]=arr1[i][j]+arr2[i][j]

    return answer

#----------------------------------------------------------------
#####with other solution1 - Using zip()
def sumMatrix1(arr1,arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1,arr2)]
    return answer

#####with other solution2 - Using numpy
import numpy as np
def sumMatrix2(A,B):
    A = np.array(A)
    B = np.array(B)
    answer = A+B  # 각 요소 더하기
    return answer.tolist()

print(sumMatrix2([[1], [2], [3]], [[3], [5], [7]]))
'''
1. zip()
    : zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함
    
    ex) %list(zip([1, 2, 3], [4, 5, 6]))
        =>[(1, 4), (2, 5), (3, 6)]
        %list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
        =>[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
        %list(zip("abc", "def"))
        =>[('a', 'd'), ('b', 'e'), ('c', 'f')]
    
2. numpy
    numpy 연산: + , -, numpy.multiply(a, b), numpy.divide(a, b)

https://programmers.co.kr/learn/courses/30/lessons/12950
'''
