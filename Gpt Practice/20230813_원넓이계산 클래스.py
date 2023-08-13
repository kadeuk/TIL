# 문제:

# Circle 클래스를 작성해 보세요. 이 클래스는 다음의 특성과 기능을 갖습니다:

# 반지름(radius)를 인스턴스 변수로 갖습니다. 생성자에서 초기화되어야 합니다.
# area 메서드를 통해 원의 넓이를 계산합니다. (원의 넓이 = π * radius^2)
# circumference 메서드를 통해 원의 둘레를 계산합니다. (원의 둘레 = 2 * π * radius)
# 여기서 π는 3.141592...로 간주하며, math 모듈의 pi를 사용하면 됩니다.

# python
# Copy code
# # 예시:
# circle1 = Circle(5)
# print(circle1.area())  # 출력: 78.53981633974483 (π * 5^2)
# print(circle1.circumference())  # 출력: 31.41592653589793 (2 * π * 5)
# 위의 예시처럼 원을 생성하고, 그 원의 넓이와 둘레를 계산하여 출력하는 Circle 클래스를 구현해 보세요.
from math import pi

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area_circle = pi*self.radius**2
        return area_circle
    
    def circumference(self):
        ference_circle = 2*pi*self.radius
        return ference_circle
    
# 예시:
circle1 = Circle(5)
print(circle1.area())  # 출력: 78.53981633974483 (π * 5^2)
print(circle1.circumference())  # 출력: 31.41592653589793 (2 * π * 5)



