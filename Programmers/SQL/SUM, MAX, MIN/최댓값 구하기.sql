-- [https://programmers.co.kr/learn/courses/30/lessons/59415]
-- 가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

SELECT DATETIME FROM ANIMAL_INS order by DATETIME DESC limit 1
