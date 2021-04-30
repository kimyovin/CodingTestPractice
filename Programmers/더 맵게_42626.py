import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville)>=2:
        min_ = heapq.heappop(scoville)
        
        if min_ >= K :
            break
        else:   # 두번째로 작은 원소와 합체
            heapq.heappush(scoville, min_ + heapq.heappop(scoville) *2)    # 이 값을 다시 넣어서 heap 정렬을 유지.
            answer += 1
    
    if scoville[0] < K:
        return -1
    
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))

'''
https://programmers.co.kr/learn/courses/30/lessons/42626
'''
