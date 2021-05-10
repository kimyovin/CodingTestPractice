def solution(answers):
    patns = { 
        1:[1, 2, 3, 4, 5],
        2:[2, 1, 2, 3, 2, 4, 2, 5],
        3:[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    l = len(answers)
    patn = list(patns.keys())
    
    for i in patn:
        user_aswr = patns.get(i)
        ul = len(user_aswr)
        patns[i] = 0
        for a in range(l):
            if answers[a]==user_aswr[a%ul]:
                patns[i] += 1
    
    answer = [user for user, score in patns.items() if max(patns.values()) == score]
    
    return sorted(answer)

print(solution([1, 2, 3, 4, 5]))
'''
https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
'''
