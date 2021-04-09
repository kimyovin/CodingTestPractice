def solution(s):
  s = s.split(" ")
  for idx, string in enumerate(s):
    s[idx]=''.join([cha.upper() if i%2==0 else cha.lower() for i, cha in enumerate(list(string))])
  answer = ' '.join(s)
  
  return answer
  
print(solution("TGFDS DSJIFD"))


'''
1. split(): 괄호 안에 아무 값도 넣어 주지 않으면 스페이스, 탭, 엔터 등 모든 공백을 기준으로 문자열을 나누는데, 문제는 스페이스만을 기준으로 나누길 원하는거군요
2. list(string) => 한 글자씩 리스트 만들기
   string.split() => 공백으로 리스트 만들기
   
https://programmers.co.kr/learn/courses/30/lessons/12930
'''
