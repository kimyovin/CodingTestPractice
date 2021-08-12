def solution(n):
    answer = [['0' for _ in range(i)] for i in range(1, n+1)]
    num = 1
    y, x = -1, 0
    for cnt in range(n):
        for _ in range(cnt, n):
            if cnt%3 == 0:    # 왼쪽 아래로 내려가기
                y += 1
            elif cnt%3 == 1:    # 오른쪽으로 이동하기
                x += 1
            else:   # 상한 대각선으로 이동하기
                y -=1
                x -=1
            answer[y][x] = num
            num += 1
            
    answer = sum(answer, [])

    return answer
  
'''
rnd : round로 회차.
        
https://programmers.co.kr/learn/courses/30/lessons/68645
'''
