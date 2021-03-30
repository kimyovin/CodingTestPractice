#myself
def solution(d, budget):
    answer = 0
    d.sort()
    for price in d:
        if budget >= price:
            answer += 1
            budget -= price
        else:
            break

    return answer
  #https://programmers.co.kr/learn/courses/30/lessons/12982
