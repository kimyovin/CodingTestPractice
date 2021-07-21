def solution(triangle):
    answer = 0
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j in [0, len(triangle[i])-1]:
                triangle[i][j] = triangle[i][j]+triangle[i-1][j if j==0 else j-1]
            else:
                triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j])+triangle[i][j]

    answer = max(triangle[-1])
    return answer
  
'''
DP 문제 
https://programmers.co.kr/learn/courses/30/lessons/43105
'''
