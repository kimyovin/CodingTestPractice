#myself
def solution(numbers):
    answer = []
    for i, pnum in enumerate(numbers):
        for num in numbers[i+1:]:
            answer.append(pnum+num)
    answer = sorted(list(set(answer)))
    return answer
