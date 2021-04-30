def solution(s):
    # length 후보 구하기(약수)
    stl= len(s)

    # 비교
    minlength = stl # answer
    for l in range(1, stl//2+1, 1):
        splitSet = []
        answerStr=''
        for i in range(0, stl, l):
            splitSet.append(s[i:i+l])
        p = 0   # pivot
        count = 1   # 연속된 횟수

        for p in range(0, len(splitSet)-1):
            if splitSet[p] == splitSet[p+1]:
                count += 1
            else:
                answerStr += str('' if count == 1 else count)+splitSet[p]
                count = 1
            
            if p == len(splitSet)-2:
                answerStr += str('' if count == 1 else count)+splitSet[p+1]
            

        if minlength > len(answerStr):
            minlength = len(answerStr)


    return minlength
  
  
print(solution("abcabcdede"))
'''
https://programmers.co.kr/learn/courses/30/lessons/60057
'''
