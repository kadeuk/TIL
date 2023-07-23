### Django에서 클래스 상속이란, 한 클래스가 다른 클래스이 속성과 메서드를 가져와 사용하는것을 의미한다.

- Django에서 클래스 상송은 주로 뷰(View)와 모델(Model)에서 사용된다
- 예를들어, 기본 뷰 클래스인 `View`나 `TemplateView`, `ListView` 등은 모두 상속 받아 사용한다. 
- 이를 통해 개발자는 복잡한 기능을 더 쉽게 구현할 수 있다.
```python
from django.views.generic import ListView
from .models import MyModel

class MyModelListView(ListView):
    model = MyModel

```
- `from django.views.generic import ListView`: Django의 내장 클래스인 `ListView`를 임포트한다. `ListView`는 데이터베이스로부터 객체 목록을 가져와 템플릿에 던달하는 뷰를 만드는데 사용된다.
- `from .models import MyModel`: 현재 앱의 models.py 파일에서 `MyModel`이라는 모델을 입포트한다. 모델은 화면에 표시하려는 데이터의 종류를 나타낸다.
- `class MyModelListView(ListView)`: `ListView`를 상속받아 새로운 클래스인 `MyModelListView`를 생성한다.
- `model = MyModel`: `ListView`가 어떤 모델의 객체 목록을 가져와야 하는지를 지정한다. 여기서는 `MyModel`의 객체들을 가져온다.

이렇게 생성된 `MyModelListView`뷰는 MyModel의 모든 객체를 가져와 템플릿에 전달한다. 그리고 템플릿 이름은 자동으로 `<app>/<model>_list.html`형식으로 결정된다. 따라서 만약 MyModel이 `Post`라는 앱의 모델이었다면, `MyModelListView`는 `Post`모델의 모든 객체를 가져와 `post_list.html`이라는 템플릿에 전달하게 된다.

이렇게 우리는 `ListView`라는 클래스를 새로 만들필요없이, 이미 만들어진 Django의 내장 클래스를 상속받아. 더 쉽게 서비스를 구현할수 있다. 

코드의 결과를 완벽하게 이해하려면 HTML 템플릿 파일과 Django의 URL설정에 대한 이해가 필요하다. HTML템플릿은 데이터를 웹피이지로 표한하는 방법을 정의하고, URL설정은  특정 URL에 어떤 뷰를 연결할 것인지를 정의한다.
이 두가지는 웹 애플리케이션에서 뷰를 완성하고 사용자에게 보여주는 중요한 부분이다.

---
#django #python [[Django HTML 템플릿]]