#가운데 글자 가져오기
def solution(s):
  answer = ''
  mid = [len(s)//2-1, len(s)//2] if len(s)%2==0 else [len(s)//2]
  answer=str([s[i] for i in mid])
  
  return answer

#-----------------------------
#with other solution - 
def string_middle(str):
  return str[(len(str)-1)//2: len(str)//2+1]
  
print(solution("qwera"))

'''
https://programmers.co.kr/learn/courses/30/lessons/12903
'''
