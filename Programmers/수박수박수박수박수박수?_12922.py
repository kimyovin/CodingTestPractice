###
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
###
def solution(n):
    answer = ''.join(['수' if i%2==0 else '박' for i in range(n)])
    return answer

print(solution(3))

#-------------------------------
#with other solution - Using 문자*n

def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)

def water_melon2(n):
    s = "수박" * (n//2+1)
    return s[:n]

print(water_melon2(3))
'''
1. 문자를 반복할 땐, '문자' * n 

https://programmers.co.kr/learn/courses/30/lessons/12922
'''
