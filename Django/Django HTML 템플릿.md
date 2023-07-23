#### Django에서 HTML 템플릿은 웹 페이지의 레이아웃과 스타일, 그리고 그 페이지에서 보여질 내용을 어떻게 표현할 것인지를 정의하는 파일이다.

Django에서는 이 HTML 템플릿에 파이썬 변수를 사용해서 동적인 웹 페이지를 만들 수 있다.

예를 들어, 우리가 Django의 ListView를 사용해서 모든 `Post`객체를 가져와서 보여주고 싶다고 가정해보자.
이 때, ListView는 `object_list`라는 변수를 사용해 모든 객체를 HTML템플릿에 전달한다. 
```html
<h1>Post Lost</h1>

<ul>
	{% for post in object_list %}
		<li>
			<h2>{{ post.title }}</h2>
			<p>{{ post.content }}</p>
		</li>
	{% endfor %}
</ul>
```
- `{% for post in object_list %}`는 파이썬의 for loop와 비슷하게, `object_list`변수에 있는 각각의 `Post`객체를 `post`변수에 넣어서 반복문을 실행한다. 그래서 `{{ post.title }}`과 `{{ post.content }}`를 화면에 표시해준다.
- 먼저 만든 웹페이지를 사용자에게 보여줄려면 `URL 설정`을 해야한다. 그리고 나면,

이렇게 만들어진 웹 페이지는 사용자에게 이렇게 표시될 것이다.
```diff
Post List

- Title 1
  content 1

- Title 2
  content 2
```

---
#django #python [[Django에서의 클래스 상속]] [[Django URL 설정]]

