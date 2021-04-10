###
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
###

def solution(s):
    answer = False
    if (len(s) == 4 or len(s)==6) and s.isdigit():
        answer = True
    return answer
print(solution("1234"))

#-------------------------------
#with other solution - Using 'in'
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

'''
1. 값을 확인할 때, 값이 n 또는 m 일 경우,
  식을 두 번 사용하는 것 대신 'in' 키워드를 사용한다.
  
https://programmers.co.kr/learn/courses/30/lessons/12918
'''
