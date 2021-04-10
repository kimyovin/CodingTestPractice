#UDF만들기
def solution(n):
    answer = []
    #3진법으로 만들기
    q, r = divmod(n, 3)
    answer.append(str(r))
    while q >= 3:
        q, r = divmod(q, 3)
        answer.append(str(r))
        print('while ', q, r)
    if q!=0:    answer.append(str(q))
    print(answer)
    #10진법으로 만들기
    realanswer = 0
    for i, num in enumerate(answer):
        realanswer += int(num)*(3**(len(answer)-i-1))
        print(i, num, realanswer)
    return realanswer

print(solution(1))

#-------------------------------
#with other solution

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

'''
docs)class int(x, base=10) : https://docs.python.org/ko/3/library/functions.html#int

https://programmers.co.kr/learn/courses/30/lessons/68935
'''
