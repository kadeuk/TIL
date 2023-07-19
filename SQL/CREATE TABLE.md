`CREATE TABLE`은 SQL에서 사용되는 문법 중 하나로, 새로운 테이블을 생성하는 데 사용됩니다.

다음은 기본적인 `CREATE TABLE` 문장의 구조입니다:
```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);

```
각 `column`은 열 이름을 나타내고, `datatype`은 해당 열의 데이터 유형을 나타냅니다.

예를 들어, 'Persons'라는 이름의 테이블을 생성하려는 경우 다음과 같이 작성할 수 있습니다:
```sql
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

```
이 예에서는 'Persons' 테이블을 생성하고, 테이블 내에는 `PersonID`, `LastName`, `FirstName`, `Address`, `City`라는 이름의 열을 생성합니다. 각 열의 데이터 유형은 `int` 또는 `varchar(255)`입니다.

이렇게 테이블을 생성한 후에는 `INSERT INTO` 명령을 사용하여 테이블에 데이터를 추가하거나, `SELECT` 명령을 사용하여 데이터를 조회할 수 있습니다.

---
#sql #gpt [[INSERT INTO]] [[AUTO_INCREMENT]] 
