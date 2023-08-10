- 데이터 분석을 위한 웹 애플리케이션을 만들 때, 
- 사용자로부터 데이터 파일을 업로드 받아 해당 데이터를 웹 페이지에 표시하는 기능은 매우 중요하다. 
- Streamlit은 이러한 기능을 간단하게 구현할 수 있게 도와주는 도구다. 
- 이번 글에서는 Streamlit을 활용하여 사용자로부터 CSV나 Excel 파일을 업로드 받아 
- 데이터프레임으로 출력하는 방법에 대해 알아보자.
```python
import streamlit as st
import pandas as pd
import time

file = st.file_uploader('파일 선택 (csv or excel)', type = ['csv', 'xls', 'xlsx'])

time.sleep(2)

if file is not None:
    ext = file.name.split('.')[-1]
    if ext == 'csv':
        df = pd.read_csv(file)
        st.dataframe(df)
    elif 'xls' in ext:
        df = pd.read_excel(file, engine='openpyxl')
        st.dataframe(df)
```

### 1. 파일 업로더 생성하기

Streamlit의 `file_uploader` 함수를 사용하면 웹 페이지에 파일 업로드 위젯을 생성할 수 있다.

```python
file = st.file_uploader('파일 선택 (csv or excel)', type = ['csv', 'xls', 'xlsx'])
```

위 코드는 CSV, XLS, XLSX 형식의 파일만 업로드 받을 수 있도록 설정한다.

### 2. 파일 확장자에 따른 데이터 로드

업로드된 파일의 확장자를 확인하여, 해당 확장자에 맞는 Pandas 함수를 사용하여 데이터를 로드한다

```python
if file is not None:
    ext = file.name.split('.')[-1]
    if ext == 'csv':
        df = pd.read_csv(file)
    elif 'xls' in ext:
        df = pd.read_excel(file, engine='openpyxl')
```

CSV 파일의 경우 `pd.read_csv()` 함수를, Excel 파일의 경우 `pd.read_excel()` 함수를 사용한다. Excel 파일을 로드할 때 `engine='openpyxl'` 옵션을 사용하는 것은 최신 버전의 Pandas에서 XLSX 파일을 읽을 때 필요하다.

### 3. 데이터프레임 출력하기

로드된 데이터프레임은 Streamlit의 `dataframe` 함수를 사용하여 웹 페이지에 출력한다.

```python
st.dataframe(df)
```

