import streamlit as st
import FinanceDataReader as fdr
import datetime
from bs4 import BeautifulSoup

# Finance Data Reader
# https://github.com/financedata-org/FinanceDataReader

date = st.date_input(
    "조회 시작일을 선택해 주세요",
    datetime.datetime(2022, 1, 1)
)

code = st.text_input(
    '종목코드', 
    value='',
    placeholder='종목코드를 입력해 주세요'
)

if code and date:
    df = fdr.DataReader(code, date)
    if 'Close' in df.columns:
        data = df.sort_index(ascending=True).loc[:, 'Close']
        st.line_chart(data)
    else:
        st.write("데이터에 'Close' 열이 없습니다.")
