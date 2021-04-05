'''

n: 전체 학생 수
lost: 체육복을 도난당한 학생들의 번호가 담긴 배열
reserve: 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열

return: 체육수업을 들을 수 있는 학생의 최댓값
'''
#myself
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # 탐욕법
    maxN = len(lost)    # 체육수업을 들 을 수 있는 학생의 최댓값
    for idx, l in enumerate(lost):
        if l in reserve:            # reserve - lost: 여분이 있었지만 도난 당한 사람 번호
            reserve.remove(l)
            maxN -= 1
        elif l-1 in reserve:
            reserve.remove(l-1)
            maxN -= 1
        elif l+1 in reserve:
            if l+1 in lost:         # 여유분이 있지만 도난 당한 사람
                pass
            else:
                reserve.remove(l+1)
                maxN -= 1
    
    answer = n - maxN
    return answer

print(solution(5, [2, 3, 4], [1, 2, 3]))
#------------------------------------
#with other solution 

def solution1(n, lost, reserve):
    _reserve = list(set(reserve) - set(lost))
    _lost = list(set(lost) - set(reserve))
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

  '''
  1. 집합의 차집합은 set을 이용한다.
  
  https://programmers.co.kr/learn/courses/30/lessons/42862#
  '''
