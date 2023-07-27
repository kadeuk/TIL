#### `Input`태그는 웹페이지에서 사용자 입력을 받는데 사용된다.

기본 모양은 이렇게 생겼다.
```html
<input type="text">
```

- 보통 `form`태그 안에서 사용된다.
- `input`태그에는 여러가지 속성이 있다. 속성에 따라 사용자에게 다른 입력값을 받을 수 있다.

#### `Input`태그의 속성

1. `value`: 만약 사용자가 id를 입력하는 창이 있다면 그 창에  미리 개발자가 정한 글자가 쓰여져 있게 하는 태그다. 
```html
<input type="text" name="username" value="John Doe">
```
- 이 경워 사용자가 이름을 입력하는 곳에 `John Doe`라는 이름이 쓰여있어고 사용자는 이 값을 사용할 수도 있고 다른 값을 입력 할 수도 있다.. 즉 입력 필드의 초기값을 설정한다.
- 만약 `type`속성이 `chekbox`나 `radio`로 설정된 경우, `value`속성은 사용자가 해당 체크박사나 라이오 버튼을 선택하고 폼을 제출했을 때 서버로 전송되는 데이터의 값을 결정한다.
- 예를 들어, 사용자에게 좋아하는 과일을 선택하게 하는 체크박스가 있다고 가정해보자. 각 체크박스 항목에 `value`를 지정하면, 사용자가 체크한 항목들이 서버로 전송될 때 그 `value`가 전송된다.
```html
<form action="submit_form" method="POST">
    <input type="checkbox" name="fruit" value="apple"> Apple <br>
    <input type="checkbox" name="fruit" value="banana"> Banana <br>
    <input type="checkbox" name="fruit" value="cherry"> Cherry <br>
    <input type="submit" value="Submit">
</form>
```
- 이 예제에서 사용자가 Apple과 Cherry 체크박스를 선택하고 Submit 버튼을 누르면, 서버로 전송되는 데이터에는 `"fruit=apple&fruit=cherry"`가 포함된다.

2. `name`: 폼 데이터가 서버로 전송될 때 사용되는 키값이다. 서버는 딕셔너리 형태로 데이터를 저장하는데 `value`나 사용자가 입력한 값이 `키 : 값`의 '값'이라면 `name`은 '키'다. 나중에 사용자가 `GET`요청을 하면 이 '키' 값에 맞는 데이터를 서버는 사용자에게 주게된다.
```html
<input type="text" name="email">
```
- 이 데이터에 사용자가 입력을 하면 `email:abc@gmail.com`으로 서버에 데이터가 전달이 된다.

3. `disabled`: 이 속성은 특정 상황에서 사용자가 입력 필드와 상호 작용하지 못하게 막는데 사용된다. 
- 예를 들어, 특정 조건이 충족되지 않으면 사용자가 입력 필드를 사용하도록 허용하지 않는 상황이 있을수 있다.
- "약관 동의" 체크박스를 체크하지 않으면 "제출"버튼을 비활성하여 사용자가 양식을 제출하는 것을 방지할 수 있다.
```html
<input type="text" id="username" name="username" disabled>
```

4.`readonly`: 이 속성은 HTML 입력 필드를 읽기 전용으로 만든다.
- 이 속성이 설정되면 사용자는 필드의 값을 변경할 수 없다.
- 예를 들어, 사용자가 주문한 상품의 총 가격을 표시하는 필드는 사용자가 수정하면 안 되므로 `readonly`로 설정할 수 있다.
- 사용자가 주문하기 버튼을 누르면 총 가격이 서버로 전송된다.
```html
<input type="text" id="total_price" name="total_price" value="100" readonly>
```

5. `required`: 이 속성이 설정된 필드는 사용자가 반드시 값을 입력한 후에 제출을 할 수 있다.
- 예를 들어, 이메일 주소나 암호와 같이 필수적으로 필요한 정보를 수집하는 폼 필드에 `required`속성의 사용하면, 사용자가 이 필드를 비워 둔 채로 폼을 제출하는 것을 방지할 수 있다.
``` html
<form action="/submit_form" method="post">
	<label for="email">Email:</label>
	<input type="email" id="email" name="email" required>
	<input type="submit" value="Submit">
</form>
```

6. `placeholder`: 입력 필드에 아직 아무런 값이 입력되지 않았을 때 나타나는 텍스트다. 
- 희미하게 보여지고 사용자에게 입력 예상값의 힌트를 준다.
```html
<input type="text" name="email" placeholder="example@domain.com">
```
- 사용자가 입력하는 이메일 창에 희미하게 `example@domail.com`이라고 쓰여있고 사용자가 입력을 시작하면 사라진다.

7. `maxlength`: 입력 필드에 입력할 수 있는 최대 문자 수를 설정한다.
```html
<input type="text" maxlength="10">
```
- 최대 10글자를 입력할 수있다.

8. `autocomplete`: 입력 필드에 값을 자동으로 채우는 기능을 제어한다.
- 이메일 같은 경우는 전에 입력한 값을 브라우저가 기억했다가 자동으로 입력을 해주면 편할것이다.
- 하지만 패스워드 같은 경우는 자동으로 입력할 시 보안에 문제가 된다.
```html
<from action="/submit" method="post">
	<label for="email">Email:</label><br>
	<input type="email" id="email" name="email" autocomplete="on"><br>
	<label for="pwd">Password:</label><br>
	<input type="password" id="pwd" name="pwd" autocomplete="off"><br>
	<input type="submit" value="Submit">
</from>
```
- 이메일 입력 필드는 자동완성이 `on` 이되어있고. 패스워드 입력필드는 `off` 가 되어있다.

9. `autofocus`: 페이지가 로드될때 사용자가 클릭하지 않아도 자동으로 입력할 곳에 커서가 위치하게 도와주는 속성이다.
- 이 속성은 하나의 페이지에서 한번만 사용할 수있고. 여러번 사용하면 처음 사용한 곳에만 커서가 위치하게 된다.
```html
<form action="/submit" method="post">
	<label for="email">Email:</label><br>
	<input type="email" id="email" name="email" autofocus><br>
	<label for="pwd">Password:</label><br>
	<input type="password" id="pwd" name="pwd"><br>
	<input type="submit" value="Submit">
</form>
```
- 이메일 입력 필드에 `autofocus`속성이 설정되어 있으므로 , 페이지가 로드되면 바로 이메일을 입력할 수 있다.

10. `pattern`: 속성은 입력 필드에 사용자가 입력한 값이 해당 정규식 패턴에 맞는지 확인하는데 사용된다.
- 정규식 표현식은 매우 강력하며 복잡한 패턴을 표현하는데 사용할 수 있지만, 직접 작성하기는 어렵다.
- 필요에 따라 적절한 정규 표현식을 찾아서 사용하는 것이 중요하다.
- 개발자가 입력한 정규 표현식에 맞지 않는다면 브라우저는 경고 메시지를 표시하고 제출을 막는다
- 이 코드는 이메일을 입력하는 정규 표현식이다.
```html
<form action="">
  <label for="email">Email:</label><br>
  <input type="text" id="email" name="email" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$" required>
  <input type="submit" value="Submit">
</form>
```

---
#html #django 