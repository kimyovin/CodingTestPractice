# myself (error) - 실패, 런타임 에러 : return 값이 int형의 범위를 초과
fibo = [0, 1]
def solution(n):
    while len(fibo) <= n:
        # print(fibo)
        fibo.append(fibo[-2]+fibo[-1])

    return fibo[n]

#-------------------------------
# myself (pass) - 통과 : 1234567까지의 범위를 정해줌으로써 int의 범위를 벗어나지 않게 하였다.

def solution1(n):
    fibo = [0, 1]
    while len(fibo) <= n:
        fibo.append((fibo[-2]+fibo[-1])%1234567)    # %1234567을 해준 이유: 언제나 값이 int형 범위에 있다.
        
    return fibo[n]

# other solution - Using pisano
def fibonacci(n):
    fibo = [0, 1]
    mod = 1000000
    p = int(mod/10*15)
    while len(fibo) <= n%p:
        fibo.append(fibo[i-1] + fibo[i-2])
        fibo[i] %= mod
 
    return fibo[n%p]


  
print(1234567)
print(solution(44))
print(solution1(44))
print(fibonacci(44))

'''
1. % 1234567 
    => int 범위 내에 항상 값이 존재함을 보장할 수 있다.
2. 모듈러의 연산) 
    => (A + B) % C ≡ ( ( A % C ) + ( B % C) ) % C
3. 피사노 주기(Pisano Period)
    : 주기의 길이가 P면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.
    => 피보나치 수를 k로 나눈 수는 항상 주기를 갖는다.

https://programmers.co.kr/learn/courses/30/lessons/12945
'''
