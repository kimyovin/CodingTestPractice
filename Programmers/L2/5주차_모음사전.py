def solution(word):
    answer = 0
    dic = {'A': 1, 'E': 2, 'I':3, 'O':4, 'U':5}
    for idx, w in enumerate(word):
        w = dic.get(w)
        if idx == 0:
            answer += 781*(w-1)+1
        elif idx == 1:
            answer += 156*(w-1)+1
        elif idx == 2:
            answer += 31*(w-1)+1
        elif idx == 3:
            answer += 6*(w-1)+1
        elif idx == 4:
            answer += w
            
    return answer
