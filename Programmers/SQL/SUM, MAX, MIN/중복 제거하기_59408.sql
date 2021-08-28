SELECT count(DISTINCT NAME) FROM ANIMAL_INS
WHERE NAME is not NULL;

# distinct (컬럼명)
# 
# count([ALL|DISTINCT] expression)
# ALL : NULL을 제외한 모든 값
# DISTINCT : NULL을 제외한 유니크한 값
# * : NULL을 포함한 테이블의 모든 행의 개수

# https://programmers.co.kr/learn/courses/30/lessons/59408
