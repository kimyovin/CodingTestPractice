SELECT ANIMAL_TYPE, if( isnull(NAME), "No name", NAME) , SEX_UPON_INTAKE FROM ANIMAL_INS order by ANIMAL_ID

-- or SELECT ANIMAL_TYPE, ifnull(NAME, "No name"), SEX_UPON_INTAKE FROM ANIMAL_INS order by ANIMAL_ID

/* sql, null 처리하기
1. if ( 조건문, 참일때 값, 거짓일때 값)

  ex)  select member_id, if ( isnull(birthday), '-', birthday ) from member
  설명 - 멤버 테이블에서 아이디(member_id) 와 생일을 뽑는데 null 일경우는 - 를 출력, 
        아니면 생일을 출력
      
2. case (조건 또는 값)
          when 값1 then 표시값
          when 값2 then 표시값
  else 표시값
  end
  
  ex)   select case a when '1' then a when '2' then b else c end from table_name
  설명 - a 값이 '1'이면 a, '2' 이면 b, 둘다 아닐경우 c 를 출력
  
3. ifnull ( 변수, null일때 값) //only my-sql

4. isnull ( 변수, null일때 값) //only mssql

5. NVL ( 변수, null일때 값) //only oracle

https://programmers.co.kr/learn/courses/30/lessons/59410
*/
