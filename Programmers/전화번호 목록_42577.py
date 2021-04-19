#myself - 효율성 테스트 4 실패
#Using Set, startswith
def solution(phone_book):
    answer = True
    print(phone_book)
    for idx,i in enumerate(phone_book):
        book = tuple(num for num in phone_book if len(num)< len(i))
        if len(i) == 1:
            return True
        elif i.startswith(tuple(book)):    
            return False
    return answer

#-------------------------------------------------------
# with other solution1 - Using zip(), startswith()

def solution(phone_book):
    phoneBook = sorted(phone_book)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):    # 바로 뒤의 값만 비교
        print(p1, p2)
        if p2.startswith(p1):
            return False
    return True
  
# with other solution2 - Using HashMap
def solution(phone_book):
  answer = True
  hash_map = {}
  for phone_number in phone_book:
      hash_map[phone_number] = 1
  for phone_number in phone_book:
      temp = ""
      for number in phone_number:
          temp += number
          if temp in hash_map and temp != phone_number:
              answer = False
  return answer

# with other solution3
def solution(phone_book):   
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1]:  # 바로 뒤의 값만 비교
            return False
        
    return True
  
'''
https://programmers.co.kr/learn/courses/30/lessons/42577
'''
