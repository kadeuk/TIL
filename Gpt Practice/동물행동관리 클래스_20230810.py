# 문제: 동물의 행동 관리
# 문제: Animal이라는 클래스를 만들어주세요. 이 클래스는 다음과 같은 속성과 메서드를 가지고 있어야 합니다:

# 속성:

# 동물의 이름 (name)
# 메서드:

# speak(): 동물의 울음소리를 출력하는 메서드. Animal 클래스에서는 "I don't know what sound I make!" 라는 메시지를 출력하도록 합니다.
# Animal 클래스를 상속받아, Dog와 Cat 클래스를 만들어주세요.

# Dog:

# speak(): "Woof!" 라는 메시지를 출력합니다.
# Cat:

# speak(): "Meow!" 라는 메시지를 출력합니다.
# 힌트:

# 상속은 class 자식클래스(부모클래스): 형태로 합니다.
# 부모 클래스의 메서드를 자식 클래스에서 재정의할 수 있습니다. 이것을 오버라이딩이라 합니다.
# 이 클래스들을 구현해보세요!

# 내답
class Animal():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("I don't know what sound I make!")

class Dog(Animal):
    print("Woof!")

class Cat(Animal):
    print("Meow!")



animal1 = Dog('cat')
animal1.speak()

# Gpt 해답


class Animal():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("I don't know what sound I make!")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animal1 = Dog('Boddy')
animal1.speak()

animal3 = Cat('Nabi')
animal3.speak()

# 만약 여러 동물 클래스가 있다고 했을때 speak. 즉 울음소리만 불러온다고하면

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I don't know what sound I make!")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Cow(Animal):
    def speak(self):
        print("Moo!")

# 동물들을 인스턴스화 하기
dog = Dog('Bobby')
cat = Cat('Nabi')
cow = Cow('Mooly')

# 여러 동물 객체를 리스트에 넣기
animals = [dog, cat, cow]

# 각 동물 울음소리 출력하기
for animal in animals:
    animal.speak()