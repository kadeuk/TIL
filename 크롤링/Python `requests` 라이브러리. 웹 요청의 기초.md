## Python `requests` 라이브러리: 웹 요청의 기초

웹 스크레이핑이나 API 호출 등, 웹과의 상호작용은 현대 프로그래밍에서 흔한 작업이다. Python에서는 `requests`라는 라이브러리를 통해 이러한 작업을 간단하게 수행할 수 있다. 이 글에서는 `requests`의 기본적인 사용법을 알아본다.

## `requests` 라이브러리란?

`requests`는 Python에서 HTTP 요청을 보내기 위한 라이브러리다. 간결한 API를 제공하여 웹 서비스와의 상호작용을 쉽게 만들어준다.

## 설치 방법

`requests`는 pip를 통해 쉽게 설치할 수 있다:
```python
pip install requests
```

## 기본적인 사용법

### GET 요청

웹 페이지의 내용을 가져오려면 GET 요청을 사용한다. `requests.get()` 함수를 사용하여 GET 요청을 보낼 수 있다.
```python
import requests

response = requests.get('https://www.example.com')
print(response.text)
```

### POST 요청

데이터를 서버에 보내려면 POST 요청을 사용한다. `requests.post()` 함수를 사용하여 POST 요청을 보낼 수 있다.
```python
data = {'key': 'value'}
response = requests.post('https://www.example.com', data=data)
print(response.text)
```

### 응답 객체

`requests` 함수는 응답 객체를 반환한다. 이 객체를 통해 응답 내용, 상태 코드, 헤더 등의 정보에 접근할 수 있다.

- `response.text`: 응답 내용
- `response.status_code`: 상태 코드
- `response.headers`: 헤더 정보

### 매개변수 전달

URL에 매개변수를 전달하려면 `params` 매개변수를 사용한다.
```python
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://www.example.com', params=params)
print(response.url)
```

### JSON 응답 처리

서버에서 JSON 형식의 응답을 받았을 때, `response.json()` 메서드를 사용하여 JSON 데이터를 파이썬 딕셔너리로 변환할 수 있다.
```python
response = requests.get('https://api.example.com/data')
data = response.json()
print(data['key'])
```

### 에러 처리

`requests`는 특정 상황에서 예외를 발생시킨다. 예를 들어, 요청이 타임아웃되면 `requests.exceptions.Timeout` 예외가 발생한다. 이러한 예외를 처리하여 안정적인 프로그램을 작성할 수 있다.
```python
try:
    response = requests.get('https://www.example.com', timeout=1)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("The request timed out")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
```