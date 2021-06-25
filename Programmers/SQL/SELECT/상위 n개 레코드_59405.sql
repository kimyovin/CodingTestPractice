-- https://programmers.co.kr/learn/courses/30/lessons/59405

SELECT NAME FROM 
(SELECT RANK() OVER (ORDER BY DATETIME) as RANKING, NAME FROM ANIMAL_INS ) c
WHERE RANKING = 1;
