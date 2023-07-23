`Django HTML 템플릿` 포스트에서 `MyModelListView`를 `/posts/`라는 URL에 연결해서 사용자에게 보여주고 싶다면 URL 설정을 해야한다고 말했었다.

그 설정은 `urls.py` 파일에서 작성할 수 있다.
```python
from django.urls import path
from .views import MyModelListView

urlpatterns = [
	path('posts/', MyModelListView.as_view(), name='post-list'),
]
```

위 코드에서 `path`함수는 첫 번째 인자로 사용자가 들어오는 URL 패턴 주소를(`posts/`), 두번째 인자로 그 URL에 연결될 뷰(`MyMoselListView.as_view()`)를 받는다. 
따라서, 사용자가 `/posts/`라는 URL에 접속하면 `MyMoselListView`가 호출되어 `Post`객체들의 리스트를 보여주는 웹 페이지가 생성된다.
- `.as_view()`메서드는 클래스를 함수로 변환하는 메서드다. 
- 쉽게말해 사용자가 GET요청을 하면 `MyMoselListView`에서 `get()`메서드를, POST요청이 오면 `post()`메서드를 호출하게 된다. 
- `.as_view()`를 사용하지 않으면 `MyModelListView.get()`, `MyModelListView.post(),` `MymodelListView.put()`, `MyModelListView.delete()`등과 같은 메서드를 일일이 지정해줘야한다.
- 그러나 `.as_view()`메서드를 사용함으로써 사용자가 요청하는 HTTP 방식에 따라 적절한 메서드를 호출해준다.

---
#django #python [[Django에서의 클래스 상속]] [[Django HTML 템플릿]]
