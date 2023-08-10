#### Streamlit 을 사용해 아주쉽게 lotto생성 사이트 만드는 방법을 알아보자

- 웹사이트를 하나 제작 하려면 아무리 쉬운 lotto생성 사이트라도 이것저것 손댈곳이 한두군데가 아니다.
- 그러나 `Streamlit`을 사용하면 아주쉽게 사이트를 구축할수 있다.
- 물론 귀여운것은 덤이다.

먼저, 필요한 라이브러리를 불러와야 한다. 파이썬의 표준 라이브러리인 `random`과 `datetime`, 그리고 웹 앱을 만드는 데 필요한 `streamlit` 라이브러리를 import한다.
```python
import streamlit as st
import random
import datetime
```

- 다음은 로또 번호를 생성하는 함수를 만드는 단계다. 
- 이 함수는 1부터 46까지의 숫자 중에서 무작위로 6개의 숫자를 뽑아 정렬한 후 반환한다. 
- 이 때, `set`을 사용하는 이유는 로또 번호가 중복되지 않아야 하기 때문이다.
```python
def generate_lotto():
    lotto = set()

    while len(lotto) <6:
        number = random.randint(1, 45)
        lotto.add(number)

    lotto_list = list(lotto)
    lotto_list.sort()
    return lotto_list
```
1. `generate_lotto`함수를 실행하면 `lotto`라는 변수를 만든다 `lotto`변수는 `set`을 사용해 중복이 없게 했다.
2. `while len(lotto) < 6`: `lotto`변수의 갯수를 세고 7미만 까지 실행한다. 
3. `number = random.randint(1, 46)`: `number`라는 변수에 1부터 45까지의 숫자를 랜덤하게 넣어준다
	-  `random`모듈의 `randint`를 사용한이유는
		1. `randint`함수는 두개의 인자를 받는다 최솟값과 최댓값이다.
		2. `randint`함수는 1이상 45이의 무작위 정수를 생성하라는 뜻이다.
		3. 이 함수는 모든 정수에 대해 균등한 확률을 갖는다. 즉, 1이 선택될 확률, 2가 선택될 확률, ..., 45이 선택될 확률은 모두 같다.
4. `lotto.add(number)`:`lotto`변수에 number를 추가 해준다
5. `lotto_list = list(lotto)`: `lotto`변수를 `list`로 만들어준다. 소트하기 위해서다.

그 다음, 웹 사이트의 제목을 설정한다. 스트림릿의 `title` 메서드를 사용하면 쉽게 제목을 설정할 수 있다.
```python
st.title(':sparkles:로또 생성기:sparkles:')
```

다음은 사용자에게 "당신의 이번주 행운의 번호"라는 메시지와 함께 생성 버튼을 제공하는 것이다. 
스트림릿의 `subheader`와 `button` 메서드를 사용해서 간단하게 구현할 수 있다.
```python
button = st.button('눌러서 번호를 생성하세요')
st.subheader('당신의 이번주 행운의 번호')
```
- `subheader`는 조금 작은 제목을 화면에 표시할 수 있다.

- 마지막으로, 사용자가 생성 버튼을 누르면 5개의 로또 번호 세트를 생성하고, 각 세트를 화면에 출력한다. 
- 이 때, 각 세트의 번호는 `generate_lotto` 함수를 호출하여 생성하고, 
- 스트림릿의 `subheader` 메서드를 사용해 화면에 출력한다. 
- 또한, `datetime` 라이브러리의 `now` 함수와 `strftime` 메서드를 사용해 번호가 생성된 시간도 함께 출력한다.
```python
if button:
    for i in range(1, 6):
        st.subheader(f'{i}. 로또 번호: :green[{generate_lotto()}]')
    st.write(f'만든 시간: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}')
```
이렇게 하면 간단한 로또 번호 생성기 웹 사이트가 완성이 된다.

- 하지만 조금 부족하다. 이 웹사이트는 사용자가 버튼을 누르면 무조건 5벌의 로또번호를 생성해준다.
- 만약 사용자가 원하는 만큼의 로또번호 셋트를 생성하는 웹사이트를 만들려면 어떻게 해야할까?
간단히 수정이 가능하다.
```python
import streamlit as st
import random
import datetime

st.title(':sparkles:로또 생성기:sparkles:')

def generate_lotto():
    lotto = set()

    while len(lotto) <6:
        number = random.randint(1, 46)
        lotto.add(number)

    lotto_list = list(lotto)
    lotto_list.sort()
    return lotto_list

num_sets = st.number_input('생성할 로또 번호 세트의 개수를 입력하세요', min_value=1, value=5)

button = st.button('눌러서 번호를 생성하세요')

st.subheader('당신의 이번주 행운의 번호')

if button:
    for i in range(1, num_sets+1):
        st.subheader(f'{i}. 로또 번호: :green[{generate_lotto()}]')
    st.write(f'만든 시간: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}')
```
- 18번 행을 추가하고 25번행을 수정했다.
- `num_sets = st.number_input('생성할 로또 번호 세트의 개수를 입력하세요', min_value=1, value=5)`
	- `Streamlit`의 `number_input`을 이용하면 사용자가 숫자를 입력할 수 있게된다. 그 결과를 `num_sets`변수에 넣었다.
- `for i in range(1, num_sets+1)`:`num_sets`변수에 1을 더해 사용자가 입력한 숫자까지 로또 번호를 생성하게 했다.

이 전체 코드를 vscode에 붙여넣고 `streamlit run filename`을 사용해 실행해보자 귀엽고 훌륭한 사이트가 금방 만들어진다.
