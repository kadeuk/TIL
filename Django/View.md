Django에서 "뷰(view)"는 웹 애플리케이션에서 사용자에게 보여주는 웹 페이지의 내용을 결정하는 부분입니다. 보다 구체적으로 말하면, 뷰는 웹 요청을 받아서 그에 따른 응답을 반환하는 함수 또는 메서드를 말합니다.

Django에서 뷰는 크게 두 가지 형태로 사용됩니다:

1. **함수형 뷰(Function-Based Views, FBV)**: 이름에서 알 수 있듯이, 이는 함수를 이용해서 구현하는 뷰입니다. 각 함수는 특정한 URL 요청에 대한 응답을 생성하도록 설계됩니다. 이 방식은 뷰 로직이 비교적 간단한 경우에 적합하며, 코드가 단순하고 이해하기 쉽습니다. 예를 들면:
```python
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world!")

```

2. **클래스형 뷰(Class-Based Views, CBV)**: 이는 Python의 클래스를 활용해 뷰를 구현하는 방식입니다. 클래스를 이용하면 코드 재사용성을 높이고, 뷰 로직을 더 체계적으로 구조화할 수 있습니다. 복잡한 기능을 제공하는 웹 애플리케이션의 경우에 주로 사용됩니다. 예를 들면:
```python
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")

```

뷰를 만들었다면, 이를 URL과 연결하기 위해 `urls.py` 파일에서 URLConf를 설정해야 합니다. 이 과정을 통해 Django는 어떤 URL 요청이 들어왔을 때 어떤 뷰를 실행해야 하는지 알 수 있게 됩니다.

---
#python #django #gpt [[URLconf]]