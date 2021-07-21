-- https://programmers.co.kr/learn/courses/30/lessons/59412
SELECT hour(DATETIME) as HOUR, COUNT(*) FROM ANIMAL_OUTS 
WHERE hour(DATETIME) BETWEEN 9 AND 19
GROUP BY hour(DATETIME) ORDER BY HOUR;
