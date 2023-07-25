#### `ImageField` 
- `ImageField`는 Django의 모델 필드 중 하나로, 이미지 파일을 업로드 하고 저장하는 데 사용된다.
- `ImageField`는 파일 시스템에 이미지를 저장하고, 데이터 베이스에는 이 이미지 파일의 경로를 문자열로 저장한다.

다음의 간단한 Django모델에서 `ImageField`를 사용하는 방법이다.
```python
from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')
```

1. `MyModel`이라는 모델에 `image`라는 변수를 만들었고 그 변수에는 `ImageField`를 추가해 사용자가 웹사이트에 이미지를 업로드 할수 있게 했다.	
2. `upload_to = 'images'`: 업로드를 하면 `MEDIA_ROOT` 설정에 지정된 디렉토리 아래의 `images/` 디렉토리에 저장이 된다

#### `ImageField`는 여러 가지 추가 옵션을 가질 수 있다.

1. `blank=True`: Django 폼 및 입력 검증 수중에서 필드의 갑이 없을 수 있음을 의미한다. 기본값은 `False`다
2. `null=True`: 데이터베이스 수준에서 필드의 값이 없을 수 있음을 의미한다. 기본값은 `False`다
3. `height_field='image_height'`와 `width_field='image_width'`: 이미지의 크기를 자동으로 저장하고 관리하기 위한 옵션이다.

#### `height_field='image_height'`와 `width_field='image_width'`

1. 이미지의 크기 정보가 필요한 경우에만 이 옵션을 사용하면 된다.
2. 예를 들어, 웹사이트에서 이미지의 크기를 미리 알고 있으면 웹페이지를 더 빠르고 효율 적으로 렌더링할 수 있다.
	1. 그 이유는 웹 브라우저가 웹 페이지를 엔더링할 때, 각 요소의 크기와 위치를 알아야 레이아웃을 결정하고 페이지를 그릴수 있기 때문이다.
	2. 또 하나는 사용자가 올리는 이미지가 너무 큰 경우 적절한 크기로 축소한 버전을 제공해 데이터 사용량을 줄이거나, 렌더링 속도를 빠르게 하는 등의 최적화를 수행할 수 있다.
---
#django #python [[Model]] 