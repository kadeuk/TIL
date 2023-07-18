Django에서 Form은 웹 애플리케이션에서 사용자의 입력을 처리하는 데 사용되는 도구입니다. 사용자로부터 데이터를 수신하고 해당 데이터의 유효성을 검증하는 작업을 담당합니다.

Form은 간단한 HTML form을 생성하거나 복잡한 form 로직을 처리하는 데도 사용할 수 있습니다. Django의 Form 클래스를 사용하면 HTML form 요소를 Python 코드로 쉽게 표현하고 관리할 수 있습니다.

다음은 Django에서 간단한 Form의 예시입니다:

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

```

이 예시에서 `ContactForm`은 Django의 `forms.Form` 클래스를 상속받아 생성된 Form입니다. 이 Form에는 3개의 필드가 있습니다: `name`, `email`, `message`. 각 필드는 특정 필드 클래스의 인스턴스로, 해당 필드가 어떤 종류의 데이터를 받을 것인지, 그리고 어떻게 처리할 것인지를 정의합니다.

Django form은 입력 데이터의 검증도 자동으로 수행합니다. `is_valid()` 메소드를 사용하면 form에 포함된 모든 필드의 데이터가 유효한지 확인할 수 있습니다. 유효하지 않은 데이터가 있는 경우, 해당 필드에 대한 에러 메시지를 제공합니다.

마지막으로, Django form은 HTML 출력을 자동으로 생성할 수 있습니다. 이를 통해, 실제 HTML form 요소를 수동으로 코딩하는 대신 Python 코드로 form을 쉽게 작성하고 관리할 수 있습니다.

---
#python #gpt #django [[ORM]]