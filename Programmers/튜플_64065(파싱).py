def solution(s):
    answer = []
    # make list
    s = s[2: -2].replace('{', '')
    s = sorted(s.split('},'), key = lambda x: len(x))

    # make tuple
    for m in s:
        mlist = list(map(int, m.split(',')))    # 안에 str 숫자를 int 숫자로 바꾸기
        answer += list(set(mlist) - set(answer))    # 다음 집합에서 없었던 숫자를 추가한다.!!!
    
    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))


'''
https://programmers.co.kr/learn/courses/30/lessons/64065
'''
