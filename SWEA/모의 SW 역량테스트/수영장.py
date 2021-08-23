T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    _day, _month, _3month, _year = map(int, input().split(" "))
    numb = list(map(int, input().split(" ")))
    pay = [0 for _ in range(12)]
    
    for i in range(12):
        m_pay = min(_day * numb[i], _month) # 1일권과 1달권 비교
        pay[i] = min(pay[i-1]+m_pay, pay[i-3]+_3month)  # 1일권/1달권을 샀을 때와 3달권을 샀을 때 비교
        
    # 마지막 1년 이용권이랑 비교
    answer = min(max(pay), _year)
    print("#{} {}".format( test_case, answer))
    
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq&categoryId=AV5PpFQaAQMDFAUq
