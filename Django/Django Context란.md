```python
def post_list(request): 
	posts = Post.objects.all() 
	context = { 
		"posts" : posts,
		 } 
	return render(request, "post_list.html", context)
```

이 코드는 Django에서 웹 요청을 처리하는 뷰 함수를 정의하는 코드다.
사용자가 `posts`라는 페이지를 요청하면 뷰 함수를 실행해 글 목록을 보여주는 코드다.
1. 여기서 `context = { "posts" : posts, }`라는 코드는 `Post` 모델의 모든 객체를 데이터 베이스 에서 가져온다.
2. 윗줄에 보면 `posts = Post.objects.all()` 이라는 코드로 `Post`모델으 모든 객체를 `posts`라는 변수에 넣었고
3. `posts`라는 변수를 `context`라는 딕션너리로 묶어서 `"posts"`라는 키를 줬다.
4. 그 후에 `return render(request, "post_list.html", context)` render 함수는 주어진 템플릿과 `context`를  이용해 `html` 페이지를 생성하고 사용자에게 반환한다.

`post_list.html`파일에서는 이렇게 코딩한다.
```html
{% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
{% endfor %}
```
1. 이 코드는 `post_list.html`파일의 일부분이다. 
2. `{% for post in posts %}`: `context = { "posts" : posts, }` 의 키인 `"posts"`를 `post`에 넣어 반복문을 돌리고 있다. 
3. 그 후에 `post`의 `tilte`과 `content`를 화면에 표시해준다. 
4. `context = { "posts" : posts, }` 의 키인 `"posts"`를 반복문에 사용하면 `Post`의 모든 객체를 불러올수 있다. 
5. 이 반복문을 사용하기 위해 `context = { "posts" : posts, }` 라는 딕셔너리를 뷰에 정의해놓은 것이다.
6. 그 이유는 백엔드에서 처리한 데이터를 프론트엔드의 HTML 템플릿에 전달하고, 이를 통해 사용자에게 동적인 웹페이지를 제공할 수 있다.
7. `context`는 딕셔너리 형태로 데이터를 저장하고, 키는 템플릿에서 사용할 변수의 이름, 값은 그 변수에 연결될 실제 데이터를 의미한다.

- 이렇게 백엔드에서 프론트 엔드로 데이터를 전달하면, `HTML`템플릿은 이 데이터를 사용해 동적으로 웹페이지를 생성하고 사용자에게 보여줄 수 있다
- 이는 웹개발에 매우 중요한 과정으로, 사용자에게 개인화된 경험을 제공하거나 실시간 데이터를 표시하는 등 다양한 상황에서 활용된다.

---
#django #python [[View]] 