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

# https://programmers.co.kr/learn/courses/30/lessons/17682
