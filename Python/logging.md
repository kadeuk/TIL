#파이썬
#decorator
[[decorator]]
---
- 함수의 `log`기능은 함수의 싱행 과정에서 발행하는 정보를 기록하는것이다. 
- 함수의 입력값, 결과값, 에러의 이유등의 정보를 포함할 수 있다.
- 로그를 사용하면 함수의 실행과정을 더 잘 이해할 수 있고, 에러가 발생했을 때 문제를 더 쉽게 진단하고 수정할 수 있다.

#### `logging`모듈의 사용예시
```python
import logging

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} 함수가 {args}와 {kwargs}를 입력으로 실행되었습니다.")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} 함수가 {result}를 반환하였습니다.")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

logging.basicConfig(level=logging.INFO)  # 로깅 레벨을 설정 한다.
add(1, 2)

INFO:root:add 함수가 (1, 2)와 {}를 입력으로 실행되었습니다.
INFO:root:add 함수가 3를 반환하였습니다.


```
1. basicConfig: 로깅 시스템의 기본 설정을 정의한다. `lovel` 매개변수는 로깅의 중요도 수준을 설정하는 데 사용된다.
2. logging.INFO: 모든 로그 메시지를 수집하지만 중요도가 낮은 (예를 들어 디버깅 목적으로만 사용되는)메시지는 무시하는 레벨
---
#### 파이썬에서 사용할 수 있는 주요 로깅레벨.`대문자주의`
- `DEBUG`: 가장 상세한 정보를 제공. 상세한 디버깅 작업에만 필요.
- `INFO`: 프로그램의 일반적인 진행 상황에 대한 확인 정보 제공
- `WARNING`: 예상치 못한 일이 발생했거나 문제가 발생할 가능성이 있는 상황에 대한 정보를 제공
- `ERROR`: 더 심각한 문제로, 프로그램이 특정 함수를 수행하지 못했음을 나타낸다.
- `CRITICAL`: 가장 심각한 오류. 프로그램이 수행을 계속할 수 없음을 나타낸다.

`logging.basicConfig(level=logging.INFO)`를 호출하면, `INFO`레벨과 그 이상의 로그(예: `WARNINNG`, `ERROR`, `CRITICAL`)가 출력된다.