#myself
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        line = format(arr1[i]|arr2[i], '0'+str(n)+'b')
        line = line.replace('1', '#')
        line = line.replace('0', ' ')
        answer.append(line)
    return answer
  
#https://programmers.co.kr/learn/courses/30/lessons/17681
'''
1. '05b' : 5자리에 맞춰진 이진수
  ex) format(3, 'b') => 101
  ex) format(3, '05b') => 00101
  
  ==>>> 포맷 맞추기에 잘 활용된다.
'''
