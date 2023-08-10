1. **필요한 라이브러리 불러오기**

```python
import streamlit as st
import FinanceDataReader as fdr
import datetime
from bs4 import BeautifulSoup
```

Streamlit은 웹 애플리케이션을 간편하게 만들 수 있는 도구다. FinanceDataReader는 주식, 지수, 환율 등의 금융 데이터를 쉽게 가져올 수 있는 라이브러리다. datetime은 날짜와 시간을 다루는 데 사용되며, BeautifulSoup은 웹 스크래핑에 필요하다.

2. **사용자로부터 입력 받기**

```python
date = st.date_input(
    "조회 시작일을 선택해 주세요",
    datetime.datetime(2022, 1, 1)
)

code = st.text_input(
    '종목코드', 
    value='',
    placeholder='종목코드를 입력해 주세요'
)
```

Streamlit의 `st.date_input()` 함수는 사용자로부터 날짜를 입력받는다. `st.text_input()` 함수는 텍스트를 입력받는다. 여기서는 주식의 종목코드를 입력받는다.

3. **주식 데이터 가져오기 및 시각화하기**

```python
if code and date:
    df = fdr.DataReader(code, date)
    if 'Close' in df.columns:
        data = df.sort_index(ascending=True).loc[:, 'Close']
        st.line_chart(data)
    else:
        st.write("데이터에 'Close' 열이 없습니다.")
```

`fdr.DataReader()` 함수를 사용하면 주식 데이터를 가져올 수 있다. 가져온 데이터 중 'Close' 열만 선택하여 선 그래프로 그린다. 만약 'Close' 열이 없다면, 해당 메시지를 출력한다.



이렇게 Streamlit과 FinanceDataReader를 활용하면 웹에서 주식 데이터를 시각화하는 애플리케이션을 간단하게 만들 수 있다. 이 도구들을 사용하면 복잡한 웹 개발 지식 없이도 데이터 시각화 웹 앱을 구축할 수 있다.