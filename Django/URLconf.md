Django에서 URLconf(URL configuration)는 URL과 뷰(view)를 매핑하는 일종의 테이블 또는 패턴 목록입니다. URLconf를 설정하면 Django는 웹 페이지 요청을 수신할 때 어떤 뷰 함수 또는 클래스를 호출해야 하는지를 알 수 있습니다.

URLconf는 각 Django 앱의 `urls.py` 파일에 정의되며, 프로젝트 전체를 아우르는 최상위 URLconf도 존재합니다. 일반적으로 각 Django 앱에는 자체 `urls.py` 파일이 있어 앱의 뷰를 구체적인 URL 패턴에 매핑하고, 프로젝트 전체의 URLconf에서는 각 앱의 URLconf를 포함(include)하여 전체 URL 체계를 관리합니다.

다음은 URLconf의 기본적인 예시입니다:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('goodbye/', views.goodbye, name='goodbye'),
]

```

위의 예시에서, `urlpatterns` 리스트는 URL 패턴과 이에 해당하는 뷰 함수를 `path()` 함수를 사용해 매핑합니다. 첫 번째 인자는 URL 패턴, 두 번째 인자는 해당 URL로 요청이 들어왔을 때 호출되는 뷰 함수입니다.

`name` 파라미터는 선택사항이며, 템플릿이나 뷰에서 이 URL 패턴을 참조할 때 사용할 수 있는 이름을 지정하는데 사용됩니다. 이를 통해 URL 자체를 하드코딩하지 않고도 URL 패턴을 참조하거나 수정할 수 있습니다.

따라서 URLconf는 Django 웹 애플리케이션에서 URL과 뷰가 어떻게 연결되는지를 정의하는 중요한 부분입니다.

---
#python #django #gpt [[View]]