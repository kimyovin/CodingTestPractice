from collections import deque
def solution(prices):
    answer = []
    stack = deque(prices.copy())
    for idx, cv in enumerate(prices):
        stack.popleft() # O(1)
        count = 0
        for i in stack:
            count += 1
            if cv > i:
                break
        
        answer.append(count)

    return answer

print('#',solution([1, 2, 3, 2, 3]))    # [4, 3, 1, 1, 0]
print('#',solution([1, 2, 5, 3, 2, 6]))    # [5, 4, 1, 1, 1, 0]
print('#',solution([1, 2, 3, 2, 3, 1]))    # [5, 4, 1, 2, 1, 0]

######################################################
##### 효율성 통과가 안된 코드들 - enumerate()

def solution(prices):
    answer = []
    for idx, cv in enumerate(prices):
        count = len(prices)-idx-1
        for nidx, nv in enumerate(prices[idx:]):
            if cv > nv:
                count = nidx
                break
        answer.append(count)
    return answer


def solution(prices):
    answer = []
    for idx, cv in enumerate(prices):
        count = len(prices)-idx-1
        for nidx, nv in enumerate(prices[idx:]):
            if cv > nv:
                count = nidx
                break
        answer.append(count)
    return answer

  
##### 효율성이 통과된 코드 - range()

def solution(prices):
    answer=[]
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[j]<prices[i]:
                break
        answer.append(count)
    return answer

'''
1. enumerate()는 반복 자료형 내 원소를 하나씩 다 봐야하므로 O(n) 인 반면, range()는 O(1)이다.

https://programmers.co.kr/learn/courses/30/lessons/42584
'''
