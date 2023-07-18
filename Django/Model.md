Django에서, 모델은 데이터베이스에서 사용할 데이터의 구조를 정의하는 것입니다. 간단히 말하자면, 모델은 애플리케이션의 데이터를 표현하는 파이썬 클래스입니다. 각 모델은 Django ORM을 통해 데이터베이스 테이블에 매핑되며, 모델의 속성(attributes)은 테이블의 필드를 나타냅니다.

모델을 정의하는 방법은 간단합니다. `models.Model`을 상속하는 파이썬 클래스를 만드는 것입니다. 클래스의 각 속성은 데이터베이스 필드를 나타내는 객체를 인스턴스화하는 `Field` 클래스입니다.

다음은 간단한 `BlogPost` 모델의 예입니다.

```python
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

```

이 예제에서, `BlogPost` 모델은 세 가지 필드를 가집니다: `title`, `content`, `pub_date`. 이들은 각각 `CharField`, `TextField`, `DateTimeField`의 인스턴스입니다.

- `CharField`: 문자열 필드로, `max_length` 파라미터를 필요로 합니다.
- `TextField`: 큰 문자열 필드로, 일반적으로 긴 텍스트를 저장하는 데 사용됩니다.
- `DateTimeField`: 날짜와 시간 필드로, `auto_now_add=True` 옵션을 사용하면, 레코드가 생성될 때 자동으로 현재 시간을 설정합니다.

Django는 이 모델을 사용하여 데이터베이스 스키마를 자동으로 생성하며, 이 모델을 사용하여 데이터베이스에 쿼리를 생성하고 데이터를 저장하거나 검색할 수 있습니다.

또한, Django 모델은 메서드를 포함할 수 있습니다. 이를 통해 데이터의 복잡한 동작이나 연산을 캡슐화하고 재사용할 수 있습니다.

---
#django #python #gpt [[ORM]]