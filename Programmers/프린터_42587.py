def solution(priorities, location):
    answer = location  # location의 위치
    l = len(priorities)
    outstack = []
    target = (location, priorities[location])   # 요청한 작업
    priset=[(i, v) for i, v in enumerate(priorities)]   #(index, value)
    print(priset[0][1])
    
    while len(outstack) != l:   # 1 step
        print(priset, outstack)
        # 가장 큰 값이면 enqueue
        if priset[0][1] == max(priset, key= lambda x: x[1])[1]:
            outstack.append(priset[0])
            del priset[0]
        else:
            # 순서 조정
            l2 = len(priset)
            for i in range(l2):
                if priset[0][1] < priset[i][1]:
                    priset.append(priset[0])
                    del priset[0]
        try:
            answer = outstack.index(target)+1
            return answer
        except ValueError:
            pass
            
    
    answer = outstack.get(target)+1
    
    print(priset, outstack)

    return answer

print(solution([1, 9, 7, 8, 6], 2))

######################
# with other solution 
def solution1(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

'''
https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3
'''def solution(priorities, location):
    answer = location  # location의 위치
    l = len(priorities)
    outstack = []
    target = (location, priorities[location])   # 요청한 작업
    priset=[(i, v) for i, v in enumerate(priorities)]   #(index, value)
    print(priset[0][1])
    
    while len(outstack) != l:   # 1 step
        print(priset, outstack)
        # 가장 큰 값이면 enqueue
        if priset[0][1] == max(priset, key= lambda x: x[1])[1]:
            outstack.append(priset[0])
            del priset[0]
        else:
            # 순서 조정
            l2 = len(priset)
            for i in range(l2):
                if priset[0][1] < priset[i][1]:
                    priset.append(priset[0])
                    del priset[0]
        try:
            answer = outstack.index(target)+1
            return answer
        except ValueError:
            pass
            
    
    answer = outstack.get(target)+1
    
    print(priset, outstack)

    return answer

print(solution([1, 9, 7, 8, 6], 2))

######################
# with other solution 
def solution1(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

'''
https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3
'''
