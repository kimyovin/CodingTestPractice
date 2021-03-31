#myself
import re
def solution(dartResult):
    answer = 0
    map_ = {'S': 1, 'D': 2, 'T': 3}
    mark = re.findall('[0-9]+[S|D|T][*]?#?', dartResult)
    prenum = 0
    for count in mark:
        num = int(re.findall('\d+', count)[0])
        sqr = re.findall('[S|D|T]', count)[0]
        num = num ** map_[sqr]

        if re.search('[*]', count):
            num *= 2
            answer += prenum
        elif re.search('#', count):
            num = -num        
        answer += num
        
        prenum = num
        print(count, num, answer)
    return answer

#----------------------------------------------------------------
#####with other solution1 - 정규표현식에 ()로 그룹화를 하여 튜플화할 수 있다.

import re
def solution1(dartResult):
    sqt = ['S', 'D', 'T']
    option = {'#': -1, '*': 2, '': 1}

    mark = re.findall('(\d+)([SDT])([*#]?)', dartResult)
    for i in range(len(mark)):
        print(mark)
        if mark[i][2] == '*' and i > 0:
            mark[i-1] *= 2  # Tuple로 이뤄진 원소가 숫자로 된다 ex) ('1', 'S', '') => 1
        
        mark[i] = int(mark[i][0]) ** (sqt.index(mark[i][1])+1) * option[mark[i][2]]
    answer = sum(mark)
    return answer

'''
1. findall에서 정규표현식에 ()로 그룹화를 시키면
    튜플화가 된다.
    mark = re.findall('([0-9]+)([S|D|T])([*]?#?)', dartResult)
    1D2S3T*
    => [('1', 'D', ''), ('2', 'S', ''), ('3', 'T', '*')]
2. 리스트에서 원소의 형을 바꿔도 된다. => 한정짓지 말자
    ex) Tuple => int
   
https://programmers.co.kr/learn/courses/30/lessons/17682
'''
