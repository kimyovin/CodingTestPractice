def solution(s):
    numbers = [int(i) for i in s.split()]
    answer = str(min(numbers))+' '+str(max(numbers))

    return answer

###########################################
# other solution - Using sort()
def solution(s):
    s_list=s.split(" ")
    n = [int(i) for i in s_list]
    n.sort()

    return str(n[0]) + " " + str(n[-1])


print(solution("1 2 3 4"))

'''
# list를 정렬하여 최솟값과 최댓값을 찾을 수 있다.
# 
https://programmers.co.kr/learn/courses/30/lessons/12939
'''
