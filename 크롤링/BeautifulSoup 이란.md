#### BeautifulSoup는 HTML과 XML 문서를 파싱하기 위한 라이브러리로, 웹 페이지의 복잡한 구조를 쉽게 분석해서 원하는 정보를 찾아낼 수 있다.
- 이번 포스팅에서는 간단히 `BeautifulSoup`의 사용법에 대해 알아보자

#### Beautifulsoup 사용법
- 먼저 BeautifulSoup를 설치해야 한다.
```python
pip install beautifulsoup4
```

- 이제 BeautifulSoup 객체를 만들어 보자. 이 객체로 HTML 문서 전체를 다룰 수 있다.
```python
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
```

- 그럼 이제 HTML 문서의 태그에 쉽게 접근할 수 있다. `soup.title` 같은 코드로 원하는 태그를 찾을 수 있다.
```python
print(soup.title)  # <title>The Dormouse's story</title>
```

- 여러 개의 태그를 찾으려면 어떻게 해야 할까? `soup.find_all()` 메서드로 쉽게 해결할 수 있다.
```python
print(soup.find('p').b)  # <b>The Dormouse's story</b>
```

- 이렇게 찾은 요소를 더 분석하려면 어떻게 해야 할까? 그냥 계속 접근하면 된다. 예를 들어, `soup.find('p').b`를 사용하면 원하는 부분을 쉽게 찾을 수 있다.
```python
print(soup.find('p').b)  # <b>The Dormouse's story</b>
```

- BeautifulSoup는 이처럼 웹 페이지를 분석하고 원하는 정보를 추출하는 데 매우 편리하다. 웹 스크래핑 작업을 할 때 매우 유용하게 사용될 수 있다.
- 앞으로 BeautifulSoup에 관해 계속 포스팅을 할 예정이다.

--- 
#크롤링 #python 