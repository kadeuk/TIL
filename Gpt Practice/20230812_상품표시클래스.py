# 쇼핑몰의 상품을 나타내는 Product 클래스를 작성하십시오. Product 클래스는 다음의 속성과 메서드를 가져야 합니다.

# 속성:

# product_id: 상품의 고유 번호
# name: 상품의 이름
# price: 상품의 가격
# 메서드:

# show_product_info(): 상품 정보를 출력하는 메서드. "상품 ID: [product_id], 상품 이름: [name], 가격: [price]원" 형식으로 출력합니다.
# 이 Product 클래스를 상속받아 할인 상품을 나타내는 DiscountProduct 클래스를 작성하십시오. DiscountProduct 클래스는 다음의 추가 속성과 메서드를 가져야 합니다.

# 추가 속성:

# discount_rate: 할인율 (예: 0.1은 10% 할인을 의미)
# 추가 메서드:

# get_discounted_price(): 할인된 가격을 반환하는 메서드
# show_product_info(): "상품 ID: [product_id], 상품 이름: [name], 원래 가격: [price]원, 할인된 가격: [할인된 가격]원" 형식으로 출력합니다.
# 두 클래스를 작성한 후, Product 객체와 DiscountProduct 객체를 각각 하나씩 만들어서 show_product_info() 메서드를 호출해보세요.

# 내코드
class Product():
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    
    def show_product_info(self):
        print(f'상품 ID: {self.product_id}, 상품 이름: {self.name}, 가격: {self.price}원')

class DiscountProduct(Product):
    def __init__(self, product_id, name, price, discount_rate):
        super().__init__(product_id, name, price)
        self.discount_rate = discount_rate

    def get_discounted_price(self, discount_rate):
        discount_price = self.price * discount_rate
        return discount_price
    ``
    def show_product_info(self):
        
        super().show_product_info()
        print(f'할인된 가격: {discount_price}원')

product = DiscountProduct(27321, '머그컵', 5400, 0.1)
product.show_product_info()

# Gpt가짠 코드

class Product():
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    
    def show_product_info(self):
        print(f'상품 ID: {self.product_id}, 상품 이름: {self.name}, 가격: {self.price}원')

class DiscountProduct(Product):
    def __init__(self, product_id, name, price, discount_rate):
        super().__init__(product_id, name, price)
        self.discount_rate = discount_rate

    def get_discounted_price(self):
        discount_price = self.price * (1 - self.discount_rate)
        return discount_price
    
    def show_product_info(self):
        super().show_product_info()
        print(f'할인된 가격: {self.get_discounted_price()}원')

product = DiscountProduct(27321, '머그컵', 5400, 0.1)
product.show_product_info()


