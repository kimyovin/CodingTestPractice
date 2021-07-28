def gototheschool(row, col, route):
    if row<1 or col<1 : return 0
    elif route[row][col] == -1 : return 0 # 웅덩이인 경우
    elif route[row][col] > 0: return route[row][col]  # 이미 값이 있을 경우
    else: route[row][col]=(gototheschool(row-1, col,route) + gototheschool(row, col-1, route))%1000000007
        
    return route[row][col]
        
def solution(m, n, puddles):
    answer = 0
    route = [[0]*(m+1) for _ in range(0, n+1)]
    route[1][1] = 1
    for i in puddles:
        route[i[1]][i[0]] = -1  # m : col 의미, n : row 의미
    answer = gototheschool(n, m, route)
    
    return answer
    
'''
m : col 의미, n : row 의미
---------------------------------------------------------
https://programmers.co.kr/learn/courses/30/lessons/42898
'''
