#myself
def solution(n):
    string = str(n)
    answer = [int(string[i-1]) for i in range(len(string), 0, -1)]
    
    return answer

print(solution(12345))

#-------------------------------
#with other solution - Using map

def digit_reverse(n):
    return list(map(int, reversed(str(n))))

'''
https://programmers.co.kr/learn/courses/30/lessons/12932
'''
