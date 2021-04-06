#문자열 내림차순으로 배치하기
#myself 
def solution(s):
    answer = list(s)
    answer = ''.join(sorted(list(s), reverse=True))
    return answer
    
print(solution("Zbcdefg"))

#--------------------------------
#with other solution - 
def solution(s):
    return ''.join(sorted(s, reverse=True)) #문자열이 자동으로 정렬된 리스트가 됨


'''
1. sorted(문자열) => 문자열이 정렬된 리스트가 됨!!

https://programmers.co.kr/learn/courses/30/lessons/12917

'''
