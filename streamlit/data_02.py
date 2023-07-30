import streamlit as st
import pandas as pd
import numpy as np

st. title('데이터프레임 튜토리얼')

dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})
# DataFrame 은 동적이라 오름차순 내림차순 정렬등이 되고
st.dataframe(dataframe, use_container_width=False)

# table 은 정적이다
st.table(dataframe)

# metric 온도는 붙여넣기 했다: °
st.metric(label='온도', value='10°C', delta="1.2°C")

# 컬럼으로 영역을 나누어 표시하기
col1, col2, col3 = st.columns(3)
col1.metric(label='달러USD', value='1,228 원', delta='-12.00 원')
col2.metric(label='일본JPY(100엔)', value='958.63 원', delta='-7.44 원')
col3.metric(label='유럽연합EUR', value='1,335.82 원', delta='11.44 원')