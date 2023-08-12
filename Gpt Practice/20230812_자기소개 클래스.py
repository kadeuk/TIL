# Person 클래스를 작성하십시오. Person 클래스는 다음의 속성과 메서드를 가져야 합니다.

# 속성:

# name: 사람의 이름
# age: 사람의 나이
# 메서드:

# introduce(): "안녕하세요, 제 이름은 [name]이고, 나이는 [age]살입니다." 형식으로 자기소개하는 메서드
# 이 Person 클래스를 상속받아 Employee 클래스를 작성하십시오. Employee 클래스는 다음의 추가 속성과 메서드를 가져야 합니다.

# 추가 속성:

# job: 직업
# 추가 메서드:

# introduce(): "안녕하세요, 제 이름은 [name]이고, 나이는 [age]살입니다. 제 직업은 [job]입니다." 형식으로 자기소개하는 메서드
# 두 클래스를 작성한 후, Person 객체와 Employee 객체를 각각 하나씩 만들어서 introduce() 메서드를 호출해보세요.

# 힌트: 자식 클래스에서 부모 클래스의 메서드를 오버라이드(재정의)할 때, super() 함수를 사용하여 부모 클래스의 메서드도 호출할 수 있습니다.


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, 제 이름은{self.name}이고, 나이는{self.age}살 입니다.')

class Job(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def introduce(self):
        super().introduce()
        print(f'제직업은 {self.job}입니다.')

person = Job('성민', 42, '사무원')
emplyee = Job('하은', 27, '분석가')
person.introduce()
emplyee.introduce()


