SELECT count(*) from ANIMAL_INS;

-- COUNT(*) 으로 존재하는 모든 행을 가져온다
-- 만약 * 대신 COUNT(NAME) 이런 식으로 사용한다면
-- NAME 컬럼에 NULL이 들어있지 않은 행 개수를 가져오게 될 것이다
-- 즉, null이 아닌 모든 값
