# 문제:
# "사각형"을 나타내는 클래스 Rectangle을 작성해주세요. 이 클래스는 다음과 같은 특징을 가집니다:

# 초기화 메서드에서 가로 길이(width)와 세로 길이(height)를 인자로 받습니다.
# area라는 메서드를 가지며, 이 메서드는 사각형의 면적을 반환합니다.
# perimeter라는 메서드를 가지며, 이 메서드는 사각형의 둘레를 반환합니다.
# 예시:
# python
# Copy code
# rect1 = Rectangle(10, 5)
# print(rect1.area())  # 출력: 50
# print(rect1.perimeter())  # 출력: 30

# rect2 = Rectangle(7, 8)
# print(rect2.area())  # 출력: 56
# print(rect2.perimeter())  # 출력: 30
# 이 문제를 바탕으로 Rectangle 클래스를 작성해 보세요.

# 내코드
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        areas = self.width * self.height
        print(f'출력: {areas}')

    def preimeter(self):
        preimeters = (self.width + self.height) *2
        print(f'출력: {preimeters}')
        
rect1 = Rectangle(10, 5)
rect1.area()
rect1.preimeter()

rect2 = Rectangle(7, 8)
rect2.area()
rect2.preimeter()

#결과
# 출력: 50
# 출력: 30
# 출력: 56
# 출력: 30

# Gpt 코드
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):  # 오타 수정
        return (self.width + self.height) * 2

rect1 = Rectangle(10, 5)
print(f'출력: {rect1.area()}')  # 출력 메서드 외부에서 처리
print(f'출력: {rect1.perimeter()}')

rect2 = Rectangle(7, 8)
print(f'출력: {rect2.area()}')
print(f'출력: {rect2.perimeter()}')

# #결과
# 출력: 50
# 출력: 30
# 출력: 56
# 출력: 30

