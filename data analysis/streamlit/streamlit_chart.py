import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams['font.family'] = "Gulim"
plt.rcParams['axes.unicode_minus'] = False


data = pd.DataFrame({
    '이름': ['영식', '철수', '영희'],
    '나이': [22, 31, 23],
    '몸무게': [75.5, 80.2, 55.1]
})


st.dataframe(data, use_container_width=True)

# fig, ax = plt.subplots()
# ax.bar(data['이름'], data['나이'])
fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3, sharex=True,
                                    figsize=(12, 6))

width = 0.6  # the width of the bars: can also be len(x) sequence


fig, ax = plt.subplots()
bottom = np.zeros(3)


st.pyplot(fig)