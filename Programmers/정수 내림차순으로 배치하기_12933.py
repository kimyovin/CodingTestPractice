# 정수 내림차순으로 배치하기
def solution(n):
    answer = int(''.join(sorted(list(str(n)), reverse=True)))
    
    return answer
    
print(solution(118372))

'''
https://programmers.co.kr/learn/courses/30/lessons/12933
'''
