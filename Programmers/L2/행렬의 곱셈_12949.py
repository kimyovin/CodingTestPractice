def solution(arr1, arr2):
    answer = [['0' for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    arr2 = list(map(list, zip(*arr2)))  # 행과 열을 뒤집음
    
    y, x = 0, 0
    for y1 in arr1:
        for x1 in arr2:
            num = sum(list(map(lambda i, j: i*j, y1, x1)))
            answer[y][x] = num 
            x += 1
        x = 0
        y += 1
            
    return answer
  
  '''
  https://programmers.co.kr/learn/courses/30/lessons/12949
  '''
