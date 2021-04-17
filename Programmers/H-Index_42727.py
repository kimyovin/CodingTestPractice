### 
# 조건)
# 1. 인용 개수 조건 : h 편 이상 인용된 논문이
# 2. 논문 개수 조건 : h 편 이상이어야 한다.
###

def solution(citations):
    answer = 0
    citations.sort(reverse=True)    # 논문 개수 조건 풀이를 위헤 reverse로 정렬
    l = len(citations)
    for i in range(l):
        if citations[i] > i:    
            answer = i+1    # 인용된 횟수가 i보다 크다면 논문 '개수'에 초점을 맞춰 h=i+1
        elif citations[i] == i:
            answer = i  # 인용된 횟수가 i와 '값'이 같다면 h=i
        else:
            break

    return answer
  
###########################################################

def solution1(citations):
    answer = 0
    citations.sort()    #논문 개수 조건 풀이를 위해 정렬
    
    for h in range(len(citations)+1):
        for idx, num in enumerate(citations):
            if h <= num and h <= len(citations) - idx:   # 인용 개수 조건 and 논문 개수 조건
                answer = h

    return answer

print(solution([3,0,6,5,1]))
print(solution([12, 11, 10, 9, 8, 1]))  # 5
print(solution([4, 4, 4]))

#-----------------------------------
#with other solution1

def solution2(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

#with other solutoin2

def solution3(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))   # enumerate(citations, start=1) => 자신보다 크거나 같은 수의 개수를 매칭
    return answer

'''

https://programmers.co.kr/learn/courses/30/lessons/42747
'''
