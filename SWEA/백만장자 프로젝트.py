
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    values=[]
    for v in input().split():
        values.append(int(v))
	
    # 팔 날
    maxv=values[-1]   # 남은 주 중에서 가장 큰 매매가
    total=0
    for i in range(N-1, -1, -1):
        if maxv < values[i]:
            maxv = values[i]
        else :
            total += maxv - values[i]
    
    print("#%d %d"%(test_case, total))
    
'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc
'''
