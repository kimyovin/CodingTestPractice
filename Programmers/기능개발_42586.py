def solution(progresses, speeds):
    answer = []
    days=[]
    # 며칠 걸리는 지 계산
    for progress, speed in zip(progresses, speeds):
        day = ((100-progress)//speed, (100-progress)%speed)
        progress = day[0] if day[1]==0 else day[0] + 1
        days.append(progress)
    
    # 각 배포 개수 구하기
    while days:
        count = 0
        while len(days) != 1 and days[0] >= days[1]:
            count += 1
            del days[1]
        del days[0]
        answer.append(count + 1)

    return answer

def solution1(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        print(Q, -((p-100)//s))
        if len(Q)==0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s),1])     # -((p-100)//s) : 나머지는 항상 양수이므로 음수//양수로 하게 되면 양수//양수 값의 올림이 된다.
            print(p, -((p-100)//s), Q)
        else:   # day[i] > day[i+1]
            Q[-1][1]+=1
            print(p, s, Q)
    return [q[1] for q in Q]

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution1([93, 30, 55], [1,30, 5]))
print(-70//30, -70%30, (-70//30)*30)      # output: -3, 20, -90
'''
https://programmers.co.kr/learn/courses/30/lessons/42586
'''
