- Streamlit과 FinanceDataReader를 활용하면 주식 데이터를 시각화하는 웹 애플리케이션을 간편하게 만들 수 있다. 
- 이번 포스트에서는 이 두 라이브러리를 활용하여 주식 차트 검색 웹 앱을 만드는 방법을 소개한다.

#### 1. 필요한 라이브러리 불러오기

```python
import streamlit as st
import FinanceDataReader as fdr
import datetime
import time
```

- `streamlit`: 웹 애플리케이션을 만들기 위한 주요 라이브러리다.
- `FinanceDataReader`: 주식, 지수, 환율 등의 금융 데이터를 쉽게 가져올 수 있는 라이브러리다.
- `datetime`: 날짜와 시간을 다루는 데 사용되는 라이브러리다.
- `time`: 시간 관련 기능을 제공하는 라이브러리다.

#### 2. 웹 앱의 제목 설정

```python
st.title('국내외 주식 차트 검색')
```

웹 앱의 상단에 "국내외 주식 차트 검색"이라는 제목을 표시한다.

#### 3. 사이드바에 사용자 입력 위젯 추가

```python
with st.sidebar:
    start_date = st.date_input(
        "조회 시작일을 선택해 주세요",
        datetime.datetime(2022, 1, 1)
    )

    stock_code = st.text_input(
        '종목코드', 
        value='',
        placeholder='종목코드를 입력해 주세요'
    )
```

사이드바에 날짜 입력 위젯과 텍스트 입력 위젯을 추가한다. 사용자는 이를 통해 조회 시작일과 종목코드를 입력할 수 있다.

#### 4. 주식 데이터 가져오기 및 표시

```python
if stock_code and start_date:
    stock_data = fdr.DataReader(stock_code, start_date)
    chart_data = stock_data.sort_index(ascending=True).loc[:, 'Close']

    chart_tab, data_tab = st.tabs(['차트', '데이터'])

    with chart_tab:    
        st.line_chart(chart_data)

    with data_tab:
        st.dataframe(stock_data.sort_index(ascending=False))
```

입력받은 종목코드와 시작일을 기반으로 주식 데이터를 가져온다. 가져온 데이터를 차트와 데이터프레임 형태로 각각 표시한다.

#### 5. 데이터 컬럼 설명 추가

```python
with st.expander('컬럼 설명'):
    st.markdown('''
    - Open: 시가
    - High: 고가
    - Low: 저가
    - Close: 종가
    - Adj Close: 수정 종가
    - Volumn: 거래량
    ''')
```

expander를 사용하여 주식 데이터의 각 컬럼에 대한 설명을 제공한다.