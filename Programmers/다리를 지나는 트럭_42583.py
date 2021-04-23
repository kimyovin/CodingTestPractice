def solution(bridge_length, weight, truck_weights):
    answer = 0  #time
    # 선작업
    moving = [[truck_weights[0], 0]]    #moving: 다리 위의 트럭, 다리를 건너는 트럭
    bridge_weight = truck_weights[0]
    del truck_weights[0]
    
    while moving:
        answer += 1
        if moving:  # 다리 위에 트럭이 있으면
            # 한 칸씩 이동
            for truck_info in moving:
                truck_info[1] += 1

            # 다 나온 애는 탈출
            if moving[0][1] > bridge_length:
                bridge_weight -= moving[0][0]
                del moving[0]
        
        # 새로운 애 투입
        if truck_weights and weight >= bridge_weight + truck_weights[0]:
            # print(answer, bridge_weight, truck_weights[0])
            bridge_weight += truck_weights[0]
            moving.append([truck_weights[0], 1])   # (truck_weight, position)
            del truck_weights[0]
        
        # print(answer, bridge_weight, moving, truck_weights)
    return answer   #마지막 원소가 다리를 건너는 시간


# def solution()
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10,10,10,10,10,10,10,10]))
print(solution(2, 10, [7, 4, 5, 6]))

'''
https://programmers.co.kr/learn/courses/30/lessons/42583
'''
