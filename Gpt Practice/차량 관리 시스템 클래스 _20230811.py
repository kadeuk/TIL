# 문제: 차량 관리 시스템
# 문제: Vehicle이라는 클래스를 만들어주세요. 이 클래스는 다음과 같은 속성과 메서드를 가지고 있어야 합니다:

# 속성:

# 차량의 브랜드 (brand)
# 차량의 연식 (year)
# 메서드:

# show_info(): 차량의 정보를 출력하는 메서드. "브랜드: [브랜드], 연식: [연식]" 형식으로 출력해주세요.
# Vehicle 클래스를 상속받아, Car와 Motorcycle 클래스를 만들어주세요.

# Car:

# 추가 속성: number_of_doors (문의 개수)
# show_info(): 차량의 정보와 함께 문의 개수를 출력합니다. "브랜드: [브랜드], 연식: [연식], 문의 개수: [문의 개수]" 형식으로 출력해주세요.
# Motorcycle:

# 추가 속성: type (오토바이의 유형, 예: '스포츠', '크루저' 등)
# show_info(): 차량의 정보와 함께 오토바이의 유형을 출력합니다. "브랜드: [브랜드], 연식: [연식], 유형: [유형]" 형식으로 출력해주세요.
# 이 클래스들을 구현해보세요!

# 내가 작성한 코드
class Vehicle():
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def show_info(self):
        print(f'브랜드: [{self.brand}], 연식: [{self.year}]')

class Car(Vehicle):
    def number_of_doors(self, number):
        print(f'브랜드: [{self.brand}], 연식: [{self.year}], 문의개수[{number}]')

class Motorcycle(Vehicle):
    def show_info(self, ctype):
        print(f'브랜드: [{self.brand}], 연식: [{self.year}], 유형:[{ctype}]')

kia = Vehicle('k5', '2009')
kia.show_info()

# Gpt 답

class Vehicle():
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_info(self):
        print(f'브랜드: {self.brand}, 연식: {self.year}')

class Car(Vehicle):
    def __init__(self, brand, year, number_of_doors):
        super().__init__(brand, year)
        self.number_of_doors = number_of_doors

    def show_info(self):
        super().show_info()
        print(f'문의개수: {self.number_of_doors}')

class Motorcycle(Vehicle):
    def __init__(self, brand, year, ctype):
        super().__init__(brand, year)
        self.ctype = ctype

    def show_info(self):
        super().show_info()
        print(f'유형: {self.ctype}')

kia = Car('k5', '2009', 4)
kia.show_info()

bike = Motorcycle('Yamaha', '2018', '스포츠')
bike.show_info()

'''
super().__init__(brand, year) == self.brand = brand self.year = year 이거 와 같은뜻이다. 
이번 문제에서 배운점
1. 부모 클래스는 호출하지 않는다 자식클래스의 상속으로 쓰일뿐 클래스를 사용할때는 자식 클래스를 변수에 넣어 사용한다.
2. 자식클래에 필요한 속성이 있다면 부모 속성뒤에 추가적으로 적어줘야한다.
3. 부모 클래스의 메서드 자식이 클래스가 쓰고 싶다면 명시 해줘야한다.
'''