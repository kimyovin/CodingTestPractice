#myself
def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    return sorted(answer) if len(answer)>0 else [-1]
  

#----------------------------------
#myself-single line 

def solution_single(arr, divisor):
    return sorted([num for num in arr if num % divisor == 0]) if len(answer)>0 else [-1]


'''
https://programmers.co.kr/learn/courses/30/lessons/12910
'''
