def solution(seoul):
    answer = ""
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = "김서방은 {0}에 있다".format(i)
    return answer

print(solution(["Jane", "Kim"]))
#------------------------------------
#with other solution - Using list.index(value)

def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

'''
https://programmers.co.kr/learn/courses/30/lessons/12919
'''
