-- https://programmers.co.kr/learn/courses/30/lessons/59041

select NAME, count(NAME) as COUNT FROM ANIMAL_INS
    group by NAME HAVING COUNT(NAME) > 1
    order by NAME;

# GROUP에 조건을 줄때는 WHERE절이 아니라 HAVING절을 사용한다.
