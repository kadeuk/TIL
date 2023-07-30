import streamlit as st

st.title('이게 타이틀')

# 이모지 ':' 콜론 옆에 붙여서 써야 된다. 주의!
st.title('스마일:sunglasses:')
st.title('커피:coffee:')

st.header('헤더를 입력:sparkles:')

# h2같은 서브헤더
st.subheader('이것은 subheader 입니다.')

# 캡션
st.caption('캡션넣기')

# 코드표시
sample_code = '''
def function():
    print('hello, world')

'''
st.code(sample_code, language="python")

# 일반 텍스트
st.text('일반 텍스트')

# 마크다운 컬러 5가지 지원 blue, green, orange, red, violet
st.markdown('텍스트의 색상을 :green[초록색]')
st.markdown('텍스트의 강조와 색상은 **:red[빨강]**')