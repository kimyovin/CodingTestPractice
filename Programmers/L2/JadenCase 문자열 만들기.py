def converter(s_):
    if len(s_) == 0: return s_    # 앞, 뒤에 " "인 문자 처리
    else: return s_[0].upper() + s_[1:]

def solution(s):
    answer = ''

    s=s.lower()
    word = list(map(converter, s.split(" ")))
    answer = ' '.join(word)

    return answer
'''
---[DJH님의 예시]-----------------------------------
s로 입력받는 모든 공백을 변환된 문자에 꼭 반영 해주셔야 합니다!!
" adgagd 3eagdag " -> " Adgagd 3eagdag "        
--------------------------------------------------

https://programmers.co.kr/learn/courses/30/lessons/12951
'''
