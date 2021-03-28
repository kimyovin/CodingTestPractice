#myself
def solution(arr):
    answer = [arr[0]]
    for num in arr:
        if answer[-1] != num:
            answer.append(num)
    
    return answer

print(solution([4,4,4,3,3]))
#https://programmers.co.kr/learn/courses/30/lessons/12906
#----------------------------#
#with other solution1
def solution1(arr):
    answer = []
    for num in arr:
        print(answer[-1:])  #마지막 원소만 들어있는 리스트!! 공집합이여도 error가 안 난다!!!
                            #슬라이싱은 인덱스 값이 범위 초과해도 오류 X
        if answer[-1:] != [num]:
            answer.append(num)
    
    return answer

print(solution1([4,4,4,5,5]))
