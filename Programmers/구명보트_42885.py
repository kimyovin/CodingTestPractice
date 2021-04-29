def solution(people, limit):
    answer = 0  # 구명보트의 개수
    people.sort()
    front, end =0, len(people)-1
    print(people)
    while front <= end:
        partner = 0
        # 같이 탈 동료 구하기   : limit 보다 작지만 제일 큰 수
        for i in range(end, front-1, -1):
            if people[front] + people[i] <= limit:
                partner = i
                break
            elif i == front+1:  # partner가 없는 경우, 혼자 빠져나가야 하는 경우
                partner = front
                
        print(front, end, partner)
        if partner == front +1 or partner == front: # 탐색이 끝난 경우, 혼자 빠져 나갈 경우
            answer += end-partner+1
            break
        elif partner != front:
            answer += end-partner+1   # 혼자 보트 타는 사람
            end = partner-1
            front += 1

        print(front, end, partner, answer)

    return answer

#######################################
#with other solution
def solution1(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer


print('#', solution([70, 50, 80, 50], 100)) # 3
print('#',solution([100, 100, 100], 100))   # 3
print('#',solution([20, 40, 50, 60, 80, 100], 100)) # 4
print('#',solution([40, 40, 30], 100))  # 2
print('#',solution([50, 50, 50, 30], 100))  # 3

'''
https://programmers.co.kr/learn/courses/30/lessons/42885
'''
