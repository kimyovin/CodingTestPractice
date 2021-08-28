SET @hour := -1;

SELECT (@hour := @hour +1 ) as HOUR, 
(SELECT count(*) from ANIMAL_OUTS where hour(DATETIME) = @hour) AS COUNT 
from ANIMAL_OUTS
WHERE @hour < 23;   -- @hour가 23보다 작을 때까지 @hour := @hour + 1이 실행된다.

# @(변수명) = (값);
# 대입연산자 :=
# 비교연산자 =

# https://programmers.co.kr/learn/courses/30/lessons/59413
