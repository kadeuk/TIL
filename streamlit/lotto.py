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