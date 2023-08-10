import streamlit as st
import FinanceDataReader as fdr
import datetime
import time

# Finance Data Reader
# https://github.com/financedata-org/FinanceDataReader

st.title('국내외 주식 차트 검색')

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

if stock_code and start_date:
    stock_data = fdr.DataReader(stock_code, start_date)
    chart_data = stock_data.sort_index(ascending=True).loc[:, 'Close']

    chart_tab, data_tab = st.tabs(['차트', '데이터'])

    with chart_tab:    
        st.line_chart(chart_data)

    with data_tab:
        st.dataframe(stock_data.sort_index(ascending=False))
        
    with st.expander('컬럼 설명'):
        st.markdown('''
        - Open: 시가
        - High: 고가
        - Low: 저가
        - Close: 종가
        - Adj Close: 수정 종가
        - Volumn: 거래량
        ''')