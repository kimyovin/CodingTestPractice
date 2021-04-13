###
# 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
# 
# 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 
# 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.
# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
# 
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 스파이는 하루에 최소 한 개의 의상은 입습니다.
# 
# [입출력 예]
# clothes	                                                                                return
# [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
# [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	            3
###

from functools import reduce
def solution(clothes):
    answer = 0
    clothesDict={}
    for one in clothes:
        if clothesDict.get(one[1]) == None:
            clothesDict[one[1]] = 1   # 0인 경우, 포함
        clothesDict[one[1]] += 1
    print(clothesDict)
    answer = reduce(lambda x, y : x*y , list(clothesDict.values())) -1 # 공집합 제거
    return answer

#--------------------------------------------------
# with other solution - Using Counter collections

def solution1(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

'''
1. 개수를 셀 때는 Counter !!!!
https://programmers.co.kr/learn/courses/30/lessons/42578
'''
