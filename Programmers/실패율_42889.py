#myself
def solution(N, stages):
    failrate = {} #stages=> key, failrate=> value

    #len: 마지막에 -j(분자), (분모)=len - (이전 분자)
    numerator = 0   #분자, not clear user
    denominator = len(stages) #분모, clear user
    
    for i in range(1, N+1): 
        denominator -= numerator
        numerator = stages.count(i)
        if denominator == 0:
            failrate[i] = 0
        else:
            failrate[i] = numerator/denominator

    answer = sorted(failrate, reverse=True, key=lambda k: failrate[k])    #failrate[key] => value
    
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42889
