select INS.NAME, INS.DATETIME
from ANIMAL_INS INS left join ANIMAL_OUTS OUTS 
on INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL
ORDER BY INS.DATETIME
LIMIT 3;

-- mysql은 MINUS, INTERSECT를 지원하지 않는다.
-- left join ~ where (column) is null 로 구현한다.

-- https://programmers.co.kr/learn/courses/30/lessons/59044
