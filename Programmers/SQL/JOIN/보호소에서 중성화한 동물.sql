SELECT OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME
FROM ANIMAL_OUTS OUTS LEFT JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE like "Intact%" AND (OUTS.SEX_UPON_OUTCOME like "Spayed%" or OUTS.SEX_UPON_OUTCOME like "Neutered%")
ORDER BY OUTS.ANIMAL_ID;

-- like ~
-- in (a, b)
-- https://programmers.co.kr/learn/courses/30/lessons/59045

-- mysql 정규식 regex 사용 가능
--
-- WHERE AI.SEX_UPON_INTAKE LIKE '%Intact%'
-- AND AO.SEX_UPON_OUTCOME REGEXP 'Spayed|Neutered'
