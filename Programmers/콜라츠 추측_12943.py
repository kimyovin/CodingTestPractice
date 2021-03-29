#myself
def solution(num):
    answer = collatz(num, 0)
    return answer

def collatz (n, i):
    if i >= 500:
        return -1
    
    if n == 1:
        return i
    elif n%2 ==0:
        i += 1
        return collatz(n//2, i) #파이썬에서 return하는 것이 명시되지 않으면 None을 리턴한다.
    else :
        i += 1
        return collatz(n*3 +1, i)
