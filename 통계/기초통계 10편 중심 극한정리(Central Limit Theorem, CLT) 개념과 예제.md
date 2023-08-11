중심 극한정리는 통계학의 핵심 원리 중 하나로, 여러 확률 변수의 합이나 평균이 정규 분포에 가까워진다는 것을 보여준다. 이 원리를 통해 실제 세상의 많은 현상들이 왜 정규 분포를 따르는지 이해할 수 있다.

### 중심 극한정리란?

중심 극한정리는 큰 표본의 특성에 관한 이론이다. 독립적이고 동일한 분포를 가진 여러 확률 변수의 합(또는 평균)이 표본의 크기가 커질수록 정규 분포에 가까워진다는 것을 의미한다.

### 중요성

많은 현상들이 정규 분포를 따르는 경향이 있는 이유는 여러 확률 변수들의 합이나 평균이 정규 분포를 따르기 때문이다. 통계학에서는 이 원리를 기반으로 많은 검정과 추정을 실시한다.

### 예제: 주사위 던지기

주사위를 한 번 던질 때, 나오는 숫자는 균등 분포를 따른다. 그런데 주사위를 여러 번 던져 나온 숫자들의 평균을 구하면 어떻게 될까?

1. 주사위를 10번 던져 나온 숫자의 평균을 구한다.
2. 이 과정을 1000번 반복한다.
3. 각 반복마다 구한 평균들의 분포를 그려본다.
```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 전역적으로 폰트를 설정한다
plt.rc('font', family='Gulim') 

# 주사위를 10번 던져 나온 숫자의 평균을 구하는 함수
def throw_dice(n=10):
    return np.mean(np.random.randint(1, 7, size=n))

# 주사위를 10번 던져 나온 숫자의 평균을 여러 번 반복하여 구하는 함수
def simulate_throws(repeats=1):
    return [throw_dice() for _ in range(repeats)]

repeat_counts = [1, 10, 100, 1000]
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

for idx, repeat in enumerate(repeat_counts):
    ax = axes[idx//2, idx%2]
    sample_means = simulate_throws(repeat)
    sns.histplot(sample_means, bins=30, kde=True, ax=ax)
    ax.set_title(f'주사위를 {repeat}번 던진 결과 그래프')
    ax.set_xlabel('평균')
    ax.set_ylabel('횟수')

plt.tight_layout()
plt.show()
```
## 코드결과
사진

위 그래프에서 볼 수 있듯이, 평균들의 분포는 정규 분포에 가까워진다. 주사위를 던지는 횟수(표본 크기)를 늘릴수록 이 분포는 더욱 정규 분포에 가까워진다.

### 마무리

중심 극한정리는 여러 확률 변수의 합이나 평균이 정규 분포에 가까워진다는 것을 보여주는 통계학의 기본적인 원리다. 이 원리를 통해 실제 세상의 많은 현상들이 왜 정규 분포를 따르는지 이해할 수 있다.