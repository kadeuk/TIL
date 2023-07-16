# ORM
>Object-Relational-Mapping

[공식문서](https://docs.djangoproject.com/en/dev/topics/db/queries/#making-queries)

- ORM은 객체지향 프로그래밍 언어를 사용하여(Python) 호환되지 않는 유형 시스템 간에 데이터를 변환하는 프로그래밍 기술이다. 즉 객체와 데이터베이스의 테이블이나 SQL 쿼리 사이에 **다리** 역할을 한다.

#### ORM의 기능

1. 데이터 베이스 스키마 생성: Django는 파이썬의 클래스 정의를 사용해 데이터베이스 스키마를 자동으로 생산한다. 이 클래스들은 Django의 모델이며, 가모델은 데이터 베이스의 테이블에 해당한다.[[스키마]]
2. 데이터 베이스 추상화: Django의 ORM은 개발자가 SQL 쿼리를 작성하지 않고도 데이터 베이스 작업을 수행할 수 있게 해준다. 파이썬의 메서드와 속성을 사용해 데이터를 생성, 조회, 업데이트, 삭제(CRUD)할 수 있다. [[SQL쿼리]]
3. 데이터베이스 간 독립성: Django의 ORM은 다양한 종류의 데이터베이스 시스템에 **동일한 파이썬 코드를** 사용할 수 있게 해준다. 예를들어, 애플리케이션을 개발할때 SQLite를 사용하고, 배포할 때는 PostgreSQL로 전환할 수 있다.
---
Django ORM을 사용해 데이터베이스에서 모든 데이터를 가져오는 코드의 예시
```python
pythom manage.py shell

from burgers.models import Burger

# 데이터베이스에서 모든 정보를 가져오기
Burger.objects.all()
# 결과
<QuerySet [<Burger: 더블와퍼>, <Burger: 트러플머쉬룸X>, <Burger: 통새우와퍼>]>

# 데이터베이스에서 특정 조건을 만족하는 한개의 정보를  가져오기
Burger.objects.get(name="더블와퍼")
# 결과
<Burger: 더블와퍼>

# 데이터베이스에서 특정 조건을 만족하는 여러개의 정보를 가져오기
burgers = Burger.objects.filter(name__endswith="와퍼")
print(burgers)
#결과
<QuerySet [<Burger: 더블와퍼>, <Burger: 통새우와퍼>]>


```

- `all`은 모든객체 `.get`은 조건을 만족하는 객체 하나. `filter`는 조건을 만족하는 여러객체
---
- `filter`를 사용하면 Burger객체 대신 QuerySet 객체가 리턴된다. QuerySet은 리스트처럼 다룰수 있다.[[QuerySet]]
```python
>>> len(burgers)
2

>>> burgers[0]
<Burger: 더블와퍼>

```