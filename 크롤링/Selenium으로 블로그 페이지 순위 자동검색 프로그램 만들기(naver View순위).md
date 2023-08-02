#### Selenium으로 검색어를 입력시 내 블로그의 페이지가 네이버 사이트의 view탭에서 몇위에 있는지 자동으로 알아내는 프로그램을 만들어보자
1. 먼저 라이브러리를 `import`하자
```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
```
여기서 `WebDriverWait`는 사용을 하지 않지만 습관적으로 이 다섯가지를 `import`하는 습관을 가지자.

2. `Chrome WebDriver`는 가장 오류가 많다. 각자의 크롬 버전이 다르기 때문인데 이걸 쉽게 해주는 코드가 있다.
```python
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
```
- `chromedriver_autoinstaller`sms Chrome브라우저와 호환되는 적절한 버전의 WebDriver를 자동으로 설치하는 라이브러리다. 
- 이 라이브러리를 사용하면 사용자가 직접 `WebDriver`를 다운로드하고 설치할 필요가 없다.
- `driver`라는 변수에 넣어줬다. 쉽게말하면 자동화 프로그램을 실행하는 직원 이름이라고 봐도된다.
- 이 직원은 시장에 가서 장을본다. 크롬이라는 웹 브라우저 시장에서 우리가 시키는 일을 할 것이다.

3. 제어할 웹 브라우저 선택
```python
driver = webdriver.Chrome()
```
- 제어할 웹 브라우저로 크롬을 선택했고 `driver`라는 변수를 만들어서 `Chrome WebDriver`객체를 생성했다.

4. 검색학 키워드 및 블로그
```python
searchqs = ['파이썬 셀레니움', '파이썬 플라스크']
target_blog_links = ['https://www.sagein.net/708', 'https://yeko90.tistory.com/252']
```
- 검색할 키워드를 `searchqs`라는 변수에 리스트 형태로 넣었다.
- 검색할 블로그 페이지 주소를 `target_blog_links`라는 변수에 리스트 형태로 넣었다.
- 키워드와 블로그는 계속 변경될수 있다.

5. 리스트들을 순서대로 짝지어 주는 반복문
```python
for searchq, target_blog_link in zip(searchqs, target_blog_links):
```
- `zip()` 함수를 사용하여 `searchqs`와 `target_blog_links` 리스트들을 순서대로 짝지어주는 반복문이다. 
- `searchq`와 `target_blog_link`에는 각각 키워드와 해당 키워드에 대응하는 블로그 링크가 대입된다.

6. 네이버 페이지에 접속
```python
search_link = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={searchq}'
driver.get(search_link)
time.sleep(2)
```
- 네이버에서 '파이썬 플라스크'라고 수동으로검색후 view탭으로 이동해 주소를 보자
- https://search.naver.com/search.naver?where=view&sm=tab_jum&query=파이썬+플라스크
- 이와같이 되어있는데 자세히 보면 맨뒤에`query=파이썬+플라스크`라고 되어있다 이부분은 `query=파이썬 플라스크`라고 바꿔도 똑같이 검색이 된다. 
- 이 부분에 `searchq`에 들어가있는 값(파이썬 플라스크)을 넣어주고 그 주소를 `search_link`라는 변수에 넣어준다.
- 여기서는 f스트링을 사용했다.
- `driver.get(search_link):`그리고 그 주소를 방문하는 코드다.
- time.sleep(2): 2초를 쉬어준다.

7. CSS선택자 생성.
```python
link_selector = f'a[href^="{target_blog_link}"]'
```
- f스트링을 사용한다.
- `href^="{target_blog_link}`: `target_blog_link`변수에 들어갔는 값을 가진 `href`를 찾는다.
- ` f'a[href^="{target_blog_link}"]'`: `target_blog_link`변수에 들어갔는 값을 가진 `href`를 가진 `a`태그를 찾는다.
- 마지막으로 찾은 `a`태그를 `link_selector`변수에 넣는다

8. 현재 랭크 변수를 -1로 설정
```python
nowlank = -1
```
- 생각보다 이 부분은 중요한다. 만약 내 블로그 페이지가 '파이썬 플라스크'라는 검색어로 검색했을때 
- 나오지 않는다면 화면에 -1이라고 표시해준다.

9. 예외처리를 위해 변수 `BLOG_FOUND`로 초기화한다.
```python
BLOG_FOUND = False
``` 

10. 예외 처리 무한 반복문
```python
try:
    element = driver.find_element(By.CSS_SELECTOR, link_selector)
    while True:
        new_element = element.find_element(By.XPATH, "./..")
        nowlank = new_element.get_attribute("data-cr-rank")
        if nowlank != None:
            BLOG_FOUND = True
            break
        element = new_element
    if BLOG_FOUND:
        break
except:
    print('타겟 블로그를 못찾음 --> 스크롤 하겠습니다.')
    driver.execute_script('window.scrollBy(0, 10000);')
    time.sleep(3)
```
- `try`와 `except`는 예외처리를 위한 구문이다. 
- `element = driver.find_element(By.CSS_SELECTOR, link_selector)`: 아까 찾은 `link_selector`변수에 담긴 값을 찾아 `element`라는 변수에 넣어준다. `driver.find_element`는 `driver`라는 직원이 무엇을 찾을지 알려준다. 여기서는 `By.CSS_SELECTOR`라는 명령으로 CSS 선택자에 해당하는 요소를 찾게했다. 이 요소는 검색 결과 페이지에서 특정 블로그 링크를 나타낸다.
- `new_element = element.find_element(By.XPATH, "./..")`:`element` 변수에서 부모요소를 찾아 `new_element` 변수에 넣어준다.
- `./..`은 consol에서 사용하는 명령어와 같다. 현재 디렉토리보다 부모 디렉토리를 찾으라는 소리다. 
- `By.XPATH`는 selenium에서 요소를 찾기 위한 선택자 중에 하나다. 이선택자를 사용하면 XML Path Language (XPath)을 통해 요소를 식별할 수 있다. `./..`이 `XPath` 언어라고 보면된다.
- `nowlank = new_element.get_attribute("data-cr-rank")`: `data-cr-rank`라는 속성을 가져온다. 찾아서 `nowlank`변수에 넣어준다.
- 이 속성은 웹사이트 페이지 마다 달라지며 개발자 도구를 통해 내가 가져오려는 랭크가 어떤 속성으로 되어있는지 확인해야한다.
- 네이버 view의 경우 사진과 같이 `data-cr-rank='3'` 이라는 속성으로 되어있다. 사진에서 보면 우리가 선택속성은 까만 배경이 있는 곳이고 위에 부모 요소까지 3~4번정도 위로 올라가야한다. 올라가는것을 `while`문을 통해 구현하고 있는것이다.
사진
- `if nowlank != None:`: 만약 `nowlank`변수의 값이 None이 아니라면. 그러니까 값이 있다면 아래코드를 실행한다.
- `BLOG_FOUND = True`: 예외처리를 위해 `False`로 했던 `BLOG_FOUND`변수를 `True`로 변경해주고 `break`로 무한루프를 빠져나온다.
- `if BLOG_FOUND:` `BLOG_FOUND`변수가 `True`로 변경됐다면 `for`문을 빠져나오게 만든다.
- `element = new_element`: 만약 `nowlank`변수의 값이 None이 라면 `new_element`값을 다시 `element`에 넣고 반복문을 실행한다.
- `driver.execute_script('window.scrollBy(0, 10000);')`: `driver.execute_script`는 `driver`라는 직원에게 자바스크립트 문법을 사용하게 해준다.
- `window.scroolBY(x, y)`: 자바스크립트의 문법으로 가로 x축만큼 세로 y축만큼 스크롤을 해준다.
이 프로그램을 실행하면 이런 결과가 나온다
```consol
DevTools listening on ws://127.0.0.1:1867/devtools/browser/9a313ba8-f9b7-4150-9856-8b63d24ea654     
타겟 블로그를 못찾음 --> 스크롤 하겠습니다.
파이썬 셀레니움 / 54 : 타켓 블로그의 랭크를 찾았습니다.
타겟 블로그를 못찾음 --> 스크롤 하겠습니다.
파이썬 플라스크 / 37 : 타켓 블로그의 랭크를 찾았습니다.
```

이상 내 블로그 페이지들의 순위를 자동으로 조회해주는 프로그램을 만들었다.
아래는 전체 코드다.
```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

searchqs = ['파이썬 셀레니움', '파이썬 플라스크']
target_blog_links =['https://www.sagein.net/708', 'https://yeko90.tistory.com/252']


for searchq, target_blog_link in zip(searchqs, target_blog_links):
    search_link=f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={searchq}'
    driver.get(search_link)
    time.sleep(2)

    link_selector = f'a[href^="{target_blog_link}"]'
    nowlank = -1
    #예외처리
    BLOG_FOUND = False
    for _ in range(7):
        try:
            element = driver.find_element(By.CSS_SELECTOR, link_selector)
            while True:
                new_element = element.find_element(By.XPATH, "./..")
                nowlank = new_element.get_attribute("data-cr-rank")
                if nowlank != None:
                   BLOG_FOUND = True
                   break
                element = new_element

            if BLOG_FOUND:
                break
        except:
            print('타겟 블로그를 못찾음 --> 스크롤 하겠습니다.')
            driver.execute_script('window.scrollBy(0, 10000);')
            time.sleep(3)

    print(f'{searchq} / {nowlank} : 타켓 블로그의 랭크를 찾았습니다.')

input()
```

