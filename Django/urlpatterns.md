Django 웹 프레임워크에서, `urlpatterns`는 웹사이트의 페이지들을 나타내는 주소(URL)들을 저장하는 장소입니다.

예를 들어, 우리가 웹사이트에 '홈', '소개', '연락처' 페이지를 만들고 싶다고 가정해봅시다. 각 페이지는 그에 맞는 URL이 있어야 합니다. '홈' 페이지는 루트 URL (예: [www.mywebsite.com/)를](http://www.mywebsite.com/)%EB%A5%BC), '소개' 페이지는 [www.mywebsite.com/about/](http://www.mywebsite.com/about/), '연락처' 페이지는 [www.mywebsite.com/contact/](http://www.mywebsite.com/contact/) 같은 URL을 가질 수 있습니다.

이런 URL들을 `urlpatterns` 리스트 안에 정의를 합니다. 이때, 각 URL에 맞는 기능(뷰 함수)을 함께 지정해줍니다. 뷰 함수란, 해당 URL을 방문했을 때 보여줄 내용을 결정하는 함수입니다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 홈 페이지
    path('about/', views.about, name='about'), # 소개 페이지
    path('contact/', views.contact, name='contact'), # 연락처 페이지
]

```

이렇게 하면, 사용자가 [www.mywebsite.com/about/을](http://www.mywebsite.com/about/%EC%9D%84) 방문하면, Django는 이 URL이 `urlpatterns`에 정의된 'about/' URL 패턴과 일치하는지 확인하고, 일치하면 `views.about` 함수를 호출하여 사용자에게 보여줄 페이지를 만들어줍니다.

즉, `urlpatterns`는 우리가 만든 웹사이트의 각 페이지에 어떤 URL을 줄 것인지, 그리고 그 URL로 접속했을 때 어떤 내용을 보여줄 것인지를 결정하는 역할을 합니다.

---
#파이썬 #django #gpt 