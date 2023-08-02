Selenium은 웹 애플리케이션을 자동화하는 데 사용되는 프레임워크로, 
웹 브라우저를 제어하고 웹 페이지를 조작하여 웹 크롤링, 웹 테스팅 등 다양한 작업을 자동으로 수행할 수 있다. 이제 Selenium에서 가장 많이 사용되는 함수들을 하나씩 알아보자.

1. get(): 웹 페이지로 이동하기
- `get()` 함수는 지정된 URL로 웹 브라우저를 이동하는 역할을 한다. 웹 페이지를 방문하고 해당 페이지의 정보를 가져오려면 먼저 해당 페이지로 이동해야 한다.
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.example.com')
```

2. find_element_by_XXX(): 웹 요소 찾기
- `find_element_by_XXX()` 함수들은 웹 페이지에서 원하는 요소를 찾는 데 사용된다. XXX 부분에는 다양한 선택자(Selector)가 들어갈 수 있으며, ID, 클래스 이름, 태그 이름 등을 이용해 원하는 요소를 찾을 수 있다.
```python
from selenium import webdriver

driver = webdriver.Chrome()
element = driver.find_element_by_id('search-box')
```

3. click(): 요소 클릭하기
- `click()` 함수는 지정된 요소를 클릭하는 역할을 한다. 웹 페이지에서 버튼을 누르거나 링크를 클릭하고자 할 때 사용한다.
```python
from selenium import webdriver

driver = webdriver.Chrome()
button = driver.find_element_by_id('submit-button')
button.click()
```

4. send_keys(): 입력 요소에 텍스트 입력하기
- `send_keys()` 함수는 입력 요소에 텍스트를 입력하는 역할을 한다. 웹 페이지의 검색창이나 로그인 폼에 텍스트를 입력하고 싶을 때 사용된다.
```python
from selenium import webdriver

driver = webdriver.Chrome()
search_box = driver.find_element_by_id('search-box')
search_box.send_keys('안녕, 세상!')
```

5.wait(): 조건에 따라 대기하기
- `wait()` 함수는 특정 조건이 충족될 때까지 대기하는 역할을 한다. 웹 페이지가 로딩되기를 기다리거나, 특정 요소가 나타날 때까지 대기하는 데 사용된다.
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.example.com')
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'search-box')))
```

6. `back()`: 뒤로가기 버튼 클릭, `forward()`: 앞으로가기 버튼 클릭, `refresh()`: 새로고침 버튼 클릭
```python
driver.get('https://www.naver.com')
time.sleep(1)
driver.get('https://google.com')

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)
print('동작끝')
input()
```

7. `title`:웹사이트의 `title`을 가져온다. `current_url`: 웹사이트의 `url`을 가져온다.
```python
driver.get('https://www.naver.com')
time.sleep(1)

title = driver.title
print(title, '가 타이틀이다')

now_addrese = driver.current_url
print(now_addrese, '가 현재주소다')
input()

결과
NAVER 가 타이틀이다
https://www.naver.com/ 가 현재주소다
```