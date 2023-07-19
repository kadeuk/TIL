`INSERT INTO`는 SQL 문에서 사용하는 구문 중 하나로, 데이터를 테이블에 삽입하는 데 사용됩니다.

기본적인 `INSERT INTO` 문의 구조는 다음과 같습니다:
```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

```
여기서 `table_name`은 데이터가 삽입될 테이블의 이름이며, `column1, column2, column3, ...`는 데이터가 삽입될 테이블의 열(column) 이름입니다. `value1, value2, value3, ...`는 각 열에 삽입될 값입니다.

예를 들어, 위에서 생성한 'Persons' 테이블에 데이터를 삽입하려면 다음과 같이 작성할 수 있습니다:
```sql
INSERT INTO Persons (PersonID, LastName, FirstName, Address, City)
VALUES (1, 'Smith', 'John', '123 Elm Street', 'Anytown');

```

모든 열에 값을 삽입하려는 경우, 열 이름을 생략하고 다음과 같이 작성할 수도 있습니다:
```sql
INSERT INTO table_name
VALUES (value1, value2, value3, ...);

```

이 경우, `VALUES` 절에 제공하는 값의 순서와 개수는 테이블의 열 순서와 개수와 일치해야 합니다

---
#sql #gpt [[CREATE TABLE]] [[AUTO_INCREMENT]]