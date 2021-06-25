-- https://programmers.co.kr/learn/courses/30/lessons/59041

select NAME, count(NAME) as COUNT FROM ANIMAL_INS
    group by NAME HAVING COUNT(NAME) > 1
    order by NAME;

