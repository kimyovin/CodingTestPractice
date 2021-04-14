# Using 'cmp' parameter in sorted()

def cmp_to_key(mycmp):  #python 2.x까지만 있었기에 추가
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def comparator(o1, o2):
    o1 = str(o1)
    o2 = str(o2)
    num = int(o1+o2)
    reverseNum = int(o2+o1)

    if num < reverseNum:
        return -1
    elif reverseNum < num:
        return 1
    else:
        return 0

def solution(numbers):

    numbers = sorted(numbers, key=cmp_to_key(comparator), reverse=True)
    print('1.',numbers)
    

    print('2.',numbers)
    
    numbers = list(map(str, numbers))
    answer = ''.join(numbers)

    if numbers[0] == '0':
        return 0

    return answer

#---------------------------------------------
def solution2(numbers):
    answer = '0'
    nlist = list(map(str, numbers))
    nlist = sorted(nlist, reverse=True, key=lambda a: (a[0], a[1%len(a)], a[2%len(a)], a[3%len(a)]))
    
    # 0만 있는 리스트 처리
    if nlist[0] == '0':
        return '0'
    
    answer = ''.join(nlist)

    return answer
    

#----------------------------------------------------------------------
#with other solution - Using 문자열 정렬

def solution3(numbers):
    numbers = list(map(str, numbers))
    
    numbers.sort(key=lambda x: x*3, reverse=True)
        #문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교
        #같으면, 다음 인덱스도 비교
        
    return str(int(''.join(numbers)))   #str(int()) => '0000' 같은 걸 '0'으로 바꾸기 위해서 작성


print(solution([412,41]))
print(solution([10, 0, 0, 1, 2, 8, 9, 10]))
print('...', solution([10, 0, 0, 1, 2, 8, 9, 10]))

'''
1. cmp_to_key => cmp 매개 변수는 python 2.x에 있었지만 언어를 단순화하고 통합하기 위한 노력의 일환으로,
                 풍부한 비교(rich comparisons)와 __cmp__() 매직 메서드 간의 충돌을 제거되었다.
2. 문자열 비교 => 아스키값을 기준으로 앞부분부터 비교한다.(사전순)

https://programmers.co.kr/learn/courses/30/lessons/42746
'''
