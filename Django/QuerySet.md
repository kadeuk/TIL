#### GPT

Django에서 QuerySet은 데이터베이스로부터 데이터를 읽고, 필터링하고, 정렬하는 객체입니다.

QuerySet은 데이터베이스의 테이블에서 특정 조건에 맞는 레코드를 조회하거나 수정하거나 삭제할 수 있습니다.

QuerySet은 'lazy'인 특성이 있습니다. 이는 QuerySet이 실제로 평가되고 데이터베이스에 쿼리를 실행하는 시점이 필요한 시점까지 미뤄진다는 뜻입니다. 이 특성으로 인해 Django는 데이터베이스에 대한 쿼리 실행을 최적화할 수 있습니다.

예를 들어, Django 모델에서 QuerySet을 생성하는 코드는 다음과 같습니다:

```python
Copy code
# 모든 객체를 가져오는 QuerySet
all_objects = MyModel.objects.all()

# 특정 조건에 맞는 객체를 필터링하는 QuerySet
filtered_objects = MyModel.objects.filter(name='example')
```
---
위의 QuerySet들은 필요한 시점, 즉 QuerySet이 실제로 평가되어야 할 때까지 데이터베이스 쿼리를 실행하지 않습니다. 평가되는 시점은 예를 들어 len(filtered_objects), list(filtered_objects), for obj in filtered_objects: 등과 같은 상황이 될 수 있습니다.