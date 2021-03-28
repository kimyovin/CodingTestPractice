#myself
def solution(participant, completion):
  participant.sort()
  completion.sort()
  answer = participant[-1]
  
  #중복 이름 방지
  for i in range(len(completion)):
    if participant[i] != completion[i]:
      answer = participant[i]
      break
      
  return answer

##삭제
#해시맵 - O(1)
#다른 구조 - O(n)
##

-------------------------------------------------------------
#with other solution1 - Using Counter Class
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
  
-------------------------------------------------------------
#with other solution2 - Hash Function
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
