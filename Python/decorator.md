#python
[[logging]]
---
- **decorator(장식자)**란 복잡한 함수를 만들어놓고 다른함수에서 그 함수를 간편히 쓰기 위한것이다. 내가 이해하기에는 클래스와 비슷한데.클래스는 함수들의 묶음이고 패키지 같은 느낌이라면 장식자는 잠깐쓰는 드라이버 같은 느낌이다.
- 예로는 **logging** 모듈이나 **time** 같은 기능을 추가하고 싶을 때 활용할 수 있다.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

```
1. my_decorator(func): `my_decorator`라는 이름의 함수를 정의한다. 이 함수는 인자로 다른 함수를 받는다 `func`는 다른 함수를 말한다.
2. def wrapper(): `my_decorator` 내부에서 또 다른 함수 `wrapper`를 정의하고 있다. 이 함수가 실제로 실행되는 함수고 다른 함수들은 `@my_decorator`라는 함수 호출로 `wrapper`내의 함수를 사용할 수 있다.
3. func(): `my_decorator`함수를 호출한 다른 함수의 결과가 출력이 된다. `func()`는 다른 함수를 말한다.
4. @my_decorator: 다른 함수들은 `@my_decorator`라는 명령어로 장식자를 호출해서 쓸수 있다. 


