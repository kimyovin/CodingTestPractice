# 2016년
def solution(a, b):
  dayofweek={1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6:"WED", 0:"THU"}
  dayDict = {i:31 if i%2==1 else 30 for i in range(1, 8)}
  dayDict.update({i:31 if i%2!=1 else 30 for i in range(8, 13)})
  dayDict[2] = 29
  days=0
  for m in range(1,a):
    days+= dayDict.get(m)
  days+= b
  
  answer = dayofweek.get(days%7)
  
  return answer

#---------------------------
#with other solution
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

#with other solution - Using datetime
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]


print(solution(1, 1))


'''
1. for문으로 돌리기 보단 sum() 함수 사용하기!!

https://programmers.co.kr/learn/courses/30/lessons/12901
'''
