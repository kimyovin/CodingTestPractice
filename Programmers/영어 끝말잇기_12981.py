def solution(n, words):
    answer = [0, 0]
    l = len(words)
    for i in range(1, l):
        if len(words[i]) == 1 or words[i-1][-1] != words[i][0]:
            answer = [i%n+1, i//n + 1]
            break
            
        if words[i] in words[:i]:
            answer = [i%n+1, i//n+1]
            break
    return answer
    
'''
https://programmers.co.kr/learn/courses/30/lessons/12981
'''
