def solution(n):
    answer = ''

    while n > 3:
        num = n%3
        n = (n-1)//3    # -1을 해준 이유: 124나라의 숫자는 0이 아니라 1부터 시작하므로. 자릿수를 맞춰주기 위함.
        answer = str(4 if num == 0 else num) + answer
    answer = str(4 if n == 3 else n) + answer
    return answer
  
for i in range(22):
    print('#', i, solution(i))
    
'''
https://programmers.co.kr/learn/courses/30/lessons/12899
'''
