def solution(brown, yellow):
    answer = []
    area = brown + yellow
    divisor = []

    # 약수 구하기
    for i in range(1, area//2+1):
        if area%i ==0 and i <= area//i:
            divisor.append((i, area//i))

    # 사각형을 만들 수 있는 조합 찾기
    for row, col in divisor:
        if (row-2)*(col-2) == yellow:
            answer.append(col)
            answer.append(row)
            break

    return answer

print(solution(8, 1))

'''
https://programmers.co.kr/learn/courses/30/lessons/42842
'''
