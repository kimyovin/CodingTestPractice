import re
def solution(str1, str2):
    answer = 0
    # step1. filtering
    p = re.compile('[^a-zA-Z]+')   # replace되어야 할 것! (즉, 문자가 아닌 것)
    
    set1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not p.findall(str1[i:i+2])]
    set2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if not p.findall(str2[i:i+2])]
    
    intr=[]
    unn=[]
    for i in set1:
        if i in set2:
            idx=set2.index(i)
            set2.pop(idx)
            intr.append(i)
        else:
            unn.append(i)
    unn = set1 + set2
    
    if not unn: # DivisionByZero 방지
        return 65536   
    answer = int((len(intr) / len(unn)) * 65536)

    
    return answer
  
#########################################################################
# other solution
def solution1(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]  # isalpha()를 하면 정규표현식을 사용할 필요가 없다!
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    tlist = set(list1) | set(list2)
    res1 = [] #합집합
    res2 = [] #교집합

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))

        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536
  
'''
자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나로 알려져 있다. 
두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.

https://programmers.co.kr/learn/courses/30/lessons/17677
'''
