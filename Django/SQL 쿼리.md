#### GPT
---
[[ORM]]
SQL(Structured Query Language) 쿼리는 데이터베이스에서 정보를 요청하고 조작하는 데 사용되는 명령어나 문장입니다.

쿼리는 기본적으로 몇 가지 유형으로 나눌 수 있습니다:

1. 선택(Select): 데이터베이스에서 데이터를 읽습니다. 이것은 보통 원하는 특정 정보를 데이터베이스로부터 요청하는데 사용됩니다.

예: SELECT * FROM Users WHERE Age > 18;

2. 삽입(Insert): 데이터베이스에 새로운 데이터를 추가합니다.

예: INSERT INTO Users (FirstName, LastName) VALUES ('John', 'Doe');

3. 갱신(Update): 데이터베이스의 기존 데이터를 변경합니다.

예: UPDATE Users SET Email = 'john.doe@example.com' WHERE UserID = 1;

4. 삭제(Delete): 데이터베이스의 데이터를 삭제합니다.

예: DELETE FROM Users WHERE UserID = 1;
---
데이터베이스 관리 시스템(DBMS)에 따라 SQL 구문의 형식이 약간 다를 수 있지만, 대부분의 DBMS에서는 위와 비슷한 구조의 SQL 쿼리를 사용하여 데이터를 조작합니다.