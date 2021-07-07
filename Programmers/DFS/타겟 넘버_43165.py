def solution(numbers, target):
    candidate = [0]
    for i in numbers:
        sub = []
        for j in candidate:
            sub.append(j+i)
            sub.append(j-i)

        candidate = sub
    
    return candidate.count(target)

print(solution([1,2,3,4], 4))

'''
https://programmers.co.kr/learn/courses/30/lessons/43165
'''
