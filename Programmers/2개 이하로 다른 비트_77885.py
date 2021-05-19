import math
def solution(numbers):
    answer = []
    for n in numbers:
        nb = bin(n)[2:]
        if n == 0:
            answer.append(1)
        elif (n+1) & (n) == 0:    # n = 2의 제곱수 - 1
            nb = '10' + nb[1:]
            print(int(nb,2))
            answer.append(int(nb,2))
        elif math.log2(n) %1 == 0:    # n = 2의 제곱수
            answer.append(n+1)
        else:   # n이 2의 제곱수 -1이 아닐 때
            if nb[-1] == '0':
                answer.append(n+1)
            elif nb[-1] == '1':
                idx0 = nb.rfind('0')
                nb = nb[:idx0] + '10'+ nb[idx0+2:]
                answer.append(int(nb,2))
        
    return answer

print(solution([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
'''
월간 코드 챌린지 시즌2
https://programmers.co.kr/learn/courses/30/lessons/77885
'''
