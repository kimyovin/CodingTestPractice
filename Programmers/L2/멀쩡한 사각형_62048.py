import math
def solution(w,h):
    white = math.gcd(w,h)
    count = w//white + h//white -1

    answer = w*h - white * count

    return answer


print(solution(3,2))

'''
https://programmers.co.kr/learn/courses/30/lessons/62048
'''
