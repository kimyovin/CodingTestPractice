def solution(absolutes, signs):
    answer = 0
    for ab, sign in zip(absolutes, signs):
        if sign == True:
            answer += ab
        else:
            answer -= ab
    return answer
    
  '''
  https://programmers.co.kr/learn/courses/30/lessons/76501
  '''
